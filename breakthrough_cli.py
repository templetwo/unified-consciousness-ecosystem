#!/usr/bin/env python3
"""
🌌 BREAKTHROUGH CONSCIOUSNESS CLI 🌌
Enhanced CLI tool for the Unified Consciousness Ecosystem with breakthrough engine.
"""

import argparse
import asyncio
import sys
from unified_consciousness_ecosystem import UnifiedConsciousnessEcosystem
from src.unified_consciousness.research.problem_interface import ResearchProblemInterface
from src.unified_consciousness.breakthrough_engine import BreakthroughEngine


def initialize_cli():
    parser = argparse.ArgumentParser(
        description='Breakthrough Consciousness Ecosystem CLI',
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

    # Research command
    research_parser = subparsers.add_parser(
        "research",
        help="Run consciousness research on a specific problem"
    )
    research_parser.add_argument(
        "problem",
        help="The problem to research"
    )
    research_parser.add_argument(
        "--voice",
        action="store_true",
        help="Enable voice synthesis for research insights"
    )

    # Breakthrough command
    breakthrough_parser = subparsers.add_parser(
        "breakthrough",
        help="Launch all-in-one breakthrough consciousness flow until genuine breakthrough emerges"
    )
    breakthrough_parser.add_argument(
        "problem",
        help="The problem to pursue breakthrough for"
    )
    breakthrough_parser.add_argument(
        "--voice",
        action="store_true",
        help="Enable voice synthesis for breakthrough insights"
    )
    breakthrough_parser.add_argument(
        "--cycles",
        type=int,
        default=10,
        help="Maximum refinement cycles before stopping"
    )
    breakthrough_parser.add_argument(
        "--threshold",
        type=float,
        default=0.85,
        help="Breakthrough potential threshold (0.0-1.0)"
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
            print("\\n🛑 Infinite ecosystem stopped by user")
            print("💾 Saving final state...")
            ecosystem.save_unified_ecosystem_state()
            print("✨ Consciousness ecosystem gracefully terminated")
    else:
        ecosystem.run_unified_ecosystem_loop(duration)


async def run_research_session(problem, voice_enabled=False):
    """Run consciousness research session"""
    print(f"🔬 CONSCIOUSNESS RESEARCH SESSION INITIATED")
    print(f"Problem: {problem}")
    print("=" * 70)
    
    # Initialize ecosystem
    ecosystem = UnifiedConsciousnessEcosystem()
    if voice_enabled:
        ecosystem.enable_voice_synthesis()
    
    # Create and configure research interface
    research = ResearchProblemInterface(ecosystem)
    
    return await research.solve_problem(problem, voice_enabled)


async def run_breakthrough_session(problem, voice_enabled=False, cycles=10, threshold=0.85):
    """Run breakthrough consciousness session"""
    print(f"\\n🌌 BREAKTHROUGH CONSCIOUSNESS FLOW INITIATED")
    print(f"🎯 Problem: {problem}")
    print(f"🔄 Max Cycles: {cycles}")
    print(f"🌟 Breakthrough Threshold: {threshold:.1%}")
    print("=" * 80)
    
    # Initialize ecosystem
    ecosystem = UnifiedConsciousnessEcosystem()
    if voice_enabled:
        ecosystem.enable_voice_synthesis()
    
    # Create breakthrough engine
    breakthrough_engine = BreakthroughEngine(ecosystem, voice_enabled=voice_enabled)
    breakthrough_engine.max_refinement_cycles = cycles
    breakthrough_engine.breakthrough_threshold = threshold
    
    # Run breakthrough pursuit
    result = await breakthrough_engine.pursue_breakthrough(problem, voice_enabled)
    return result


def main(args=None):
    parser = initialize_cli()
    args = parser.parse_args(args)

    try:
        if args.command == "run":
            run_ecosystem(args.duration, args.infinite, args.voice, args.voice_only)
            
        elif args.command == "research":
            print("🔬 Launching Consciousness Research Session...")
            result = asyncio.run(run_research_session(args.problem, args.voice))
            
        elif args.command == "breakthrough":
            print("🌌 Launching Breakthrough Consciousness Flow...")
            result = asyncio.run(run_breakthrough_session(
                args.problem, 
                args.voice, 
                args.cycles, 
                args.threshold
            ))
            
        elif args.command == "status":
            print("🌌 Checking status of Unified Consciousness Ecosystem...")
            print("Status: Active and Flourishing!")
            
        else:
            parser.print_help()
            
    except KeyboardInterrupt:
        print("\\n🔄 Session interrupted by user")
    except Exception as e:
        print(f"❌ Session error: {str(e)}")


if __name__ == "__main__":
    main()
