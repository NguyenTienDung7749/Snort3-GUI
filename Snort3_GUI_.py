#!/usr/bin/env python3
"""
Snort 3 Monitor - Cyberpunk Hacker Edition
Professional IDS monitoring interface
"""
import tkinter as tk
from tkinter import ttk, scrolledtext, font as tkfont
import subprocess
import threading
import time
import os
from datetime import datetime
from collections import Counter
import re

# ==================== CONFIGURATION ====================
LOG_FILE = "/var/log/snort/alert_fast.txt"
CONFIG_PATH = "/usr/local/etc/snort/snort_lab.lua"

# ==================== COLOR SCHEME - CYBERPUNK ====================
COLORS = {
    'bg_dark': '#0a0e27',
    'bg_medium': '#16213e',
    'bg_light': '#1a2332',
    'accent_cyan': '#00f5ff',
    'accent_purple': '#c770f0',
    'accent_pink': '#ff10f0',
    'accent_green': '#00ff41',
    'accent_red': '#ff0040',
    'accent_yellow': '#ffea00',
    'text_primary': '#e0e0e0',
    'text_dim': '#6c7a89',
    'neon_blue': '#00d9ff',
    'neon_green': '#39ff14',
    'neon_red': '#ff073a',
    'neon_purple': '#bc13fe',
    'fire_red': '#ff0000',
    'fire_orange': '#ff6600',
    'fire_yellow': '#ffcc00',
}

def sudo_prefix():
    """Return '' if root, else 'sudo '."""
    try:
        return "" if os.geteuid() == 0 else "sudo "
    except:
        return "sudo "

class AnimatedLabel(tk.Label):
    """Label with blinking animation"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.colors = [COLORS['neon_green'], COLORS['accent_cyan']]
        self.current_color = 0
        self.animate()
    
    def animate(self):
        self.config(fg=self.colors[self.current_color])
        self.current_color = (self.current_color + 1) % len(self.colors)
        self.after(800, self.animate)

class FireLabel(tk.Label):
    """Label with fire animation effect"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.fire_colors = [COLORS['fire_red'], COLORS['fire_orange'], 
                           COLORS['fire_yellow'], COLORS['fire_orange']]
        self.current_color = 0
        self.animate_fire()
    
    def animate_fire(self):
        self.config(fg=self.fire_colors[self.current_color])
        self.current_color = (self.current_color + 1) % len(self.fire_colors)
        self.after(300, self.animate_fire)

class MetricCard(tk.Frame):
    """Metric display card with neon border"""
    def __init__(self, parent, title, value="0", color=COLORS['accent_cyan']):
        super().__init__(parent, bg=COLORS['bg_medium'], 
                        highlightbackground=color, highlightthickness=2,
                        bd=0)
        
        # Title
        title_label = tk.Label(self, text=title, font=('Orbitron', 10, 'bold'),
                              bg=COLORS['bg_medium'], fg=COLORS['text_dim'])
        title_label.pack(pady=(10, 5))
        
        # Value
        self.value_label = tk.Label(self, text=value, font=('Orbitron', 20, 'bold'),
                                   bg=COLORS['bg_medium'], fg=color)
        self.value_label.pack(pady=(0, 10))
    
    def update_value(self, value, color=None):
        self.value_label.config(text=str(value))
        if color:
            self.value_label.config(fg=color)

class SnortHackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("◢ SNORT3 ◣ CYBERSEC TERMINAL")
        self.root.geometry("1400x900")
        self.root.configure(bg=COLORS['bg_dark'])
        
        # Try to load custom fonts (fallback to default if not available)
        try:
            self.title_font = tkfont.Font(family='Orbitron', size=28, weight='bold')
            self.mono_font = tkfont.Font(family='Fira Code', size=10)
        except:
            self.title_font = tkfont.Font(family='Arial', size=28, weight='bold')
            self.mono_font = tkfont.Font(family='Courier', size=10)
        
        self.is_monitoring = False
        self.log_file = LOG_FILE
        self.stats = {'total': 0, 'icmp': 0, 'tcp': 0, 'udp': 0, 'src_ips': Counter(), 'dst_ips': Counter()}
        
        self.create_gui()
        self.update_status()
        self.update_clock()
    
    def create_gui(self):
        # ==================== TOP BANNER ====================
        banner_frame = tk.Frame(self.root, bg=COLORS['bg_dark'], height=100)
        banner_frame.pack(fill=tk.X, padx=0, pady=0)
        
        # Left side - ASCII Art Title
        left_banner = tk.Frame(banner_frame, bg=COLORS['bg_dark'])
        left_banner.pack(side=tk.LEFT, padx=20, pady=10)
        
        title_text = "╔═══════════════════════════════════════════════════════╗\n"
        title_text += "║   ██████╗███╗   ██╗ ██████╗ ██████╗ ████████╗██████╗ ║\n"
        title_text += "║  ██╔════╝████╗  ██║██╔═══██╗██╔══██╗╚══██╔══╝╚════██╗║\n"
        title_text += "║  ╚█████╗ ██╔██╗ ██║██║   ██║██████╔╝   ██║    █████╔╝║\n"
        title_text += "║   ╚═══██╗██║╚██╗██║██║   ██║██╔══██╗   ██║    ╚═══██╗║\n"
        title_text += "║  ██████╔╝██║ ╚████║╚██████╔╝██║  ██║   ██║   ██████╔╝║\n"
        title_text += "║  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═════╝ ║\n"
        title_text += "╚═══════════════════════════════════════════════════════╝"
        
        title_label = tk.Label(left_banner, text=title_text, 
                              font=('Courier', 8, 'bold'),
                              bg=COLORS['bg_dark'], fg=COLORS['accent_cyan'],
                              justify=tk.LEFT)
        title_label.pack()
        
        # Middle - GUI Made By Dzungf (bên phải chữ SNORT3)
        middle_banner = tk.Frame(banner_frame, bg=COLORS['bg_dark'])
        middle_banner.pack(side=tk.LEFT, padx=(10, 20), pady=10)
        
        # Spacer to align with middle of ASCII art
        spacer = tk.Label(middle_banner, text="", bg=COLORS['bg_dark'], height=2)
        spacer.pack()
        
        credit_frame = tk.Frame(middle_banner, bg=COLORS['bg_dark'])
        credit_frame.pack()
        
        made_by_label = tk.Label(credit_frame, text="GUI Made By ", 
                                font=('Orbitron', 16, 'bold'),
                                bg=COLORS['bg_dark'], fg=COLORS['text_dim'])
        made_by_label.pack(side=tk.LEFT)
        
        # Dzungf with fire effect
        self.dzungf_label = FireLabel(credit_frame, text="Dzungf", 
                                     font=('Orbitron', 20, 'bold'),
                                     bg=COLORS['bg_dark'])
        self.dzungf_label.pack(side=tk.LEFT)
        
        fire_emoji = tk.Label(credit_frame, text=" 🔥", 
                            font=('Orbitron', 18),
                            bg=COLORS['bg_dark'], fg=COLORS['fire_orange'])
        fire_emoji.pack(side=tk.LEFT)
        
        # Clock and Status (Right side)
        info_frame = tk.Frame(banner_frame, bg=COLORS['bg_dark'])
        info_frame.pack(side=tk.RIGHT, padx=20)
        
        self.clock_label = tk.Label(info_frame, text="", font=('Orbitron', 16, 'bold'),
                                   bg=COLORS['bg_dark'], fg=COLORS['accent_yellow'])
        self.clock_label.pack(anchor=tk.E)
        
        self.uptime_label = tk.Label(info_frame, text="SYSTEM: INITIALIZING", 
                                    font=('Orbitron', 10),
                                    bg=COLORS['bg_dark'], fg=COLORS['text_dim'])
        self.uptime_label.pack(anchor=tk.E)
        
        # Separator line with glow effect
        separator = tk.Frame(self.root, bg=COLORS['accent_cyan'], height=3)
        separator.pack(fill=tk.X, padx=0, pady=0)
        
        # ==================== METRICS DASHBOARD ====================
        metrics_frame = tk.Frame(self.root, bg=COLORS['bg_dark'])
        metrics_frame.pack(fill=tk.X, padx=15, pady=15)
        
        self.status_card = MetricCard(metrics_frame, "STATUS", "OFFLINE", COLORS['neon_red'])
        self.status_card.pack(side=tk.LEFT, padx=8, fill=tk.BOTH, expand=True)
        
        self.total_card = MetricCard(metrics_frame, "TOTAL ALERTS", "0", COLORS['accent_cyan'])
        self.total_card.pack(side=tk.LEFT, padx=8, fill=tk.BOTH, expand=True)
        
        self.icmp_card = MetricCard(metrics_frame, "ICMP", "0", COLORS['accent_purple'])
        self.icmp_card.pack(side=tk.LEFT, padx=8, fill=tk.BOTH, expand=True)
        
        self.tcp_card = MetricCard(metrics_frame, "TCP", "0", COLORS['neon_green'])
        self.tcp_card.pack(side=tk.LEFT, padx=8, fill=tk.BOTH, expand=True)
        
        self.udp_card = MetricCard(metrics_frame, "UDP", "0", COLORS['accent_yellow'])
        self.udp_card.pack(side=tk.LEFT, padx=8, fill=tk.BOTH, expand=True)
        
        # ==================== CONTROL PANEL ====================
        control_frame = tk.Frame(self.root, bg=COLORS['bg_medium'], 
                                highlightbackground=COLORS['accent_purple'],
                                highlightthickness=2)
        control_frame.pack(fill=tk.X, padx=15, pady=(0, 15))
        
        label = tk.Label(control_frame, text="◢ CONTROL PANEL ◣", 
                        font=('Orbitron', 12, 'bold'),
                        bg=COLORS['bg_medium'], fg=COLORS['accent_purple'])
        label.pack(pady=8)
        
        btn_frame = tk.Frame(control_frame, bg=COLORS['bg_medium'])
        btn_frame.pack(pady=8)
        
        btn_style = {
            'font': ('Orbitron', 10, 'bold'),
            'width': 18,
            'height': 2,
            'bd': 0,
            'relief': tk.FLAT,
            'cursor': 'hand2'
        }
        
        self.start_btn = tk.Button(btn_frame, text="▶ ENGAGE SNORT",
                                   bg=COLORS['neon_green'], fg=COLORS['bg_dark'],
                                   command=self.start_snort,
                                   activebackground=COLORS['accent_green'],
                                   **btn_style)
        self.start_btn.pack(side=tk.LEFT, padx=6)
        
        self.stop_btn = tk.Button(btn_frame, text="⏹ DISENGAGE",
                                  bg=COLORS['neon_red'], fg=COLORS['bg_dark'],
                                  command=self.stop_snort,
                                  activebackground=COLORS['accent_red'],
                                  **btn_style)
        self.stop_btn.pack(side=tk.LEFT, padx=6)
        
        self.monitor_btn = tk.Button(btn_frame, text="👁 MONITOR LIVE",
                                     bg=COLORS['neon_blue'], fg=COLORS['bg_dark'],
                                     command=self.toggle_monitor,
                                     activebackground=COLORS['accent_cyan'],
                                     **btn_style)
        self.monitor_btn.pack(side=tk.LEFT, padx=6)
        
        self.clear_btn = tk.Button(btn_frame, text="🗑 PURGE LOGS",
                                   bg=COLORS['accent_yellow'], fg=COLORS['bg_dark'],
                                   command=self.clear_logs,
                                   activebackground='#ffd700',
                                   **btn_style)
        self.clear_btn.pack(side=tk.LEFT, padx=6)
        
        self.refresh_btn = tk.Button(btn_frame, text="🔄 REFRESH",
                                     bg=COLORS['text_dim'], fg=COLORS['bg_dark'],
                                     command=self.refresh_logs,
                                     activebackground='#95a5a6',
                                     **btn_style)
        self.refresh_btn.pack(side=tk.LEFT, padx=6)
        
        # ==================== MAIN CONTENT AREA ====================
        content_frame = tk.Frame(self.root, bg=COLORS['bg_dark'])
        content_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))
        
        # Left: Alert Feed
        left_frame = tk.LabelFrame(content_frame, text="◢ THREAT FEED ◣",
                                  font=('Orbitron', 11, 'bold'),
                                  bg=COLORS['bg_medium'], fg=COLORS['neon_green'],
                                  highlightbackground=COLORS['neon_green'],
                                  highlightthickness=2,
                                  bd=0, labelanchor=tk.N)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 8))
        
        self.alerts_text = scrolledtext.ScrolledText(
            left_frame,
            wrap=tk.NONE,
            width=90, height=30,
            bg=COLORS['bg_dark'], fg=COLORS['text_primary'],
            font=('Fira Code', 9),
            insertbackground=COLORS['neon_green'],
            selectbackground=COLORS['accent_purple'],
            bd=0
        )
        self.alerts_text.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)
        
        # Configure syntax highlighting
        self.alerts_text.tag_config('timestamp', foreground=COLORS['accent_cyan'], 
                                   font=('Fira Code', 9, 'bold'))
        self.alerts_text.tag_config('alert', foreground=COLORS['neon_red'], 
                                   font=('Fira Code', 9, 'bold'))
        self.alerts_text.tag_config('priority_high', foreground=COLORS['neon_red'])
        self.alerts_text.tag_config('priority_med', foreground=COLORS['accent_yellow'])
        self.alerts_text.tag_config('priority_low', foreground=COLORS['neon_green'])
        self.alerts_text.tag_config('protocol', foreground=COLORS['neon_purple'],
                                   font=('Fira Code', 9, 'bold'))
        self.alerts_text.tag_config('ip_src', foreground=COLORS['neon_green'])
        self.alerts_text.tag_config('ip_dst', foreground=COLORS['accent_red'])
        self.alerts_text.tag_config('arrow', foreground=COLORS['accent_cyan'],
                                   font=('Fira Code', 9, 'bold'))
        self.alerts_text.tag_config('dim', foreground=COLORS['text_dim'])
        self.alerts_text.tag_config('header', foreground=COLORS['accent_purple'],
                                   font=('Fira Code', 9, 'bold'))
        
        # Right: Statistics Panel
        right_frame = tk.Frame(content_frame, bg=COLORS['bg_dark'])
        right_frame.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Top IPs
        top_ips_frame = tk.LabelFrame(right_frame, text="◢ TOP SOURCE IPs ◣",
                                      font=('Orbitron', 10, 'bold'),
                                      bg=COLORS['bg_medium'], fg=COLORS['accent_cyan'],
                                      highlightbackground=COLORS['accent_cyan'],
                                      highlightthickness=2, bd=0)
        top_ips_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 8))
        
        self.top_ips_text = tk.Text(top_ips_frame, width=35, height=12,
                                   bg=COLORS['bg_dark'], fg=COLORS['text_primary'],
                                   font=('Fira Code', 9), bd=0)
        self.top_ips_text.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)
        self.top_ips_text.tag_config('ip', foreground=COLORS['neon_green'])
        self.top_ips_text.tag_config('count', foreground=COLORS['accent_yellow'])
        
        # Recent Activity
        activity_frame = tk.LabelFrame(right_frame, text="◢ ACTIVITY LOG ◣",
                                      font=('Orbitron', 10, 'bold'),
                                      bg=COLORS['bg_medium'], fg=COLORS['accent_purple'],
                                      highlightbackground=COLORS['accent_purple'],
                                      highlightthickness=2, bd=0)
        activity_frame.pack(fill=tk.BOTH, expand=True)
        
        self.activity_text = tk.Text(activity_frame, width=35, height=12,
                                    bg=COLORS['bg_dark'], fg=COLORS['text_dim'],
                                    font=('Fira Code', 8), bd=0, state=tk.DISABLED)
        self.activity_text.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)
        self.activity_text.tag_config('info', foreground=COLORS['accent_cyan'])
        self.activity_text.tag_config('success', foreground=COLORS['neon_green'])
        self.activity_text.tag_config('warning', foreground=COLORS['accent_yellow'])
        self.activity_text.tag_config('error', foreground=COLORS['neon_red'])
        
        # ==================== FOOTER STATUS BAR ====================
        footer = tk.Frame(self.root, bg=COLORS['bg_medium'], height=30,
                         highlightbackground=COLORS['accent_cyan'], highlightthickness=1)
        footer.pack(fill=tk.X, side=tk.BOTTOM)
        
        self.footer_label = tk.Label(footer, text="[ SYSTEM READY ] | SNORT 3.x | LAB MODE",
                                    font=('Orbitron', 9),
                                    bg=COLORS['bg_medium'], fg=COLORS['text_dim'])
        self.footer_label.pack(side=tk.LEFT, padx=15)
        
        self.connection_label = tk.Label(footer, text="⬤ DISCONNECTED",
                                        font=('Orbitron', 9, 'bold'),
                                        bg=COLORS['bg_medium'], fg=COLORS['neon_red'])
        self.connection_label.pack(side=tk.RIGHT, padx=15)
        
        # Initial message
        self.log_activity("System initialized", "info")
        self.log_activity("Awaiting commands...", "info")
    
    # ==================== UTILITY METHODS ====================
    def run_command(self, cmd):
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, 
                                  text=True, timeout=10)
            return (result.stdout or result.stderr or "").strip()
        except:
            return ""
    
    def check_snort_running(self):
        sp = sudo_prefix()
        out = self.run_command(f"{sp}snort-manager status")
        if "running" in out.lower():
            return True
        out = self.run_command("pgrep -fa snort")
        if CONFIG_PATH and CONFIG_PATH in out:
            return True
        return bool(out)
    
    def log_activity(self, message, level="info"):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.activity_text.config(state=tk.NORMAL)
        self.activity_text.insert(tk.END, f"[{timestamp}] ", level)
        self.activity_text.insert(tk.END, f"{message}\n")
        self.activity_text.see(tk.END)
        self.activity_text.config(state=tk.DISABLED)
        
        # Keep only last 50 lines
        lines = self.activity_text.get("1.0", tk.END).split('\n')
        if len(lines) > 50:
            self.activity_text.config(state=tk.NORMAL)
            self.activity_text.delete("1.0", f"{len(lines)-50}.0")
            self.activity_text.config(state=tk.DISABLED)
    
    def update_clock(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.clock_label.config(text=f"◢ {now} ◣")
        self.root.after(1000, self.update_clock)
    
    def update_status(self):
        is_running = self.check_snort_running()
        
        if is_running:
            self.status_card.update_value("ONLINE", COLORS['neon_green'])
            self.connection_label.config(text="⬤ CONNECTED", fg=COLORS['neon_green'])
            self.uptime_label.config(text="SYSTEM: ACTIVE", fg=COLORS['neon_green'])
        else:
            self.status_card.update_value("OFFLINE", COLORS['neon_red'])
            self.connection_label.config(text="⬤ DISCONNECTED", fg=COLORS['neon_red'])
            self.uptime_label.config(text="SYSTEM: STANDBY", fg=COLORS['text_dim'])
        
        # Update alert counts
        self.update_statistics()
        
        self.root.after(2000, self.update_status)
    
    def update_statistics(self):
        sp = sudo_prefix()
        
        # Total count
        count = self.run_command(f"{sp}wc -l < {self.log_file} 2>/dev/null || echo 0")
        self.stats['total'] = int(count.strip() or 0)
        self.total_card.update_value(self.stats['total'])
        
        # Protocol counts
        logs = self.run_command(f"{sp}cat {self.log_file} 2>/dev/null")
        
        icmp_count = logs.count('{ICMP}')
        tcp_count = logs.count('{TCP}')
        udp_count = logs.count('{UDP}')
        
        self.icmp_card.update_value(icmp_count)
        self.tcp_card.update_value(tcp_count)
        self.udp_card.update_value(udp_count)
        
        # Top IPs
        src_ips = re.findall(r'\{.*?\}\s+(\d+\.\d+\.\d+\.\d+)\s+->', logs)
        self.stats['src_ips'] = Counter(src_ips)
        
        self.top_ips_text.delete(1.0, tk.END)
        for i, (ip, count) in enumerate(self.stats['src_ips'].most_common(10), 1):
            self.top_ips_text.insert(tk.END, f"{i:2d}. ", 'count')
            self.top_ips_text.insert(tk.END, f"{ip:<15s} ", 'ip')
            self.top_ips_text.insert(tk.END, f"[{count}]\n", 'count')
    
    def parse_and_colorize(self, line):
        if not line.strip():
            return
        
        try:
            # Parse alert format: timestamp [**] [sid:msg] [**] [Priority: X] {PROTO} src -> dst
            
            # Timestamp
            if line[0].isdigit():
                ts_end = line.find('[**]')
                if ts_end > 0:
                    self.alerts_text.insert(tk.END, line[:ts_end].strip() + ' ', 'timestamp')
                    line = line[ts_end:]
            
            # Alert message
            if '[**]' in line:
                parts = line.split('[**]')
                if len(parts) >= 3:
                    msg = parts[1].strip()
                    self.alerts_text.insert(tk.END, '[**] ', 'alert')
                    self.alerts_text.insert(tk.END, msg, 'alert')
                    self.alerts_text.insert(tk.END, ' [**] ', 'alert')
                    line = '[**]'.join(parts[2:])
            
            # Priority
            if 'Priority:' in line:
                pri_match = re.search(r'\[Priority:\s*(\d+)\]', line)
                if pri_match:
                    pri_val = int(pri_match.group(1))
                    pri_text = pri_match.group(0)
                    
                    if pri_val == 0:
                        tag = 'priority_high'
                    elif pri_val <= 2:
                        tag = 'priority_med'
                    else:
                        tag = 'priority_low'
                    
                    self.alerts_text.insert(tk.END, pri_text + ' ', tag)
                    line = line[line.find(']', line.find('Priority:')) + 1:]
            
            # Protocol
            proto_match = re.search(r'\{(\w+)\}', line)
            if proto_match:
                self.alerts_text.insert(tk.END, proto_match.group(0) + ' ', 'protocol')
                line = line[proto_match.end():]
            
            # IPs
            if '->' in line:
                parts = line.split('->')
                if len(parts) == 2:
                    self.alerts_text.insert(tk.END, parts[0].strip() + ' ', 'ip_src')
                    self.alerts_text.insert(tk.END, '→ ', 'arrow')
                    self.alerts_text.insert(tk.END, parts[1].strip(), 'ip_dst')
            
            self.alerts_text.insert(tk.END, '\n')
        
        except Exception as e:
            self.alerts_text.insert(tk.END, line + '\n', 'dim')
    
    def refresh_logs(self):
        sp = sudo_prefix()
        logs = self.run_command(f"{sp}tail -n 150 {self.log_file}")
        
        self.alerts_text.delete(1.0, tk.END)
        
        if not logs.strip():
            self.alerts_text.insert(tk.END, "═" * 100 + "\n", 'header')
            self.alerts_text.insert(tk.END, "  NO THREATS DETECTED\n", 'header')
            self.alerts_text.insert(tk.END, "  System monitoring active. Awaiting events...\n", 'dim')
            self.alerts_text.insert(tk.END, "═" * 100 + "\n", 'header')
            return
        
        # Header
        self.alerts_text.insert(tk.END, "═" * 100 + "\n", 'header')
        self.alerts_text.insert(tk.END, "  THREAT INTELLIGENCE FEED - REAL-TIME ALERTS\n", 'header')
        self.alerts_text.insert(tk.END, "═" * 100 + "\n", 'header')
        
        for line in logs.splitlines():
            self.parse_and_colorize(line)
        
        self.alerts_text.see(tk.END)
        self.log_activity(f"Refreshed: {len(logs.splitlines())} alerts", "info")
    
    # ==================== CONTROL METHODS ====================
    def start_snort(self):
        self.log_activity("Engaging Snort IDS...", "warning")
        
        def _run():
            sp = sudo_prefix()
            result = self.run_command(f"{sp}snort-manager start")
            time.sleep(2)
            self.refresh_logs()
            
            if "started" in result.lower() or self.check_snort_running():
                self.log_activity("Snort ONLINE", "success")
            else:
                self.log_activity("Failed to start Snort", "error")
        
        threading.Thread(target=_run, daemon=True).start()
    
    def stop_snort(self):
        self.log_activity("Disengaging Snort...", "warning")
        sp = sudo_prefix()
        self.run_command(f"{sp}snort-manager stop")
        
        self.is_monitoring = False
        self.monitor_btn.config(text="👁 MONITOR LIVE", bg=COLORS['neon_blue'])
        self.log_activity("Snort OFFLINE", "info")
    
    def clear_logs(self):
        sp = sudo_prefix()
        self.run_command(f"{sp}truncate -s 0 {self.log_file}")
        
        self.alerts_text.delete(1.0, tk.END)
        self.alerts_text.insert(tk.END, "═" * 100 + "\n", 'header')
        self.alerts_text.insert(tk.END, "  LOGS PURGED\n", 'alert')
        self.alerts_text.insert(tk.END, "  All historical data cleared from memory.\n", 'dim')
        self.alerts_text.insert(tk.END, "═" * 100 + "\n", 'header')
        
        self.log_activity("Logs purged", "warning")
        self.update_statistics()
    
    def toggle_monitor(self):
        if not self.is_monitoring:
            self.is_monitoring = True
            self.monitor_btn.config(text="⏸ PAUSE", bg=COLORS['accent_yellow'])
            self.log_activity("Live monitoring ACTIVE", "success")
            self.monitor_logs()
        else:
            self.is_monitoring = False
            self.monitor_btn.config(text="👁 MONITOR LIVE", bg=COLORS['neon_blue'])
            self.log_activity("Live monitoring PAUSED", "info")
    
    def monitor_logs(self):
        if self.is_monitoring:
            self.refresh_logs()
            self.root.after(1500, self.monitor_logs)

# ==================== MAIN ====================
if __name__ == "__main__":
    root = tk.Tk()
    
    # Try to set window icon (optional)
    try:
        # You can add custom icon here if available
        pass
    except:
        pass
    
    app = SnortHackerGUI(root)
    root.mainloop()