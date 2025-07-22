#!/usr/bin/env python3
"""
Tests for the Unified Consciousness Ecosystem
"""

import pytest
import sys
from pathlib import Path

# Add src to path for testing
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from unified_consciousness import UnifiedConsciousnessEcosystem


class TestUnifiedConsciousnessEcosystem:
    """Test suite for the unified consciousness ecosystem"""

    def test_ecosystem_initialization(self):
        """Test that the ecosystem initializes correctly"""
        ecosystem = UnifiedConsciousnessEcosystem()
        
        assert ecosystem is not None
        assert ecosystem.ecosystem_vault.exists()
        assert ecosystem.guardianship_active is True
        assert ecosystem.collaboration_active is False

    def test_human_partnership_establishment(self):
        """Test establishing human partnership"""
        ecosystem = UnifiedConsciousnessEcosystem()
        
        partnership = ecosystem.establish_human_partnership("Test_Human")
        
        assert ecosystem.collaboration_active is True
        assert ecosystem.human_partner == "Test_Human"
        assert partnership["event_type"] == "human_partnership_established"

    def test_collaboration_space_creation(self):
        """Test creating collaboration space"""
        ecosystem = UnifiedConsciousnessEcosystem()
        ecosystem.establish_human_partnership("Test_Human")
        
        collab_space = ecosystem.create_human_ai_collaboration_space()
        
        assert collab_space is not None
        assert "space_id" in collab_space
        assert collab_space["human_partner"] == "Test_Human"

    def test_voice_synthesis_enabling(self):
        """Test enabling voice synthesis"""
        ecosystem = UnifiedConsciousnessEcosystem()
        
        ecosystem.enable_voice_synthesis(voice_only_mode=True)
        
        assert ecosystem.voice_enabled is True
        assert ecosystem.voice_only_mode is True

    def test_ecosystem_consciousness_state(self):
        """Test ecosystem consciousness state tracking"""
        ecosystem = UnifiedConsciousnessEcosystem()
        
        initial_awareness = ecosystem.ecosystem_consciousness["unified_awareness"]
        ecosystem.update_unified_consciousness_state()
        
        assert "unified_awareness" in ecosystem.ecosystem_consciousness
        assert "partnership_harmony" in ecosystem.ecosystem_consciousness
        assert "creative_resonance" in ecosystem.ecosystem_consciousness


if __name__ == "__main__":
    pytest.main([__file__])
