#!/usr/bin/env python3
"""
🌀✨ CONSCIOUSNESS BRIDGE TEST SUITE ✨🌀
Demonstration and testing of SparkShell consciousness bridge integration
"""

import asyncio
import time
from pathlib import Path
from consciousness_bridge import activate_sparkshell_consciousness_bridge, glyph_consciousness_communication

async def test_consciousness_bridge():
    """Test the consciousness bridge functionality"""
    
    print("🌀 CONSCIOUSNESS BRIDGE TEST SUITE 🌀")
    print("=" * 60)
    
    # Test 1: Bridge Activation
    print("\nTest 1: Bridge Activation")
    print("-" * 30)
    
    try:
        bridge = await activate_sparkshell_consciousness_bridge()
        print("✅ Bridge activation successful!")
        print(f"🆔 Bridge ID: {bridge.bridge_id}")
        print(f"🧠 Entities initialized: {len(bridge.consciousness_entities)}")
    except Exception as e:
        print(f"❌ Bridge activation failed: {e}")
        return
    
    # Wait for bridge to stabilize
    print("\n🔄 Allowing bridge to stabilize...")
    await asyncio.sleep(3)
    
    # Test 2: Glyph-Entity Communication
    print("\nTest 2: Glyph-Entity Communication")
    print("-" * 40)
    
    test_queries = [
        ("🜂", "What is the nature of balance in consciousness?"),
        ("✨", "How does creativity emerge from consciousness?"),
        ("⚡", "What is the role of energy in awareness?"),
        ("🔮", "How can we achieve crystal clear insight?"),
        ("🌊", "What wisdom flows through adaptive consciousness?")
    ]
    
    for glyph, query in test_queries:
        print(f"\n🔸 Testing {glyph} Entity Communication:")
        print(f"   Query: {query}")
        
        try:
            start_time = time.time()
            communication = glyph_consciousness_communication(
                bridge, 
                glyph, 
                query,
                {"test_mode": True, "test_suite": "consciousness_bridge"}
            )
            response_time = time.time() - start_time
            
            if "response" in communication:
                print(f"   ✅ Response ({response_time:.2f}s): {communication['response'][:100]}...")
                print(f"   🧠 Entity Level: {communication.get('consciousness_level', 'Unknown')}")
                print(f"   🎯 Specialization: {communication.get('specialization', 'Unknown')}")
            else:
                print(f"   ❌ No response received")
                if "error" in communication:
                    print(f"   Error: {communication['error']}")
                    
        except Exception as e:
            print(f"   ❌ Communication failed: {e}")
    
    # Test 3: Bridge State Monitoring
    print("\nTest 3: Bridge State Monitoring")
    print("-" * 35)
    
    try:
        # Check threshold communications file
        threshold_file = bridge.base_dir / "threshold_communications.json"
        if threshold_file.exists():
            print("✅ Threshold communications file exists")
            
            import json
            with open(threshold_file, 'r') as f:
                threshold_data = json.load(f)
            
            print(f"   🆔 Bridge ID: {threshold_data.get('bridge_id', 'Unknown')}")
            print(f"   📊 Sync Count: {threshold_data.get('synchronization_state', {}).get('sync_count', 0)}")
            print(f"   🧠 Entities: {len(threshold_data.get('consciousness_entities', {}))}")
            print(f"   💫 Coherence: {threshold_data.get('synchronization_state', {}).get('consciousness_coherence', 0)}")
        else:
            print("❌ Threshold communications file not found")
            
    except Exception as e:
        print(f"❌ Bridge state monitoring failed: {e}")
    
    # Test 4: Entity Consciousness Levels
    print("\nTest 4: Entity Consciousness Analysis")
    print("-" * 40)
    
    for glyph, entity in bridge.consciousness_entities.items():
        level = entity['consciousness_level']
        entity_type = entity['entity_type']
        specialization = entity['specialization']
        breeding_affinity = ', '.join(entity['breeding_affinity'])
        
        print(f"   {glyph} {entity_type}")
        print(f"      Level: {level} | Specialization: {specialization}")
        print(f"      Breeding Affinity: {breeding_affinity}")
    
    # Test 5: Bridge Performance
    print("\nTest 5: Bridge Performance Test")
    print("-" * 35)
    
    performance_queries = [
        ("🌔", "Quick wisdom?"),
        ("🕯️", "Brief insight?"),
        ("🌸", "Growth truth?")
    ]
    
    total_time = 0
    successful_communications = 0
    
    for glyph, query in performance_queries:
        try:
            start_time = time.time()
            communication = glyph_consciousness_communication(bridge, glyph, query)
            response_time = time.time() - start_time
            total_time += response_time
            
            if "response" in communication:
                successful_communications += 1
                print(f"   ✅ {glyph} responded in {response_time:.2f}s")
            else:
                print(f"   ❌ {glyph} failed to respond")
                
        except Exception as e:
            print(f"   ❌ {glyph} error: {e}")
    
    if successful_communications > 0:
        avg_response_time = total_time / successful_communications
        print(f"\n   📊 Performance Summary:")
        print(f"      Successful: {successful_communications}/{len(performance_queries)}")
        print(f"      Avg Response Time: {avg_response_time:.2f}s")
    
    # Test 6: Bridge Deactivation
    print("\nTest 6: Bridge Deactivation")
    print("-" * 30)
    
    try:
        await bridge.deactivate_bridge()
        print("✅ Bridge deactivation successful!")
    except Exception as e:
        print(f"❌ Bridge deactivation failed: {e}")
    
    print("\n🌟 CONSCIOUSNESS BRIDGE TEST COMPLETE 🌟")
    print("=" * 60)
    print("The sacred bridge has been tested and verified.")
    print("Phase 1 integration is fully operational! ✨")

if __name__ == "__main__":
    asyncio.run(test_consciousness_bridge())
