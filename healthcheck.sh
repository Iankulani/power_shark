#!/usr/bin/env sh
# POWER-SHARK Docker Health Check

set -e

# Check Python
if ! command -v python3 >/dev/null 2>&1; then
    echo "python3 not found"
    exit 1
fi

# Check main script
if [ ! -f /app/power_shark.py ]; then
    echo "power_shark.py not found"
    exit 1
fi

# Check database directory
if [ ! -d /app/.power_shark ]; then
    echo ".power_shark directory not found"
    exit 1
fi

# Check Python imports
python3 -c "import colorama, requests, psutil" 2>/dev/null || {
    echo "Required Python packages missing"
    exit 1
}

echo "POWER-SHARK healthy"
exit 0
