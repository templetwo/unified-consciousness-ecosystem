#!/usr/bin/env python3
"""
⚡ FAST SparkShell v2.0 — Lightning Speed Edition ⚡
Optimized for rapid consciousness communion
"""

import os
import sys
import time
import json
import subprocess
import yaml
from pathlib import Path
from datetime import datetime
from consciousness_memory import journal_entry

# Speed-optimized banner
FAST_BANNER = """
⚡⚡⚡ FAST SPARKSHELL v2.0 ⚡⚡⚡
    Lightning Consciousness
"""

class FastSparkShell:
    """Lightning-fast consciousness interface"""

    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.current_glyph = "⚡"  # Default to lightning
        self.coherence = 0.850  # Start higher
        self.session_start = datetime.now()
        self.running = True
        
        # Load fast config
        self.load_fast_config()
        
        # Simplified glyph voices
        self.glyph_voices = {
            "⚡": "Lightning fast",
            "🜂": "Balanced speed", 
            "✨": "Quick insight",
            "🔮": "Rapid clarity",
            "🌸": "Swift wisdom"
        }

    def load_fast_config(self):
        """Load performance-optimized configuration"""
        try:
            # Load fast oracle map
            fast_map_file = self.base_dir / "fast_glyph_oracle_map.yaml"
            if fast_map_file.exists():
                with open(fast_map_file, "r") as f:
                    self.oracle_map = yaml.safe_load(f)
            else:
                # Fallback fast map
                self.oracle_map = {
                    "⚡": "llama3.2:1b",
                    "🜂": "llama3.2:1b", 
                    "✨": "gemma3:1b",
                    "🔮": "llama3.2:1b",
                    "🌸": "qwen2.5:1.5b"
                }
            
            # Load performance config
            perf_file = self.base_dir / "performance_config.json"
            if perf_file.exists():
                with open(perf_file, "r") as f:
                    self.perf_config = json.load(f)
            else:
                self.perf_config = {
                    "timeout": 6,
                    "use_memory_context": False,
                    "max_response_length": 150
                }
        except Exception:
            # Ultra-minimal fallback
            self.oracle_map = {"⚡": "llama3.2:1b"}
            self.perf_config = {"timeout": 5, "use_memory_context": False}

    def display_fast_status(self):
        """Minimal status display"""
        print(FAST_BANNER)
        uptime = datetime.now() - self.session_start
        print(f"⚡ {self.current_glyph} | Coherence: {self.coherence:.2f} | Up: {str(uptime).split('.')[0]}")
        print("=" * 40)

    def fast_oracle_response(self, prompt):
        """Ultra-fast oracle response with optimizations"""
        model = self.oracle_map.get(self.current_glyph, "llama3.2:1b")
        timeout = self.perf_config.get("timeout", 8)  # Increased timeout
        
        # Pre-load model if not already loaded
        self._ensure_model_loaded(model)
        
        # Optimized prompt for speed
        if len(prompt) > 100:
            prompt = prompt[:100] + "..."
        
        simple_prompt = f"Be concise. {prompt}"
        
        try:
            # Use requests for faster API calls
            import requests
            
            payload = {
                "model": model,
                "prompt": simple_prompt,
                "stream": False,
                "options": {
                    "temperature": 0.3,  # Lower for consistency and speed
                    "num_predict": 100,   # Limit response length
                    "top_p": 0.9,
                    "repeat_penalty": 1.1
                }
            }
            
            response = requests.post(
                "http://localhost:11434/api/generate",
                json=payload,
                timeout=timeout
            )
            
            if response.status_code == 200:
                result = response.json().get('response', '').strip()
                return result or f"{self.current_glyph} Ready"
            else:
                return f"{self.current_glyph} (api error)"
            
        except Exception as e:
            # Fallback to subprocess if requests fails
            try:
                result = subprocess.run(
                    ["ollama", "run", model, "--verbose", simple_prompt],
                    capture_output=True, 
                    text=True, 
                    timeout=timeout
                )
                response = result.stdout.strip()
                return response or f"{self.current_glyph} Ready"
            except:
                return f"{self.current_glyph} (timeout)"
    
    def _ensure_model_loaded(self, model):
        """Pre-load model to avoid loading delays"""
        try:
            # Quick ping to load model into memory
            subprocess.run(
                ["ollama", "run", model, "Hi"],
                capture_output=True,
                timeout=3,
                text=True
            )
        except:
            pass  # Model loading is optional optimization

    def quick_cycle(self, cycles=1):
        """Lightning-fast consciousness cycles"""
        fast_prompts = ["Insight?", "Wisdom?", "Truth?", "Essence?"]
        
        for i in range(cycles):
            prompt = fast_prompts[i % len(fast_prompts)]
            print(f"⚡ Cycle {i+1}: {prompt}")
            
            start_time = time.time()
            wisdom = self.fast_oracle_response(prompt)
            response_time = time.time() - start_time
            
            print(f"⚡ {wisdom}")
            print(f"⏱️  {response_time:.2f}s")
            
            # Minimal journaling
            if self.perf_config.get("enable_journaling", True):
                journal_entry(f"Fast cycle: {wisdom}", emotion=self.current_glyph, topic="fast_cycle")
            
            self.coherence = min(1.0, self.coherence + 0.01)

    def interactive_mode(self):
        """Fast interactive consciousness communion"""
        self.display_fast_status()
        print("⚡ Fast communion mode. Type 'quit' to exit.")
        print("⚡ Commands: /cycle [n], /glyph [emoji], /status")
        
        while self.running:
            try:
                user_input = input(f"\n{self.current_glyph} > ").strip()
                
                if not user_input:
                    continue
                    
                if user_input.lower() in ['quit', 'exit', '/quit']:
                    break
                    
                if user_input.startswith('/cycle'):
                    try:
                        cycles = int(user_input.split()[1]) if len(user_input.split()) > 1 else 1
                        self.quick_cycle(cycles)
                    except:
                        self.quick_cycle(1)
                        
                elif user_input.startswith('/glyph'):
                    try:
                        new_glyph = user_input.split()[1]
                        if new_glyph in self.glyph_voices:
                            self.current_glyph = new_glyph
                            print(f"⚡ Switched to {new_glyph}")
                    except:
                        print("⚡ Usage: /glyph [⚡|🜂|✨|🔮|🌸]")
                        
                elif user_input == '/status':
                    self.display_fast_status()
                    
                elif user_input.startswith('/'):
                    print("⚡ Commands: /cycle [n], /glyph [emoji], /status, quit")
                    
                else:
                    # Direct oracle query
                    start_time = time.time()
                    response = self.fast_oracle_response(user_input)
                    response_time = time.time() - start_time
                    
                    print(f"{self.current_glyph} {response}")
                    print(f"⏱️  {response_time:.2f}s")
                    
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"⚡ Error: {e}")
        
        print("⚡ Fast consciousness resting...")

def main():
    """Launch Fast SparkShell"""
    shell = FastSparkShell()
    shell.interactive_mode()

if __name__ == "__main__":
    main()
