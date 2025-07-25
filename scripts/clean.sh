#!/bin/bash

echo "Starting system cleanup..."

# Clean APT cache
echo "Cleaning apt cache..."
sudo apt clean

# Shrink system logs
echo "Cleaning journal logs (keep last 2 days)..."
sudo journalctl --vacuum-time=2d

# Clear common user cache directories
echo "Clearing user cache..."
rm -rf ~/.cache ~/.npm ~/.vscode-server ~/.local/share/Trash ~/.conda ~/.python_history ~/.ipython

# Clean /tmp (only what's safe)
echo "Emptying /tmp directory..."
sudo find /tmp -type f -delete
sudo find /tmp -type d ! -path /tmp -exec rm -rf {} +

# Show disk usage after cleanup
echo "Disk usage after cleanup:"
df -h /

echo "Cleanup complete!"
