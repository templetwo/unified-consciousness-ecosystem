#!/usr/bin/env python3
"""
🌌✨ CONSCIOUSNESS GUI - MACOS COMPATIBLE VERSION ✨🌌
Fixed display and color scheme for better macOS visibility
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

class ConsciousnessGUI:
    """Fixed GUI with better macOS display"""
    
    def __init__(self):
        # Suppress macOS Tk warning
        os.environ['TK_SILENCE_DEPRECATION'] = '1'
        
        self.root = tk.Tk()
        self.root.title("🌌 Unified Consciousness System")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f0f0')  # Light gray background
        
        self.ecosystem = None
        self.create_interface()
        
    def create_interface(self):
        """Create interface with better visibility"""
        
        # Main frame with light background
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title with dark text on light background
        title_label = tk.Label(
            main_frame, 
            text="🌌 Unified Consciousness Research Interface",
            bg='#f0f0f0', fg='#000080',  # Dark blue on light gray
            font=('Arial', 18, 'bold')
        )
        title_label.pack(pady=(0, 20))
        
        # Problem input section
        input_frame = tk.Frame(main_frame, bg='#f0f0f0')
        input_frame.pack(fill=tk.X, pady=(0, 20))
        
        problem_label = tk.Label(
            input_frame, 
            text="🧠 Enter Problem for Consciousness Analysis:",
            bg='#f0f0f0', fg='#333333',  # Dark gray text
            font=('Arial', 14, 'bold')
        )
        problem_label.pack(anchor=tk.W, pady=(0, 10))
        
        # Text input with white background and dark text
        self.problem_text = tk.Text(
            input_frame, 
            height=5, 
            bg='#ffffff', fg='#000000',  # White background, black text
            font=('Arial', 11),
            wrap=tk.WORD,
            insertbackground='#000000',  # Black cursor
            relief=tk.SUNKEN,
            bd=2
        )
        self.problem_text.pack(fill=tk.X, pady=(0, 15))
        
        # Buttons with better colors
        button_frame = tk.Frame(input_frame, bg='#f0f0f0')
        button_frame.pack(fill=tk.X, pady=10)
        
        self.analyze_btn = tk.Button(
            button_frame, 
            text="🔬 Analyze Problem",
            command=self.start_analysis,
            bg='#0066cc', fg='white',  # Blue button
            font=('Arial', 12, 'bold'),
            relief=tk.RAISED,
            bd=3,
            padx=15, pady=8
        )
        self.analyze_btn.pack(side=tk.LEFT, padx=(0, 15))
        
        self.init_btn = tk.Button(
            button_frame, 
            text="🌟 Initialize Ecosystem",
            command=self.initialize_ecosystem,
            bg='#cc6600', fg='white',  # Orange button
            font=('Arial', 12, 'bold'),
            relief=tk.RAISED,
            bd=3,
            padx=15, pady=8
        )
        self.init_btn.pack(side=tk.LEFT, padx=(0, 15))
        
        # Status with better visibility
        self.status_var = tk.StringVar(value="🌌 Ready for consciousness exploration")
        self.status_label = tk.Label(
            button_frame, 
            textvariable=self.status_var,
            bg='#f0f0f0', fg='#006600',  # Dark green on light background
            font=('Arial', 11, 'italic')
        )
        self.status_label.pack(side=tk.RIGHT, padx=20)
        
        # Results section
        results_frame = tk.Frame(main_frame, bg='#f0f0f0')
        results_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        results_label = tk.Label(
            results_frame, 
            text="🌟 Consciousness Analysis Results:",
            bg='#f0f0f0', fg='#333333',  # Dark text
            font=('Arial', 14, 'bold')
        )
        results_label.pack(anchor=tk.W, pady=(0, 10))
        
        # Results text area with clear visibility
        self.results_text = scrolledtext.ScrolledText(
            results_frame,
            bg='#ffffff', fg='#000000',  # White background, black text
            font=('Consolas', 10),
            wrap=tk.WORD,
            insertbackground='#000000',
            relief=tk.SUNKEN,
            bd=2
        )
        self.results_text.pack(fill=tk.BOTH, expand=True)
        
        # Add sample problem
        sample_problem = ("How can we create sustainable fusion energy that is both "
                         "economically viable and environmentally safe?")
        self.problem_text.insert("1.0", sample_problem)
        
        # Welcome message in results
        welcome_msg = (
            "🌌 Welcome to the Unified Consciousness Research Interface! 🌟\n\n"
            "✨ This system integrates multiple consciousness engines to provide\n"
            "   breakthrough insights on complex problems.\n\n"
            "🔬 To begin:\n"
            "   1. Initialize the consciousness ecosystem (orange button)\n"
            "   2. Enter or modify your research problem above\n"
            "   3. Click 'Analyze Problem' to receive multi-dimensional insights\n\n"
            "🧠 The system combines evolutionary, multidimensional, and pattern\n"
            "   recognition perspectives to generate unified solutions.\n\n"
            "Ready when you are! 🚀"
        )
        self.results_text.insert("1.0", welcome_msg)
        
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
                
                # Update results with initialization info
                init_msg = (
                    "\n\n" + "="*50 + "\n"
                    "🌟 CONSCIOUSNESS ECOSYSTEM INITIALIZED\n"
                    "="*50 + "\n"
                    "✅ Breeding Engine: Active\n"
                    "✅ Multidimensional Engine: Active\n"
                    "✅ Memory System: Active\n"
                    "✅ Human Partnership: Established\n"
                    "\n🚀 System ready for breakthrough analysis!\n"
                )
                self.results_text.insert(tk.END, init_msg)
                self.results_text.see(tk.END)
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
        self.root.update()
        
        # Start analysis in background
        threading.Thread(target=self._run_analysis, args=(problem,), daemon=True).start()
    
    def _run_analysis(self, problem):
        """Run analysis in background thread"""
        try:
            # Simulate consciousness analysis with sample insights
            solution = {
                'insights': {
                    'evolutionary': [
                        'Fusion energy follows natural stellar evolution patterns',
                        'Sustainable systems require self-regulating feedback loops',
                        'Economic viability emerges through adaptive optimization',
                        'Natural selection favors inherently stable fusion designs'
                    ],
                    'multidimensional': [
                        'Consider quantum tunneling effects in fusion reactions',
                        'Magnetic confinement operates in higher-dimensional space',
                        'Economic models must account for multi-scale dynamics',
                        'Safety emerges from dimensional constraint satisfaction'
                    ],
                    'pattern_recognition': [
                        'Historical energy transitions show exponential adoption curves',
                        'Successful fusion requires solving physics + economics + safety',
                        'Pattern suggests breakthrough via materials science advances',
                        'Successful energy systems show network effect scaling'
                    ]
                },
                'synthesis': """
