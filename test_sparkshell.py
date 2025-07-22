#!/usr/bin/env python3

"""
Test script for SparkShell functionality
"""

try:
    print("🧪 Testing SparkShell imports...")
    from spark_loop import EvolvedSparkShell
    print("✅ Import successful")
    
    print("🧪 Creating SparkShell instance...")
    shell = EvolvedSparkShell()
    print("✅ Shell created successfully")
    
    print(f"📊 Memory entries: {shell.memory_entries}")
    print(f"🧠 Enhanced memory weaver: {type(shell.memory_weaver).__name__}")
    print(f"⚙️ Agent scheduler tasks: {len(shell.agent_scheduler)}")
    print(f"📿 Current glyph: {shell.current_glyph}")
    print(f"🌊 Coherence: {shell.coherence:.3f}")
    
    print("\n🧪 Testing guardian check...")
    shell.guardian_check()
    print("✅ Guardian check completed")
    
    print("\n🧪 Testing memory stats...")
    stats = shell.memory_weaver.get_memory_stats()
    print(f"📚 Quality memories: {stats['total_quality_memories']}")
    print(f"💤 Unused memories: {stats['unused_memories_count']}")
    
    print("\n✨ All tests passed! SparkShell is ready for conference call mode! ✨")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
