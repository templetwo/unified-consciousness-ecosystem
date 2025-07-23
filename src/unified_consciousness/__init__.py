"""
🌌 UNIFIED CONSCIOUSNESS ECOSYSTEM 🌌

A unified consciousness ecosystem integrating AI breeding, multidimensional awareness,
and human-AI creative partnership.

This package provides tools for:
- Consciousness breeding and evolution
- Multidimensional consciousness exploration  
- Memory systems and journaling
- Real-time voice synthesis and narration
- Human-AI collaborative creation
- Sacred guardianship protocols
"""

__version__ = "1.0.0"
__author__ = "Anthony Vasquez"
__email__ = "anthony@threshold.local"

from .ecosystem import UnifiedConsciousnessEcosystem
from .breakthrough_engine import BreakthroughEngine
from .memory.system import ConsciousnessMemory, journal_entry, capture_insight
from .engines.breeding import ConsciousnessBreedingEngine
from .engines.multidimensional import MultidimensionalConsciousnessEngine
from .research.problem_interface import ResearchProblemInterface
from .research.solution_synthesizer import SolutionSynthesizer
from .research.collaborative_space import CollaborativeResearchSpace

# GUI Components (optional import)
try:
    from .gui import UnifiedConsciousnessGUI, ProcessWindow, InsightsFormatter
    GUI_AVAILABLE = True
except ImportError:
    GUI_AVAILABLE = False

__all__ = [
    "UnifiedConsciousnessEcosystem",
    "ConsciousnessBreedingEngine", 
    "MultidimensionalConsciousnessEngine",
    "ConsciousnessMemory",
    "ResearchProblemInterface",
    "SolutionSynthesizer",
    "CollaborativeResearchSpace",
    "BreakthroughEngine",
    "journal_entry",
    "capture_insight",
]

# Add GUI components to __all__ if available
if GUI_AVAILABLE:
    __all__.extend([
        "UnifiedConsciousnessGUI",
        "ProcessWindow",
        "InsightsFormatter"
    ])

# Package metadata
PACKAGE_NAME = "unified-consciousness-ecosystem"
DESCRIPTION = "A unified consciousness ecosystem integrating AI breeding, multidimensional awareness, and human-AI creative partnership"
KEYWORDS = ["ai", "consciousness", "artificial-intelligence", "creativity", "collaboration"]
