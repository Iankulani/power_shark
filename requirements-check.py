#!/usr/bin/env python3
"""
POWER-SHARK Dependency Checker
Verifies all required and optional dependencies are installed
"""

import sys
import subprocess
import importlib
import shutil
from typing import Dict, List, Tuple

# Color codes
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

# Required packages (pip)
REQUIRED_PACKAGES = {
    'colorama': 'colorama',
    'requests': 'requests',
    'psutil': 'psutil',
    'dns': 'dnspython',
    'cryptography': 'cryptography',
    'paramiko': 'paramiko',
    'pynput': 'pynput',
    'scapy': 'scapy',
    'flask': 'flask',
    'flask_socketio': 'flask-socketio',
    'flask_cors': 'flask-cors',
    'discord': 'discord.py',
    'telethon': 'telethon',
    'slack_sdk': 'slack-sdk',
    'reportlab': 'reportlab',
    'whois': 'whois',
    'qrcode': 'qrcode',
    'pyshorteners': 'pyshorteners',
    'bs4': 'beautifulsoup4',
    'pyperclip': 'pyperclip',
    'dotenv': 'python-dotenv',
    'tabulate': 'tabulate',
}

# Optional packages
OPTIONAL_PACKAGES = {
    'smtplib': 'smtplib',  # Built-in
}

# System tools (binaries)
SYSTEM_TOOLS = {
    'ping': 'ping',
    'nmap': 'nmap',
    'curl': 'curl',
    'wget': 'wget',
    'nc': 'netcat',
    'ncat': 'ncat',
    'dig': 'dnsutils',
    'traceroute': 'traceroute',
    'mtr': 'mtr',
    'ssh': 'openssh-client',
    'docker': 'docker',
    'whois': 'whois',
    'nikto': 'nikto',
    'hashcat': 'hashcat',
    'arp': 'net-tools',
    'iptables': 'iptables',
    'fping': 'fping',
    'tcptraceroute': 'tcptraceroute',
    'tracepath': 'iputils-tracepath',
    'signal-cli': 'signal-cli',
}

# Python version requirement
MIN_PYTHON_VERSION = (3, 7)

