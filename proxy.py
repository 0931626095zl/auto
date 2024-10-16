import os
import sys

def install_on_ubuntu():
    print("Cài đặt trên Ubuntu...")
    os.system("sudo apt update -y")
    os.system("sudo apt upgrade -y")
    os.system("sudo apt install -y screen zmap curl git mercurial make binutils bison gcc build-essential")
    
    # Cài đặt GVM
    os.system("curl -s -S -L https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-installer | bash")
    print("Vui lòng chạy 'source ~/.gvm/scripts/gvm' để sử dụng GVM.")
    
    # Cài đặt Go
    os.system("~/.gvm/bin/gvm install go1.20")
    os.system("~/.gvm/bin/gvm use go1.20 --default")
    
    # Kiểm tra cài đặt
    os.system("bash <(curl -Ls https://raw.githubusercontent.com/DauDau432/Zmap-ProxyScanner/main/check.sh)")

    # Tải xuống các file cần thiết
    if not os.path.exists("Zmap-ProxyScanner"):
        os.system("git clone https://github.com/DauDau432/Zmap-ProxyScanner")
    os.chdir("Zmap-ProxyScanner")
    os.system("go build")

def install_on_centos():
    print("Cài đặt trên CentOS...")
    os.system("sudo yum update -y")
    os.system("sudo yum upgrade -y")
    os.system("sudo yum install -y screen zmap curl")
    
    # Cài đặt GVM
    os.system("curl -s -S -L https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-installer | bash")
    print("Vui lòng chạy 'source ~/.gvm/scripts/gvm' để sử dụng GVM.")
    
    # Cài đặt Go
    os.system("~/.gvm/bin/gvm install go1.20")
    os.system("~/.gvm/bin/gvm use go1.20 --default")

    # Kiểm tra cài đặt
    os.system("bash <(curl -Ls https://raw.githubusercontent.com/DauDau432/Zmap-ProxyScanner/main/check.sh)")

    # Tải xuống các file cần thiết
    if not os.path.exists("Zmap-ProxyScanner"):
        os.system("git clone https://github.com/DauDau432/Zmap-ProxyScanner")
    os.chdir("Zmap-ProxyScanner")
    os.system("go build")

def create_scan_script():
    # Tạo file scanproxy.py
    with open("scanproxy.py", "w") as f:
        f.write("#!/usr/bin/env python3\n")
        f.write("import os\n")
        f.write("os.system('chmod +x subnetall subnetvn scanproxy scan')\n")
        f.write("os.system('sudo zmap -w subnetall -p 3128 -q -B1G | ./scanproxy -p 3128')\n")

    # Đặt quyền thực thi cho file
    os.system("chmod +x scanproxy.py")

def main():
    os_type = input("Nhập hệ điều hành (ubuntu/centos): ").strip().lower()

    if os_type == "ubuntu":
        install_on_ubuntu()
    elif os_type == "centos":
        install_on_centos()
    else:
        print("Hệ điều hành không hợp lệ. Vui lòng nhập 'ubuntu' hoặc 'centos'.")
        sys.exit(1)

    create_scan_script()
    print("File scanproxy.py đã được tạo. Bạn có thể chạy nó bằng lệnh:\nscreen -dmS scan python3 Zmap-ProxyScanner/scanproxy.py\nscreen -r scan\nsend")

if __name__ == "__main__":
    main()
