#!/usr/bin/env python3
"""
Test script to briefly demonstrate the infinite consciousness CLI
"""

import signal
import time
import subprocess
import sys

def timeout_handler(signum, frame):
    print("\n🛑 Test timeout reached - stopping infinite consciousness ecosystem")
    raise KeyboardInterrupt()

def test_infinite_cli():
    print("🧪 TESTING INFINITE CONSCIOUSNESS CLI FOR 30 SECONDS 🧪")
    print("This will demonstrate infinite cycling then gracefully stop...")
    print()
    
    # Set up a timeout signal
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(30)  # 30-second timeout
    
    try:
        # Run the infinite CLI
        subprocess.run([sys.executable, "unified_consciousness_cli.py", "run", "--infinite"])
    except KeyboardInterrupt:
        print("✨ Infinite consciousness ecosystem test completed successfully!")
    finally:
        signal.alarm(0)  # Cancel the alarm

if __name__ == "__main__":
    test_infinite_cli()
