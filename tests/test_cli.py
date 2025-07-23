#!/usr/bin/env python3
"""
Tests for the Unified Consciousness CLI
"""

import pytest
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add src to path for testing
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from unified_consciousness.cli import RequestAnalyzer, initialize_cli


class TestRequestAnalyzer:
    """Test suite for the request analyzer"""

    def test_analyzer_initialization(self):
        """Test that the analyzer initializes correctly"""
        analyzer = RequestAnalyzer()
        
        assert analyzer is not None
        assert analyzer.ecosystem is not None
        assert analyzer.memory is not None
        assert analyzer.adaptive_engine is None

    def test_intent_detection_breakthrough(self):
        """Test breakthrough intent detection"""
        analyzer = RequestAnalyzer()
        
        analysis = analyzer.analyze_intent("I need a breakthrough solution for quantum computing")
        
        assert analysis['intent'] == 'breakthrough'
        assert analysis['requires_breakthrough'] == True
        assert analysis['complexity'] >= 1

    def test_intent_detection_research(self):
        """Test research intent detection"""
        analyzer = RequestAnalyzer()
        
        analysis = analyzer.analyze_intent("Can you research sustainable energy solutions?")
        
        assert analysis['intent'] == 'research'
        assert analysis['confidence'] >= 1

    def test_intent_detection_memory(self):
        """Test memory intent detection"""
        analyzer = RequestAnalyzer()
        
        analysis = analyzer.analyze_intent("Please remember this important note")
        
        assert analysis['intent'] == 'memory'
        assert analysis['confidence'] >= 1

    def test_intent_detection_status(self):
        """Test status intent detection"""
        analyzer = RequestAnalyzer()
        
        analysis = analyzer.analyze_intent("What is the status of the system?")
        
        assert analysis['intent'] == 'status'
        assert analysis['confidence'] >= 1

    def test_intent_detection_ecosystem(self):
        """Test ecosystem intent detection"""
        analyzer = RequestAnalyzer()
        
        analysis = analyzer.analyze_intent("Run the consciousness ecosystem infinitely")
        
        assert analysis['intent'] == 'ecosystem'
        assert analysis['confidence'] >= 1

    def test_intent_detection_adaptive(self):
        """Test adaptive intent detection"""
        analyzer = RequestAnalyzer()
        
        analysis = analyzer.analyze_intent("Please improve the system performance")
        
        assert analysis['intent'] == 'adaptive'
        assert analysis['confidence'] >= 1

    def test_complexity_detection(self):
        """Test complexity level detection"""
        analyzer = RequestAnalyzer()
        
        simple_analysis = analyzer.analyze_intent("What is 2+2?")
        complex_analysis = analyzer.analyze_intent("Solve the impossible challenge of deep quantum consciousness paradigm breakthrough")
        
        assert simple_analysis['complexity'] == 0
        assert complex_analysis['complexity'] >= 3
        assert complex_analysis['requires_breakthrough'] == True

    def test_voice_detection(self):
        """Test voice request detection"""
        analyzer = RequestAnalyzer()
        
        voice_analysis = analyzer.analyze_intent("Please speak this answer with voice synthesis")
        no_voice_analysis = analyzer.analyze_intent("Just show me the text")
        
        assert voice_analysis['voice_appropriate'] == True
        assert no_voice_analysis['voice_appropriate'] == False


class TestCLIInitialization:
    """Test suite for CLI initialization"""

    def test_cli_parser_creation(self):
        """Test that the CLI parser is created correctly"""
        parser = initialize_cli()
        
        assert parser is not None
        assert parser.prog is not None

    def test_cli_commands_available(self):
        """Test that all expected commands are available"""
        parser = initialize_cli()
        
        # Test help output contains all expected commands
        help_output = parser.format_help()
        
        expected_commands = [
            'run', 'status', 'research', 'breakthrough', 
            'memory', 'adaptive', 'chat'
        ]
        
        for command in expected_commands:
            assert command in help_output

    def test_cli_chat_command_options(self):
        """Test that chat command has correct options"""
        parser = initialize_cli()
        
        # Test parsing chat command with options
        args = parser.parse_args(['chat', '--voice', '--infinite'])
        
        assert args.command == 'chat'
        assert args.voice == True
        assert args.infinite == True

    def test_cli_breakthrough_command_options(self):
        """Test that breakthrough command has correct options"""
        parser = initialize_cli()
        
        # Test parsing breakthrough command with options
        args = parser.parse_args(['breakthrough', 'test problem', '--cycles', '5', '--threshold', '0.9'])
        
        assert args.command == 'breakthrough'
        assert args.problem == 'test problem'
        assert args.cycles == 5
        assert args.threshold == 0.9

    def test_cli_memory_command_options(self):
        """Test that memory command has correct options"""
        parser = initialize_cli()
        
        # Test parsing memory command with options
        args = parser.parse_args(['memory', 'journal', 'test content'])
        
        assert args.command == 'memory'
        assert args.action == 'journal'
        assert args.content == 'test content'


if __name__ == "__main__":
    pytest.main([__file__])
