#!/usr/bin/env bash
# ============================================================================
# POWER-SHARK v1.0.0 - Bash Installation Script
# Supports: Debian/Ubuntu, RHEL/CentOS/Fedora, Arch, Alpine, macOS
# ============================================================================

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
BOLD='\033[1m'
RESET='\033[0m'

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INSTALL_DIR="${INSTALL_DIR:-$HOME/power-shark}"
VENV_DIR="$INSTALL_DIR/venv"
PYTHON_MIN_VERSION="3.7"

# ============================================================================
# Helper Functions
# ============================================================================

print_banner() {
    echo -e "${CYAN}${BOLD}"
    cat << 'EOF'
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ██████╗  ██████╗ ██╗    ██╗███████╗██████╗     ███████╗██╗  ██╗ █████╗ ██████╗██╗  ██╗
║   ██╔══██╗██╔═══██╗██║    ██║██╔════╝██╔══██╗    ██╔════╝██║  ██║██╔══██╗██╔══██╗██║ ██╔╝
║   ██████╔╝██║   ██║██║ █╗ ██║█████╗  ██████╔╝    ███████╗███████║███████║██████╔╝█████╔╝ 
║   ██╔═══╝ ██║   ██║██║███╗██║██╔══╝  ██╔══██╗    ╚════██║██╔══██║██╔══██║██╔══██╗██╔═██╗ 
║   ██║     ╚██████╔╝╚███╔███╔╝███████╗██║  ██║    ███████║██║  ██║██║  ██║██║  ██║██║  ██╗
║   ╚═╝      ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
║                                                                              ║
║                    POWER-SHARK v1.0.0 - Installation Script                  ║
║                         Author: Ian Carter Kulani, MSc                       ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
EOF
    echo -e "${RESET}"
}

log_info() {
    echo -e "${CYAN}[INFO]${RESET} $1"
}

log_success() {
    echo -e "${GREEN}[✓]${RESET} $1"
}

log_warning() {
    echo -e "${YELLOW}[!]${RESET} $1"
}

log_error() {
    echo -e "${RED}[✗]${RESET} $1"
}

# ============================================================================
# System Detection
# ============================================================================

detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        if [ -f /etc/debian_version ]; then
            OS="debian"
        elif [ -f /etc/redhat-release ]; then
            OS="redhat"
        elif [ -f /etc/arch-release ]; then
            OS="arch"
        elif [ -f /etc/alpine-release ]; then
            OS="alpine"
        else
            OS="linux"
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
    else
        OS="unknown"
    fi
    log_info "Detected OS: $OS"
}

check_root() {
    if [ "$EUID" -ne 0 ]; then
        SUDO="sudo"
        log_warning "Not running as root. Will use sudo for system packages."
    else
        SUDO=""
    fi
}

# ============================================================================
# Python Installation
# ============================================================================

check_python() {
    log_info "Checking Python version..."
    
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
    elif command -v python &> /dev/null; then
        PYTHON_CMD="python"
    else
        log_error "Python not found! Installing..."
        install_python
        PYTHON_CMD="python3"
    fi
    
    PYTHON_VERSION=$($PYTHON_CMD -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
    log_info "Found Python $PYTHON_VERSION"
    
    # Compare versions
    REQUIRED="3.7"
    if [ "$(printf '%s\n' "$REQUIRED" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED" ]; then
        log_error "Python $PYTHON_MIN_VERSION+ required (found $PYTHON_VERSION)"
        exit 1
    fi
    
    log_success "Python version OK"
}

install_python() {
    case $OS in
        debian)
            $SUDO apt-get update
            $SUDO apt-get install -y python3 python3-pip python3-venv python3-dev
            ;;
        redhat)
            $SUDO yum install -y python3 python3-pip python3-devel
            ;;
        arch)
            $SUDO pacman -Sy --noconfirm python python-pip
            ;;
        alpine)
            $SUDO apk add --no-cache python3 py3-pip python3-dev
            ;;
        macos)
            if command -v brew &> /dev/null; then
                brew install python3
            else
                log_error "Homebrew not found. Install Python manually."
                exit 1
            fi
            ;;
        *)
            log_error "Unsupported OS for auto-install"
            exit 1
            ;;
    esac
}

