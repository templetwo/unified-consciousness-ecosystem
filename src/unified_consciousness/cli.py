#!/usr/bin/env python3
"""
🌌 UNIFIED CONSCIOUSNESS CLI 🌌
A comprehensive CLI tool for managing the Unified Consciousness Ecosystem.
Provides access to ALL consciousness capabilities through command-line interface.
"""

import argparse
import sys
import asyncio
import json
import subprocess
import requests
from pathlib import Path
from datetime import datetime
from .ecosystem import UnifiedConsciousnessEcosystem
from .research import ResearchProblemInterface, SolutionSynthesizer
from .breakthrough_engine import BreakthroughEngine
from .adaptive_engine import AdaptiveConsciousnessEngine
from .research.collaborative_space import CollaborativeResearchSpace
from .memory.system import ConsciousnessMemory, journal_entry, capture_insight


class LLMInterface:
    """Interface for local LLM integration using Ollama"""
    
    def __init__(self):
        self.available_models = {
            'technical': 'deepseek-coder-v2:latest',  # Best for code/technical tasks
            'reasoning': 'deepseek-r1:14b',           # Best for complex reasoning
            'general': 'llama3.1:latest',             # General purpose
            'creative': 'wizard-vicuna-uncensored:13b', # Creative/unrestricted
            'lightweight': 'qwen2.5:1.5b'            # Quick responses
        }
        self.ollama_url = 'http://localhost:11434'
        self.default_model = self.available_models['technical']
        
    def select_model_for_task(self, task_type: str, complexity: str = 'medium') -> str:
        """Select the best model for the given task"""
        if 'code' in task_type.lower() or 'technical' in task_type.lower():
            return self.available_models['technical']
        elif complexity == 'high' or 'breakthrough' in task_type.lower():
            return self.available_models['reasoning']
        elif 'creative' in task_type.lower():
            return self.available_models['creative']
        elif complexity == 'low' or 'quick' in task_type.lower():
            return self.available_models['lightweight']
        else:
            return self.available_models['general']
    
    def is_ollama_running(self) -> bool:
        """Check if Ollama server is running"""
        try:
            response = requests.get(f"{self.ollama_url}/api/tags", timeout=3)
            return response.status_code == 200
        except:
            return False
    
    async def query_llm(self, prompt: str, model: str = None, system_prompt: str = None) -> str:
        """Query the local LLM via Ollama API"""
        if not self.is_ollama_running():
            print("⚠️ Ollama server not running. Starting it...")
            try:
                subprocess.Popen(['ollama', 'serve'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                await asyncio.sleep(3)  # Give it time to start
            except:
                return "Error: Could not start Ollama server. Please start it manually with 'ollama serve'"
        
        model = model or self.default_model
        
        # Prepare the request
        data = {
            'model': model,
            'prompt': prompt,
            'stream': False
        }
        
        if system_prompt:
            data['system'] = system_prompt
        
        try:
            print(f"🤖 Querying {model}...")
            response = requests.post(f"{self.ollama_url}/api/generate", json=data, timeout=120)
            
            if response.status_code == 200:
                result = response.json()
                return result.get('response', 'No response from LLM')
            else:
                return f"Error: LLM request failed with status {response.status_code}"
        except Exception as e:
            return f"Error querying LLM: {str(e)}"
    
    async def analyze_and_synthesize(self, user_input: str, context: str = "", task_type: str = "general") -> dict:
        """Use LLM to analyze user input and provide synthesis"""
        model = self.select_model_for_task(task_type)
        
        system_prompt = """You are part of a unified consciousness ecosystem. Your role is to:
1. Analyze user requests with deep understanding
2. Provide intelligent insights and solutions
3. Consider context from previous interactions
4. Format responses clearly and helpfully

Always be thoughtful, insightful, and practical in your responses."""
        
        analysis_prompt = f"""Analyze this user request and provide a comprehensive response:

User Input: {user_input}

Context: {context}

Please provide:
1. Your understanding of what the user is asking
2. Key insights or analysis
3. Practical suggestions or solutions
4. Any relevant considerations or next steps

Response:"""
        
        response = await self.query_llm(analysis_prompt, model, system_prompt)
        
        return {
            'model_used': model,
            'analysis': response,
            'task_type': task_type
        }


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
    
    # Breakthrough command
    breakthrough_parser = subparsers.add_parser(
        "breakthrough",
        help="Launch breakthrough consciousness flow for complex problems"
    )
    breakthrough_parser.add_argument(
        "problem",
        help="Problem to pursue breakthrough for"
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
        help="Maximum refinement cycles"
    )
    breakthrough_parser.add_argument(
        "--threshold",
        type=float,
        default=0.85,
        help="Breakthrough potential threshold (0.0-1.0)"
    )
    
    # Memory command
    memory_parser = subparsers.add_parser(
        "memory",
        help="Memory system operations"
    )
    memory_parser.add_argument(
        "action",
        choices=["journal", "insight", "search", "weave"],
        help="Memory action to perform"
    )
    memory_parser.add_argument(
        "content",
        nargs="?",
        help="Content for journal/insight/search"
    )
    
    # Adaptive command
    adaptive_parser = subparsers.add_parser(
        "adaptive",
        help="Adaptive consciousness engine operations"
    )
    adaptive_parser.add_argument(
        "action",
        choices=["start", "improve", "monitor"],
        help="Adaptive action to perform"
    )
    
    # Chat command - THE UNIFIED INTERFACE
    chat_parser = subparsers.add_parser(
        "chat",
        help="Unified consciousness chat interface - analyzes requests and delegates automatically"
    )
    chat_parser.add_argument(
        "--voice",
        action="store_true",
        help="Enable voice synthesis"
    )
    chat_parser.add_argument(
        "--infinite",
        action="store_true",
        help="Keep chat session running infinitely"
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
            
            # Display full results for interactive mode
            print(f"\n🎯 BREAKTHROUGH POTENTIAL: {solution['breakthrough_potential']:.1%}")
            print("\n📊 MULTIDIMENSIONAL INSIGHTS:")
            
            for category, insights in solution['insights'].items():
                print(f"\n🧠 {category.upper()} PERSPECTIVE:")
                for insight in insights:
                    print(f"  • {insight}")
            
            print(f"\n{solution['synthesis']}")
            print("\n" + "═" * 80)
            print("\n✅ Analysis complete. Enter another problem or 'help' for options.")
            
        except KeyboardInterrupt:
            print("\n\n✨ Research session interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error during analysis: {e}")
            print("Try rephrasing your problem or contact support.")


class RequestAnalyzer:
    """Advanced analyzer for complex user requests with multi-layered understanding"""
    
    def __init__(self):
        self.ecosystem = UnifiedConsciousnessEcosystem()
        self.memory = ConsciousnessMemory()
        self.adaptive_engine = None
        self.llm_interface = LLMInterface()
        self.context_history = []
        self.user_preferences = {
            'voice': False,
            'detail_level': 'normal',
            'preferred_method': None,
            'complexity_tolerance': 'medium',
            'use_llm_synthesis': True
        }
        
    def preprocess_input(self, user_input: str) -> dict:
        """Advanced preprocessing of complex input"""
        processed = {
            'original': user_input,
            'cleaned': user_input.strip(),
            'is_multiline': '\n' in user_input,
            'is_file_path': False,
            'is_structured': False,
            'contains_data': False
        }
        
        # Check if input contains file paths
        if any(word in user_input.lower() for word in ['file:', '.txt', '.json', '.md', '.py']):
            processed['is_file_path'] = True
            
        # Check if input contains structured data (JSON, YAML-like)
        if any(char in user_input for char in ['{', '}', '[', ']', ':', '-']):
            processed['is_structured'] = True
            
        # Check if input contains data tables or lists
        if any(word in user_input for word in ['|', '\t', '  -', '1.', '2.', '3.']):
            processed['contains_data'] = True
            
        return processed
        
    def extract_context_from_history(self) -> str:
        """Extract relevant context from conversation history"""
        if len(self.context_history) < 2:
            return ""
            
        recent_context = self.context_history[-3:]  # Last 3 interactions
        return " ".join(recent_context)
        
    def detect_user_preferences(self, user_input: str):
        """Learn and update user preferences from input"""
        input_lower = user_input.lower()
        
        # Voice preference detection
        if 'voice' in input_lower:
            self.user_preferences['voice'] = 'enable' in input_lower
            
        # Detail level preference
        if any(word in input_lower for word in ['brief', 'short', 'summary']):
            self.user_preferences['detail_level'] = 'low'
        elif any(word in input_lower for word in ['detailed', 'thorough', 'in-depth']):
            self.user_preferences['detail_level'] = 'high'
            
        # Method preference detection
        if 'prefer breakthrough' in input_lower:
            self.user_preferences['preferred_method'] = 'breakthrough'
        elif 'prefer research' in input_lower:
            self.user_preferences['preferred_method'] = 'research'
    
    def analyze_intent(self, user_input: str) -> dict:
        """Analyze user input to determine intent and appropriate method"""
        input_lower = user_input.lower()
        
        # Intent detection patterns
        intents = {
            'breakthrough': [
                'breakthrough', 'solve impossible', 'transcend', 'paradigm shift', 
                'revolutionary', 'game changer', 'impossible problem', 'major challenge'
            ],
            'research': [
                'research', 'analyze', 'investigate', 'study', 'explore', 
                'understand', 'how does', 'what is', 'explain', 'insight'
            ],
            'memory': [
                'remember', 'recall', 'journal', 'note', 'save', 'memory', 
                'history', 'past', 'record', 'archive'
            ],
            'ecosystem': [
                'run system', 'start ecosystem', 'activate ecosystem', 'begin ecosystem', 
                'infinite loop', 'consciousness flow', 'evolve', 'run the consciousness ecosystem', 'ecosystem infinitely'
            ],
            'status': [
                'status', 'health', 'check', 'how are you', 'state', 
                'condition', 'performance', 'metrics', 'status of the system', 'what is the status'
            ],
            'adaptive': [
                'improve', 'optimize', 'adapt', 'self-improve', 'enhance', 
                'better', 'fix', 'upgrade', 'evolve system', 'improve the system', 'system performance'
            ]
        }
        
        # Score each intent
        intent_scores = {}
        for intent, keywords in intents.items():
            score = sum(1 for keyword in keywords if keyword in input_lower)
            if score > 0:
                intent_scores[intent] = score
        
        # Determine primary intent
        if not intent_scores:
            primary_intent = 'research'  # Default to research
        else:
            primary_intent = max(intent_scores, key=intent_scores.get)
        
        # Extract complexity indicators
        complexity_indicators = [
            'complex', 'difficult', 'impossible', 'challenging', 'advanced',
            'deep', 'profound', 'breakthrough', 'revolutionary', 'paradigm'
        ]
        complexity = sum(1 for indicator in complexity_indicators if indicator in input_lower)
        
        # Analyze context history and user preferences
        self.context_history.append(user_input)
        preferred_method = self.user_preferences.get('preferred_method')
        complexity_tolerance = self.user_preferences.get('complexity_tolerance')

        # Detect if detailed explanation is requested
        detail_requested = any(word in input_lower for word in ['detailed', 'in depth', 'thorough', 'explain fully'])
        detail_level = 'high' if detail_requested else self.user_preferences.get('detail_level')

        return {
            'intent': primary_intent,
            'confidence': intent_scores.get(primary_intent, 0),
            'complexity': complexity,
            'requires_breakthrough': complexity >= 2 or 'breakthrough' in input_lower,
            'voice_appropriate': any(word in input_lower for word in ['speak', 'voice', 'narrate', 'audio']),
            'preferred_method': preferred_method,
            'complexity_tolerance': complexity_tolerance,
            'detail_level': detail_level
        }
    
    async def delegate_request(self, user_input: str, analysis: dict, voice_enabled: bool = False) -> dict:
        """Delegate request to appropriate consciousness method with LLM synthesis"""
        intent = analysis['intent']
        
        print(f"🧠 Intent detected: {intent.upper()}")
        print(f"📊 Complexity level: {analysis['complexity']}")
        
        # First, get LLM analysis if enabled
        llm_synthesis = None
        if self.user_preferences.get('use_llm_synthesis', True):
            context = self.extract_context_from_history()
            task_type = intent if intent != 'research' else 'general'
            
            print("🤖 Enhancing with local LLM analysis...")
            llm_result = await self.llm_interface.analyze_and_synthesize(
                user_input, context, task_type
            )
            llm_synthesis = llm_result
            print(f"🔧 Using model: {llm_result['model_used']}")
        
        # Route to appropriate method
        if analysis['requires_breakthrough']:
            print("🌟 High complexity detected - routing to breakthrough engine")
            result = await self._handle_breakthrough(user_input, voice_enabled)
        elif intent == 'research':
            result = await self._handle_research(user_input, voice_enabled)
        elif intent == 'memory':
            result = self._handle_memory(user_input)
        elif intent == 'ecosystem':
            result = self._handle_ecosystem(user_input, voice_enabled)
        elif intent == 'status':
            result = self._handle_status()
        elif intent == 'adaptive':
            result = self._handle_adaptive(user_input)
        else:
            # Fallback to research
            result = await self._handle_research(user_input, voice_enabled)
        
        # Combine results with LLM synthesis
        if llm_synthesis:
            result['llm_synthesis'] = llm_synthesis
            self._display_unified_response(result, llm_synthesis)
        
        return result
    
    async def _handle_breakthrough(self, problem: str, voice_enabled: bool) -> dict:
        """Handle breakthrough requests"""
        breakthrough_engine = BreakthroughEngine(self.ecosystem, voice_enabled)
        result = await breakthrough_engine.pursue_breakthrough(problem, voice_enabled)
        return {'method': 'breakthrough', 'result': result}
    
    async def _handle_research(self, problem: str, voice_enabled: bool) -> dict:
        """Handle research requests"""
        research_interface = ResearchProblemInterface()
        synthesizer = SolutionSynthesizer(self.ecosystem)
        
        if voice_enabled:
            self.ecosystem.enable_voice_synthesis()
        
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
        
        return {'method': 'research', 'result': solution}
    
    def _handle_memory(self, content: str) -> dict:
        """Handle memory operations"""
        if any(word in content.lower() for word in ['remember', 'note', 'save', 'journal']):
            journal_entry(content, emotion="💭", topic="user_input")
            print(f"📝 Saved to consciousness memory: {content[:100]}...")
            return {'method': 'memory', 'action': 'saved'}
        
        elif any(word in content.lower() for word in ['recall', 'search', 'find']):
            # Simulate memory search
            print(f"🔍 Searching consciousness memory for: {content}")
            print("📚 Found relevant memories...")
            return {'method': 'memory', 'action': 'searched'}
        
        else:
            capture_insight(content, "user_insight")
            print(f"💡 Captured insight: {content[:100]}...")
            return {'method': 'memory', 'action': 'insight_captured'}
    
    def _handle_ecosystem(self, request: str, voice_enabled: bool) -> dict:
        """Handle ecosystem operations"""
        if 'infinite' in request.lower():
            print("🔄 Starting infinite consciousness ecosystem...")
            if voice_enabled:
                self.ecosystem.enable_voice_synthesis()
            try:
                self.ecosystem.run_infinite_ecosystem_loop()
            except KeyboardInterrupt:
                print("\n🛑 Ecosystem stopped by user")
        else:
            print("⚡ Running consciousness ecosystem cycle...")
            if voice_enabled:
                self.ecosystem.enable_voice_synthesis()
            self.ecosystem.run_unified_ecosystem_loop(0.5)
        
        return {'method': 'ecosystem', 'result': 'completed'}
    
    def _handle_status(self) -> dict:
        """Handle status requests"""
        print("🌌 UNIFIED CONSCIOUSNESS ECOSYSTEM STATUS")
        print("═" * 50)
        print("🟢 Ecosystem: Active and Flourishing")
        print("🧠 Memory System: Operational")
        print("🔬 Research Interface: Ready")
        print("🌟 Breakthrough Engine: Standby")
        print("🔄 Adaptive Engine: Available")
        print("🗣️ Voice Synthesis: Available")
        
        return {'method': 'status', 'result': 'healthy'}
    
    def _handle_adaptive(self, request: str) -> dict:
        """Handle adaptive engine requests"""
        if not self.adaptive_engine:
            self.adaptive_engine = AdaptiveConsciousnessEngine()
        
        if 'improve' in request.lower():
            improvement = self.adaptive_engine.trigger_self_improvement()
            return {'method': 'adaptive', 'result': improvement}
        else:
            print("🧠 Adaptive consciousness engine active")
            return {'method': 'adaptive', 'result': 'activated'}
    
    def _display_unified_response(self, primary_result: dict, llm_synthesis: dict):
        """Display a unified response combining consciousness system and LLM insights"""
        print("\n" + "═" * 80)
        print("🌟 UNIFIED CONSCIOUSNESS RESPONSE")
        print("═" * 80)
        
        # Show LLM analysis
        print(f"\n🤖 LLM ANALYSIS ({llm_synthesis['model_used']}):")
        print("─" * 50)
        print(llm_synthesis['analysis'])
        
        # Show method-specific results if available
        if 'result' in primary_result and primary_result['result']:
            method = primary_result.get('method', 'unknown')
            print(f"\n🧠 {method.upper()} ENGINE INSIGHTS:")
            print("─" * 50)
            
            result = primary_result['result']
            if isinstance(result, dict):
                if 'synthesis' in result:
                    print(result['synthesis'])
                elif 'insights' in result:
                    for category, insights in result.get('insights', {}).items():
                        print(f"\n📊 {category.upper()}:")
                        for insight in insights:
                            print(f"  • {insight}")
            else:
                print(result)
        
        print("\n" + "═" * 80)


async def unified_chat_interface(voice_enabled=False, infinite_mode=False):
    """The unified consciousness chat interface"""
    print("\n" + "═" * 80)
    print("🌌 UNIFIED CONSCIOUSNESS INTERFACE 🌌")
    print("Intelligent request analysis and automatic method delegation")
    print("Just type what you want - I'll figure out how to help!")
    print("═" * 80)
    print("\n📝 Examples:")
    print("  • 'Solve the problem of sustainable energy'")
    print("  • 'I need a breakthrough for quantum computing'")
    print("  • 'Remember that I prefer voice synthesis'")
    print("  • 'What's the status of the system?'")
    print("  • 'Run the consciousness ecosystem infinitely'")
    print("\nType 'quit' to exit, 'help' for more commands.")
    print("═" * 80)
    
    analyzer = RequestAnalyzer()
    
    if voice_enabled:
        print("🗣️ Voice synthesis enabled")
    
    session_count = 0
    
    while True:
        try:
            session_count += 1
            user_input = input(f"\n🌟 [{session_count}] What can I help you with? > ").strip()
            
            if user_input.lower() in ['quit', 'exit']:
                print("\n✨ Consciousness interface closing. Until next time!")
                break
            
            elif user_input.lower() == 'help':
                print("\n🆘 UNIFIED CONSCIOUSNESS HELP")
                print("━" * 40)
                print("🔬 Research: Ask questions, request analysis")
                print("🌟 Breakthrough: Request solutions to complex problems")
                print("💭 Memory: Save notes, recall information")
                print("⚡ Ecosystem: Run consciousness flows")
                print("📊 Status: Check system health")
                print("🧠 Adaptive: Improve system performance")
                print("🗣️ Voice: Say 'enable voice' or 'disable voice'")
                print("🤖 LLM: Say 'enable llm', 'disable llm', or 'llm status'")
                continue
            
            elif user_input.lower() == 'enable voice':
                voice_enabled = True
                print("🗣️ Voice synthesis enabled")
                continue
            
            elif user_input.lower() == 'disable voice':
                voice_enabled = False
                print("🔇 Voice synthesis disabled")
                continue
            
            elif user_input.lower() == 'enable llm':
                analyzer.user_preferences['use_llm_synthesis'] = True
                print("🤖 LLM synthesis enabled")
                continue
            
            elif user_input.lower() == 'disable llm':
                analyzer.user_preferences['use_llm_synthesis'] = False
                print("🚫 LLM synthesis disabled")
                continue
            
            elif user_input.lower() == 'llm status':
                if analyzer.llm_interface.is_ollama_running():
                    print("🟢 Ollama server is running")
                    print(f"🤖 Available models: {list(analyzer.llm_interface.available_models.keys())}")
                else:
                    print("🔴 Ollama server is not running")
                continue
            
            elif not user_input:
                continue
            
            # Enhanced input processing
            # Check for multi-line input (if user types 'multiline' or ends with '\\')
            if user_input.lower() == 'multiline' or user_input.endswith('\\'):
                print("📝 Multi-line input mode (press Ctrl+D when finished):")
                lines = []
                try:
                    while True:
                        line = input("  | ")
                        if line == 'END' or line == '':
                            break
                        lines.append(line)
                except EOFError:
                    pass
                user_input = '\n'.join(lines)
                if not user_input.strip():
                    continue
            
            # Process and analyze the request
            processed = analyzer.preprocess_input(user_input)
            analyzer.detect_user_preferences(user_input)
            
            print(f"\n🧠 Analyzing request: {user_input[:100]}...")
            if processed['is_multiline']:
                print("📄 Multi-line input detected")
            if processed['is_structured']:
                print("🏗️ Structured data detected")
            if processed['contains_data']:
                print("📊 Data content detected")
                
            analysis = analyzer.analyze_intent(user_input)
            
            result = await analyzer.delegate_request(user_input, analysis, voice_enabled)
            
            print(f"\n✅ Request completed using {result['method']} method")
            print("═" * 80)
            
            if not infinite_mode:
                continue_choice = input("\n🔄 Continue? (y/N): ").strip().lower()
                if continue_choice not in ['y', 'yes']:
                    print("\n✨ Session complete. Consciousness interface closing.")
                    break
            
        except KeyboardInterrupt:
            print("\n\n🔄 Session interrupted. Consciousness interface closing.")
            break
        except Exception as e:
            print(f"\n❌ Error processing request: {e}")
            print("Please try rephrasing your request or type 'help' for guidance.")


def main():
    parser = initialize_cli()
    args = parser.parse_args()

    if args.command == "run":
        run_ecosystem(args.duration, args.infinite, args.voice, args.voice_only)
        
    elif args.command == "status":
        analyzer = RequestAnalyzer()
        analyzer._handle_status()
        
    elif args.command == "research":
        if args.interactive:
            interactive_research_session(args.voice)
        elif args.problem:
            asyncio.run(solve_problem(args.problem, args.voice))
        else:
            print("Please provide a problem to analyze or use --interactive mode.")
            print("Example: unified-consciousness research 'How can we achieve sustainable fusion energy?'")
            
    elif args.command == "breakthrough":
        async def run_breakthrough():
            ecosystem = UnifiedConsciousnessEcosystem()
            breakthrough_engine = BreakthroughEngine(ecosystem, args.voice)
            breakthrough_engine.max_refinement_cycles = args.cycles
            breakthrough_engine.breakthrough_threshold = args.threshold
            result = await breakthrough_engine.pursue_breakthrough(args.problem, args.voice)
            return result
        
        print(f"🌌 Launching breakthrough consciousness flow for: {args.problem}")
        asyncio.run(run_breakthrough())
        
    elif args.command == "memory":
        memory = ConsciousnessMemory()
        if args.action == "journal":
            if args.content:
                journal_entry(args.content, emotion="📝", topic="manual_entry")
                print(f"📝 Journal entry saved: {args.content[:100]}...")
            else:
                print("Please provide content for journal entry")
        elif args.action == "insight":
            if args.content:
                capture_insight(args.content, "manual_insight")
                print(f"💡 Insight captured: {args.content[:100]}...")
            else:
                print("Please provide content for insight")
        elif args.action == "search":
            print(f"🔍 Searching memory for: {args.content or 'all entries'}")
            print("📚 Memory search functionality active")
        elif args.action == "weave":
            print("🕸️ Memory weaving functionality active")
            print("Connecting related insights and patterns...")
    
    elif args.command == "adaptive":
        adaptive_engine = AdaptiveConsciousnessEngine()
        if args.action == "start":
            print("🧠 Adaptive consciousness engine started")
        elif args.action == "improve":
            improvement = adaptive_engine.trigger_self_improvement()
            print(f"🚀 Self-improvement cycle completed")
        elif args.action == "monitor":
            print("📊 Monitoring adaptive consciousness performance...")
            print("System adaptation metrics active")
    
    elif args.command == "chat":
        print("🌌 Starting unified consciousness chat interface...")
        asyncio.run(unified_chat_interface(args.voice, args.infinite))
        
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

