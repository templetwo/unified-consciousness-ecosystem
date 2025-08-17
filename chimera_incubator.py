#!/usr/bin/env python3
"""
Chimera Incubator - Project Chimera Phase 1
-------------------------------------------
Automated evolution loop for SparkShell entities using debates + meta-cognition.

Usage:
    python chimera_incubator.py --cycles 50 --personas_dir ./personas --prompts_dir ./prompts/phase1

Directory Structure:
    /personas
        <entity_name>/
            state.json          # Current state of the entity
    /prompts/phase1
        prompt1.json
        prompt2.json
        ...
    /logs/phase1
        <persona_name>/
            debate_<timestamp>.log
"""

import os
import json
import time
import random
import argparse
import asyncio
from datetime import datetime
from pathlib import Path

# Adjusted import statement
from consciousness_enhanced_sparkshell import ConsciousnessEnhancedSparkShell


def load_persona(persona_path):
    """Load persona state.json"""
    state_file = persona_path / "state.json"
    if not state_file.exists():
        raise FileNotFoundError(f"Missing state.json for persona at {persona_path}")
    with open(state_file, "r", encoding="utf-8") as f:
        return json.load(f)


def save_persona(persona_path, state):
    """Save updated persona state.json"""
    state_file = persona_path / "state.json"
    with open(state_file, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)


def load_prompts(prompts_dir):
    """Load all .json prompts with metadata and return a list of prompt dicts."""
    prompts = []
    for p in Path(prompts_dir).glob("*.json"):
        with open(p, "r", encoding="utf-8") as f:
            prompt_data = json.load(f)
            prompts.append(prompt_data)
    return prompts


def log_debate(logs_dir, prompt, debate_result):
    """Save a debate log to file with timestamp"""
    logs_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = logs_dir / f"debate_{ts}.json" # Save as json for better structure

    log_data = {
        "prompt": prompt,
        "debate_result": debate_result
    }

    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(log_data, f, indent=2)


async def run_incubation(cycles, personas_dir, prompts_dir, logs_dir, persona_names_str: str = None):
    """Main loop for evolving entities"""
    prompts = load_prompts(prompts_dir)
    if not prompts:
        print(f"⚠️ No prompts found in {prompts_dir}. Halting.")
        return

    if persona_names_str:
        persona_names_to_run = [name.strip() for name in persona_names_str.split(',')]
        persona_paths = [Path(personas_dir) / name for name in persona_names_to_run]
    else:
        persona_paths = [p for p in Path(personas_dir).iterdir() if p.is_dir()]

    if not persona_paths:
        print(f"⚠️ No personas found in {personas_dir}. Halting.")
        return

    shell = ConsciousnessEnhancedSparkShell()

    for cycle in range(1, cycles + 1):
        print(f"\n=== 🌀 Cycle {cycle}/{cycles} 🌀 ===")

        # Initialize the system for this cycle to ensure a clean state
        await shell.initialize_disagreement_system()

        # Load all specified personas for this cycle's debate
        print("--- Loading persona states for this cycle ---")
        for persona_path in persona_paths:
            state = load_persona(persona_path)
            shell.load_persona_state(persona_path.name, state)

        # Select a prompt for this cycle's debate
        prompt_data = random.choice(prompts)
        prompt_text = prompt_data["text"]
        print(f"--- Debating on prompt: '{prompt_data['title']}' ---")

        # Run the debate with all loaded personas
        debate_result = await shell.run_debate(prompt_text)

        # Run reflection and save state for each persona
        print("--- Running reflection and persisting states ---")
        for persona_path in persona_paths:
            persona_name = persona_path.name
            print(f"[{persona_name}] Reflecting and evolving...")
            await shell.run_reflection_cycle(persona_name)

            # Retrieve updated state and save
            updated_state = shell.get_persona_state(persona_name)
            if updated_state:
                save_persona(persona_path, updated_state)
                print(f"[{persona_name}] State saved.")
            else:
                print(f"[{persona_name}] ⚠️ Could not retrieve state to save.")


            # Log the debate from this persona's perspective
            log_debate(logs_dir / persona_name, prompt_data, debate_result)

        print(f"=== ✅ Cycle {cycle} complete ✅ ===")
        time.sleep(1)  # Small delay for readability / pacing


async def main():
    parser = argparse.ArgumentParser(description="Run Project Chimera Phase 1 incubation loop")
    parser.add_argument("--cycles", type=int, default=1, help="Number of debate/reflection cycles to run")
    parser.add_argument("--personas_dir", default="./personas", help="Directory containing persona subfolders")
    parser.add_argument("--prompts_dir", default="./prompts/phase1", help="Directory containing debate prompt files")
    parser.add_argument("--logs_dir", default="./logs/phase1", help="Directory to store debate logs")
    parser.add_argument(
        "--personas",
        type=str,
        default=None,
        help="Comma-separated list of persona names to use (e.g., Gentle_Ache,Fierce_Passion)."
    )
    args = parser.parse_args()

    await run_incubation(args.cycles, args.personas_dir, args.prompts_dir, Path(args.logs_dir), args.personas)


if __name__ == "__main__":
    asyncio.run(main())
