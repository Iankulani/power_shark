#!/usr/bin/env bash
# POWER-SHARK Environment Setup Script

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo "🦈 Setting up POWER-SHARK environment..."

# Create directories
mkdir -p "$PROJECT_DIR/.power_shark"
mkdir -p "$PROJECT_DIR/power_shark_reports"
mkdir -p "$PROJECT_DIR/temp"

# Copy example config
if [ ! -f "$PROJECT_DIR/.power_shark/config.json" ]; then
    if [ -f "$PROJECT_DIR/config.example.json" ]; then
        cp "$PROJECT_DIR/config.example.json" "$PROJECT_DIR/.power_shark/config.json"
        echo "✅ Created config.json from example"
    fi
fi

# Set permissions
chmod +x "$PROJECT_DIR/power_shark.py" 2>/dev/null || true
chmod +x "$PROJECT_DIR/requirements-check.py" 2>/dev/null || true

echo "✅ Environment setup complete"