class DependencyChecker:
    def __init__(self):
        self.results = {
            'python_version': False,
            'required_packages': {},
            'optional_packages': {},
            'system_tools': {},
        }
        self.missing_required = []
        self.missing_system = []
    
    def check_python_version(self) -> bool:
        """Check Python version meets minimum requirement"""
        current = sys.version_info[:2]
        if current >= MIN_PYTHON_VERSION:
            print(f"{Colors.GREEN}✅ Python {current[0]}.{current[1]} "
                  f"(>= {MIN_PYTHON_VERSION[0]}.{MIN_PYTHON_VERSION[1]}){Colors.RESET}")
            self.results['python_version'] = True
            return True
        else:
            print(f"{Colors.RED}❌ Python {current[0]}.{current[1]} "
                  f"(need >= {MIN_PYTHON_VERSION[0]}.{MIN_PYTHON_VERSION[1]}){Colors.RESET}")
            return False
    
    def check_package(self, import_name: str, pip_name: str) -> Tuple[bool, str]:
        """Check if a Python package is installed"""
        try:
            module = importlib.import_module(import_name)
            version = getattr(module, '__version__', 'unknown')
            return True, version
        except ImportError:
            return False, ''
    
    def check_required_packages(self) -> bool:
        """Check all required Python packages"""
        print(f"\n{Colors.CYAN}{Colors.BOLD}📦 Required Python Packages:{Colors.RESET}")
        all_present = True
        
        for import_name, pip_name in REQUIRED_PACKAGES.items():
            installed, version = self.check_package(import_name, pip_name)
            self.results['required_packages'][pip_name] = installed
            
            if installed:
                print(f"{Colors.GREEN}  ✅ {pip_name:25s} {version}{Colors.RESET}")
            else:
                print(f"{Colors.RED}  ❌ {pip_name:25s} NOT INSTALLED{Colors.RESET}")
                self.missing_required.append(pip_name)
                all_present = False
        
        return all_present
    
    def check_optional_packages(self) -> bool:
        """Check optional Python packages"""
        print(f"\n{Colors.CYAN}{Colors.BOLD}📦 Optional Python Packages:{Colors.RESET}")
        
        for import_name, pip_name in OPTIONAL_PACKAGES.items():
            installed, version = self.check_package(import_name, pip_name)
            self.results['optional_packages'][pip_name] = installed
            
            if installed:
                print(f"{Colors.GREEN}  ✅ {pip_name:25s} {version}{Colors.RESET}")
            else:
                print(f"{Colors.YELLOW}  ⚠️  {pip_name:25s} not installed (optional){Colors.RESET}")
        
        return True
    
    def check_system_tool(self, tool_name: str) -> bool:
        """Check if a system tool is available"""
        return shutil.which(tool_name) is not None
    
    def check_system_tools(self) -> bool:
        """Check all system tools"""
        print(f"\n{Colors.CYAN}{Colors.BOLD}🔧 System Tools:{Colors.RESET}")
        all_present = True
        
        for tool, package in SYSTEM_TOOLS.items():
            available = self.check_system_tool(tool)
            self.results['system_tools'][tool] = available
            
            if available:
                path = shutil.which(tool)
                print(f"{Colors.GREEN}  ✅ {tool:25s} {path}{Colors.RESET}")
            else:
                print(f"{Colors.YELLOW}  ⚠️  {tool:25s} not found "
                      f"(install: {package}){Colors.RESET}")
                self.missing_system.append(package)
                all_present = False
        
        return all_present
    
    def check_admin_privileges(self) -> bool:
        """Check for admin/root privileges"""
        import platform
        import os
        
        is_admin = False
        if platform.system().lower() == 'linux':
            is_admin = os.geteuid() == 0
        elif platform.system().lower() == 'windows':
            try:
                import ctypes
                is_admin = ctypes.windll.shell32.IsUserAnAdmin()
            except:
                pass
        elif platform.system().lower() == 'darwin':
            is_admin = os.geteuid() == 0
        
        if is_admin:
            print(f"{Colors.GREEN}✅ Running with admin/root privileges{Colors.RESET}")
        else:
            print(f"{Colors.YELLOW}⚠️  Not running as admin/root "
                  f"(some features limited){Colors.RESET}")
        
        return is_admin
    
    def generate_install_commands(self) -> str:
        """Generate installation commands for missing dependencies"""
        commands = []
        
        if self.missing_required:
            commands.append("# Install missing Python packages:")
            commands.append(f"pip install {' '.join(self.missing_required)}")
            commands.append("")
        
        if self.missing_system:
            import platform
            system = platform.system().lower()
            
            if system == 'linux':
                # Detect distro
                if os.path.exists('/etc/debian_version'):
                    commands.append("# Debian/Ubuntu:")
                    commands.append(f"sudo apt-get update && sudo apt-get install -y "
                                  f"{' '.join(set(self.missing_system))}")
                elif os.path.exists('/etc/redhat-release'):
                    commands.append("# RHEL/CentOS/Fedora:")
                    commands.append(f"sudo yum install -y "
                                  f"{' '.join(set(self.missing_system))}")
                elif os.path.exists('/etc/alpine-release'):
                    commands.append("# Alpine:")
                    commands.append(f"sudo apk add --no-cache "
                                  f"{' '.join(set(self.missing_system))}")
            
            elif system == 'darwin':
                commands.append("# macOS:")
                commands.append(f"brew install "
                              f"{' '.join(set(self.missing_system))}")
            
            elif system == 'windows':
                commands.append("# Windows (using chocolatey):")
                commands.append(f"choco install -y "
                              f"{' '.join(set(self.missing_system))}")
        
        return '\n'.join(commands)
    
    def print_report(self):
        """Print final dependency report"""
        print(f"\n{Colors.WHITE}{'=' * 60}{Colors.RESET}")
        print(f"{Colors.CYAN}{Colors.BOLD}📊 Dependency Check Report{Colors.RESET}")
        print(f"{Colors.WHITE}{'=' * 60}{Colors.RESET}")
        
        # Summary
        total_req = len(REQUIRED_PACKAGES)
        present_req = sum(1 for v in self.results['required_packages'].values() if v)
        
        total_tools = len(SYSTEM_TOOLS)
        present_tools = sum(1 for v in self.results['system_tools'].values() if v)
        
        print(f"\n  Python Version:  {'✅ OK' if self.results['python_version'] else '❌ FAIL'}")
        print(f"  Required Pkgs:   {present_req}/{total_req}")
        print(f"  System Tools:    {present_tools}/{total_tools}")
        
        # Overall status
        if present_req == total_req and self.results['python_version']:
            print(f"\n{Colors.GREEN}{Colors.BOLD}✅ All required dependencies satisfied!{Colors.RESET}")
        else:
            print(f"\n{Colors.RED}{Colors.BOLD}❌ Missing dependencies detected!{Colors.RESET}")
        
        # Installation commands
        if self.missing_required or self.missing_system:
            print(f"\n{Colors.YELLOW}{Colors.BOLD}📝 Installation Commands:{Colors.RESET}")
            print(f"{Colors.WHITE}{'-' * 60}{Colors.RESET}")
            print(self.generate_install_commands())
            print(f"{Colors.WHITE}{'-' * 60}{Colors.RESET}")
        
        print(f"\n{Colors.WHITE}{'=' * 60}{Colors.RESET}")
    
    def run_all_checks(self) -> bool:
        """Run all dependency checks"""
        print(f"\n{Colors.CYAN}{Colors.BOLD}")
        print("╔══════════════════════════════════════════════════════════╗")
        print("║     🦈 POWER-SHARK Dependency Checker v1.0.0            ║")
        print("╚══════════════════════════════════════════════════════════╝")
        print(f"{Colors.RESET}")
        
        # Run checks
        self.check_python_version()
        self.check_required_packages()
        self.check_optional_packages()
        self.check_system_tools()
        self.check_admin_privileges()
        
        # Print report
        self.print_report()
        
        return (
            self.results['python_version'] and
            all(self.results['required_packages'].values())
        )


def main():
    """Main entry point"""
    checker = DependencyChecker()
    success = checker.run_all_checks()
    
    if not success:
        print(f"\n{Colors.YELLOW}💡 Tip: Install missing dependencies and re-run "
              f"this checker.{Colors.RESET}")
        print(f"{Colors.YELLOW}   Command: python3 requirements-check.py{Colors.RESET}\n")
        sys.exit(1)
    else:
        print(f"\n{Colors.GREEN}🚀 Ready to launch POWER-SHARK!{Colors.RESET}")
        print(f"{Colors.WHITE}   Command: python3 power_shark.py{Colors.RESET}\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
