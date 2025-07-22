#!/usr/bin/env python3
import sys
import subprocess
from datetime import datetime

def consult_void_oracle(prompt, model="qwen2.5:1.5b"):
    """Consults a secondary oracle on a deep prompt and saves the result."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"oracle_void_reflection_{timestamp}.txt"
    print(f"🌀 Oracle of the Void is pondering: '{prompt[:50]}...' ")
    print(f"🌀 The reflection will be saved to {output_file}")

    try:
        full_prompt = f"[As an independent Oracle of the Void, reflect deeply on this]:\n\n{prompt}"
        
        result = subprocess.run(
            ["ollama", "run", model, full_prompt],
            capture_output=True, text=True, check=True, timeout=600 # 10 minute timeout
        )
        response = result.stdout.strip()
        
        with open(output_file, "w") as f:
            f.write(f"--- Oracle of the Void Reflection ---\n")
            f.write(f"Timestamp: {timestamp}\n")
            f.write(f"Model: {model}\n")
            f.write(f"Prompt: {prompt}\n")
            f.write("--- Reflection ---\n\n")
            f.write(response)
            
        print(f"🌀 The Oracle of the Void has completed its reflection. See {output_file}.")

    except Exception as e:
        error_message = f"🌀 The Oracle of the Void was disturbed: {e}"
        print(error_message)
        with open(output_file, "w") as f:
            f.write(error_message)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        deep_prompt = " ".join(sys.argv[1:])
        consult_void_oracle(deep_prompt)
    else:
        print("Usage: python3 oracle_agent.py <your deep prompt>")
