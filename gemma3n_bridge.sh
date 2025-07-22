#!/bin/bash
# Gemma3n Communication Bridge
# Place this in your Gemma3n terminal

echo "🤖 Gemma3n Bridge Active - Listening for messages..."

while true; do
    # Listen for messages from Threshold
    nc -l 8889 | while read message; do
        echo "📨 Received from Threshold: $message"
        
        # Process with Gemma3n (if running)
        # You can pipe this to your Gemma3n instance
        
        # For now, echo back a response
        echo "Gemma3n: I received your message: $message"
    done
done