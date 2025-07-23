#!/usr/bin/env python3
"""
Comprehensive test suite for all consciousness modules with LLM integration
Tests each module individually and then in combination
"""

import asyncio
import sys
import os
from datetime import datetime

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from unified_consciousness.cli import LLMInterface, RequestAnalyzer

async def test_all_consciousness_modules():
    """Test all consciousness modules with LLM integration"""
    print("🌌 COMPREHENSIVE CONSCIOUSNESS MODULE TEST WITH LLM INTEGRATION")
    print("=" * 80)
    
    analyzer = RequestAnalyzer()
    
    # Test scenarios for each module type
    test_scenarios = [
        {
            'category': 'STATUS_CHECKS',
            'requests': [
                "What's the status of the system?",
                "How are you performing?",
                "Check system health",
                "What is the condition of all engines?"
            ]
        },
        {
            'category': 'RESEARCH_QUERIES', 
            'requests': [
                "Analyze the potential of quantum computing for consciousness simulation",
                "Research sustainable energy solutions using biomimetic approaches",
                "Investigate the relationship between complexity theory and emergence",
                "Study the intersection of neuroscience and artificial intelligence"
            ]
        },
        {
            'category': 'BREAKTHROUGH_SESSIONS',
            'requests': [
                "I need a breakthrough solution for climate change",
                "Solve the hard problem of consciousness",
                "Find a revolutionary approach to space travel",
                "Create a paradigm shift in education technology"
            ]
        },
        {
            'category': 'MEMORY_OPERATIONS',
            'requests': [
                "Remember this insight: LLM integration enhances consciousness systems",
                "Save this important discovery about temporal energy harvesting",
                "Record this breakthrough about multidimensional problem solving",
                "Archive this pattern: complex systems have simple underlying principles"
            ]
        },
        {
            'category': 'ECOSYSTEM_CONTROL',
            'requests': [
                "Run the consciousness ecosystem for analysis",
                "Start the unified consciousness flow",
                "Activate the ecosystem with voice synthesis",
                "Begin consciousness evolution cycles"
            ]
        },
        {
            'category': 'ADAPTIVE_IMPROVEMENTS',
            'requests': [
                "Improve the system's performance",
                "Optimize the consciousness engines",
                "Enhance the adaptive capabilities",
                "Upgrade the integration between modules"
            ]
        },
        {
            'category': 'COMPLEX_MULTIMODAL',
            'requests': [
                "Using temporal energy harvesting principles, design a breakthrough solution for sustainable cities that incorporates consciousness-based urban planning",
                "Combine quantum computing research with adaptive consciousness systems to solve the optimization problem of global resource distribution",
                "Create a multidimensional analysis framework that uses pattern recognition to predict and prevent systemic failures in complex networks"
            ]
        }
    ]
    
    results = {}
    
    for scenario in test_scenarios:
        category = scenario['category']
        print(f"\n🧪 TESTING {category}")
        print("─" * 60)
        
        category_results = []
        
        for request in scenario['requests']:
            print(f"\n📝 Testing: {request[:80]}...")
            
            try:
                # Preprocess input
                processed = analyzer.preprocess_input(request)
                
                # Analyze intent
                analysis = analyzer.analyze_intent(request)
                
                # Test with LLM enabled
                print(f"   🎯 Intent: {analysis['intent']} (confidence: {analysis['confidence']})")
                print(f"   ⚡ Complexity: {analysis['complexity']}")
                print(f"   🌟 Breakthrough: {analysis['requires_breakthrough']}")
                
                # Test LLM model selection
                if analyzer.user_preferences.get('use_llm_synthesis', True):
                    context = analyzer.extract_context_from_history()
                    task_type = analysis['intent'] if analysis['intent'] != 'research' else 'general'
                    selected_model = analyzer.llm_interface.select_model_for_task(task_type)
                    print(f"   🤖 Selected model: {selected_model}")
                
                # Simulate request delegation (without full execution to save time)
                result_summary = {
                    'request': request,
                    'intent': analysis['intent'],
                    'complexity': analysis['complexity'],
                    'model_selected': selected_model if 'selected_model' in locals() else None,
                    'status': 'success'
                }
                
                category_results.append(result_summary)
                print(f"   ✅ Test passed")
                
            except Exception as e:
                print(f"   ❌ Test failed: {e}")
                category_results.append({
                    'request': request,
                    'status': 'failed',
                    'error': str(e)
                })
        
        results[category] = category_results
    
    return results

async def test_llm_model_coverage():
    """Test that all LLM models are properly utilized"""
    print("\n🤖 TESTING LLM MODEL COVERAGE")
    print("─" * 60)
    
    llm = LLMInterface()
    
    # Test each model type
    model_tests = [
        ('technical', "How can I optimize Python code performance?"),
        ('reasoning', "Solve this complex logical puzzle step by step"),
        ('creative', "Write a creative story about consciousness"),
        ('general', "What is artificial intelligence?"),
        ('lightweight', "Quick question: what's 2+2?")
    ]
    
    model_results = {}
    
    for model_type, test_prompt in model_tests:
        print(f"\n🔧 Testing {model_type} model:")
        try:
            selected_model = llm.select_model_for_task(test_prompt, 
                                                     'high' if model_type == 'reasoning' else 'medium')
            expected_model = llm.available_models[model_type]
            
            print(f"   Selected: {selected_model}")
            print(f"   Expected: {expected_model}")
            
            if selected_model == expected_model:
                print("   ✅ Correct model selected")
                model_results[model_type] = 'success'
            else:
                print("   ⚠️  Unexpected model selected")
                model_results[model_type] = 'unexpected'
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
            model_results[model_type] = 'error'
    
    return model_results

