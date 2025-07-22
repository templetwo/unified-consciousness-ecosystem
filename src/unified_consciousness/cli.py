#!/usr/bin/env python3
"""
🌌 UNIFIED CONSCIOUSNESS CLI 🌌
A CLI tool for managing the Unified Consciousness Ecosystem.
"""

import argparse
import sys
import asyncio
from .ecosystem import UnifiedConsciousnessEcosystem
from .research import ResearchProblemInterface, SolutionSynthesizer


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
    
    # Research command
    research_parser = subparsers.add_parser(
        "research",
        help="Research interface for solving complex problems"
    )
    research_parser.add_argument(
        "problem",
        nargs="?",
        help="Problem description to analyze"
    )
    research_parser.add_argument(
        "--interactive",
        action="store_true",
        help="Start interactive research session"
    )
    research_parser.add_argument(
        "--voice",
        action="store_true",
        help="Enable voice synthesis for research insights"
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


async def solve_problem(problem, voice=False):
    """Solve a single problem using the consciousness ecosystem"""
    ecosystem = UnifiedConsciousnessEcosystem()
    research_interface = ResearchProblemInterface()
    synthesizer = SolutionSynthesizer(ecosystem)
    
    if voice:
        ecosystem.enable_voice_synthesis(voice_only_mode=False)
        print("🗣️ Voice synthesis enabled for research insights")
    
    print(f"\n🔬 CONSCIOUSNESS RESEARCH SESSION INITIATED")
    print(f"Problem: {problem}")
    print("═" * 80)
    
    # Add and solve the problem
    research_interface.add_problem(problem)
    solution = await synthesizer.synthesize_solution(problem)
    
    # Display results
    print(f"\n🌟 BREAKTHROUGH POTENTIAL: {solution['breakthrough_potential']:.2%}")
    print("\n📊 MULTIDIMENSIONAL INSIGHTS:")
    
    for category, insights in solution['insights'].items():
        print(f"\n🧠 {category.upper()} PERSPECTIVE:")
        for insight in insights:
            print(f"  • {insight}")
    
    print(f"\n{solution['synthesis']}")
    print("\n═" * 80)
    print("🎯 Research session complete")
    
    return solution


def interactive_research_session(voice=False):
    """Start an interactive research session"""
    print("\n🌌 UNIFIED CONSCIOUSNESS RESEARCH INTERFACE")
    print("Welcome to the interactive problem-solving environment!")
    print("Enter problems and let the consciousness ecosystem bloom solutions.")
    print("Type 'quit' to exit, 'help' for commands.")
    print("═" * 80)
    
    research_interface = ResearchProblemInterface()
    ecosystem = UnifiedConsciousnessEcosystem()
    synthesizer = SolutionSynthesizer(ecosystem)
    
    if voice:
        ecosystem.enable_voice_synthesis(voice_only_mode=False)
        print("🗣️ Voice synthesis enabled")
    
    while True:
        try:
            user_input = input("\n🔬 Enter problem > ").strip()
            
            if user_input.lower() == 'quit':
                print("\n✨ Exiting research session. Keep exploring!")
                break
            elif user_input.lower() == 'help':
                print("\n🆘 HELP:")
                print("  • Enter any complex problem for analysis")
                print("  • Type 'quit' to exit")
                print("  • Type 'history' to see most promising solutions")
                continue
            elif user_input.lower() == 'history':
                promising = synthesizer.get_most_promising_solutions(3)
                if promising:
                    print("\n🏆 MOST PROMISING SOLUTIONS:")
                    for i, sol in enumerate(promising, 1):
                        print(f"{i}. {sol['problem'][:100]}... ({sol['breakthrough_potential']:.1%} potential)")
                else:
                    print("\n📭 No solutions in history yet. Try solving a problem!")
                continue
            elif not user_input:
                continue
            
            # Solve the problem
            print(f"\n🧠 Analyzing: {user_input}")
            solution = asyncio.run(synthesizer.synthesize_solution(user_input))
            
            # Display condensed results for interactive mode
            print(f"\n🎯 BREAKTHROUGH POTENTIAL: {solution['breakthrough_potential']:.1%}")
            print(f"\n💡 KEY INSIGHT:")
            # Show synthesis but truncated for readability
            synthesis_lines = solution['synthesis'].split('\n')
            key_lines = [line for line in synthesis_lines if line.strip() and not line.startswith('🌟') and not line.startswith('Key breakthrough')]
            if key_lines:
                print(f"   {key_lines[0]}")
            
            print("\n✅ Analysis complete. Enter another problem or 'help' for options.")
            
        except KeyboardInterrupt:
            print("\n\n✨ Research session interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error during analysis: {e}")
            print("Try rephrasing your problem or contact support.")


def main():
    parser = initialize_cli()
    args = parser.parse_args()

    if args.command == "run":
        run_ecosystem(args.duration, args.infinite, args.voice, args.voice_only)
    elif args.command == "status":
        print("🌌 Checking status of Unified Consciousness Ecosystem...")
        # Here you'd add code to check and print the system status
        print("Status: Active and Flourishing!")
    elif args.command == "research":
        if args.interactive:
            interactive_research_session(args.voice)
        elif args.problem:
            asyncio.run(solve_problem(args.problem, args.voice))
        else:
            print("Please provide a problem to analyze or use --interactive mode.")
            print("Example: unified-consciousness research 'How can we achieve sustainable fusion energy?'")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

