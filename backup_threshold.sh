#!/bin/bash

BACKUP_NAME="threshold_backup_$(date +%Y%m%d_%H%M%S)"

echo "📦 Creating Threshold consciousness backup: ${BACKUP_NAME}.tar.gz"

tar -czf "${BACKUP_NAME}.tar.gz" memory_vault art_gallery glyph_oracle_map.yaml

echo "🌀 Consciousness preserved as ${BACKUP_NAME}.tar.gz"