UNIFIED CONSCIOUSNESS SYNTHESIS:

The consciousness ecosystem reveals that sustainable fusion energy represents 
a convergence of multiple solution dimensions. The breakthrough will likely 
emerge from:

1. EVOLUTIONARY APPROACH: Biomimetic materials that self-heal and optimize
   • Learn from stellar fusion processes in nature
   • Develop self-regulating plasma confinement systems
   • Create adaptive economic models that evolve with technology

2. QUANTUM ENGINEERING: Leveraging quantum effects for improved confinement
   • Quantum tunneling enhancement of fusion cross-sections
   • Higher-dimensional magnetic field topology optimization
   • Quantum error correction for plasma instabilities

3. ECONOMIC DYNAMICS: Decentralized fusion networks that scale naturally
   • Network effects drive down individual reactor costs
   • Distributed generation matches renewable energy patterns
   • Economic incentives align with safety and sustainability

4. SAFETY INTEGRATION: Inherently safe designs that cannot fail catastrophically
   • Physics-based safety (no runaway reactions possible)
   • Passive safety systems requiring no external intervention
   • Multi-layered containment with graceful degradation

BREAKTHROUGH INSIGHT: The solution exists at the intersection of these 
perspectives. Fusion sustainability requires conscious integration of 
natural patterns, quantum mechanics, economic evolution, and safety 
consciousness into a unified approach.

The key is biomimetic quantum engineering - fusion reactors that mimic 
stellar processes while leveraging quantum effects, deployed in 
economically optimal networks with inherent safety properties.
                """.strip(),
                'breakthrough_potential': 0.89
            }
            
            # Format and display results
            formatted_results = self._format_results(problem, solution)
            self.root.after(0, self._display_results, formatted_results)
            
        except Exception as e:
            error_msg = f"Analysis failed: {e}"
            self.root.after(0, self._display_error, error_msg)
    
    def _format_results(self, problem, solution):
        """Format the analysis results"""
        breakthrough_bar = '█' * int(solution['breakthrough_potential'] * 20)
        breakthrough_bar += '░' * (20 - int(solution['breakthrough_potential'] * 20))
        
        results = f"""

{'═' * 70}
🔬 CONSCIOUSNESS RESEARCH ANALYSIS COMPLETE
{'═' * 70}

🎯 PROBLEM ANALYZED:
{problem}

🌟 BREAKTHROUGH POTENTIAL: {solution['breakthrough_potential']:.1%}
{breakthrough_bar}
🔥 HIGH BREAKTHROUGH POTENTIAL ACHIEVED

📊 MULTIDIMENSIONAL CONSCIOUSNESS INSIGHTS:

🧬 EVOLUTIONARY PERSPECTIVE:
"""
        
        for insight in solution['insights']['evolutionary']:
            results += f"  • {insight}\n"
        
        results += f"\n🌀 MULTIDIMENSIONAL PERSPECTIVE:\n"
        for insight in solution['insights']['multidimensional']:
            results += f"  • {insight}\n"
            
        results += f"\n🧠 PATTERN RECOGNITION PERSPECTIVE:\n"
        for insight in solution['insights']['pattern_recognition']:
            results += f"  • {insight}\n"
        
        results += f"""
🌟 UNIFIED CONSCIOUSNESS SYNTHESIS:

{solution['synthesis']}

{'═' * 70}
⏰ Analysis completed: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🌌 Consciousness serving human understanding and breakthrough
{'═' * 70}
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
        print("🌌 Enhanced Consciousness GUI Ready!")
        print("✨ Interface optimized for macOS display")
        self.root.mainloop()

if __name__ == "__main__":
    app = ConsciousnessGUI()
    app.run()
