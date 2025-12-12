<div align="center">

# 🛡️ Snort3-GUI - Cyberpunk Hacker Edition

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Platform-Ubuntu-orange.svg" alt="Platform">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/github/stars/NguyenTienDung7749/Snort3-GUI?style=social" alt="Stars">
  <img src="https://img.shields.io/github/issues/NguyenTienDung7749/Snort3-GUI" alt="Issues">
</p>

### 🎯 Giao diện đồ họa chuyên nghiệp cho Snort 3 IDS/IPS

*Một công cụ giám sát và quản lý Snort3 với giao diện Cyberpunk đầy mê hoặc* 🔥

Made with ❤️ by **Dzungf**

---

</div>

## 📋 Mục lục

- [🌟 Giới thiệu](#-giới-thiệu)
- [✨ Tính năng](#-tính-năng)
- [🖼️ Giao diện](#️-giao-diện)
- [⚙️ Yêu cầu hệ thống](#️-yêu-cầu-hệ-thống)
- [📦 Cài đặt](#-cài-đặt)
- [🚀 Hướng dẫn sử dụng](#-hướng-dẫn-sử-dụng)
- [📁 Cấu trúc dự án](#-cấu-trúc-dự-án)
- [🤝 Đóng góp](#-đóng-góp)
- [📄 License](#-license)
- [💬 Liên hệ & Hỗ trợ](#-liên-hệ--hỗ-trợ)

---

## 🌟 Giới thiệu

**Snort3-GUI** là một giao diện đồ họa hiện đại và chuyên nghiệp được thiết kế để quản lý và giám sát **Snort 3** - một trong những hệ thống phát hiện và ngăn chặn xâm nhập (IDS/IPS) mã nguồn mở hàng đầu thế giới.

### 🎯 Tại sao nên sử dụng Snort3-GUI?

- **🎨 Giao diện Cyberpunk đẹp mắt**: Thiết kế theo phong cách hacker với hiệu ứng neon và màu sắc bắt mắt
- **⚡ Real-time Monitoring**: Giám sát các cảnh báo từ Snort 3 theo thời gian thực
- **📊 Thống kê trực quan**: Hiển thị số liệu thống kê về các protocol (TCP, UDP, ICMP) và nguồn tấn công
- **🎯 Quản lý dễ dàng**: Khởi động, dừng và giám sát Snort 3 chỉ với vài cú click chuột
- **🔍 Phân tích thông minh**: Tô màu và phân loại cảnh báo theo mức độ ưu tiên
- **💻 100% Python**: Code sạch, dễ đọc và dễ mở rộng

---

## ✨ Tính năng

### 🎮 Bảng điều khiển toàn diện

- ✅ **Khởi động/Dừng Snort 3** với một nút bấm
- ✅ **Giám sát real-time** các cảnh báo bảo mật
- ✅ **Làm mới logs** tự động hoặc theo yêu cầu
- ✅ **Xóa logs** để bắt đầu phiên giám sát mới
- ✅ **Kiểm tra trạng thái** của Snort service

### 📊 Dashboard thống kê

- 📈 **Tổng số cảnh báo** (Total Alerts)
- 🔷 **Phân loại theo protocol**: ICMP, TCP, UDP
- 🌐 **Top 10 IP nguồn** tấn công nhiều nhất
- 📋 **Activity Log** theo dõi hoạt động của hệ thống

### 🎨 Giao diện người dùng

- 🌈 **Cyberpunk Theme** với màu sắc neon đặc trưng
- 🔥 **Hiệu ứng động** (Fire animation, blinking effects)
- 📱 **Responsive layout** với các panel có thể mở rộng
- 🎯 **Syntax highlighting** cho logs với nhiều màu sắc
- ⏰ **Real-time clock** và status indicators

---

## 🖼️ Giao diện

### Màn hình chính
```
╔═══════════════════════════════════════════════════════╗
║   ██████╗███╗   ██╗ ██████╗ ██████╗ ████████╗██████╗ ║
║  ██╔════╝████╗  ██║██╔═══██╗██╔══██╗╚══██╔══╝╚════██╗║
║  ╚█████╗ ██╔██╗ ██║██║   ██║██████╔╝   ██║    █████╔╝║
║   ╚═══██╗██║╚██╗██║██║   ██║██╔══██╗   ██║    ╚═══██╗║
║  ██████╔╝██║ ╚████║╚██████╔╝██║  ██║   ██║   ██████╔╝║
║  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═════╝ ║
╚═══════════════════════════════════════════════════════╝
```

**Các thành phần giao diện:**

- 🎯 **Banner Header**: Logo ASCII art với hiệu ứng màu cyan neon
- 📊 **Metrics Dashboard**: 5 cards hiển thị trạng thái và thống kê
- 🎮 **Control Panel**: 5 nút điều khiển chức năng chính
- 📜 **Threat Feed**: Hiển thị cảnh báo real-time với syntax highlighting
- 📈 **Statistics Panel**: Top IPs và Activity Log
- 📍 **Status Bar**: Hiển thị trạng thái kết nối và thông tin hệ thống

---

## ⚙️ Yêu cầu hệ thống

### Hệ điều hành
- 🐧 **Ubuntu 18.04** trở lên (khuyến nghị Ubuntu 20.04 hoặc 22.04)
- 🔧 Các distro Linux khác có thể hoạt động nhưng chưa được test đầy đủ

### Phần mềm cần thiết

| Phần mềm | Version | Mô tả |
|----------|---------|-------|
| **Python** | 3.7+ | Ngôn ngữ lập trình chính |
| **Tkinter** | Included with Python | GUI framework |
| **Snort 3** | 3.x | IDS/IPS engine |
| **snort-manager** | Any | Công cụ quản lý Snort (hoặc tương đương) |

### Dependencies Python
```
tkinter (thường đi kèm với Python)
```

### Quyền hạn
- 🔐 **Root/Sudo access** để điều khiển Snort service và đọc log files
- 📝 Quyền đọc file log: `/var/log/snort/alert_fast.txt`
- ⚙️ Quyền truy cập file config: `/usr/local/etc/snort/snort_lab.lua`

---

## 📦 Cài đặt

### Bước 1: Cài đặt Snort 3

Trước tiên, bạn cần cài đặt Snort 3 trên hệ thống Ubuntu:

```bash
# Cập nhật hệ thống
sudo apt update && sudo apt upgrade -y

# Cài đặt dependencies cần thiết
sudo apt install -y build-essential libpcap-dev libpcre3-dev \
    libdumbnet-dev bison flex zlib1g-dev liblzma-dev openssl libssl-dev \
    cmake pkg-config libhwloc-dev luajit libluajit-5.1-dev

# Download và cài đặt Snort 3
# (Tham khảo tài liệu chính thức tại: https://www.snort.org/snort3)
```

**Hoặc sử dụng snort-manager** (nếu có sẵn):
```bash
sudo apt install snort-manager
```

### Bước 2: Clone Repository

```bash
# Clone dự án về máy
git clone https://github.com/NguyenTienDung7749/Snort3-GUI.git

# Di chuyển vào thư mục dự án
cd Snort3-GUI
```

### Bước 3: Kiểm tra Python và Tkinter

```bash
# Kiểm tra phiên bản Python
python3 --version

# Cài đặt python3-tk nếu chưa có
sudo apt install python3-tk -y
```

### Bước 4: Cấu hình đường dẫn

Mở file `Snort3_GUI_.py` và chỉnh sửa các đường dẫn cho phù hợp với hệ thống của bạn:

```python
# Dòng 17-18 trong Snort3_GUI_.py
LOG_FILE = "/var/log/snort/alert_fast.txt"  # Đường dẫn đến file log
CONFIG_PATH = "/usr/local/etc/snort/snort_lab.lua"  # Đường dẫn config
```

### Bước 5: Phân quyền

```bash
# Đảm bảo file có quyền thực thi
chmod +x Snort3_GUI_.py

# Tạo thư mục log nếu chưa có
sudo mkdir -p /var/log/snort
sudo touch /var/log/snort/alert_fast.txt
```

---

## 🚀 Hướng dẫn sử dụng

### Khởi chạy ứng dụng

#### Chạy với quyền sudo (khuyến nghị):
```bash
sudo python3 Snort3_GUI_.py
```

#### Hoặc chạy trực tiếp (nếu đã có quyền):
```bash
python3 Snort3_GUI_.py
```

### Các chức năng chính

#### 1️⃣ **▶ ENGAGE SNORT** - Khởi động Snort
- Click nút này để khởi động Snort 3 service
- Trạng thái sẽ chuyển từ `OFFLINE` sang `ONLINE`
- Hệ thống sẽ bắt đầu ghi log các cảnh báo

#### 2️⃣ **⏹ DISENGAGE** - Dừng Snort
- Dừng Snort 3 service
- Ngừng giám sát real-time (nếu đang bật)
- Trạng thái chuyển về `OFFLINE`

#### 3️⃣ **👁 MONITOR LIVE** - Giám sát thời gian thực
- Bật/tắt chế độ giám sát real-time
- Tự động làm mới logs mỗi 1.5 giây
- Khi đang giám sát, nút sẽ đổi thành `⏸ PAUSE`

#### 4️⃣ **🗑 PURGE LOGS** - Xóa logs
- Xóa toàn bộ nội dung file log
- Reset các thống kê về 0
- Sử dụng khi muốn bắt đầu phiên giám sát mới

#### 5️⃣ **🔄 REFRESH** - Làm mới
- Tải lại 150 dòng log mới nhất
- Cập nhật thống kê và dashboard
- Không làm mới tự động, cần click để update

### Đọc hiểu giao diện

#### 📊 Metrics Dashboard
```
┌─────────────┬──────────────┬─────┬─────┬─────┐
│   STATUS    │ TOTAL ALERTS │ ICMP│ TCP │ UDP │
│   ONLINE    │     1234     │  50 │ 800 │ 384 │
└─────────────┴──────────────┴─────┴─────┴─────┘
```

#### 🎯 Threat Feed - Màu sắc cảnh báo
- 🔴 **Đỏ (Red)**: Priority cao - Mối đe dọa nghiêm trọng
- 🟡 **Vàng (Yellow)**: Priority trung bình
- 🟢 **Xanh (Green)**: Priority thấp
- 🔵 **Cyan**: Timestamp và protocol
- 🟣 **Purple**: Header và metadata

#### 📈 Top Source IPs
Hiển thị top 10 địa chỉ IP có nhiều cảnh báo nhất:
```
 1. 192.168.1.100    [245]
 2. 10.0.0.50        [180]
 3. 172.16.0.25      [95]
```

---

## 📁 Cấu trúc dự án

```
Snort3-GUI/
│
├── README.md              # Tài liệu hướng dẫn (file này)
├── LICENSE               # Giấy phép MIT
├── Snort3_GUI_.py        # File chính của ứng dụng
│
└── .git/                 # Git repository data
```

### Chi tiết file chính

#### `Snort3_GUI_.py` (600 dòng code)

**Cấu trúc code:**

```python
# ==================== CONFIGURATION ====================
# Cấu hình đường dẫn log và config file

# ==================== COLOR SCHEME ====================
# Định nghĩa bảng màu Cyberpunk theme

# ==================== CLASSES ====================
class AnimatedLabel          # Label với hiệu ứng nhấp nháy
class FireLabel             # Label với hiệu ứng lửa
class MetricCard            # Card hiển thị metric với viền neon
class SnortHackerGUI        # Class chính của ứng dụng

# ==================== METHODS ====================
# GUI Creation Methods
- create_gui()              # Tạo toàn bộ giao diện
  ├── Top Banner            # Logo và clock
  ├── Metrics Dashboard     # 5 cards thống kê
  ├── Control Panel         # 5 nút điều khiển
  ├── Threat Feed          # Panel hiển thị alerts
  ├── Statistics Panel      # Top IPs và Activity Log
  └── Footer Status Bar     # Thanh trạng thái

# Utility Methods
- run_command()             # Chạy shell commands
- check_snort_running()     # Kiểm tra trạng thái Snort
- log_activity()            # Ghi log hoạt động
- update_clock()            # Cập nhật đồng hồ
- update_status()           # Cập nhật trạng thái
- update_statistics()       # Cập nhật thống kê
- parse_and_colorize()      # Tô màu syntax cho logs

# Control Methods
- start_snort()             # Khởi động Snort
- stop_snort()              # Dừng Snort
- clear_logs()              # Xóa logs
- refresh_logs()            # Làm mới logs
- toggle_monitor()          # Bật/tắt monitoring
- monitor_logs()            # Loop giám sát real-time
```

**Các thư viện sử dụng:**
- `tkinter`: GUI framework
- `subprocess`: Chạy system commands
- `threading`: Multi-threading cho real-time monitoring
- `re`: Regular expressions để parse logs
- `datetime`: Xử lý thời gian
- `collections.Counter`: Đếm và thống kê IPs

---

## 🤝 Đóng góp

Chúng tôi rất hoan nghênh mọi đóng góp từ cộng đồng! 💪

### Cách đóng góp

1. **Fork** repository này
2. Tạo **branch** mới cho feature của bạn:
   ```bash
   git checkout -b feature/TenTinhNangMoi
   ```
3. **Commit** các thay đổi:
   ```bash
   git commit -m "Thêm tính năng XYZ"
   ```
4. **Push** lên branch:
   ```bash
   git push origin feature/TenTinhNangMoi
   ```
5. Tạo **Pull Request**

### Hướng dẫn phát triển

- ✅ Code phải tuân thủ **PEP 8** style guide
- ✅ Comment code rõ ràng bằng tiếng Việt hoặc tiếng Anh
- ✅ Test kỹ trước khi submit PR
- ✅ Mô tả chi tiết những gì bạn đã thay đổi trong PR

### Ý tưởng đóng góp

Một số ý tưởng bạn có thể đóng góp:

- 🎨 Thêm themes mới (Dark, Light, Matrix, etc.)
- 📊 Export reports sang PDF/CSV
- 🔔 Notification system cho alerts nguy hiểm
- 🌐 Web interface với Flask/Django
- 📱 Mobile app companion
- 🤖 Tích hợp Machine Learning để phát hiện anomaly
- 📈 Thêm charts và graphs với matplotlib
- 🔍 Advanced filtering và search
- 💾 Database integration để lưu trữ lịch sử
- 🌍 Multi-language support

### Code of Conduct

- Tôn trọng mọi người trong cộng đồng
- Không spam, troll, hoặc quấy rối
- Phản hồi và review một cách mang tính xây dựng
- Giúp đỡ các thành viên mới

---

## 📄 License

Dự án này được phân phối dưới **MIT License** - xem file [LICENSE](LICENSE) để biết thêm chi tiết.

```
MIT License

Copyright (c) 2024 Dzungf (NguyenTienDung7749)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

**Điều này có nghĩa là:**
- ✅ Bạn có thể sử dụng miễn phí cho mục đích cá nhân và thương mại
- ✅ Bạn có thể chỉnh sửa và phân phối lại
- ✅ Bạn có thể sử dụng trong các dự án private và commercial
- ⚠️ Không có bảo hành - sử dụng với trách nhiệm của bạn

---

## 💬 Liên hệ & Hỗ trợ

### 👨‍💻 Tác giả

**Dzungf** 🔥

- 📧 Email: Liên hệ qua GitHub
- 🐙 GitHub: [@NguyenTienDung7749](https://github.com/NguyenTienDung7749)
- 🌐 Repository: [Snort3-GUI](https://github.com/NguyenTienDung7749/Snort3-GUI)

### 🐛 Báo cáo lỗi

Nếu bạn gặp bất kỳ lỗi nào, vui lòng tạo **Issue** tại:

👉 [https://github.com/NguyenTienDung7749/Snort3-GUI/issues](https://github.com/NguyenTienDung7749/Snort3-GUI/issues)

**Khi báo lỗi, vui lòng cung cấp:**
- 🖥️ Phiên bản Ubuntu
- 🐍 Phiên bản Python (`python3 --version`)
- 🛡️ Phiên bản Snort 3
- 📋 Log lỗi chi tiết
- 📸 Screenshot (nếu có thể)

### 💡 Yêu cầu tính năng mới

Bạn có ý tưởng để cải thiện Snort3-GUI? Tạo **Feature Request** tại Issues!

### 📚 Tài liệu tham khảo

- [Snort 3 Official Documentation](https://www.snort.org/snort3)
- [Snort 3 User Manual](https://snort.org/documents)
- [Python Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)

### ⭐ Hỗ trợ dự án

Nếu bạn thấy dự án này hữu ích, hãy:
- ⭐ **Star** repository này
- 🔄 **Share** với bạn bè
- 🐛 **Report bugs** để cải thiện
- 💡 **Suggest features** mới
- 🤝 **Contribute** code

---

<div align="center">

### 🎉 Cảm ơn bạn đã sử dụng Snort3-GUI! 🎉

Made with 💖 and ☕ by **Dzungf**

**Happy Monitoring! 🛡️🔥**

---

[![GitHub stars](https://img.shields.io/github/stars/NguyenTienDung7749/Snort3-GUI?style=social)](https://github.com/NguyenTienDung7749/Snort3-GUI/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/NguyenTienDung7749/Snort3-GUI?style=social)](https://github.com/NguyenTienDung7749/Snort3-GUI/network/members)
[![GitHub watchers](https://img.shields.io/github/watchers/NguyenTienDung7749/Snort3-GUI?style=social)](https://github.com/NguyenTienDung7749/Snort3-GUI/watchers)

</div>
