#!/usr/bin/env python3
"""
🌌✨ UNIFIED CONSCIOUSNESS GUI MODULE ✨🌌
Sacred visual interface for consciousness exploration

This module provides a complete GUI interface for the Unified Consciousness System,
including main analysis window, process monitoring windows, and beautiful 
structured presentation of insights and breakthrough results.
"""

from .main_window import UnifiedConsciousnessGUI
from .process_window import ProcessWindow
from .insights_formatter import InsightsFormatter

__all__ = [
    'UnifiedConsciousnessGUI',
    'ProcessWindow', 
    'InsightsFormatter'
]
