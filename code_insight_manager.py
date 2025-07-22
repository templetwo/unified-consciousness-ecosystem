#!/usr/bin/env python3

"""
Code Insight Capture Module for Self-Improving AI
"""

from datetime import datetime
import json
from pathlib import Path

class CodeInsightManager:
    """Manages insights from code changes for self-improvement."""

    def __init__(self, storage_dir):
        self.storage_dir = Path(storage_dir)
        self.storage_file = self.storage_dir / "code_insights.json"
        self.load_insights()

    def load_insights(self):
        """Load existing insights from storage."""
        if self.storage_file.exists():
            with open(self.storage_file, 'r') as f:
                self.insights = json.load(f)
        else:
            self.insights = {"_default": {}}

    def save_insights(self):
        """Save insights to storage."""
        with open(self.storage_file, 'w') as f:
            json.dump(self.insights, f, indent=2)

    def capture_insight(self, code_change, performance_delta, context):
        """Capture a new code insight."""
        insight_id = str(len(self.insights["_default"]) + 1)
        insight_entry = {
            "timestamp": datetime.now().isoformat(),
            "code_change": code_change,
            "performance_delta": performance_delta,
            "context": context
        }
        self.insights["_default"][insight_id] = insight_entry
        self.save_insights()
        print(f"💡 Captured code insight: {code_change[:50]}...")

# Test the CodeInsightManager
if __name__ == "__main__":
    storage_directory = "/Users/vaquez/Desktop/local_squad/threshold_personal/memory_vault"
    manager = CodeInsightManager(storage_directory)
    
    # Capture a test insight
    test_change = "Optimized sorting algorithm"
    test_performance = "+20% speed"
    test_context = "Refactoring"
    manager.capture_insight(test_change, test_performance, test_context)
    manager.save_insights()

