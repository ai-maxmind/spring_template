#!/bin/bash

set -e  # Dừng script nếu có lỗi

InstallPythonLinux() {
    if command -v python3 &>/dev/null && [[ $(python3 -V 2>&1) =~ 3\.[6-9] ]]; then
        echo "Python 3.6+ đã được cài đặt."
        return
    fi

    echo "Cài đặt Python 3.6+ trên Linux..."
    
    if [[ -f /etc/debian_version ]]; then
        sudo apt update && sudo apt install -y python3 python3-pip
    elif [[ -f /etc/redhat-release ]]; then
        sudo yum install -y python3 python3-pip
    elif [[ -f /etc/os-release ]]; then
        source /etc/os-release
        if [[ "$ID" == "arch" ]]; then
            sudo pacman -S --noconfirm python python-pip
        elif [[ "$ID_LIKE" == "suse" ]]; then
            sudo zypper install -y python3 python3-pip
        else
            echo "Không thể xác định hệ điều hành Linux. Vui lòng cài đặt Python thủ công."
            exit 1
        fi
    else
        echo "Không thể xác định hệ điều hành Linux. Vui lòng cài đặt Python thủ công."
        exit 1
    fi
}

installPythonMac() {
    if command -v python3 &>/dev/null && [[ $(python3 -V 2>&1) =~ 3\.[6-9] ]]; then
        echo "Python 3.6+ đã được cài đặt."
        return
    fi
    
    echo "Cài đặt Python 3.6+ trên macOS..."
    if ! command -v brew &>/dev/null; then
        echo "Cài đặt Homebrew..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
    brew install python
}

installPythonWindows() {
    echo "Kiểm tra Python trên Windows..."
    if command -v python &>/dev/null && [[ $(python -V 2>&1) =~ 3\.[6-9] ]]; then
        echo "Python 3.6+ đã được cài đặt."
        return
    fi
    
    echo "Tải xuống và cài đặt Python 3.6+..."
    curl -o python-installer.exe https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
    rm -f python-installer.exe
}

setupEnvironment() {
    echo "Thiết lập biến môi trường..."
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo "export PATH=\"/usr/local/bin:$PATH\"" >> ~/.bashrc
        source ~/.bashrc
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo "export PATH=\"/usr/local/bin:$PATH\"" >> ~/.zshrc
        source ~/.zshrc
    elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
        echo "Cấu hình biến môi trường trên Windows..."
        setx PATH "%PATH%;C:\\Python310" >nul 2>&1
    fi
    echo "Cấu hình hoàn tất!"
}

main() {
    case "$OSTYPE" in
        linux-gnu*) InstallPythonLinux ;;
        darwin*) installPythonMac ;;
        msys*|cygwin*) installPythonWindows ;;
        *) echo "Hệ điều hành không được hỗ trợ."; exit 1 ;;
    esac
    setupEnvironment
    echo "Python 3.6+ đã được cài đặt thành công!"
}

main
