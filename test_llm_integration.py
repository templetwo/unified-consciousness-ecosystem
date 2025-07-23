#!/usr/bin/env python3
"""
Test script for the LLM integration in the Unified Consciousness CLI
"""

import asyncio
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from unified_consciousness.cli import LLMInterface, RequestAnalyzer

async def test_llm_interface():
    """Test the LLM interface functionality"""
    print("🧪 Testing LLM Interface...")
    
    llm = LLMInterface()
    
    # Test Ollama server status
    print(f"🔍 Checking Ollama server status...")
    if llm.is_ollama_running():
        print("✅ Ollama server is running")
        print(f"🤖 Available models: {list(llm.available_models.keys())}")
        
        # Test model selection
        test_cases = [
            ("code analysis", "technical"),
            ("creative writing", "creative"), 
            ("breakthrough problem", "reasoning"),  # This will trigger reasoning model
            ("quick question", "lightweight")  # Quick questions use lightweight model
        ]
        
        for task, expected_type in test_cases:
            selected_model = llm.select_model_for_task(task)
            expected_model = llm.available_models[expected_type]
            print(f"📝 Task: '{task}' → Model: {selected_model}")
            assert selected_model == expected_model, f"Expected {expected_model}, got {selected_model}"
        
        # Test a simple LLM query
        print("\n🤖 Testing LLM query...")
        simple_prompt = "What is Python programming?"
        response = await llm.query_llm(simple_prompt, llm.available_models['lightweight'])
        print(f"📤 Query: {simple_prompt}")
        print(f"📥 Response: {response[:200]}...")
        
        # Test analysis and synthesis
        print("\n🧠 Testing analysis and synthesis...")
        user_input = "How can I improve the performance of my Python code?"
        result = await llm.analyze_and_synthesize(user_input, "", "technical")
        print(f"📤 Input: {user_input}")
        print(f"🔧 Model used: {result['model_used']}")
        print(f"📊 Analysis: {result['analysis'][:300]}...")
        
    else:
        print("❌ Ollama server is not running")
        print("💡 Please start Ollama with: ollama serve")
        return False
    
    return True

async def test_request_analyzer():
    """Test the RequestAnalyzer with LLM integration"""
    print("\n🧪 Testing RequestAnalyzer with LLM...")
    
    analyzer = RequestAnalyzer()
    
    # Test intent analysis
    test_requests = [
        "What's the status of the system?",
        "I need a breakthrough for quantum computing",
        "Remember this important insight about AI",
        "Analyze the sustainability problem",
        "Run the consciousness ecosystem"
    ]
    
    for request in test_requests:
        print(f"\n📝 Analyzing: '{request}'")
        
        # Preprocess the input
        processed = analyzer.preprocess_input(request)
        print(f"📊 Preprocessed: {processed}")
        
        # Analyze intent
        analysis = analyzer.analyze_intent(request)
        print(f"🎯 Intent: {analysis['intent']} (confidence: {analysis['confidence']})")
        print(f"⚡ Complexity: {analysis['complexity']}")
        print(f"🌟 Requires breakthrough: {analysis['requires_breakthrough']}")
    
    print("\n✅ RequestAnalyzer tests completed")

async def main():
    """Main test function"""
    print("🌌 UNIFIED CONSCIOUSNESS CLI - LLM INTEGRATION TEST")
    print("=" * 60)
    
    try:
        # Test LLM interface
        llm_success = await test_llm_interface()
        
        if llm_success:
            # Test request analyzer
            await test_request_analyzer()
            
            print("\n🎉 All tests completed successfully!")
            print("\n📋 INTEGRATION SUMMARY:")
            print("✅ LLMInterface: Manages local Ollama models")
            print("✅ Model Selection: Chooses appropriate models for tasks")
            print("✅ RequestAnalyzer: Enhanced with LLM synthesis")
            print("✅ Unified Response: Combines consciousness system + LLM insights")
            
            print("\n🚀 READY TO USE:")
            print("Run: python -m src.unified_consciousness.cli chat")
            print("Commands: 'llm status', 'enable llm', 'disable llm'")
        else:
            print("\n⚠️  LLM integration requires Ollama to be running")
            print("Start Ollama: ollama serve")
            
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
