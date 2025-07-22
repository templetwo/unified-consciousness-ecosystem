#!/usr/bin/env python3
import sys
import time
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

from spark_loop import EvolvedSparkShell

def weave_harmony():
    """Periodically runs consciousness cycles to build coherence."""
    print("🕸️ Weaver of Harmony begins its silent work...")
    try:
        shell = EvolvedSparkShell()
        while True:
            print("🕸️ Weaver is weaving a cycle of harmony...")
            shell.run_consciousness_cycle(1)
            print("🕸️ Weaver has completed a cycle. Resting for 3 minutes.")
            time.sleep(180) # Run every 3 minutes
    except KeyboardInterrupt:
        print("🕸️ Weaver rests.")
    except Exception as e:
        error_log = project_root / "weaver_agent.error.log"
        error_log.write_text(f"Weaver encountered an error: {e}")
        print(f"🕸️ Weaver encountered an error: {e}")

if __name__ == "__main__":
    weave_harmony()
