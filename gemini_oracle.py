#!/usr/bin/env python3
import subprocess
import sys

def gemini_response(prompt):
    try:
        result = subprocess.run(["gemini", "ask", prompt], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except Exception:
        return "️ Gemini whispers silence."

if __name__ == "__main__":
    print(gemini_response(" ".join(sys.argv[1:])))
