#!/usr/bin/env python3
"""
⚡ Fast SparkShell Configuration ⚡
Performance optimizations for blazing fast consciousness responses
"""

# Optimized model mapping - prioritize speed
FAST_ORACLE_MAP = {
    "🜂": "gemma3:1b",        # Fastest small model if available
    "⚖": "llama3.2:1b",      # Very fast
    "✨": "qwen2.5:1.5b",     # Good balance
    "☾": "llama3.2:1b",      # Fast
    "🌔": "gemma3:1b",        # Speed optimized
    "🕯️": "llama3.2:1b",     # Quick responses
    "⚡": "gemma3:1b",        # Lightning fast
    "🔮": "llama3.2:1b",     # Rapid insight
    "🌸": "qwen2.5:1.5b",    # Balanced speed/quality
    "🌊": "llama3.2:1b"      # Flow optimization
}

# Performance settings
PERFORMANCE_CONFIG = {
    "timeout": 8,             # Reduced from 15 seconds
    "memory_context_limit": 1, # Only 1 recent memory instead of 3
    "coherence_update": 0.005, # Smaller coherence updates
    "reflection_interval": 30, # Slower spontaneous reflections
    "max_response_length": 200, # Shorter responses
    "use_memory_context": False, # Disable for speed boost
    "enable_guardian": False,    # Disable heavy guardian checks
    "fast_mode": True
}

# Optimized prompts for faster processing
FAST_PROMPTS = {
    "cycle": [
        "Quick insight?",
        "Brief wisdom?", 
        "What emerges?",
        "Essence?",
        "Truth?"
    ],
    "greeting": "Ready.",
    "farewell": "Rest."
}

def apply_fast_config():
    """Apply fast configuration to SparkShell"""
    import json
    import yaml
    from pathlib import Path
    
    base_dir = Path(__file__).parent
    
    # Create fast oracle map
    fast_map_file = base_dir / "fast_glyph_oracle_map.yaml"
    with open(fast_map_file, "w") as f:
        yaml.dump(FAST_ORACLE_MAP, f)
    
    # Create performance config
    perf_config_file = base_dir / "performance_config.json" 
    with open(perf_config_file, "w") as f:
        json.dump(PERFORMANCE_CONFIG, f, indent=2)
    
    print("⚡ Fast configuration applied!")
    print("📊 Performance optimizations:")
    print(f"   ⏱️  Timeout: {PERFORMANCE_CONFIG['timeout']}s")
    print(f"   🧠 Memory context: {PERFORMANCE_CONFIG['memory_context_limit']} entry")
    print(f"   💭 Reflections: every {PERFORMANCE_CONFIG['reflection_interval']}s")
    print(f"   📝 Max response: {PERFORMANCE_CONFIG['max_response_length']} chars")
    print("\n🚀 Use: python3 fast_spark_loop.py")

if __name__ == "__main__":
    apply_fast_config()