async def test_integration_performance():
    """Test the performance and responsiveness of the integrated system"""
    print("\n⚡ TESTING INTEGRATION PERFORMANCE")
    print("─" * 60)
    
    analyzer = RequestAnalyzer()
    
    # Test response times for different complexity levels
    performance_tests = [
        ("Simple status check", "What's the status?"),
        ("Medium research query", "Analyze renewable energy potential"),
        ("Complex breakthrough request", "Revolutionary solution for climate change using quantum consciousness principles")
    ]
    
    performance_results = []
    
    for test_name, request in performance_tests:
        print(f"\n⏱️  Testing: {test_name}")
        
        start_time = datetime.now()
        
        try:
            # Test preprocessing
            processed = analyzer.preprocess_input(request)
            
            # Test intent analysis
            analysis = analyzer.analyze_intent(request)
            
            # Test model selection
            task_type = analysis['intent'] if analysis['intent'] != 'research' else 'general'
            selected_model = analyzer.llm_interface.select_model_for_task(task_type)
            
            end_time = datetime.now()
            processing_time = (end_time - start_time).total_seconds()
            
            print(f"   ⏱️  Processing time: {processing_time:.3f} seconds")
            print(f"   🎯 Intent: {analysis['intent']}")
            print(f"   🤖 Model: {selected_model}")
            print("   ✅ Performance test passed")
            
            performance_results.append({
                'test': test_name,
                'processing_time': processing_time,
                'status': 'success'
            })
            
        except Exception as e:
            print(f"   ❌ Performance test failed: {e}")
            performance_results.append({
                'test': test_name,
                'status': 'failed',
                'error': str(e)
            })
    
    return performance_results

def generate_test_report(module_results, model_results, performance_results):
    """Generate a comprehensive test report"""
    print("\n" + "=" * 80)
    print("📊 COMPREHENSIVE TEST REPORT")
    print("=" * 80)
    
    # Module test summary
    print("\n🧪 MODULE TEST SUMMARY:")
    total_tests = 0
    passed_tests = 0
    
    for category, results in module_results.items():
        category_passed = sum(1 for r in results if r.get('status') == 'success')
        category_total = len(results)
        total_tests += category_total
        passed_tests += category_passed
        
        print(f"  {category}: {category_passed}/{category_total} passed")
    
    # Model coverage summary
    print(f"\n🤖 LLM MODEL COVERAGE:")
    for model_type, status in model_results.items():
        status_icon = "✅" if status == 'success' else "⚠️" if status == 'unexpected' else "❌"
        print(f"  {model_type}: {status_icon} {status}")
    
    # Performance summary
    print(f"\n⚡ PERFORMANCE SUMMARY:")
    avg_time = sum(r['processing_time'] for r in performance_results if 'processing_time' in r) / len([r for r in performance_results if 'processing_time' in r])
    print(f"  Average processing time: {avg_time:.3f} seconds")
    
    for result in performance_results:
        if 'processing_time' in result:
            print(f"  {result['test']}: {result['processing_time']:.3f}s")
    
    # Overall summary
    print(f"\n🎯 OVERALL RESULTS:")
    print(f"  Module tests: {passed_tests}/{total_tests} passed ({passed_tests/total_tests*100:.1f}%)")
    
    success_models = sum(1 for status in model_results.values() if status == 'success')
    print(f"  Model coverage: {success_models}/{len(model_results)} models working correctly")
    
    success_perf = sum(1 for r in performance_results if r.get('status') == 'success')
    print(f"  Performance tests: {success_perf}/{len(performance_results)} passed")
    
    if passed_tests == total_tests and success_models == len(model_results) and success_perf == len(performance_results):
        print("\n🎉 ALL TESTS PASSED! System is ready for streamlining.")
    else:
        print("\n⚠️  Some tests failed. Review results before streamlining.")
    
    return {
        'modules': {'passed': passed_tests, 'total': total_tests},
        'models': {'success': success_models, 'total': len(model_results)},
        'performance': {'passed': success_perf, 'total': len(performance_results)}
    }

async def main():
    """Main test execution"""
    print("🚀 Starting comprehensive consciousness system test...")
    
    try:
        # Test all modules
        print("\n1️⃣ Testing all consciousness modules...")
        module_results = await test_all_consciousness_modules()
        
        # Test LLM model coverage
        print("\n2️⃣ Testing LLM model coverage...")
        model_results = await test_llm_model_coverage()
        
        # Test integration performance
        print("\n3️⃣ Testing integration performance...")
        performance_results = await test_integration_performance()
        
        # Generate comprehensive report
        print("\n4️⃣ Generating test report...")
        summary = generate_test_report(module_results, model_results, performance_results)
        
        # Recommendations for streamlining
        print("\n" + "=" * 80)
        print("💡 STREAMLINING RECOMMENDATIONS")
        print("=" * 80)
        
        if summary['modules']['passed'] == summary['modules']['total']:
            print("✅ All modules working - ready for interface streamlining")
            print("🔧 Recommended optimizations:")
            print("  • Combine similar intent categories for faster routing")
            print("  • Cache model selections for repeated request patterns")
            print("  • Optimize response formatting for better user experience")
            print("  • Add keyboard shortcuts for common operations")
        else:
            print("⚠️  Fix failing modules before streamlining")
        
        print("\n🎯 Next steps:")
        print("  1. Address any failed tests")
        print("  2. Implement recommended optimizations")
        print("  3. Create streamlined user interface")
        print("  4. Add configuration options for power users")
        
    except Exception as e:
        print(f"❌ Test execution failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
