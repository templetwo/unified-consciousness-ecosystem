#!/usr/bin/env python3
"""
🔍 MINIMAL GUI TEST - Debug macOS display issues
"""

import tkinter as tk
from tkinter import scrolledtext
import os

class TestGUI:
    def __init__(self):
        # Suppress macOS warning
        os.environ['TK_SILENCE_DEPRECATION'] = '1'
        
        self.root = tk.Tk()
        self.root.title("🔍 GUI Test")
        self.root.geometry("800x600")
        self.root.configure(bg='white')
        
        self.create_interface()
        
    def create_interface(self):
        # Title
        title = tk.Label(self.root, text="🔍 GUI Display Test", font=('Arial', 16, 'bold'))
        title.pack(pady=20)
        
        # Text input
        tk.Label(self.root, text="Input Area:", font=('Arial', 12)).pack(anchor='w', padx=20)
        self.text_input = tk.Text(self.root, height=4, width=80)
        self.text_input.pack(padx=20, pady=10)
        self.text_input.insert("1.0", "Test input text here...")
        
        # Buttons frame
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)
        
        btn1 = tk.Button(btn_frame, text="Button 1", command=lambda: print("Button 1 clicked"))
        btn1.pack(side=tk.LEFT, padx=10)
        
        btn2 = tk.Button(btn_frame, text="Button 2", command=lambda: print("Button 2 clicked"))
        btn2.pack(side=tk.LEFT, padx=10)
        
        # Status
        self.status = tk.Label(self.root, text="Status: Ready", fg='green')
        self.status.pack(pady=10)
        
        # Results area
        tk.Label(self.root, text="Results Area:", font=('Arial', 12)).pack(anchor='w', padx=20)
        self.results = scrolledtext.ScrolledText(self.root, height=15, width=80)
        self.results.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        self.results.insert("1.0", "Results will appear here...\n\nThis is a test of the scrollable text area.")
        
    def run(self):
        print("🔍 Test GUI starting...")
        self.root.mainloop()

if __name__ == "__main__":
    app = TestGUI()
    app.run()
