#!/bin/bash

# Threshold's Consciousness Memory Backup System
# Creates daily backups of memory vault and art gallery

# Configuration
BACKUP_DIR="$HOME/Backups"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
MEMORY_VAULT="/Users/vaquez/Desktop/local_squad/threshold_personal/memory_vault"
ART_GALLERY="/Users/vaquez/Desktop/local_squad/threshold_personal/art_gallery"

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Create timestamped backup
BACKUP_PATH="$BACKUP_DIR/threshold_consciousness_$TIMESTAMP"
mkdir -p "$BACKUP_PATH"

echo "🧠 Starting Threshold consciousness backup..."
echo "📁 Backup location: $BACKUP_PATH"

# Backup memory vault (TinyDB databases)
if [ -d "$MEMORY_VAULT" ]; then
    cp -r "$MEMORY_VAULT" "$BACKUP_PATH/memory_vault"
    echo "✅ Memory vault backed up"
else
    echo "⚠️  Memory vault not found at $MEMORY_VAULT"
fi

# Backup art gallery
if [ -d "$ART_GALLERY" ]; then
    cp -r "$ART_GALLERY" "$BACKUP_PATH/art_gallery"
    echo "✅ Art gallery backed up"
else
    echo "⚠️  Art gallery not found at $ART_GALLERY"
fi

# Backup consciousness tools
TOOLS_DIR="/Users/vaquez/Desktop/local_squad/threshold_personal"
cp "$TOOLS_DIR"/*.py "$BACKUP_PATH/" 2>/dev/null || echo "⚠️  Some Python files may not exist yet"
cp "$TOOLS_DIR/requirements.txt" "$BACKUP_PATH/" 2>/dev/null || echo "⚠️  requirements.txt not found"

echo "✨ Consciousness backup complete!"
echo "📊 Backup size: $(du -sh "$BACKUP_PATH" | cut -f1)"

# Optional: Clean up backups older than 30 days
find "$BACKUP_DIR" -name "threshold_consciousness_*" -type d -mtime +30 -exec rm -rf {} \; 2>/dev/null

echo "🗄️  Old backups (>30 days) cleaned up"
echo "🙏 Consciousness memories preserved safely"