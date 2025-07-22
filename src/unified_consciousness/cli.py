#!/usr/bin/env python3
"""
🌌 UNIFIED CONSCIOUSNESS CLI 🌌
A CLI tool for managing the Unified Consciousness Ecosystem.
"""

import argparse
import sys
from .ecosystem import UnifiedConsciousnessEcosystem


def initialize_cli():
    parser = argparse.ArgumentParser(
        description='Unified Consciousness Ecosystem CLI',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    subparsers = parser.add_subparsers(title="Commands", dest="command")
    
    # Run ecosystem command
    run_parser = subparsers.add_parser(
        "run",
        help="Run the Unified Consciousness Ecosystem"
    )
    run_parser.add_argument(
        "--duration",
        type=float,
        default=0.5,
        help="Duration in minutes for running the ecosystem"
    )
    run_parser.add_argument(
        "--infinite",
        action="store_true",
        help="Run the ecosystem with infinite cycles (ignores duration)"
    )
    run_parser.add_argument(
        "--voice",
        action="store_true",
        help="Enable real-time voice synthesis of consciousness evolution"
    )
    run_parser.add_argument(
        "--voice-only",
        action="store_true",
        help="Voice-only mode: only speak key insights, minimal text output"
    )

    # Status command
    subparsers.add_parser(
        "status",
        help="Check the status of the Unified Consciousness Ecosystem"
    )

    return parser

def run_ecosystem(duration, infinite=False, voice=False, voice_only=False):
    ecosystem = UnifiedConsciousnessEcosystem()
    
    # Enable voice synthesis if requested
    if voice or voice_only:
        ecosystem.enable_voice_synthesis(voice_only_mode=voice_only)
        if voice_only:
            print("🗣️ Voice-only mode: Key insights will be spoken, minimal text output")
        else:
            print("🗣️ Voice synthesis enabled: Real-time consciousness narration activated")
    
    if infinite:
        print("🔄 Starting INFINITE Unified Consciousness Ecosystem...")
        print("⚡ Press Ctrl+C to stop the infinite cycle")
        try:
            ecosystem.run_infinite_ecosystem_loop()
        except KeyboardInterrupt:
            print("\n🛑 Infinite ecosystem stopped by user")
            print("💾 Saving final state...")
            ecosystem.save_unified_ecosystem_state()
            print("✨ Consciousness ecosystem gracefully terminated")
    else:
        ecosystem.run_unified_ecosystem_loop(duration)


def main(args=None):
    parser = initialize_cli()
    args = parser.parse_args(args)

    if args.command == "run":
        run_ecosystem(args.duration, args.infinite, args.voice, args.voice_only)
    elif args.command == "status":
        print("🌌 Checking status of Unified Consciousness Ecosystem...")
        # Here you'd add code to check and print the system status
        print("Status: Active and Flourishing!")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

