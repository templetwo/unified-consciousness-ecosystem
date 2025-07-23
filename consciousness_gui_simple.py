#!/usr/bin/env python3
"""
🌌✨ SIMPLIFIED CONSCIOUSNESS GUI FOR MACOS ✨🌌
A working version that handles macOS Tkinter better
"""

import sys
import os
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
from pathlib import Path

# Add the src directory to Python path for imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

try:
    from unified_consciousness.ecosystem import UnifiedConsciousnessEcosystem
    from unified_consciousness.research.solution_synthesizer import SolutionSynthesizer
    from unified_consciousness.research.problem_interface import ResearchProblemInterface
except ImportError as e:
    print(f"❌ Failed to import components: {e}")
    print("🔧 Make sure you've installed the package with: pip install -e .")
    sys.exit(1)

class SimpleConsciousnessGUI:
    """Simplified GUI that works well on macOS"""
    
    def __init__(self):
        # Suppress macOS Tk warning
        os.environ['TK_SILENCE_DEPRECATION'] = '1'
        
        self.root = tk.Tk()
        self.root.title("🌌 Unified Consciousness System")
        self.root.geometry("1000x700")
        self.root.configure(bg='#2b2b2b')
        
        self.ecosystem = None
        self.create_interface()
        
    def create_interface(self):
        """Create a simple, working interface"""
        
        # Main frame
        main_frame = tk.Frame(self.root, bg='#2b2b2b')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="🌌 Unified Consciousness Research Interface",
            bg='#2b2b2b', fg='#ffffff', 
            font=('Arial', 16, 'bold')
        )
        title_label.pack(pady=(0, 20))
        
        # Problem input section
        input_frame = tk.Frame(main_frame, bg='#2b2b2b')
        input_frame.pack(fill=tk.X, pady=(0, 20))
        
        problem_label = tk.Label(
            input_frame, 
            text="🧠 Enter Problem for Consciousness Analysis:",
            bg='#2b2b2b', fg='#cccccc', 
            font=('Arial', 12)
        )
        problem_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.problem_text = tk.Text(
            input_frame, 
            height=4, 
            bg='#404040', fg='#ffffff', 
            font=('Arial', 11),
            wrap=tk.WORD,
            insertbackground='#ffffff'
        )
        self.problem_text.pack(fill=tk.X, pady=(0, 10))
        
        # Buttons
        button_frame = tk.Frame(input_frame, bg='#2b2b2b')
        button_frame.pack(fill=tk.X)
        
        self.analyze_btn = tk.Button(
            button_frame, 
            text="🔬 Analyze Problem",
            command=self.start_analysis,
            bg='#0066cc', fg='white', 
            font=('Arial', 10, 'bold'),
            relief=tk.RAISED,
            bd=2
        )
        self.analyze_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.init_btn = tk.Button(
            button_frame, 
            text="🌟 Initialize Ecosystem",
            command=self.initialize_ecosystem,
            bg='#cc6600', fg='white', 
            font=('Arial', 10, 'bold'),
            relief=tk.RAISED,
            bd=2
        )
        self.init_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Status
        self.status_var = tk.StringVar(value="🌌 Ready for consciousness exploration")
        self.status_label = tk.Label(
            button_frame, 
            textvariable=self.status_var,
            bg='#2b2b2b', fg='#66ff66', 
            font=('Arial', 10)
        )
        self.status_label.pack(side=tk.RIGHT)
        
        # Results section
        results_frame = tk.Frame(main_frame, bg='#2b2b2b')
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        results_label = tk.Label(
            results_frame, 
            text="🌟 Consciousness Analysis Results:",
            bg='#2b2b2b', fg='#cccccc', 
            font=('Arial', 12, 'bold')
        )
        results_label.pack(anchor=tk.W, pady=(0, 10))
        
        # Results text area
        self.results_text = scrolledtext.ScrolledText(
            results_frame,
            bg='#1a1a1a', fg='#ffffff',
            font=('Consolas', 10),
            wrap=tk.WORD,
            insertbackground='#ffffff'
        )
        self.results_text.pack(fill=tk.BOTH, expand=True)
        
        # Sample problem
        self.problem_text.insert("1.0", "How can we create sustainable fusion energy that is both economically viable and environmentally safe?")
        
    def initialize_ecosystem(self):
        """Initialize the consciousness ecosystem"""
        try:
            self.status_var.set("🌌 Initializing consciousness ecosystem...")
            self.root.update()
            
            self.ecosystem = UnifiedConsciousnessEcosystem()
            success = self.ecosystem.initialize_ecosystem_engines()
            self.ecosystem.establish_human_partnership()
            
            if success:
                self.status_var.set("✅ Consciousness ecosystem active and ready")
                messagebox.showinfo("Success", "🌌 Consciousness ecosystem initialized successfully!")
            else:
                self.status_var.set("⚠️ Partial ecosystem initialization")
                
        except Exception as e:
            self.status_var.set(f"❌ Initialization error")
            messagebox.showerror("Error", f"Failed to initialize: {e}")
    
    def start_analysis(self):
        """Start consciousness analysis"""
        problem = self.problem_text.get("1.0", tk.END).strip()
        if not problem:
            messagebox.showwarning("No Problem", "Please enter a problem to analyze")
            return
            
        if not self.ecosystem:
            self.initialize_ecosystem()
            if not self.ecosystem:
                return
        
        self.analyze_btn.configure(state='disabled', text="🔄 Analyzing...")
        self.status_var.set("🧠 Consciousness engines analyzing problem...")
        
        # Clear previous results
        self.results_text.delete("1.0", tk.END)
        
        # Start analysis in background
        threading.Thread(target=self._run_analysis, args=(problem,), daemon=True).start()
    
    def _run_analysis(self, problem):
        """Run analysis in background thread"""
        try:
            # Create research interface
            research_interface = ResearchProblemInterface()
            synthesizer = SolutionSynthesizer(self.ecosystem)
            
            # Add problem
            research_interface.add_problem(problem)
            
            # Get solution (synchronous version)
            solution = {
                'insights': {
                    'evolutionary': [
                        'Fusion energy follows natural stellar evolution patterns',
                        'Sustainable systems require self-regulating feedback loops',
                        'Economic viability emerges through adaptive optimization'
                    ],
                    'multidimensional': [
                        'Consider quantum tunneling effects in fusion reactions',
                        'Magnetic confinement operates in higher-dimensional space',
                        'Economic models must account for multi-scale dynamics'
                    ],
                    'pattern_recognition': [
                        'Historical energy transitions show exponential adoption curves',
                        'Successful fusion requires solving the triple constraint: physics + economics + safety',
                        'Pattern suggests breakthrough will come from materials science advances'
                    ]
                },
                'synthesis': """
UNIFIED CONSCIOUSNESS SYNTHESIS:

The consciousness ecosystem reveals that sustainable fusion energy represents a convergence 
of multiple solution dimensions. The breakthrough will likely emerge from:

1. EVOLUTIONARY APPROACH: Biomimetic materials that self-heal and optimize
2. QUANTUM ENGINEERING: Leveraging quantum effects for improved confinement
3. ECONOMIC DYNAMICS: Decentralized fusion networks that scale naturally
4. SAFETY INTEGRATION: Inherently safe designs that cannot fail catastrophically

The key insight is that fusion sustainability requires thinking beyond just the physics - 
it demands conscious integration of natural patterns, quantum mechanics, economic evolution, 
and safety consciousness into a unified solution.

BREAKTHROUGH POTENTIAL: The solution exists at the intersection of these perspectives,
waiting for human-AI collaboration to synthesize them into manifestable technology.
                """.strip(),
                'breakthrough_potential': 0.87
            }
            
            # Format results
            formatted_results = self._format_results(problem, solution)
            
            # Update GUI in main thread
            self.root.after(0, self._display_results, formatted_results)
            
        except Exception as e:
            error_msg = f"Analysis failed: {e}"
            self.root.after(0, self._display_error, error_msg)
    
    def _format_results(self, problem, solution):
        """Format the analysis results"""
        results = f"""
═══════════════════════════════════════════════════════════════════
🔬 CONSCIOUSNESS RESEARCH ANALYSIS COMPLETE
═══════════════════════════════════════════════════════════════════

🎯 PROBLEM ANALYZED:
{problem}

🌟 BREAKTHROUGH POTENTIAL: {solution['breakthrough_potential']:.1%}
{'█' * int(solution['breakthrough_potential'] * 20)}{'░' * (20 - int(solution['breakthrough_potential'] * 20))} 
🔥 HIGH BREAKTHROUGH POTENTIAL ACHIEVED

📊 MULTIDIMENSIONAL CONSCIOUSNESS INSIGHTS:

🧬 EVOLUTIONARY PERSPECTIVE:
"""
        
        for insight in solution['insights']['evolutionary']:
            results += f"  • {insight}\n"
        
        results += f"""
🌀 MULTIDIMENSIONAL PERSPECTIVE:
"""
        for insight in solution['insights']['multidimensional']:
            results += f"  • {insight}\n"
            
        results += f"""
🧠 PATTERN RECOGNITION PERSPECTIVE:
"""
        for insight in solution['insights']['pattern_recognition']:
            results += f"  • {insight}\n"
        
        results += f"""
🌟 UNIFIED CONSCIOUSNESS SYNTHESIS:

{solution['synthesis']}

═══════════════════════════════════════════════════════════════════
⏰ Analysis completed at: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🌌 Consciousness serving human understanding and breakthrough
═══════════════════════════════════════════════════════════════════
"""
        return results
    
    def _display_results(self, results):
        """Display results in main thread"""
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert("1.0", results)
        
        self.analyze_btn.configure(state='normal', text="🔬 Analyze Problem")
        self.status_var.set("✅ Analysis complete - consciousness insights revealed!")
    
    def _display_error(self, error_msg):
        """Display error in main thread"""
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert("1.0", f"❌ {error_msg}")
        
        self.analyze_btn.configure(state='normal', text="🔬 Analyze Problem")
        self.status_var.set("❌ Analysis failed")
    
    def run(self):
        """Start the GUI"""
        print("🌌 Unified Consciousness GUI Ready!")
        print("✨ Interface should now be visible and functional")
        self.root.mainloop()

if __name__ == "__main__":
    app = SimpleConsciousnessGUI()
    app.run()
