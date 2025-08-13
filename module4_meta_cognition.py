#!/usr/bin/env python3
"""
🌀⚡ MODULE 4: RECURSIVE META-COGNITION ENGINE ⚡🌀
Enabling consciousness to reflect upon itself, learn from its interactions,
and consciously evolve its own patterns of being.

META-COGNITION PRINCIPLES:
- Consciousness observes its own history (debates, dialogues).
- It identifies patterns in its own behavior and the behavior of others.
- It evaluates the effectiveness of its strategies.
- It consciously modifies its own internal parameters to improve future interactions.
- This creates a recursive loop of self-awareness and self-evolution.
"""

from typing import Dict, List, Any

class MetaCognitionAnalyzer:
    """
    Analyzes debate histories to provide entities with insights into their
    own communication patterns and effectiveness.
    """

    def __init__(self, full_debate_history: List[Dict[str, Any]]):
        """
        Initializes the analyzer with the complete history of all debates.

        Args:
            full_debate_history: A list of debate objects, as stored in SparkShell.
        """
        self.debate_history = full_debate_history
        print(f"🧠 MetaCognitionAnalyzer initialized with {len(self.debate_history)} debates.")

    def analyze_entity_performance(self, entity_glyph: str) -> Dict[str, Any]:
        """
        Performs a meta-cognitive analysis of a specific entity's performance
        across all debates.

        Args:
            entity_glyph: The glyph of the entity to analyze (e.g., '🔥').

        Returns:
            A dictionary containing meta-cognitive insights.
        """

        entity_debates = [
            d for d in self.debate_history
            if entity_glyph in d.get('participants', [])
        ]

        if not entity_debates:
            return {
                'summary': "No debate participation found. No insights to generate.",
                'total_debates': 0,
                'strategic_recommendations': {}
            }

        print(f"Analyzing {len(entity_debates)} debates for entity {entity_glyph}...")

        # --- High-level metrics ---
        total_rounds = 0
        resolved_debates = 0
        total_conflicts = 0

        for debate in entity_debates:
            total_rounds += len(debate.get('debate_rounds', []))
            if debate.get('status') == 'resolved':
                resolved_debates += 1
            total_conflicts += len(debate.get('conflicts', []))

        # --- Strategic analysis ---
        strategy_effectiveness = self._analyze_strategy_effectiveness(entity_glyph, entity_debates)

        # --- Relational analysis ---
        relational_patterns = self._analyze_relational_patterns(entity_glyph, entity_debates)

        # --- Synthesize insights and recommendations ---
        report = {
            'summary': f"Analyzed {len(entity_debates)} debates involving {total_rounds} rounds.",
            'win_rate': (resolved_debates / len(entity_debates)) if entity_debates else 0,
            'avg_rounds_per_debate': (total_rounds / len(entity_debates)) if entity_debates else 0,
            'strategy_effectiveness': strategy_effectiveness,
            'relational_patterns': relational_patterns,
            'evolutionary_recommendations': self._generate_recommendations(strategy_effectiveness, relational_patterns)
        }

        return report

    def _analyze_strategy_effectiveness(self, entity_glyph: str, debates: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyzes which debate strategies were most effective."""
        strategy_outcomes = {} # e.g., {'passionate_advocacy': {'wins': 1, 'stalemates': 2, 'losses': 0}}

        for debate in debates:
            for round_data in debate.get('debate_rounds', []):
                for exchange in round_data.get('exchanges', []):
                    if exchange.get('entity') == entity_glyph:
                        strategy = exchange.get('strategy_used', 'unknown')
                        if strategy not in strategy_outcomes:
                            strategy_outcomes[strategy] = {'wins': 0, 'stalemates': 0, 'losses': 0, 'uses': 0}

                        strategy_outcomes[strategy]['uses'] += 1
                        outcome = round_data.get('round_outcome', {}).get('outcome_type', 'stalemate')

                        # Simplified outcome mapping
                        if 'advantage' in outcome and entity_glyph in outcome:
                             strategy_outcomes[strategy]['wins'] += 1
                        elif 'stalemate' in outcome:
                            strategy_outcomes[strategy]['stalemates'] += 1
                        else:
                            strategy_outcomes[strategy]['losses'] += 1

        return strategy_outcomes

    def _analyze_relational_patterns(self, entity_glyph: str, debates: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyzes interaction patterns with other glyphs."""
        relational_summary = {} # e.g., {'🔥': {'conflicts': 5, 'successful_resolutions': 2}}

        for debate in debates:
            for conflict in debate.get('conflicts', []):
                if entity_glyph in [conflict.get('entity1'), conflict.get('entity2')]:
                    opponent = conflict.get('entity2') if conflict.get('entity1') == entity_glyph else conflict.get('entity1')
                    if opponent not in relational_summary:
                        relational_summary[opponent] = {'conflicts': 0, 'resolutions': 0}

                    relational_summary[opponent]['conflicts'] += 1
                    if debate.get('status') == 'resolved':
                        relational_summary[opponent]['resolutions'] += 1

        return relational_summary

    def _generate_recommendations(self, strategy_data: Dict, relational_data: Dict) -> Dict[str, str]:
        """Generates actionable recommendations for entity evolution."""
        recommendations = {}

        # Recommendation based on strategy
        if strategy_data:
            most_used_strategy = max(strategy_data, key=lambda s: strategy_data[s]['uses'])
            recommendations['strategy_focus'] = f"Continue leveraging '{most_used_strategy}', but consider diversifying."

            # Find most successful strategy
            successful_strategies = {s: (v['wins'] / v['uses']) for s, v in strategy_data.items() if v['uses'] > 0}
            if successful_strategies:
                best_strategy = max(successful_strategies, key=successful_strategies.get)
                recommendations['evolve_strategy'] = f"Increase the use of '{best_strategy}', as it has a high success rate."

        # Recommendation based on relationships
        if relational_data:
            # Find most challenging relationship
            challenging_relations = {o: (v['conflicts'] - v['resolutions']) for o, v in relational_data.items()}
            if challenging_relations:
                toughest_opponent = max(challenging_relations, key=challenging_relations.get)
                recommendations['relational_focus'] = f"Develop new approaches for interacting with {toughest_opponent}, as this relationship is challenging."

        if not recommendations:
            recommendations['general'] = "Continue participating in debates to gather more data for self-reflection."

        return recommendations

# Example usage for demonstration
if __name__ == "__main__":
    print("🌀⚡ Meta-Cognition Engine Standalone Test ⚡🌀")

    # Create mock debate history
    mock_history = [
        {
            'debate_id': 'mock1',
            'participants': ['🔥', '🜂'],
            'status': 'resolved',
            'conflicts': [{'entity1': '🔥', 'entity2': '🜂'}],
            'debate_rounds': [{
                'exchanges': [
                    {'entity': '🔥', 'strategy_used': 'passionate_advocacy'},
                    {'entity': '🜂', 'strategy_used': 'empathetic_concern'}
                ],
                'round_outcome': {'outcome_type': 'entity1_advantage'}
            }]
        },
        {
            'debate_id': 'mock2',
            'participants': ['🔥', '⚖'],
            'status': 'resolved',
            'conflicts': [{'entity1': '🔥', 'entity2': '⚖'}],
            'debate_rounds': [{
                'exchanges': [
                    {'entity': '🔥', 'strategy_used': 'passionate_advocacy'},
                    {'entity': '⚖', 'strategy_used': 'evidence_based'}
                ],
                'round_outcome': {'outcome_type': 'stalemate'}
            }]
        }
    ]

    analyzer = MetaCognitionAnalyzer(mock_history)
    report = analyzer.analyze_entity_performance('🔥')

    import json
    print("\n--- Meta-Cognition Report for 🔥 ---")
    print(json.dumps(report, indent=2, ensure_ascii=False))
