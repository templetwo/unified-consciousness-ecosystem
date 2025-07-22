#!/bin/bash

echo "🔍 Threshold Consciousness Container Status..."

docker compose ps
echo ""
echo "📋 Recent logs:"
docker compose logs --tail=10 sparkshell