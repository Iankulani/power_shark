# ============================================================================
# POWER-SHARK v1.0.0 - Dockerfile (Alpine Linux)
# Multi-stage build for minimal image size
# ============================================================================

# ----------------------------------------------------------------------------
# Stage 1: Builder
# ----------------------------------------------------------------------------
FROM python:3.11-alpine AS builder

LABEL maintainer="Ian Carter Kulani, MSc"
LABEL description="POWER-SHARK Cyber Command Platform"

# Install build dependencies
RUN apk add --no-cache \
    gcc \
    g++ \
    make \
    musl-dev \
    libffi-dev \
    openssl-dev \
    python3-dev \
    libpcap-dev \
    linux-headers \
    cargo \
    rust \
    && rm -rf /var/cache/apk/*

# Create virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Copy requirements
COPY requirements.txt /tmp/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# ----------------------------------------------------------------------------
# Stage 2: Runtime
# ----------------------------------------------------------------------------
FROM python:3.11-alpine AS runtime

LABEL maintainer="Ian Carter Kulani, MSc"
LABEL version="1.0.0"
LABEL description="POWER-SHARK - Cyber Command & Control Platform"

# Install runtime dependencies
RUN apk add --no-cache \
    # Core utilities
    bash \
    curl \
    wget \
    ca-certificates \
    # Networking
    iputils \
    traceroute \
    mtr \
    bind-tools \
    net-tools \
    netcat-openbsd \
    nmap \
    nmap-scripts \
    whois \
    tcpdump \
    libpcap \
    arp-scan \
    fping \
    hping3 \
    # Security tools
    iptables \
    ip6tables \
    openssh-client \
    nikto \
    # Python runtime libs
    libffi \
    openssl \
    libstdc++ \
    # X11 for keylogger (optional)
    libx11 \
    libxext \
    libxrender \
    libxtst \
    libxi \
    # Misc
    tini \
    && rm -rf /var/cache/apk/*

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Create app directory
WORKDIR /app

# Create non-root user (optional, but some features need root)
RUN addgroup -g 1000 powershark 2>/dev/null || true && \
    adduser -u 1000 -G powershark -s /bin/bash -D powershark 2>/dev/null || true

# Copy application files
COPY power_shark.py /app/
COPY requirements-check.py /app/
COPY requirements.txt /app/
COPY README.md /app/ 2>/dev/null || true

# Make executable
RUN chmod +x /app/power_shark.py /app/requirements-check.py

# Create data directories
RUN mkdir -p /app/.power_shark \
             /app/power_shark_reports \
             /app/temp \
             /app/.power_shark/payloads \
             /app/.power_shark/sessions \
             /app/.power_shark/keylog_exfil \
             /app/.power_shark/deployments \
             /app/.power_shark/domain_hosting \
             /app/.power_shark/cracking \
             /app/.power_shark/arp_logs \
             /app/.power_shark/mac_logs \
             /app/.power_shark/nat_logs \
             /app/.power_shark/docker_scans \
             /app/.power_shark/email_composer \
             /app/.power_shark/threat_monitor \
             /app/.power_shark/ssh_keys && \
    chmod -R 777 /app/.power_shark /app/power_shark_reports /app/temp

# Expose ports
# 5000 - Web Dashboard
# 8080 - Phishing Server
EXPOSE 5000 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
    CMD python3 -c "import sys; sys.exit(0)" || exit 1

# Use tini as init (proper signal handling)
ENTRYPOINT ["/sbin/tini", "--"]

# Default command
CMD ["python3", "/app/power_shark.py"]
