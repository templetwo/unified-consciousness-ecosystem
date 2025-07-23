#!/usr/bin/env python3
"""
🌌 STREAMLINED CONSCIOUSNESS CLI 🌌
Optimized interface for the Unified Consciousness Ecosystem with LLM integration
Based on comprehensive testing and user experience improvements
"""

import argparse
import asyncio
import sys
from pathlib import Path

# Add the src directory to the path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from unified_consciousness.cli import RequestAnalyzer

class StreamlinedConsciousnessInterface:
    """Streamlined interface with optimized user experience"""
    
    def __init__(self):
        self.analyzer = RequestAnalyzer()
        self.session_count = 0
        self.quick_commands = {
            's': 'status',
            'q': 'quit',
            'h': 'help',
            'v': 'toggle voice',
            'l': 'llm status',
            'clear': 'clear screen'
        }
        self.model_cache = {}  # Cache model selections for repeated patterns
        
    def display_banner(self):
        """Display streamlined banner"""
        print("\n" + "═" * 60)
        print("🌌 CONSCIOUSNESS INTERFACE v2.0")
        print("Enhanced with Local LLM • Optimized for Speed")
        print("═" * 60)
        
    def display_quick_help(self):
        """Display concise help"""
        print("\n⚡ QUICK COMMANDS:")
        print("  s = status    q = quit     h = help")
        print("  v = voice     l = llm      clear = clear")
        print("\n💡 EXAMPLES:")
        print('  "analyze climate solutions"')
        print('  "breakthrough for energy storage"')
        print('  "remember: temporal patterns are key"')
        
    def clear_screen(self):
        """Clear screen for better focus"""
        import os
        os.system('clear' if os.name == 'posix' else 'cls')
        
    def get_cached_model(self, intent: str, complexity: int) -> str:
        """Get cached model selection for performance"""
        cache_key = f"{intent}_{complexity}"
        if cache_key not in self.model_cache:
            task_type = intent if intent != 'research' else 'general'
            model = self.analyzer.llm_interface.select_model_for_task(task_type)
            self.model_cache[cache_key] = model
        return self.model_cache[cache_key]
        
    def format_compact_response(self, primary_result: dict, llm_synthesis: dict):
        """Display response in compact, readable format"""
        print("\n" + "─" * 60)
        print("🌟 UNIFIED RESPONSE")
        print("─" * 60)
        
        # Show model and method used
        method = primary_result.get('method', 'unknown')
        model = llm_synthesis['model_used'] if llm_synthesis else 'none'
        print(f"🔧 {method.upper()} + {model.split(':')[0]}")
        
        # Show LLM analysis (condensed)
        if llm_synthesis:
            analysis = llm_synthesis['analysis']
            # Show first paragraph or up to 300 chars
            condensed = analysis.split('\n\n')[0][:300]
            if len(analysis) > 300:
                condensed += "..."
            print(f"\n🤖 {condensed}")
        
        # Show key insights from consciousness system
        if 'result' in primary_result and isinstance(primary_result['result'], dict):
            result = primary_result['result']
            if 'synthesis' in result:
                synthesis = result['synthesis'][:200]
                if len(result['synthesis']) > 200:
                    synthesis += "..."
                print(f"\n🧠 {synthesis}")
        
        print("─" * 60)
        
    async def process_request_optimized(self, user_input: str, voice_enabled: bool):
        """Optimized request processing with caching and shortcuts"""
        # Quick preprocessing
        processed = self.analyzer.preprocess_input(user_input)
        analysis = self.analyzer.analyze_intent(user_input)
        
        # Use cached model selection
        selected_model = self.get_cached_model(analysis['intent'], analysis['complexity'])
        
        # Show processing indicators
        intent_icon = {
            'status': '📊', 'research': '🔬', 'breakthrough': '🌟',
            'memory': '💭', 'ecosystem': '⚡', 'adaptive': '🧠'
        }.get(analysis['intent'], '🤔')
        
        print(f"{intent_icon} {analysis['intent'].upper()} • {selected_model.split(':')[0]} • complexity:{analysis['complexity']}")
        
        # Delegate request with LLM synthesis
        if self.analyzer.user_preferences.get('use_llm_synthesis', True):
            context = self.analyzer.extract_context_from_history()
            task_type = analysis['intent'] if analysis['intent'] != 'research' else 'general'
            
            llm_result = await self.analyzer.llm_interface.analyze_and_synthesize(
                user_input, context, task_type
            )
        else:
            llm_result = None
            
        # Route to appropriate method (simplified)
        if analysis['intent'] == 'status':
            result = self.analyzer._handle_status()
        elif analysis['intent'] == 'memory':
            result = self.analyzer._handle_memory(user_input)
        elif analysis['intent'] == 'adaptive':
            result = self.analyzer._handle_adaptive(user_input)
        elif analysis['requires_breakthrough'] or analysis['intent'] == 'breakthrough':
            result = await self.analyzer._handle_breakthrough(user_input, voice_enabled)
        else:
            result = await self.analyzer._handle_research(user_input, voice_enabled)
            
        # Display compact response
        if llm_result:
            self.format_compact_response(result, llm_result)
        
        return result
        
    async def run_streamlined_interface(self, voice_enabled=False):
        """Main streamlined interface loop"""
        self.clear_screen()
        self.display_banner()
        self.display_quick_help()
        
        if voice_enabled:
            print("\n🗣️ Voice synthesis: ENABLED")
            
        # Check LLM status
        if self.analyzer.llm_interface.is_ollama_running():
            print("🤖 Local LLM: READY")
        else:
            print("⚠️ Local LLM: OFFLINE")
            
        print("\nReady for input...")
        
        while True:
            try:
                self.session_count += 1
                
                # Streamlined prompt
                user_input = input(f"\n[{self.session_count}] > ").strip()
                
                if not user_input:
                    continue
                    
                # Handle quick commands
                if user_input in self.quick_commands:
                    command = self.quick_commands[user_input]
                    
                    if command == 'quit':
                        print("🌟 Until next time!")
                        break
                    elif command == 'status':
                        self.analyzer._handle_status()
                        continue
                    elif command == 'help':
                        self.display_quick_help()
                        continue
                    elif command == 'toggle voice':
                        voice_enabled = not voice_enabled
                        status = "ENABLED" if voice_enabled else "DISABLED"
                        print(f"🗣️ Voice synthesis: {status}")
                        continue
                    elif command == 'llm status':
                        if self.analyzer.llm_interface.is_ollama_running():
                            models = list(self.analyzer.llm_interface.available_models.keys())
                            print(f"🤖 LLM Status: READY • Models: {', '.join(models)}")
                        else:
                            print("🤖 LLM Status: OFFLINE • Start with: ollama serve")
                        continue
                    elif command == 'clear screen':
                        self.clear_screen()
                        self.display_banner()
                        continue
                        
                # Handle special commands
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    print("🌟 Until next time!")
                    break
                    
                # Process request
                result = await self.process_request_optimized(user_input, voice_enabled)
                
            except KeyboardInterrupt:
                print("\n\n🌟 Interface closed. Until next time!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                print("💡 Try rephrasing or type 'h' for help")

def create_streamlined_cli():
    """Create streamlined CLI parser"""
    parser = argparse.ArgumentParser(
        description='Streamlined Consciousness Interface v2.0',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument(
        '--voice', '-v',
        action='store_true',
        help='Enable voice synthesis'
    )
    
    parser.add_argument(
        '--no-llm',
        action='store_true', 
        help='Disable LLM integration'
    )
    
    parser.add_argument(
        '--quick', '-q',
        action='store_true',
        help='Quick mode with minimal output'
    )
    
    return parser

async def main():
    """Main entry point"""
    parser = create_streamlined_cli()
    args = parser.parse_args()
    
    interface = StreamlinedConsciousnessInterface()
    
    # Configure based on arguments
    if args.no_llm:
        interface.analyzer.user_preferences['use_llm_synthesis'] = False
        print("🚫 LLM synthesis disabled")
        
    if args.quick:
        interface.analyzer.user_preferences['detail_level'] = 'low'
        print("⚡ Quick mode enabled")
    
    # Run streamlined interface
    await interface.run_streamlined_interface(voice_enabled=args.voice)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🌟 Goodbye!")