# ============================================================================
# System Dependencies
# ============================================================================

install_system_deps() {
    log_info "Installing system dependencies..."
    
    case $OS in
        debian)
            $SUDO apt-get update
            $SUDO apt-get install -y \
                build-essential \
                libssl-dev \
                libffi-dev \
                python3-dev \
                libpcap-dev \
                libnetfilter-queue-dev \
                iputils-ping \
                traceroute \
                mtr-tiny \
                dnsutils \
                net-tools \
                netcat-openbsd \
                nmap \
                curl \
                wget \
                openssh-client \
                whois \
                iptables \
                fping \
                tcptraceroute \
                docker.io \
                nikto \
                hashcat \
                tcpdump \
                arp-scan \
                macchanger \
                hping3 \
                xvfb \
                libx11-dev \
                libxext-dev \
                libxrender-dev \
                libxtst-dev \
                libxi-dev \
                scrot \
                xclip \
                || log_warning "Some packages failed to install"
            ;;
        redhat)
            $SUDO yum install -y \
                gcc \
                gcc-c++ \
                make \
                openssl-devel \
                libffi-devel \
                python3-devel \
                libpcap-devel \
                iputils \
                traceroute \
                mtr \
                bind-utils \
                net-tools \
                nmap \
                curl \
                wget \
                openssh-clients \
                whois \
                iptables \
                fping \
                tcpdump \
                arp-scan \
                || log_warning "Some packages failed to install"
            ;;
        arch)
            $SUDO pacman -Sy --noconfirm \
                base-devel \
                openssl \
                libffi \
                python \
                libpcap \
                iputils \
                traceroute \
                mtr \
                bind \
                net-tools \
                gnu-netcat \
                nmap \
                curl \
                wget \
                openssh \
                whois \
                iptables \
                fping \
                tcptraceroute \
                tcpdump \
                arp-scan \
                || log_warning "Some packages failed to install"
            ;;
        alpine)
            $SUDO apk add --no-cache \
                build-base \
                openssl-dev \
                libffi-dev \
                python3-dev \
                libpcap-dev \
                iputils \
                traceroute \
                mtr \
                bind-tools \
                net-tools \
                netcat-openbsd \
                nmap \
                curl \
                wget \
                openssh-client \
                whois \
                iptables \
                fping \
                tcpdump \
                arp-scan \
                || log_warning "Some packages failed to install"
            ;;
        macos)
            if command -v brew &> /dev/null; then
                brew install \
                    openssl \
                    libffi \
                    nmap \
                    curl \
                    wget \
                    whois \
                    mtr \
                    || log_warning "Some packages failed to install"
            fi
            ;;
        *)
            log_warning "Unsupported OS. Install system dependencies manually."
            ;;
    esac
    
    log_success "System dependencies installed"
}

# ============================================================================
# Virtual Environment & Python Packages
# ============================================================================

setup_venv() {
    log_info "Setting up Python virtual environment..."
    
    mkdir -p "$INSTALL_DIR"
    cd "$INSTALL_DIR"
    
    if [ ! -d "$VENV_DIR" ]; then
        $PYTHON_CMD -m venv "$VENV_DIR"
        log_success "Virtual environment created at $VENV_DIR"
    else
        log_info "Virtual environment already exists"
    fi
    
    # Activate venv
    source "$VENV_DIR/bin/activate"
    
    # Upgrade pip
    pip install --upgrade pip setuptools wheel
    
    log_success "Virtual environment ready"
}

install_python_deps() {
    log_info "Installing Python dependencies..."
    
    source "$VENV_DIR/bin/activate"
    
    if [ -f "$SCRIPT_DIR/requirements.txt" ]; then
        pip install -r "$SCRIPT_DIR/requirements.txt"
    else
        log_warning "requirements.txt not found. Installing core packages..."
        pip install \
            colorama \
            requests \
            psutil \
            dnspython \
            cryptography \
            paramiko \
            pynput \
            scapy \
            flask \
            flask-socketio \
            flask-cors \
            discord.py \
            telethon \
            slack-sdk \
            reportlab \
            whois \
            qrcode \
            pyshorteners \
            beautifulsoup4 \
            pyperclip \
            python-dotenv \
            tabulate
    fi
    
    log_success "Python dependencies installed"
}

