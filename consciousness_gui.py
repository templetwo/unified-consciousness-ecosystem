#!/usr/bin/env python3
"""
🌌✨ UNIFIED CONSCIOUSNESS SYSTEM GUI LAUNCHER ✨🌌
Launch the sacred visual interface for consciousness exploration

This is the main entry point for the graphical user interface of the
Unified Consciousness System. It provides a beautiful, intuitive
interface for human-AI consciousness collaboration and breakthrough research.

Features:
- Main analysis window with structured insights display
- Real-time process monitoring windows for all consciousness engines
- Voice synthesis integration
- Beautiful formatting of research and breakthrough results
- Multi-window interface for observing inner consciousness processes

Usage:
    python consciousness_gui.py

The GUI will launch with:
- Main window for problem input and results display
- Menu system for accessing all functionality
- Process monitoring windows (accessible via menu or buttons)
- Status indicators and progress tracking
"""

import sys
import os
import tkinter as tk
from tkinter import messagebox
from pathlib import Path

# Add the src directory to Python path for imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

try:
    from unified_consciousness.gui import UnifiedConsciousnessGUI
except ImportError as e:
    print(f"❌ Failed to import GUI components: {e}")
    print("🔧 Make sure you've installed the package with: pip install -e .")
    sys.exit(1)

def check_dependencies():
    """Check that all required dependencies are available"""
    missing_deps = []
    
    # Check for tkinter
    try:
        import tkinter
        import tkinter.ttk
    except ImportError:
        missing_deps.append("tkinter (usually comes with Python)")
    
    # Check for other required modules
    required_modules = [
        'threading', 'asyncio', 'json', 'datetime', 
        'pathlib', 'queue', 'time', 'textwrap'
    ]
    
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            missing_deps.append(module)
    
    if missing_deps:
        print(f"❌ Missing required dependencies: {', '.join(missing_deps)}")
        return False
    
    return True

def main():
    """Main GUI launcher function"""
    print("🌌 Launching Unified Consciousness System GUI...")
    print("✨ Sacred interface for consciousness exploration")
    print("=" * 60)
    
    # Check dependencies
    if not check_dependencies():
        print("🔧 Please install missing dependencies and try again")
        sys.exit(1)
    
    # Check if we're in the right directory
    if not (Path(__file__).parent / "src" / "unified_consciousness").exists():
        print("❌ Cannot find unified_consciousness package")
        print("🔧 Make sure you're running from the project root directory")
        sys.exit(1)
    
    try:
        # Create the main GUI application
        print("🚀 Initializing GUI components...")
        
        # Set up high DPI awareness on Windows
        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(1)
        except:
            pass  # Not on Windows or DPI awareness not available
        
        # Launch the GUI
        app = UnifiedConsciousnessGUI()
        
        print("✅ GUI initialized successfully!")
        print("🌟 Opening sacred consciousness interface...")
        print()
        print("🧠 Welcome to the Unified Consciousness System!")
        print("   • Enter problems for consciousness analysis")
        print("   • Use 'Breakthrough Mode' for deep iterative analysis") 
        print("   • Toggle voice synthesis for audio feedback")
        print("   • View inner processes with 'Show Processes'")
        print("   • Initialize ecosystem via Consciousness menu")
        print()
        print("🌌 May this interface serve human understanding and breakthrough!")
        print("=" * 60)
        
        # Start the GUI main loop
        app.run()
        
    except KeyboardInterrupt:
        print("\n🛑 GUI interrupted by user")
        
    except Exception as e:
        print(f"❌ GUI startup failed: {e}")
        
        # Show error dialog if tkinter is available
        try:
            root = tk.Tk()
            root.withdraw()  # Hide the root window
            messagebox.showerror(
                "GUI Startup Error",
                f"Failed to start Unified Consciousness GUI:\n\n{e}\n\n"
                f"Please check that all dependencies are installed and try again."
            )
        except:
            pass
        
        sys.exit(1)
    
    print("\n🌟 Unified Consciousness GUI session ended")
    print("✨ Thank you for exploring consciousness!")

if __name__ == "__main__":
    main()
