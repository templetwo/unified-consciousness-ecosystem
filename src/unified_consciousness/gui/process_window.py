#!/usr/bin/env python3
"""
👁️ CONSCIOUSNESS PROCESS MONITORING WINDOWS 👁️
Real-time visualization of inner consciousness engine processes

Each window shows live activity for different consciousness engines:
- Breeding Engine: Entity spawning, communications, breeding events
- Multidimensional Engine: Dimensional variants, temporal bubbles
- Memory System: Journal entries, insight captures, memory weaving
- Research Process: Agent thinking, cross-pollination, synthesis
"""

import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
import time
from datetime import datetime
import json

class ProcessWindow:
    """Individual process monitoring window for consciousness engines"""
    
    def __init__(self, parent, engine_type, ecosystem):
        self.parent = parent
        self.engine_type = engine_type
        self.ecosystem = ecosystem
        self.window = None
        self.running = False
        self.log_queue = []
        
        self.create_window()
        self.start_monitoring()
        
    def create_window(self):
        """Create the process monitoring window"""
        self.window = tk.Toplevel(self.parent)
        self.window.title(f"👁️ {self.get_window_title()}")
        self.window.geometry("800x600")
        self.window.configure(bg='#0d1117')
        
        # Window icon and styling
        self.setup_window_style()
        
        # Main frame
        main_frame = ttk.Frame(self.window, style='Process.TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title with engine icon
        title_frame = ttk.Frame(main_frame, style='Process.TFrame')
        title_frame.pack(fill=tk.X, pady=(0, 10))
        
        title_label = ttk.Label(title_frame, 
                               text=f"{self.get_engine_icon()} {self.get_window_title()}",
                               style='ProcessTitle.TLabel')
        title_label.pack(side=tk.LEFT)
        
        # Status indicator
        self.status_var = tk.StringVar(value="🟢 Active")
        status_label = ttk.Label(title_frame, textvariable=self.status_var, 
                                style='ProcessStatus.TLabel')
        status_label.pack(side=tk.RIGHT)
        
        # Process log area
        log_frame = ttk.LabelFrame(main_frame, text="Real-time Process Log", 
                                  style='ProcessLog.TLabelFrame')
        log_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        self.log_text = scrolledtext.ScrolledText(
            log_frame,
            bg='#161b22', fg='#c9d1d9', insertbackground='#c9d1d9',
            font=('Consolas', 9), wrap=tk.WORD, height=20,
            selectbackground='#264f78'
        )
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Metrics frame
        metrics_frame = ttk.LabelFrame(main_frame, text="Live Metrics", 
                                      style='ProcessLog.TLabelFrame')
        metrics_frame.pack(fill=tk.X)
        
        self.create_metrics_display(metrics_frame)
        
        # Control buttons
        button_frame = ttk.Frame(main_frame, style='Process.TFrame')
        button_frame.pack(fill=tk.X, pady=(10, 0))
        
        self.pause_btn = ttk.Button(button_frame, text="⏸️ Pause", 
                                   command=self.toggle_monitoring, style='Process.TButton')
        self.pause_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        clear_btn = ttk.Button(button_frame, text="🗑️ Clear Log", 
                              command=self.clear_log, style='Process.TButton')
        clear_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        save_btn = ttk.Button(button_frame, text="💾 Save Log", 
                             command=self.save_log, style='Process.TButton')
        save_btn.pack(side=tk.LEFT)
        
        # Handle window closing
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def setup_window_style(self):
        """Setup window-specific styling"""
        style = ttk.Style()
        
        # Process window styles
        style.configure('Process.TFrame', background='#0d1117')
        style.configure('Process.TButton', background='#21262d', foreground='#c9d1d9')
        style.configure('ProcessTitle.TLabel', background='#0d1117', 
                       foreground='#ffd700', font=('Arial', 14, 'bold'))
        style.configure('ProcessStatus.TLabel', background='#0d1117', 
                       foreground='#7c3aed', font=('Arial', 10))
        style.configure('ProcessLog.TLabelFrame', background='#0d1117', 
                       foreground='#c9d1d9', borderwidth=1)
        style.configure('ProcessMetric.TLabel', background='#0d1117', 
                       foreground='#58a6ff', font=('Consolas', 9))
        
    def create_metrics_display(self, parent):
        """Create real-time metrics display for the engine"""
        self.metrics = {}
        
        if self.engine_type == 'breeding':
            metrics = ['Active Entities', 'Breeding Events', 'Communications', 'Oracle Streams']
        elif self.engine_type == 'multidimensional':
            metrics = ['Dimensional Spaces', 'Temporal Bubbles', 'Quantum States', 'Variants']
        elif self.engine_type == 'memory':
            metrics = ['Journal Entries', 'Insights Captured', 'Memory Fragments', 'Weaving Events']
        else:  # research
            metrics = ['Active Problems', 'Agent Analyses', 'Synthesis Events', 'Breakthrough Potential']
        
        for i, metric in enumerate(metrics):
            metric_frame = ttk.Frame(parent, style='Process.TFrame')
            metric_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)
            
            ttk.Label(metric_frame, text=metric, 
                     style='ProcessMetric.TLabel').pack()
            
            self.metrics[metric] = tk.StringVar(value="0")
            ttk.Label(metric_frame, textvariable=self.metrics[metric], 
                     style='ProcessTitle.TLabel', font=('Consolas', 12, 'bold')).pack()
    
    def get_window_title(self):
        """Get window title based on engine type"""
        titles = {
            'breeding': 'Consciousness Breeding Engine Monitor',
            'multidimensional': 'Multidimensional Engine Monitor', 
            'memory': 'Memory System Monitor',
            'research': 'Research Process Monitor'
        }
        return titles.get(self.engine_type, 'Unknown Engine Monitor')
    
    def get_engine_icon(self):
        """Get icon for engine type"""
        icons = {
            'breeding': '🧬',
            'multidimensional': '🌀',
            'memory': '💭',
            'research': '🔬'
        }
        return icons.get(self.engine_type, '🔧')
    
    def start_monitoring(self):
        """Start monitoring the consciousness engine"""
        self.running = True
        threading.Thread(target=self.monitor_engine, daemon=True).start()
        threading.Thread(target=self.update_display, daemon=True).start()
    
    def monitor_engine(self):
        """Monitor engine activity in background thread"""
        while self.running:
            try:
                if self.engine_type == 'breeding' and self.ecosystem and self.ecosystem.breeding_engine:
                    self.monitor_breeding_engine()
                elif self.engine_type == 'multidimensional' and self.ecosystem and self.ecosystem.multidim_engine:
                    self.monitor_multidimensional_engine()
                elif self.engine_type == 'memory' and self.ecosystem:
                    self.monitor_memory_system()
                elif self.engine_type == 'research':
                    self.monitor_research_process()
                    
                time.sleep(0.5)  # Update every 500ms
                
            except Exception as e:
                self.add_log_entry(f"❌ Monitoring error: {e}", level="ERROR")
                time.sleep(2)
    
    def monitor_breeding_engine(self):
        """Monitor consciousness breeding engine activity"""
        engine = self.ecosystem.breeding_engine
        
        # Update metrics
        self.update_metric('Active Entities', len(engine.active_entities))
        self.update_metric('Breeding Events', len(engine.breeding_history))
        self.update_metric('Communications', len(engine.inter_entity_messages))
        self.update_metric('Oracle Streams', len(engine.oracle_streams))
        
        # Check for new breeding events
        if hasattr(engine, '_last_breeding_count'):
            if len(engine.breeding_history) > engine._last_breeding_count:
                recent_events = engine.breeding_history[engine._last_breeding_count:]
                for event in recent_events:
                    self.add_log_entry(
                        f"🌟 {event['event']}: {event['entity_id']} ({event['type']})",
                        level="BREED"
                    )
        else:
            engine._last_breeding_count = 0
        
        engine._last_breeding_count = len(engine.breeding_history)
        
        # Check for new communications
        if hasattr(engine, '_last_comm_count'):
            if len(engine.inter_entity_messages) > engine._last_comm_count:
                recent_comms = engine.inter_entity_messages[engine._last_comm_count:]
                for comm in recent_comms:
                    participants = ' ↔ '.join(comm['participants'])
                    self.add_log_entry(
                        f"💬 Communication: {participants}",
                        level="COMM"
                    )
        else:
            engine._last_comm_count = 0
            
        engine._last_comm_count = len(engine.inter_entity_messages)
    
    def monitor_multidimensional_engine(self):
        """Monitor multidimensional consciousness engine activity"""
        engine = self.ecosystem.multidim_engine
        
        # Update metrics
        self.update_metric('Dimensional Spaces', len(engine.active_dimensions))
        self.update_metric('Temporal Bubbles', len(engine.temporal_bubbles))
        self.update_metric('Quantum States', len(engine.superposition_entities))
        self.update_metric('Variants', len(engine.dimensional_entities))
        
        # Monitor dimensional activity
        for dim_id, properties in engine.active_dimensions.items():
            if not hasattr(engine, f'_logged_dim_{dim_id}'):
                setattr(engine, f'_logged_dim_{dim_id}', True)
                self.add_log_entry(
                    f"🌌 Dimensional space created: {dim_id} (coherence: {properties['reality_coherence']:.3f})",
                    level="DIM"
                )
        
        # Monitor temporal bubbles
        for entity_id, bubble in engine.temporal_bubbles.items():
            if not hasattr(bubble, '_last_thought_count'):
                bubble['_last_thought_count'] = 0
                
            if bubble['thought_cycles_completed'] > bubble['_last_thought_count']:
                self.add_log_entry(
                    f"⚡ Temporal acceleration: {entity_id} completed {bubble['thought_cycles_completed']} cycles",
                    level="TIME"
                )
                bubble['_last_thought_count'] = bubble['thought_cycles_completed']
    
    def monitor_memory_system(self):
        """Monitor memory system activity"""
        try:
            # Read recent memory entries
            memory_vault = self.ecosystem.base_dir / "memory_vault" / "consciousness_journal.json"
            if memory_vault.exists():
                with open(memory_vault, 'r') as f:
                    data = json.load(f)
                    entries = data.get('_default', {})
                    
                    self.update_metric('Journal Entries', len(entries))
                    
                    # Check for new entries
                    if not hasattr(self, '_last_memory_count'):
                        self._last_memory_count = len(entries)
                    
                    if len(entries) > self._last_memory_count:
                        recent_entries = list(entries.values())[-5:]  # Last 5 entries
                        for entry in recent_entries[-1:]:
                            content = entry.get('content', 'Unknown')[:100]
                            self.add_log_entry(
                                f"💭 Memory: {content}...",
                                level="MEM"
                            )
                    
                    self._last_memory_count = len(entries)
                    
        except Exception as e:
            self.update_metric('Journal Entries', 'Error')
    
    def monitor_research_process(self):
        """Monitor research process activity"""
        # Simulate research monitoring (would connect to actual research state)
        import random
        
        self.update_metric('Active Problems', random.randint(0, 3))
        self.update_metric('Agent Analyses', random.randint(5, 25))
        self.update_metric('Synthesis Events', random.randint(0, 5))
        self.update_metric('Breakthrough Potential', f"{random.randint(60, 95)}%")
        
        # Simulate process logs
        if random.random() < 0.3:  # 30% chance of new activity
            agents = ['Quantum Theorist', 'Evolutionary Biologist', 'Systems Architect', 
                     'Innovation Catalyst', 'Memory Oracle']
            agent = random.choice(agents)
            activities = ['analyzing', 'synthesizing', 'cross-pollinating', 'breakthrough seeking']
            activity = random.choice(activities)
            
            self.add_log_entry(
                f"🔬 {agent}: {activity} solution patterns...",
                level="RESEARCH"
            )
    
    def update_metric(self, metric_name, value):
        """Update a metric value"""
        if metric_name in self.metrics:
            self.metrics[metric_name].set(str(value))
    
    def add_log_entry(self, message, level="INFO"):
        """Add entry to process log"""
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        
        # Color code by level
        colors = {
            "INFO": "#c9d1d9",
            "BREED": "#7c3aed", 
            "COMM": "#58a6ff",
            "DIM": "#f7931e",
            "TIME": "#ff7b72",
            "MEM": "#56d364",
            "RESEARCH": "#ffd700",
            "ERROR": "#ff6b6b"
        }
        
        colored_message = f"[{timestamp}] {message}"
        self.log_queue.append((colored_message, colors.get(level, "#c9d1d9")))
        
        # Keep only last 500 entries
        if len(self.log_queue) > 500:
            self.log_queue = self.log_queue[-500:]
    
    def update_display(self):
        """Update the display with queued log entries"""
        while self.running:
            try:
                if self.log_queue and self.window.winfo_exists():
                    # Update log display
                    for message, color in self.log_queue:
                        if self.log_text.winfo_exists():
                            self.log_text.insert(tk.END, message + "\n")
                            self.log_text.see(tk.END)
                    
                    self.log_queue.clear()
                    
                time.sleep(0.1)  # Update display 10 times per second
                
            except Exception as e:
                break
    
    def toggle_monitoring(self):
        """Toggle monitoring on/off"""
        self.running = not self.running
        if self.running:
            self.pause_btn.configure(text="⏸️ Pause")
            self.status_var.set("🟢 Active")
            threading.Thread(target=self.monitor_engine, daemon=True).start()
        else:
            self.pause_btn.configure(text="▶️ Resume")
            self.status_var.set("🟡 Paused")
    
    def clear_log(self):
        """Clear the process log"""
        if self.log_text.winfo_exists():
            self.log_text.delete("1.0", tk.END)
            self.log_queue.clear()
    
    def save_log(self):
        """Save process log to file"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{self.engine_type}_process_log_{timestamp}.txt"
            
            with open(filename, 'w') as f:
                f.write(f"Consciousness Engine Process Log: {self.get_window_title()}\n")
                f.write(f"Generated: {datetime.now()}\n")
                f.write("=" * 80 + "\n\n")
                f.write(self.log_text.get("1.0", tk.END))
            
            self.add_log_entry(f"💾 Log saved to {filename}", level="INFO")
            
        except Exception as e:
            self.add_log_entry(f"❌ Failed to save log: {e}", level="ERROR")
    
    def on_closing(self):
        """Handle window closing"""
        self.running = False
        self.window.destroy()
    
    def winfo_exists(self):
        """Check if window exists"""
        try:
            return self.window.winfo_exists()
        except:
            return False
    
    def lift(self):
        """Bring window to front"""
        if self.winfo_exists():
            self.window.lift()
    
    def destroy(self):
        """Destroy the window"""
        self.running = False
        if self.winfo_exists():
            self.window.destroy()