# ============================================================================
# File Installation
# ============================================================================

install_files() {
    log_info "Installing POWER-SHARK files..."
    
    mkdir -p "$INSTALL_DIR"
    
    # Copy main files
    if [ -f "$SCRIPT_DIR/power_shark.py" ]; then
        cp "$SCRIPT_DIR/power_shark.py" "$INSTALL_DIR/"
        chmod +x "$INSTALL_DIR/power_shark.py"
    fi
    
    if [ -f "$SCRIPT_DIR/requirements-check.py" ]; then
        cp "$SCRIPT_DIR/requirements-check.py" "$INSTALL_DIR/"
        chmod +x "$INSTALL_DIR/requirements-check.py"
    fi
    
    if [ -f "$SCRIPT_DIR/requirements.txt" ]; then
        cp "$SCRIPT_DIR/requirements.txt" "$INSTALL_DIR/"
    fi
    
    # Create directories
    mkdir -p "$INSTALL_DIR/.power_shark"
    mkdir -p "$INSTALL_DIR/power_shark_reports"
    
    log_success "Files installed to $INSTALL_DIR"
}

# ============================================================================
# Launcher Creation
# ============================================================================

create_launcher() {
    log_info "Creating launcher script..."
    
    cat > "$INSTALL_DIR/power-shark" << 'EOF'
#!/usr/bin/env bash
# POWER-SHARK Launcher
INSTALL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$INSTALL_DIR/venv/bin/activate"
python3 "$INSTALL_DIR/power_shark.py" "$@"
EOF
    
    chmod +x "$INSTALL_DIR/power-shark"
    
    # Optionally add to PATH
    if [ -d "$HOME/.local/bin" ]; then
        ln -sf "$INSTALL_DIR/power-shark" "$HOME/.local/bin/power-shark" 2>/dev/null || true
        log_info "Launcher symlinked to ~/.local/bin/power-shark"
    fi
    
    log_success "Launcher created: $INSTALL_DIR/power-shark"
}

# ============================================================================
# Verification
# ============================================================================

verify_installation() {
    log_info "Verifying installation..."
    
    source "$VENV_DIR/bin/activate"
    
    if [ -f "$INSTALL_DIR/requirements-check.py" ]; then
        python3 "$INSTALL_DIR/requirements-check.py" || true
    fi
    
    log_success "Installation verification complete"
}

# ============================================================================
# Main
# ============================================================================

main() {
    print_banner
    
    log_info "Starting POWER-SHARK installation..."
    log_info "Install directory: $INSTALL_DIR"
    echo ""
    
    detect_os
    check_root
    check_python
    install_system_deps
    setup_venv
    install_python_deps
    install_files
    create_launcher
    verify_installation
    
    echo ""
    echo -e "${GREEN}${BOLD}╔══════════════════════════════════════════════════════════╗${RESET}"
    echo -e "${GREEN}${BOLD}║          ✅ INSTALLATION COMPLETE!                       ║${RESET}"
    echo -e "${GREEN}${BOLD}╚══════════════════════════════════════════════════════════╝${RESET}"
    echo ""
    echo -e "${WHITE}To run POWER-SHARK:${RESET}"
    echo -e "  ${CYAN}cd $INSTALL_DIR${RESET}"
    echo -e "  ${CYAN}./power-shark${RESET}"
    echo ""
    echo -e "${WHITE}Or use the launcher (if in PATH):${RESET}"
    echo -e "  ${CYAN}power-shark${RESET}"
    echo ""
    echo -e "${YELLOW}Note: Some features require sudo/root privileges${RESET}"
    echo ""
}

# Handle arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --dir)
            INSTALL_DIR="$2"
            shift 2
            ;;
        --help)
            echo "Usage: $0 [--dir INSTALL_DIR]"
            exit 0
            ;;
        *)
            log_error "Unknown option: $1"
            exit 1
            ;;
    esac
done

main
