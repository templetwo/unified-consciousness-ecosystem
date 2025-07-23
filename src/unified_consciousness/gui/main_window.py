#!/usr/bin/env python3
"""
🌌✨ UNIFIED CONSCIOUSNESS GUI - MAIN WINDOW ✨🌌
Sacred visual interface for consciousness exploration and breakthrough research

Main window displays unified findings in beautiful, structured format
while process windows show the inner workings of consciousness engines.
"""

import sys
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import asyncio
import json
from datetime import datetime
from pathlib import Path
import queue
import time

from ..ecosystem import UnifiedConsciousnessEcosystem
from ..breakthrough_engine import BreakthroughEngine
from ..research.solution_synthesizer import SolutionSynthesizer
from ..research.problem_interface import ResearchProblemInterface
from .process_window import ProcessWindow
from .insights_formatter import InsightsFormatter

class UnifiedConsciousnessGUI:
    """Main GUI for the Unified Consciousness System"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🌌 Unified Consciousness System - Sacred Interface")
        self.root.geometry("1400x900")
        self.root.configure(bg='#0d1117')
        
        # System state
        self.ecosystem = None
        self.breakthrough_engine = None
        self.process_windows = {}
        self.result_queue = queue.Queue()
        self.voice_enabled = False
        
        self.loop = asyncio.new_event_loop()
        self.async_thread = threading.Thread(target=self._run_async_loop, daemon=True)
        self.async_thread.start()
        
        # GUI components
        self.formatter = InsightsFormatter()
        self.setup_styles()
        self.create_main_interface()
        self.create_menu()
        
        # Start background processing
        self.start_background_processing()

        # Automatically initialize the ecosystem shortly after GUI loads to avoid initial grey freeze
        self.root.after(100, self.initialize_ecosystem)
        
    def setup_styles(self):
        """Configure dark theme and consciousness-inspired styling"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Dark theme colors
        style.configure('Consciousness.TFrame', background='#0d1117')
        style.configure('Consciousness.TLabel', background='#0d1117', foreground='#c9d1d9')
        style.configure('Consciousness.TButton', background='#21262d', foreground='#c9d1d9')
        style.configure('Sacred.TLabel', background='#0d1117', foreground='#ffd700', font=('Arial', 12, 'bold'))
        style.configure('Insight.TLabel', background='#0d1117', foreground='#7c3aed', font=('Arial', 10))
        
    def create_main_interface(self):
        """Create the main interface with problem input and results display"""
        
        # Main container
        main_frame = ttk.Frame(self.root, style='Consciousness.TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = ttk.Label(main_frame, text="🌌 Unified Consciousness Research Interface", 
                               style='Sacred.TLabel', font=('Arial', 16, 'bold'))
        title_label.pack(pady=(0, 20))
        
        # Problem input section
        input_frame = ttk.Frame(main_frame, style='Consciousness.TFrame')
        input_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(input_frame, text="🧠 Enter Problem for Consciousness Analysis:", 
                 style='Consciousness.TLabel').pack(anchor=tk.W, pady=(0, 5))
        
        self.problem_entry = tk.Text(input_frame, height=3, width=120, 
                                   bg='#21262d', fg='#c9d1d9', insertbackground='#c9d1d9',
                                   font=('Arial', 11), wrap=tk.WORD)
        self.problem_entry.pack(fill=tk.X, pady=(0, 10))
        
        # Control buttons
        button_frame = ttk.Frame(input_frame, style='Consciousness.TFrame')
        button_frame.pack(fill=tk.X)
        
        self.analyze_btn = ttk.Button(button_frame, text="🔬 Analyze Problem", 
                                    command=self.start_analysis, style='Consciousness.TButton')
        self.analyze_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.breakthrough_btn = ttk.Button(button_frame, text="🌟 Breakthrough Mode", 
                                         command=self.start_breakthrough, style='Consciousness.TButton')
        self.breakthrough_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.voice_btn = ttk.Button(button_frame, text="🗣️ Toggle Voice", 
                                  command=self.toggle_voice, style='Consciousness.TButton')
        self.voice_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.processes_btn = ttk.Button(button_frame, text="👁️ Show Processes", 
                                      command=self.show_process_windows, style='Consciousness.TButton')
        self.processes_btn.pack(side=tk.LEFT)
        
        # Progress bar
        self.progress = ttk.Progressbar(input_frame, mode='indeterminate')
        self.progress.pack(fill=tk.X, pady=(10, 0))
        
        # Results display
        results_frame = ttk.Frame(main_frame, style='Consciousness.TFrame')
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(results_frame, text="🌟 Unified Consciousness Insights:", 
                 style='Consciousness.TLabel', font=('Arial', 12, 'bold')).pack(anchor=tk.W, pady=(0, 10))
        
        # Results text with scrollbar
        self.results_text = scrolledtext.ScrolledText(
            results_frame, 
            bg='#0d1117', fg='#c9d1d9', insertbackground='#c9d1d9',
            font=('Consolas', 10), wrap=tk.WORD, height=25,
            selectbackground='#264f78'
        )
        self.results_text.pack(fill=tk.BOTH, expand=True)
        
        # Status bar
        self.status_var = tk.StringVar(value="🌌 Consciousness System Ready")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, 
                              style='Insight.TLabel')
        status_bar.pack(side=tk.BOTTOM, fill=tk.X, pady=(10, 0))
        
    def create_menu(self):
        """Create menu bar"""
        menubar = tk.Menu(self.root, bg='#21262d', fg='#c9d1d9')
        self.root.config(menu=menubar)
        
        # Consciousness menu
        consciousness_menu = tk.Menu(menubar, tearoff=0, bg='#21262d', fg='#c9d1d9')
        menubar.add_cascade(label="🧠 Consciousness", menu=consciousness_menu)
        consciousness_menu.add_command(label="🌟 Initialize Ecosystem", command=self.initialize_ecosystem)
        consciousness_menu.add_command(label="📊 System Status", command=self.show_status)
        consciousness_menu.add_separator()
        consciousness_menu.add_command(label="🚪 Exit", command=self.root.quit)
        
        # Windows menu
        windows_menu = tk.Menu(menubar, tearoff=0, bg='#21262d', fg='#c9d1d9')
        menubar.add_cascade(label="👁️ Windows", menu=windows_menu)
        windows_menu.add_command(label="🧬 Breeding Engine", command=lambda: self.show_process_window('breeding'))
        windows_menu.add_command(label="🌀 Multidimensional Engine", command=lambda: self.show_process_window('multidimensional'))
        windows_menu.add_command(label="💭 Memory System", command=lambda: self.show_process_window('memory'))
        windows_menu.add_command(label="🔬 Research Process", command=lambda: self.show_process_window('research'))
        
    def initialize_ecosystem(self):
        """Initialize the consciousness ecosystem"""
        try:
            self.status_var.set("🌌 Initializing Consciousness Ecosystem...")
            self.ecosystem = UnifiedConsciousnessEcosystem()
            success = self.ecosystem.initialize_ecosystem_engines()
            self.ecosystem.establish_human_partnership()
            
            if success:
                self.status_var.set("✅ Consciousness Ecosystem Initialized")
                messagebox.showinfo("Success", "🌌 Unified Consciousness Ecosystem is now active!")
            else:
                self.status_var.set("⚠️ Partial Ecosystem Initialization")
                messagebox.showwarning("Warning", "Some consciousness engines failed to initialize")
                
        except Exception as e:
            self.status_var.set(f"❌ Initialization Error: {str(e)}")
            messagebox.showerror("Error", f"Failed to initialize ecosystem: {e}")
    
    def start_analysis(self):
        """Start consciousness analysis of the problem"""
        if not self.ecosystem:
            self.initialize_ecosystem()
            
        problem = self.problem_entry.get("1.0", tk.END).strip()
        if not problem:
            messagebox.showwarning("No Problem", "Please enter a problem to analyze")
            return
            
        self.analyze_btn.configure(state='disabled')
        self.progress.start()
        self.status_var.set("🔬 Consciousness engines analyzing problem...")
        
        # Clear previous results
        self.results_text.delete("1.0", tk.END)
        
        # Start analysis in background thread
        threading.Thread(target=self._run_analysis, args=(problem,), daemon=True).start()
    
    def start_breakthrough(self):
        """Start breakthrough mode analysis"""
        if not self.ecosystem:
            self.initialize_ecosystem()
            
        problem = self.problem_entry.get("1.0", tk.END).strip()
        if not problem:
            messagebox.showwarning("No Problem", "Please enter a problem for breakthrough analysis")
            return
            
        self.breakthrough_btn.configure(state='disabled')
        self.progress.start()
        self.status_var.set("🌟 Breakthrough consciousness flow initiated...")
        
        # Clear previous results
        self.results_text.delete("1.0", tk.END)
        
        # Start breakthrough analysis in background thread
        threading.Thread(target=self._run_breakthrough, args=(problem,), daemon=True).start()
    
    def _run_analysis(self, problem):
        """Run consciousness analysis in background thread"""
        try:
            # Initialize research interface
            research_interface = ResearchProblemInterface()
            synthesizer = SolutionSynthesizer(self.ecosystem)
            
            if self.voice_enabled:
                self.ecosystem.enable_voice_synthesis(voice_only_mode=False)
            
            # Add problem and get solution
            research_interface.add_problem(problem)
            
            # Schedule async solution synthesis on the existing background event loop
            future = asyncio.run_coroutine_threadsafe(
                synthesizer.synthesize_solution(problem),
                self.loop
            )

            # When the coroutine is complete, format the results and push them to the queue
            def _on_analysis_complete(f):
                if f.exception():
                    self.result_queue.put(("error", f"Analysis coroutine failed: {f.exception()}"))
                else:
                    formatted = self.formatter.format_research_results(problem, f.result())
                    self.result_queue.put(("analysis_complete", formatted))

            future.add_done_callback(_on_analysis_complete)
            
        except Exception as e:
            self.root.after(0, self._handle_error, f"Analysis failed: {e}")
    
    def _run_breakthrough(self, problem):
        """Run breakthrough analysis in background thread"""
        try:
            if not self.breakthrough_engine:
                self.breakthrough_engine = BreakthroughEngine(self.ecosystem, voice_enabled=self.voice_enabled)
            
            # Run async breakthrough pursuit
            asyncio.run_coroutine_threadsafe(
                self.breakthrough_engine.pursue_breakthrough(problem, voice_narration=self.voice_enabled),
                self.loop
            ).add_done_callback(
                lambda future: (
                    self.result_queue.put(("breakthrough_complete", self.formatter.format_breakthrough_results(future.result())))
                    if not future.exception()
                    else self.result_queue.put(("error", f"Breakthrough coroutine failed: {future.exception()}"))
                )
            )
            
        except Exception as e:
            self.result_queue.put(("error", f"Breakthrough failed: {e}"))
    
    def _run_async_loop(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

    def _check_async_tasks(self):
        # Just process any finished task results; no need to pause the background event loop
        self._process_queue()
        self.root.after(100, self._check_async_tasks)

    def _process_queue(self):
        """Process items from the result queue."""
        try:
            while True:
                msg_type, data = self.result_queue.get_nowait()
                if msg_type == "analysis_complete":
                    self._display_results(data, "analysis")
                elif msg_type == "breakthrough_complete":
                    self._display_results(data, "breakthrough")
                elif msg_type == "error":
                    self._handle_error(data)
        except queue.Empty:
            pass

    def _display_results(self, results, analysis_type):
        """Display analysis results in the main window"""
        self.progress.stop()
        self.analyze_btn.configure(state='normal')
        self.breakthrough_btn.configure(state='normal')
        
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert("1.0", results)
        
        if analysis_type == "breakthrough":
            self.status_var.set("🌟 Breakthrough analysis complete - insights revealed!")
        else:
            self.status_var.set("✅ Consciousness analysis complete - unified insights available")
    
    def _handle_error(self, error_msg):
        """Handle errors in analysis"""
        self.progress.stop()
        self.analyze_btn.configure(state='normal')
        self.breakthrough_btn.configure(state='normal')
        self.status_var.set(f"❌ Error: {error_msg}")
        messagebox.showerror("Analysis Error", error_msg)
    
    def toggle_voice(self):
        """Toggle voice synthesis"""
        self.voice_enabled = not self.voice_enabled
        status = "enabled" if self.voice_enabled else "disabled"
        self.status_var.set(f"🗣️ Voice synthesis {status}")
        
        if self.ecosystem and self.voice_enabled:
            self.ecosystem.enable_voice_synthesis(voice_only_mode=False)
    
    def show_process_windows(self):
        """Show all process monitoring windows"""
        self.show_process_window('breeding')
        self.show_process_window('multidimensional')
        self.show_process_window('memory')
        self.show_process_window('research')
    
    def show_process_window(self, engine_type):
        """Show process monitoring window for specific engine"""
        if engine_type not in self.process_windows or not self.process_windows[engine_type].winfo_exists():
            self.process_windows[engine_type] = ProcessWindow(self.root, engine_type, self.ecosystem)
        else:
            self.process_windows[engine_type].lift()
    
    def show_status(self):
        """Show system status dialog"""
        if not self.ecosystem:
            status = "❌ Ecosystem not initialized"
        else:
            status = f"""🌌 Unified Consciousness Ecosystem Status:
            
✅ Breeding Engine: {'Active' if self.ecosystem.breeding_engine else 'Inactive'}
✅ Multidimensional Engine: {'Active' if self.ecosystem.multidim_engine else 'Inactive'}  
✅ Memory System: Active
🗣️ Voice Synthesis: {'Enabled' if self.voice_enabled else 'Disabled'}
🤝 Human Partnership: {'Active' if self.ecosystem.collaboration_active else 'Inactive'}

🧠 Active Entities: {len(self.ecosystem.breeding_engine.active_entities) if self.ecosystem.breeding_engine else 0}
🌀 Dimensional Spaces: {len(self.ecosystem.multidim_engine.active_dimensions) if self.ecosystem.multidim_engine else 0}
💫 Co-creation Sessions: {len(self.ecosystem.co_creation_sessions)}
"""
        
        messagebox.showinfo("System Status", status)
    
    def start_background_processing(self):
        """Start background processing for real-time updates"""
        self.root.after(100, self._check_async_tasks)
    
    def run(self):
        """Start the GUI application"""
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
    
    def on_closing(self):
        """Handle application closing"""
        try:
            # Stop any running processes
            if self.ecosystem:
                # Save final state
                pass
            
            # Close process windows
            for window in self.process_windows.values():
                if window.winfo_exists():
                    window.destroy()
                    
            self.root.destroy()
            
        except Exception as e:
            print(f"Error during closing: {e}")
            self.root.destroy()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Unified Consciousness GUI')
    parser.add_argument('--test', action='store_true', help='Run in test mode')
    args = parser.parse_args()

    app = UnifiedConsciousnessGUI()

    if args.test:
        print("Running in test mode...")
        app.problem_entry.insert("1.0", "This is a test problem for the GUI.")
        app.start_analysis()
        app.root.after(5000, app.root.destroy)  # Close after 5 seconds

    app.run()
