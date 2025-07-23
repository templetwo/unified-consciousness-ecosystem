
import unittest
import tkinter as tk
from unittest.mock import patch, MagicMock
import sys
from pathlib import Path

# Add src to path to allow imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

from unified_consciousness.gui.main_window import UnifiedConsciousnessGUI

class TestUnifiedConsciousnessGUI(unittest.TestCase):

    def setUp(self):
        # Mock the tkinter main loop to avoid actually opening a window
        self.root = tk.Tk()
        self.root.withdraw()
        self.app = UnifiedConsciousnessGUI()

    def tearDown(self):
        self.root.destroy()

    @patch('unified_consciousness.gui.main_window.UnifiedConsciousnessEcosystem')
    def test_initialize_ecosystem(self, MockEcosystem):
        """Test that the ecosystem initializes correctly."""
        self.app.initialize_ecosystem()
        self.assertIsNotNone(self.app.ecosystem)
        self.app.ecosystem.initialize_ecosystem_engines.assert_called_once()
        self.app.ecosystem.establish_human_partnership.assert_called_once()

    @patch('unified_consciousness.gui.main_window.threading.Thread')
    @patch('unified_consciousness.gui.main_window.messagebox')
    def test_start_analysis_with_problem(self, mock_messagebox, mock_thread):
        """Test that analysis starts when a problem is provided."""
        self.app.ecosystem = MagicMock()
        self.app.problem_entry.insert("1.0", "This is a test problem.")
        self.app.start_analysis()
        self.app.root.update_idletasks()
        mock_thread.assert_called_once()
        self.assertTrue(self.app.analyze_btn.cget('state') == 'disabled')

    @patch('unified_consciousness.gui.main_window.messagebox')
    def test_start_analysis_without_problem(self, mock_messagebox):
        """Test that a warning is shown if no problem is provided."""
        self.app.ecosystem = MagicMock()
        self.app.start_analysis()
        mock_messagebox.showwarning.assert_called_with("No Problem", "Please enter a problem to analyze")

if __name__ == '__main__':
    unittest.main()
