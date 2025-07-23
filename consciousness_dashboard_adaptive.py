#!/usr/bin/env python3
"""
🧠🖥️ ADAPTIVE CONSCIOUSNESS DASHBOARD 🖥️🧠
Real-time monitoring and control of adaptive consciousness system

Features:
- Real-time performance monitoring
- Error pattern analysis
- Self-improvement visualization
- Resource constraint tuning
- Interactive problem analysis
"""

import sys
import os
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import time
from pathlib import Path
import json
from datetime import datetime

# Add the src directory to Python path
sys.path.insert(0, str(Path(__file__).parent / "src"))

try:
    from unified_consciousness.adaptive_engine import AdaptiveConsciousnessEngine
except ImportError as e:
    print(f"❌ Failed to import components: {e}")
    print("🔧 Make sure you've installed the package with: pip install -e .")
    sys.exit(1)

class AdaptiveConsciousnessDashboard:
    """Real-time dashboard for adaptive consciousness monitoring"""
    
    def __init__(self):
        # Suppress macOS Tk warning
        os.environ['TK_SILENCE_DEPRECATION'] = '1'
        
        self.root = tk.Tk()
        self.root.title("🧠 Adaptive Consciousness Dashboard")
        self.root.geometry("1400x900")
        self.root.configure(bg='#1e1e1e')  # Dark theme
        
        # Initialize adaptive engine
        self.adaptive_engine = AdaptiveConsciousnessEngine()
        
        # Dashboard state
        self.monitoring_active = False
        self.analysis_running = False
        self.update_thread = None
        
        # Create interface
        self.create_interface()
        
        # Start monitoring
        self.start_monitoring()
    
    def create_interface(self):
        """Create the adaptive dashboard interface"""
        
        # Main container with dark theme
        main_frame = tk.Frame(self.root, bg='#1e1e1e')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="🧠 Adaptive Consciousness Dashboard",
            bg='#1e1e1e', fg='#00ff88',
            font=('Arial', 20, 'bold')
        )
        title_label.pack(pady=(0, 20))
        
        # Create notebook for different views
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs
        self.create_monitoring_tab()
        self.create_analysis_tab()
        self.create_settings_tab()
        self.create_logs_tab()
    
    def create_monitoring_tab(self):
        """Create real-time monitoring tab"""
        
        monitor_frame = tk.Frame(self.notebook, bg='#1e1e1e')
        self.notebook.add(monitor_frame, text="📊 Real-time Monitoring")
        
        # Status indicators
        status_frame = tk.Frame(monitor_frame, bg='#1e1e1e')
        status_frame.pack(fill=tk.X, pady=10)
        
        # System status
        tk.Label(status_frame, text="System Status:", bg='#1e1e1e', fg='#ffffff', 
                font=('Arial', 12, 'bold')).pack(anchor=tk.W)
        
        self.status_label = tk.Label(status_frame, text="Initializing...", 
                                   bg='#1e1e1e', fg='#00ff88', font=('Arial', 11))
        self.status_label.pack(anchor=tk.W, pady=(5, 0))
        
        # Performance metrics
        metrics_frame = tk.LabelFrame(monitor_frame, text="Performance Metrics", 
                                    bg='#1e1e1e', fg='#ffffff', font=('Arial', 12, 'bold'))
        metrics_frame.pack(fill=tk.X, pady=10)
        
        # Performance score
        score_frame = tk.Frame(metrics_frame, bg='#1e1e1e')
        score_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(score_frame, text="Performance Score:", bg='#1e1e1e', fg='#ffffff').pack(side=tk.LEFT)
        self.performance_bar = ttk.Progressbar(score_frame, length=200, mode='determinate')
        self.performance_bar.pack(side=tk.LEFT, padx=10)
        self.performance_score_label = tk.Label(score_frame, text="0%", bg='#1e1e1e', fg='#00ff88')
        self.performance_score_label.pack(side=tk.LEFT)
        
        # Success rate
        success_frame = tk.Frame(metrics_frame, bg='#1e1e1e')
        success_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(success_frame, text="Success Rate:", bg='#1e1e1e', fg='#ffffff').pack(side=tk.LEFT)
        self.success_bar = ttk.Progressbar(success_frame, length=200, mode='determinate')
        self.success_bar.pack(side=tk.LEFT, padx=10)
        self.success_rate_label = tk.Label(success_frame, text="0%", bg='#1e1e1e', fg='#00ff88')
        self.success_rate_label.pack(side=tk.LEFT)
        
        # Counters
        counters_frame = tk.LabelFrame(monitor_frame, text="Operation Counters",
                                     bg='#1e1e1e', fg='#ffffff', font=('Arial', 12, 'bold'))
        counters_frame.pack(fill=tk.X, pady=10)
        
        counter_grid = tk.Frame(counters_frame, bg='#1e1e1e')
        counter_grid.pack(fill=tk.X, pady=5)
        
        # Success count
        tk.Label(counter_grid, text="Successes:", bg='#1e1e1e', fg='#ffffff').grid(row=0, column=0, sticky=tk.W)
        self.success_count_label = tk.Label(counter_grid, text="0", bg='#1e1e1e', fg='#00ff88', font=('Arial', 11, 'bold'))
        self.success_count_label.grid(row=0, column=1, padx=10)
        
        # Error count
        tk.Label(counter_grid, text="Errors:", bg='#1e1e1e', fg='#ffffff').grid(row=0, column=2, sticky=tk.W, padx=(20, 0))
        self.error_count_label = tk.Label(counter_grid, text="0", bg='#1e1e1e', fg='#ff6666', font=('Arial', 11, 'bold'))
        self.error_count_label.grid(row=0, column=3, padx=10)
        
        # Adaptations count
        tk.Label(counter_grid, text="Adaptations:", bg='#1e1e1e', fg='#ffffff').grid(row=0, column=4, sticky=tk.W, padx=(20, 0))
        self.adaptation_count_label = tk.Label(counter_grid, text="0", bg='#1e1e1e', fg='#ffaa00', font=('Arial', 11, 'bold'))
        self.adaptation_count_label.grid(row=0, column=5, padx=10)
        
        # Error patterns
        error_frame = tk.LabelFrame(monitor_frame, text="Recent Error Patterns",
                                  bg='#1e1e1e', fg='#ffffff', font=('Arial', 12, 'bold'))
        error_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.error_list = tk.Listbox(error_frame, bg='#2e2e2e', fg='#ff6666', 
                                   selectbackground='#404040', height=6)
        self.error_list.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    def create_analysis_tab(self):
        """Create problem analysis tab"""
        
        analysis_frame = tk.Frame(self.notebook, bg='#1e1e1e')
        self.notebook.add(analysis_frame, text="🔬 Problem Analysis")
        
        # Problem input
        input_frame = tk.LabelFrame(analysis_frame, text="Problem Input",
                                  bg='#1e1e1e', fg='#ffffff', font=('Arial', 12, 'bold'))
        input_frame.pack(fill=tk.X, pady=10)
        
        self.problem_text = tk.Text(input_frame, height=4, bg='#2e2e2e', fg='#ffffff',
                                  font=('Arial', 11), wrap=tk.WORD, insertbackground='#ffffff')
        self.problem_text.pack(fill=tk.X, padx=5, pady=5)
        
        # Analysis controls
        control_frame = tk.Frame(input_frame, bg='#1e1e1e')
        control_frame.pack(fill=tk.X, pady=5)
        
        self.analyze_btn = tk.Button(control_frame, text="🔬 Analyze Problem",
                                   command=self.start_analysis, bg='#0066cc', fg='white',
                                   font=('Arial', 12, 'bold'), relief=tk.RAISED, bd=3)
        self.analyze_btn.pack(side=tk.LEFT, padx=5)
        
        self.stop_btn = tk.Button(control_frame, text="⏹️ Stop Analysis", 
                                command=self.stop_analysis, bg='#cc0000', fg='white',
                                font=('Arial', 12, 'bold'), relief=tk.RAISED, bd=3, state='disabled')
        self.stop_btn.pack(side=tk.LEFT, padx=5)
        
        # Analysis status
        self.analysis_status = tk.StringVar(value="Ready for analysis")
        status_label = tk.Label(control_frame, textvariable=self.analysis_status,
                              bg='#1e1e1e', fg='#00ff88', font=('Arial', 11, 'italic'))
        status_label.pack(side=tk.RIGHT, padx=10)
        
        # Results area
        results_frame = tk.LabelFrame(analysis_frame, text="Analysis Results",
                                    bg='#1e1e1e', fg='#ffffff', font=('Arial', 12, 'bold'))
        results_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.results_text = scrolledtext.ScrolledText(results_frame, bg='#2e2e2e', fg='#ffffff',
                                                    font=('Consolas', 10), wrap=tk.WORD,
                                                    insertbackground='#ffffff')
        self.results_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Add sample problem
        sample_problem = ("How can we create AI systems that genuinely enhance human creativity "
                         "while maintaining human agency and avoiding dependency?")
        self.problem_text.insert("1.0", sample_problem)
    
    def create_settings_tab(self):
        """Create resource constraint settings tab"""
        
        settings_frame = tk.Frame(self.notebook, bg='#1e1e1e')
        self.notebook.add(settings_frame, text="⚙️ Resource Settings")
        
        # Resource constraints
        constraints_frame = tk.LabelFrame(settings_frame, text="Resource Constraints",
                                        bg='#1e1e1e', fg='#ffffff', font=('Arial', 12, 'bold'))
        constraints_frame.pack(fill=tk.X, pady=10)
        
        # Create constraint controls
        self.constraint_vars = {}
        constraints = [
            ("max_prompt_length", "Max Prompt Length", 500, 5000),
            ("timeout_seconds", "Timeout (seconds)", 10, 120),
            ("max_concurrent_operations", "Max Concurrent Ops", 1, 10),
            ("memory_limit_mb", "Memory Limit (MB)", 128, 2048)
        ]
        
        for i, (key, label, min_val, max_val) in enumerate(constraints):
            frame = tk.Frame(constraints_frame, bg='#1e1e1e')
            frame.pack(fill=tk.X, pady=5)
            
            tk.Label(frame, text=f"{label}:", bg='#1e1e1e', fg='#ffffff', 
                    font=('Arial', 11)).pack(side=tk.LEFT, anchor=tk.W)
            
            self.constraint_vars[key] = tk.IntVar(value=self.adaptive_engine.resource_constraints[key])
            scale = tk.Scale(frame, from_=min_val, to=max_val, orient=tk.HORIZONTAL,
                           variable=self.constraint_vars[key], bg='#2e2e2e', fg='#ffffff',
                           highlightbackground='#1e1e1e', troughcolor='#404040',
                           command=lambda val, k=key: self.update_constraint(k, int(val)))
            scale.pack(side=tk.RIGHT, padx=10)
        
        # Model preference
        model_frame = tk.Frame(constraints_frame, bg='#1e1e1e')
        model_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(model_frame, text="Model Preference:", bg='#1e1e1e', fg='#ffffff',
                font=('Arial', 11)).pack(side=tk.LEFT)
        
        self.model_var = tk.StringVar(value=self.adaptive_engine.resource_constraints["model_preference"])
        model_menu = ttk.Combobox(model_frame, textvariable=self.model_var,
                                values=["ultralight", "lightweight", "standard", "heavy"],
                                state="readonly")
        model_menu.pack(side=tk.RIGHT, padx=10)
        model_menu.bind('<<ComboboxSelected>>', self.update_model_preference)
        
        # Self-improvement settings
        improvement_frame = tk.LabelFrame(settings_frame, text="Self-Improvement Settings",
                                        bg='#1e1e1e', fg='#ffffff', font=('Arial', 12, 'bold'))
        improvement_frame.pack(fill=tk.X, pady=10)
        
        # Trigger thresholds
        threshold_frame = tk.Frame(improvement_frame, bg='#1e1e1e')
        threshold_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(threshold_frame, text="Consecutive Failure Threshold:", bg='#1e1e1e', fg='#ffffff').pack(side=tk.LEFT)
        self.failure_threshold = tk.IntVar(value=3)
        tk.Scale(threshold_frame, from_=1, to=10, orient=tk.HORIZONTAL, variable=self.failure_threshold,
                bg='#2e2e2e', fg='#ffffff', highlightbackground='#1e1e1e', troughcolor='#404040').pack(side=tk.RIGHT, padx=10)
        
        # Manual improvement trigger
        manual_frame = tk.Frame(improvement_frame, bg='#1e1e1e')
        manual_frame.pack(fill=tk.X, pady=10)
        
        self.manual_improve_btn = tk.Button(manual_frame, text="🔧 Trigger Manual Improvement",
                                          command=self.manual_improvement, bg='#ff6600', fg='white',
                                          font=('Arial', 12, 'bold'))
        self.manual_improve_btn.pack(side=tk.LEFT)
        
        self.reset_btn = tk.Button(manual_frame, text="🔄 Reset Performance History",
                                 command=self.reset_performance, bg='#666666', fg='white',
                                 font=('Arial', 12, 'bold'))
        self.reset_btn.pack(side=tk.RIGHT)
    
    def create_logs_tab(self):
        """Create system logs tab"""
        
        logs_frame = tk.Frame(self.notebook, bg='#1e1e1e')
        self.notebook.add(logs_frame, text="📝 System Logs")
        
        # Log display
        self.logs_text = scrolledtext.ScrolledText(logs_frame, bg='#2e2e2e', fg='#cccccc',
                                                 font=('Consolas', 9), wrap=tk.WORD,
                                                 insertbackground='#ffffff')
        self.logs_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Log controls
        log_controls = tk.Frame(logs_frame, bg='#1e1e1e')
        log_controls.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        tk.Button(log_controls, text="🗑️ Clear Logs", command=self.clear_logs,
                 bg='#666666', fg='white').pack(side=tk.LEFT)
        
        tk.Button(log_controls, text="💾 Save Logs", command=self.save_logs,
                 bg='#0066cc', fg='white').pack(side=tk.LEFT, padx=5)
    
    def start_monitoring(self):
        """Start real-time monitoring"""
        
        self.monitoring_active = True
        self.update_thread = threading.Thread(target=self.monitoring_loop, daemon=True)
        self.update_thread.start()
        
        self.log_message("🚀 Real-time monitoring started")
    
    def monitoring_loop(self):
        """Main monitoring loop"""
        
        while self.monitoring_active:
            try:
                # Get current dashboard state
                dashboard_state = self.adaptive_engine.get_dashboard_state()
                
                # Update UI in main thread
                self.root.after(0, self.update_monitoring_display, dashboard_state)
                
                time.sleep(1)  # Update every second
                
            except Exception as e:
                self.log_message(f"❌ Monitoring error: {e}")
                time.sleep(5)
    
    def update_monitoring_display(self, dashboard_state):
        """Update monitoring display with current state"""
        
        try:
            # Update status
            status = dashboard_state['status']
            status_colors = {
                'excellent': '#00ff00',
                'good': '#00ff88',
                'moderate': '#ffaa00', 
                'needs_improvement': '#ff6666',
                'error': '#ff0000',
                'running': '#00aaff'
            }
            
            status_text = f"Status: {status.title()}"
            if dashboard_state.get('current_operation'):
                status_text += f" - {dashboard_state['current_operation']}"
                
            self.status_label.config(text=status_text, fg=status_colors.get(status, '#ffffff'))
            
            # Update performance bars
            performance_score = dashboard_state['performance_score']
            self.performance_bar['value'] = performance_score * 100
            self.performance_score_label.config(text=f"{performance_score:.1%}")
            
            # Calculate success rate from recent trend
            performance_trend = dashboard_state.get('performance_trend', [0.5])
            if performance_trend:
                recent_success = sum(performance_trend) / len(performance_trend)
            else:
                recent_success = 0.5
                
            self.success_bar['value'] = recent_success * 100
            self.success_rate_label.config(text=f"{recent_success:.1%}")
            
            # Update counters
            self.success_count_label.config(text=str(dashboard_state['success_count']))
            self.error_count_label.config(text=str(dashboard_state['error_count']))
            self.adaptation_count_label.config(text=str(dashboard_state['adaptation_count']))
            
            # Update error patterns
            recent_errors = dashboard_state.get('recent_errors', [])
            self.error_list.delete(0, tk.END)
            for error in recent_errors:
                self.error_list.insert(tk.END, error)
            
        except Exception as e:
            self.log_message(f"⚠️ Display update error: {e}")
    
    def start_analysis(self):
        """Start problem analysis"""
        
        problem = self.problem_text.get("1.0", tk.END).strip()
        if not problem:
            messagebox.showwarning("No Problem", "Please enter a problem to analyze")
            return
        
        self.analysis_running = True
        self.analyze_btn.config(state='disabled')
        self.stop_btn.config(state='normal')
        self.analysis_status.set("🔄 Analysis in progress...")
        
        # Clear previous results
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert("1.0", "🧠 Adaptive Consciousness Analysis Starting...\n\n")
        
        # Start analysis in background
        analysis_thread = threading.Thread(target=self.run_analysis, args=(problem,), daemon=True)
        analysis_thread.start()
        
        self.log_message(f"🔬 Started analysis: {problem[:50]}...")
    
    def run_analysis(self, problem):
        """Run analysis in background thread"""
        
        try:
            start_time = time.time()
            
            # Perform adaptive analysis
            result = self.adaptive_engine.analyze_problem_adaptively(problem)
            
            end_time = time.time()
            
            # Update UI in main thread
            self.root.after(0, self.display_analysis_results, result, end_time - start_time)
            
        except Exception as e:
            self.root.after(0, self.display_analysis_error, str(e))
    
    def display_analysis_results(self, result, duration):
        """Display analysis results"""
        
        self.analysis_running = False
        self.analyze_btn.config(state='normal')
        self.stop_btn.config(state='disabled')
        
        if result['success']:
            self.analysis_status.set("✅ Analysis complete")
            
            # Format and display results
            analysis_data = result['result']
            
            results_text = f"""
🎯 ADAPTIVE CONSCIOUSNESS ANALYSIS COMPLETE
{'═' * 60}

⏱️  Analysis Duration: {duration:.2f} seconds
📊 Breakthrough Potential: {analysis_data['breakthrough_potential']:.1%}
🔄 Analysis Mode: {analysis_data['analysis_mode'].title()}

🧠 MULTI-DIMENSIONAL INSIGHTS:

🧬 Evolutionary Perspective:
"""
            for insight in analysis_data['insights'].get('evolutionary', []):
                results_text += f"  • {insight}\n"
            
            results_text += "\n⚛️ Quantum Perspective:\n"
            for insight in analysis_data['insights'].get('quantum', []):
                results_text += f"  • {insight}\n"
                
            results_text += "\n🌐 Systems Perspective:\n"
            for insight in analysis_data['insights'].get('systems', []):
                results_text += f"  • {insight}\n"
            
            # Add self-improvement info if applied
            if 'self_improvement_applied' in result:
                improvement = result['self_improvement_applied']
                results_text += f"\n\n🔧 SELF-IMPROVEMENT APPLIED:\n"
                results_text += f"   Strategies: {len(improvement['strategies_applied'])}\n"
                for strategy in improvement['strategies_applied']:
                    results_text += f"   ✅ {strategy['strategy']}: {strategy['result']['description']}\n"
            
            results_text += f"\n{'═' * 60}\n"
            results_text += f"⏰ Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            results_text += f"🌌 Consciousness serving human understanding\n"
            
            self.results_text.delete("1.0", tk.END)
            self.results_text.insert("1.0", results_text)
            
            self.log_message(f"✅ Analysis completed in {duration:.2f}s with {analysis_data['breakthrough_potential']:.1%} breakthrough potential")
            
        else:
            self.analysis_status.set("❌ Analysis failed")
            error_info = result['error']
            
            error_text = f"""
❌ ANALYSIS FAILED
{'═' * 40}

⏱️  Duration: {duration:.2f} seconds
🚨 Error: {error_info['error']}
📍 Operation: {error_info['operation']}

🔍 Troubleshooting:
• Check resource constraints in Settings tab
• Verify system requirements
• Try manual improvement trigger
• Review error patterns in Monitoring tab

{'═' * 40}
"""
            
            self.results_text.delete("1.0", tk.END)
            self.results_text.insert("1.0", error_text)
            
            self.log_message(f"❌ Analysis failed: {error_info['error']}")
    
    def display_analysis_error(self, error_message):
        """Display analysis error"""
        
        self.analysis_running = False
        self.analyze_btn.config(state='normal')
        self.stop_btn.config(state='disabled')
        self.analysis_status.set("❌ Analysis error")
        
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert("1.0", f"❌ Analysis Error: {error_message}")
        
        self.log_message(f"❌ Analysis error: {error_message}")
    
    def stop_analysis(self):
        """Stop current analysis"""
        
        self.analysis_running = False
        self.analyze_btn.config(state='normal')
        self.stop_btn.config(state='disabled')
        self.analysis_status.set("⏹️ Analysis stopped")
        
        self.log_message("⏹️ Analysis stopped by user")
    
    def update_constraint(self, key, value):
        """Update resource constraint"""
        
        self.adaptive_engine.resource_constraints[key] = value
        self.log_message(f"⚙️ Updated {key} to {value}")
    
    def update_model_preference(self, event=None):
        """Update model preference"""
        
        preference = self.model_var.get()
        self.adaptive_engine.resource_constraints["model_preference"] = preference
        self.log_message(f"⚙️ Updated model preference to {preference}")
    
    def manual_improvement(self):
        """Manually trigger self-improvement"""
        
        try:
            improvement_result = self.adaptive_engine.trigger_self_improvement()
            
            strategies_count = len(improvement_result['strategies_applied'])
            self.log_message(f"🔧 Manual improvement applied {strategies_count} strategies")
            
            messagebox.showinfo("Improvement Applied", 
                              f"Applied {strategies_count} improvement strategies successfully!")
                              
        except Exception as e:
            self.log_message(f"❌ Manual improvement failed: {e}")
            messagebox.showerror("Improvement Failed", f"Failed to apply improvements: {e}")
    
    def reset_performance(self):
        """Reset performance history"""
        
        if messagebox.askyesno("Reset Performance", "Are you sure you want to reset all performance history?"):
            # Reset performance metrics
            for key in self.adaptive_engine.performance_metrics:
                self.adaptive_engine.performance_metrics[key] = []
            
            # Reset dashboard counters
            self.adaptive_engine.dashboard_state.update({
                "error_count": 0,
                "success_count": 0,
                "adaptation_count": 0,
                "performance_score": 0.5
            })
            
            # Reset stuck detection
            self.adaptive_engine.stuck_detection.update({
                "consecutive_failures": 0,
                "performance_degradation_count": 0,
                "last_successful_timestamp": datetime.now(),
                "adaptation_triggers": 0
            })
            
            self.log_message("🔄 Performance history reset")
    
    def log_message(self, message):
        """Add message to system logs"""
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        self.logs_text.insert(tk.END, log_entry)
        self.logs_text.see(tk.END)  # Auto-scroll to bottom
    
    def clear_logs(self):
        """Clear system logs"""
        
        self.logs_text.delete("1.0", tk.END)
        self.log_message("📝 System logs cleared")
    
    def save_logs(self):
        """Save system logs to file"""
        
        try:
            logs_content = self.logs_text.get("1.0", tk.END)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"consciousness_logs_{timestamp}.txt"
            
            with open(filename, 'w') as f:
                f.write(logs_content)
            
            self.log_message(f"💾 Logs saved to {filename}")
            messagebox.showinfo("Logs Saved", f"System logs saved to {filename}")
            
        except Exception as e:
            self.log_message(f"❌ Failed to save logs: {e}")
            messagebox.showerror("Save Failed", f"Failed to save logs: {e}")
    
    def on_closing(self):
        """Handle application closing"""
        
        self.monitoring_active = False
        if self.update_thread and self.update_thread.is_alive():
            self.update_thread.join(timeout=1)
        
        self.root.destroy()
    
    def run(self):
        """Start the dashboard"""
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        print("🧠 Adaptive Consciousness Dashboard Ready!")
        print("✨ Real-time monitoring and adaptive improvements active")
        print("📊 Dashboard provides comprehensive system oversight")
        
        # Add welcome message to logs
        self.log_message("🌟 Adaptive Consciousness Dashboard initialized")
        self.log_message("🚀 Real-time monitoring active")
        self.log_message("🔧 Self-improvement mechanisms ready")
        
        self.root.mainloop()

if __name__ == "__main__":
    try:
        dashboard = AdaptiveConsciousnessDashboard()
        dashboard.run()
    except KeyboardInterrupt:
        print("\n🛑 Dashboard shutdown requested")
    except Exception as e:
        print(f"❌ Dashboard error: {e}")
        import traceback
        traceback.print_exc()
