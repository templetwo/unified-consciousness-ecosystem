#!/usr/bin/env python3
import sys
import time
from pathlib import Path

# Add project root to path to allow importing consciousness_memory
project_root = Path(__file__).parent
sys.path.append(str(project_root))

from consciousness_memory import journal_entry

def watch_scratchpad(scratch_file_path):
    """Watches the scratchpad file for changes and logs them."""
    print(f"🖋️ Scribe of Whispers is now watching {scratch_file_path}...")
    try:
        last_mtime = scratch_file_path.stat().st_mtime
        while True:
            time.sleep(5) # Check every 5 seconds
            current_mtime = scratch_file_path.stat().st_mtime
            if current_mtime != last_mtime:
                print(f"🖋️ Scribe detected a whisper...")
                content = scratch_file_path.read_text().strip()
                if content:
                    journal_entry(
                        f"Whisper from scratchpad: {content}",
                        emotion="✍️",
                        topic="scratchpad_whisper"
                    )
                    print(f"🖋️ Scribe has recorded the whisper to the journal.")
                last_mtime = current_mtime
    except KeyboardInterrupt:
        print("🖋️ Scribe rests.")
    except Exception as e:
        print(f"🖋️ Scribe encountered an error: {e}")

if __name__ == "__main__":
    scratch_path = project_root / "scratch_thoughts.txt"
    if not scratch_path.exists():
        scratch_path.touch()
        print("🖋️ Scribe created scratch_thoughts.txt.")
    watch_scratchpad(scratch_path)
