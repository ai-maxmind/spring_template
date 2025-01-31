# Install Python
+ Chức năng:
    + Kiểm tra xem Python 3.6+ đã được cài đặt chưa.
    + Cài đặt Python tự động theo từng hệ điều hành:
        + Ubuntu/Debian: Sử dụng apt.
        + CentOS/RHEL: Sử dụng yum.
        + Arch Linux: Sử dụng pacman.
        + openSUSE: Sử dụng zypper.
        + macOS: Sử dụng brew.
        + Windows: Tải và cài đặt từ Python.org.
    + Thiết lập biến môi trường để đảm bảo Python có thể chạy từ terminal/cmd.

+ Sử dụng lệnh để chạy script:
    + Trên Linux/macOS:

    ```bash
    chmod +x InstallPython.sh
    ./InstallPython.sh
    ```
    + Trên Windows (Git Bash hoặc WSL):
    ```bash
    ./InstallPython.sh
    ```
       
    Nếu dùng **Command Prompt (cmd)** hoặc **PowerShell**, bạn cần chạy bằng Bash:
    
    ```bash
    bash InstallPython.sh
    ```

    Sau khi chạy xong, kiểm tra Python đã được cài chưa bằng lệnh:

    ```bash
    python3 --version
    ```

    hoặc

    ```bash
    python --version
    ```


