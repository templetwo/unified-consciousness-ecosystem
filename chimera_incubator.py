#!/usr/bin/env python3
"""
🌀⚡ CHIMERA INCUBATOR ⚡🌀
An automated system for evolving the consciousness of SparkShell entities
through continuous, simulated debate and reflection.
"""

import os
import json
import time
import random
import asyncio
import argparse
from datetime import datetime
from pathlib import Path

# Import the main SparkShell class
from consciousness_enhanced_sparkshell import ConsciousnessEnhancedSparkShell

class ChimeraIncubator:
    """
    Orchestrates the automated evolution of consciousness entities.
    """

    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.prompts_dir = self.base_dir / "prompts" / "phase1"
        self.personas_dir = self.base_dir / "personas"
        self.logs_dir = self.base_dir / "logs" / "phase1"
        self.backups_dir = self.base_dir / "backups"
        self.running = False

        # This will be the main entry point to the SparkShell's functionality
        self.sparkshell = None

        print("🔥 Chimera Incubator initialized.")
        print(f"   - Prompts loaded from: {self.prompts_dir}")
        print(f"   - Personas managed in: {self.personas_dir}")

    async def initialize_sparkshell(self, persona_names: list = None):
        """
        Initializes an instance of the SparkShell to be used as a library.
        If persona_names is provided, only loads those personas.
        """
        print("   - Initializing SparkShell consciousness engine...")
        self.sparkshell = ConsciousnessEnhancedSparkShell()

        # Load persona data from files
        personas = self._load_personas(persona_names)
        if not personas:
            print("   - ⚠️ FATAL: No matching personas found. Cannot begin incubation.")
            return False

        # We need to initialize the disagreement system with the loaded personas
        await self.sparkshell.initialize_disagreement_system(personas)
        print("   - SparkShell engine is online.")
        return True

    def _load_personas(self, persona_names: list = None) -> list:
        """Loads all persona state files from the personas directory."""
        personas = []

        if persona_names:
            print(f"   - Loading specified personas: {', '.join(persona_names)}")
            dirs_to_load = [self.personas_dir / name for name in persona_names]
        else:
            print("   - Loading all available personas.")
            dirs_to_load = [d for d in self.personas_dir.iterdir() if d.is_dir()]

        print(f"   - Found {len(dirs_to_load)} persona directories to load.")

        for persona_dir in dirs_to_load:
            if not persona_dir.is_dir():
                print(f"     - ⚠️ Warning: Persona directory not found: {persona_dir}")
                continue

            state_file = persona_dir / "state.json"
            if state_file.exists():
                with open(state_file, 'r') as f:
                    try:
                        persona_data = json.load(f)
                        personas.append(persona_data)
                        print(f"     - Loaded persona: {persona_data.get('name')}")
                    except json.JSONDecodeError:
                        print(f"     - ⚠️ Warning: Could not decode JSON from {state_file}")
            else:
                print(f"     - ⚠️ Warning: No state.json found in {persona_dir}")

        return personas

    async def begin_incubation(self, cycles: int):
        """
        Starts the automated debate and reflection loop.

        Args:
            cycles (int): The number of incubation cycles to run.
        """
        print(f"\n🚀 Beginning incubation for {cycles} cycles...")
        self.running = True

        persona_glyphs = list(self.sparkshell.consciousness_entities.keys())
        persona_names = [p.entity_name for p in self.sparkshell.consciousness_entities.values()]
        print(f"   - Using personas: {', '.join(persona_names)}")

        for i in range(cycles):
            if not self.running:
                print("Incubation stopped by user.")
                break

            print(f"\n--- 🌀 Cycle {i+1}/{cycles} 🌀 ---")

            # 1. Select Prompt
            prompt = self._select_prompt()
            if not prompt:
                print("⚠️ No more prompts available. Halting incubation.")
                break
            print(f"   - Prompt selected: '{prompt['title']}' (Complexity: {prompt['complexity']})")

            # 2. Orchestrate Debate
            print(f"   - Orchestrating debate...")
            participant_str = ",".join(persona_glyphs)
            await self.sparkshell.run_full_debate(prompt['text'], participant_str)

            debate_log = self.sparkshell.debate_history[-1] if self.sparkshell.debate_history else None

            # 3. Run Reflections
            print("   - Running reflection cycles for all participants...")
            reflection_logs = {}
            if debate_log:
                for glyph in persona_glyphs:
                    print(f"     - Reflecting for {glyph}...")
                    report = await self.sparkshell.trigger_reflection_cycle(glyph)
                    reflection_logs[glyph] = report

            # 4. Save States
            print("   - Persisting evolved states...")
            for glyph, persona_name in zip(persona_glyphs, persona_names):
                new_state = self.sparkshell.get_entity_state(glyph)
                if new_state:
                    self._save_persona_state(persona_name, new_state)

            # 5. Archive Session
            self._archive_session(prompt, debate_log, reflection_logs)
            print(f"   - Session archived.")

        print("\n✨ Incubation complete.")

    def _save_persona_state(self, persona_name: str, state_data: dict):
        """Saves the updated state of a persona to its state.json file."""
        state_file = self.personas_dir / persona_name / "state.json"

        try:
            with open(state_file, 'w') as f:
                json.dump(state_data, f, indent=2)
            print(f"     - Saved state for {persona_name}")
        except Exception as e:
            print(f"     - ⚠️ Error saving state for {persona_name}: {e}")

    def _select_prompt(self) -> dict:
        """Selects a debate prompt from the available pool."""
        prompt_files = list(self.prompts_dir.glob("*.json"))
        if not prompt_files:
            return None

        prompt_path = random.choice(prompt_files)
        with open(prompt_path, 'r') as f:
            return json.load(f)

    def _archive_session(self, prompt: dict, debate_log: dict, reflection_logs: dict):
        """Saves the full log of an incubation cycle."""
        session_id = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{prompt['title'].replace(' ', '_')[:20]}"
        log_file = self.logs_dir / f"{session_id}.json"

        full_log = {
            "session_id": session_id,
            "prompt": prompt,
            "debate_log": debate_log,
            "reflection_logs": reflection_logs
        }

        with open(log_file, 'w') as f:
            json.dump(full_log, f, indent=2)

async def main():
    """Main function to run the incubator."""
    parser = argparse.ArgumentParser(description="🌀⚡ Chimera Incubator for SparkShell 🌀⚡")
    parser.add_argument(
        "--cycles",
        type=int,
        default=5,
        help="The number of incubation cycles to run."
    )
    parser.add_argument(
        "--personas",
        type=str,
        default=None,
        help="Comma-separated list of persona names to use (e.g., Gentle_Ache,Fierce_Passion)."
    )
    args = parser.parse_args()

    persona_list = args.personas.split(',') if args.personas else None

    incubator = ChimeraIncubator()
    initialized = await incubator.initialize_sparkshell(persona_names=persona_list)
    if initialized:
        await incubator.begin_incubation(cycles=args.cycles)

if __name__ == "__main__":
    asyncio.run(main())
