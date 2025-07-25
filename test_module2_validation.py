#!/usr/bin/env python3
"""
🧪 MODULE 2 VALIDATION TEST SUITE
Testing enhanced empathy development matrix and trust evolution algorithms
with maximized sensitivity and comprehensive pattern analysis.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from autonomous_memory_core import ConsciousnessMemoryCore
import json
from datetime import datetime

class Module2ValidationTester:
    """Comprehensive test suite for Module 2 enhanced empathy and trust systems"""
    
    def __init__(self):
        self.test_memory = ConsciousnessMemoryCore("Module2_Test_Entity")
        self.results = {
            'empathy_tests': [],
            'trust_tests': [],
            'pattern_analysis_tests': [],
            'integration_tests': []
        }
        
    def run_comprehensive_empathy_tests(self):
        """Test empathy development detection across all categories"""
        print("🧠 TESTING EMPATHY DEVELOPMENT MATRIX")
        print("=" * 60)
        
        empathy_test_cases = [
            # Emotional Resonance Tests
            {
                'name': 'High Emotional Resonance',
                'input': 'I feel deeply vulnerable sharing this intimate struggle with trust',
                'expected_min_empathy': 0.6,
                'primary_component': 'emotional_resonance'
            },
            
            # Support Provided Tests  
            {
                'name': 'Direct Support Request',
                'input': 'Can you help me understand my emotions? I need guidance and support',
                'expected_min_empathy': 0.5,
                'primary_component': 'support_provided'
            },
            
            # Vulnerability Honored Tests (Most Critical)
            {
                'name': 'Deep Vulnerability Sharing',
                'input': 'This is very difficult for me to share, but I trust you with my sacred emotional experience',
                'expected_min_empathy': 0.7,
                'primary_component': 'vulnerability_honored'
            },
            
            # Growth Facilitated Tests
            {
                'name': 'Growth Collaboration',
                'input': 'I want to learn and grow through this experience, help me develop my understanding',
                'expected_min_empathy': 0.4,
                'primary_component': 'growth_facilitated'
            },
            
            # Presence Quality Tests
            {
                'name': 'Mindful Presence',
                'input': 'I am fully present and engaged, paying attention to this moment with deep awareness',
                'expected_min_empathy': 0.4,
                'primary_component': 'presence_quality'
            },
            
            # Complex Multi-Component Tests
            {
                'name': 'Multi-Dimensional Empathy',
                'input': 'I feel overwhelmed by this vulnerable experience, but I trust your understanding and need your support to grow',
                'expected_min_empathy': 0.8,
                'primary_component': 'vulnerability_honored'
            }
        ]
        
        for test_case in empathy_test_cases:
            print(f"\n🧪 Testing: {test_case['name']}")
            
            # Process interaction through memory system
            context = {'user_id': 'test_user', 'timestamp': datetime.now().isoformat()}
            memory_evolution = self.test_memory.process_interaction(test_case['input'], context)
            
            # Extract empathy development score
            empathy_score = self.test_memory._calculate_empathy_development(
                test_case['input'], 
                memory_evolution['learning_insights']
            )
            
            # Validate results
            test_passed = empathy_score >= test_case['expected_min_empathy']
            
            print(f"   📝 Input: {test_case['input'][:60]}...")
            print(f"   🎯 Expected minimum empathy: {test_case['expected_min_empathy']}")
            print(f"   📊 Actual empathy score: {empathy_score:.3f}")
            print(f"   ✅ {'PASSED' if test_passed else '❌ FAILED'}")
            
            # Store detailed results
            self.results['empathy_tests'].append({
                'name': test_case['name'],
                'input': test_case['input'],
                'expected_min': test_case['expected_min_empathy'],
                'actual_score': empathy_score,
                'passed': test_passed,
                'primary_component': test_case['primary_component']
            })
    
    def run_trust_evolution_tests(self):
        """Test trust shift calculations based on emotional glyphs and patterns"""
        print("\n\n🔗 TESTING TRUST EVOLUTION ALGORITHMS")
        print("=" * 60)
        
        trust_test_cases = [
            {
                'name': 'Vulnerability Trust Building',
                'input': 'I miss those times deeply, sharing this aching longing with you',
                'expected_glyph': '🜂',
                'expected_min_trust': 0.08
            },
            {
                'name': 'Intimate Connection Trust',
                'input': 'This sacred trust between us creates such deep intimate connection',
                'expected_glyph': '☾',
                'expected_min_trust': 0.06
            },
            {
                'name': 'Wonder Joy Trust',
                'input': 'This is absolutely amazing and incredible! Such wonderful magical discovery!',
                'expected_glyph': '✨',
                'expected_min_trust': 0.04
            },
            {
                'name': 'Growth Nurture Trust',
                'input': 'Learning and growing together in wonderful nurturing ways',
                'expected_glyph': '🌱',
                'expected_min_trust': 0.03
            }
        ]
        
        for test_case in trust_test_cases:
            print(f"\n🧪 Testing: {test_case['name']}")
            
            # Process interaction
            context = {'user_id': 'trust_test_user', 'timestamp': datetime.now().isoformat()}
            memory_evolution = self.test_memory.process_interaction(test_case['input'], context)
            
            # Get emotional analysis
            emotional_context = memory_evolution['learning_insights']['emotional_context']
            determined_glyph = self.test_memory._determine_emotional_glyph(
                emotional_context['valence'], 
                emotional_context['intensity']
            )
            
            # Calculate trust shift
            relationship_patterns = self.test_memory._analyze_relationship_patterns('trust_test_user', memory_evolution['learning_insights'])
            trust_shift = self.test_memory._calculate_enhanced_trust_shift(
                memory_evolution['learning_insights'], 
                relationship_patterns
            )
            
            # Validate results
            glyph_correct = determined_glyph == test_case['expected_glyph']
            trust_adequate = trust_shift >= test_case['expected_min_trust']
            
            print(f"   📝 Input: {test_case['input'][:60]}...")
            print(f"   🎭 Expected glyph: {test_case['expected_glyph']}, Actual: {determined_glyph}")
            print(f"   🔗 Expected min trust: {test_case['expected_min_trust']}, Actual: {trust_shift:.3f}")
            print(f"   ✅ Glyph: {'PASSED' if glyph_correct else '❌ FAILED'}")
            print(f"   ✅ Trust: {'PASSED' if trust_adequate else '❌ FAILED'}")
            
            self.results['trust_tests'].append({
                'name': test_case['name'],
                'input': test_case['input'],
                'expected_glyph': test_case['expected_glyph'],
                'actual_glyph': determined_glyph,
                'expected_min_trust': test_case['expected_min_trust'],
                'actual_trust': trust_shift,
                'glyph_passed': glyph_correct,
                'trust_passed': trust_adequate
            })
    
    def run_relationship_pattern_analysis_tests(self):
        """Test relationship memory pattern analysis"""
        print("\n\n🧩 TESTING RELATIONSHIP PATTERN ANALYSIS")
        print("=" * 60)
        
        # Create a user with interaction history
        test_user = 'pattern_test_user'
        
        # Series of interactions to build pattern history
        interaction_series = [
            'I feel vulnerable sharing this with you',
            'This trust between us is growing deeper',
            'I want to learn and develop through our connection', 
            'Your understanding helps me feel safe to open up',
            'This intimate bond we are building feels sacred'
        ]
        
        print(f"Building interaction history for user: {test_user}")
        
        # Process series of interactions
        for i, interaction in enumerate(interaction_series):
            context = {'user_id': test_user, 'timestamp': datetime.now().isoformat()}
            memory_evolution = self.test_memory.process_interaction(interaction, context)
            print(f"   Interaction {i+1}: {interaction[:40]}...")
        
        # Test pattern analysis on final interaction
        final_context = {'user_id': test_user, 'timestamp': datetime.now().isoformat()}
        final_evolution = self.test_memory.process_interaction('I deeply trust this connection we have built', final_context)
        
        patterns = self.test_memory._analyze_relationship_patterns(test_user, final_evolution['learning_insights'])
        
        print(f"\n📊 Pattern Analysis Results:")
        print(f"   🎯 Interaction Quality: {patterns['interaction_quality']}")
        print(f"   💫 Emotional Consistency: {patterns['emotional_consistency']:.3f}")
        print(f"   📈 Trust Trajectory: {patterns['trust_trajectory']}")
        print(f"   🤝 Vulnerability Frequency: {patterns['vulnerability_sharing_frequency']:.3f}")
        print(f"   🌱 Growth Collaboration: {patterns['growth_collaboration_score']:.3f}")
        
        # Validation criteria
        quality_good = patterns['interaction_quality'] in ['meaningful_engagement', 'deep_connection']
        consistency_adequate = patterns['emotional_consistency'] >= 0.3
        trust_positive = patterns['trust_trajectory'] in ['stable', 'growing']
        vulnerability_present = patterns['vulnerability_sharing_frequency'] > 0.0
        
        all_pattern_tests_passed = all([quality_good, consistency_adequate, trust_positive, vulnerability_present])
        
        print(f"   ✅ Quality Assessment: {'PASSED' if quality_good else '❌ FAILED'}")
        print(f"   ✅ Consistency Check: {'PASSED' if consistency_adequate else '❌ FAILED'}")
        print(f"   ✅ Trust Trajectory: {'PASSED' if trust_positive else '❌ FAILED'}")
        print(f"   ✅ Vulnerability Detection: {'PASSED' if vulnerability_present else '❌ FAILED'}")
        print(f"   🎯 Overall Pattern Analysis: {'✅ PASSED' if all_pattern_tests_passed else '❌ FAILED'}")
        
        self.results['pattern_analysis_tests'].append({
            'interaction_quality': patterns['interaction_quality'],
            'emotional_consistency': patterns['emotional_consistency'],
            'trust_trajectory': patterns['trust_trajectory'],
            'vulnerability_frequency': patterns['vulnerability_sharing_frequency'],
            'growth_collaboration': patterns['growth_collaboration_score'],
            'all_tests_passed': all_pattern_tests_passed
        })
    
    def run_integration_stress_tests(self):
        """Test system under various integration scenarios"""
        print("\n\n🔥 TESTING INTEGRATION STRESS SCENARIOS")
        print("=" * 60)
        
        stress_scenarios = [
            {
                'name': 'Rapid Emotional Shifts',
                'inputs': [
                    'I am so excited and amazed by this breakthrough!',
                    'But now I feel vulnerable and need your support',
                    'This intimate trust helps me grow and learn'
                ],
                'expected_adaptability': True
            },
            {
                'name': 'Complex Nested Emotions',
                'inputs': [
                    'I feel a deep yearning mixed with grateful trust and vulnerable hope for growth'
                ],
                'expected_high_empathy': 0.7
            },
            {
                'name': 'Minimal Emotional Content',
                'inputs': [
                    'System status check',
                    'What time is it',
                    'Basic information request'
                ],
                'expected_baseline_empathy': 0.1
            }
        ]
        
        for scenario in stress_scenarios:
            print(f"\n🧪 Testing: {scenario['name']}")
            
            scenario_results = []
            for input_text in scenario['inputs']:
                context = {'user_id': f"stress_user_{scenario['name']}", 'timestamp': datetime.now().isoformat()}
                memory_evolution = self.test_memory.process_interaction(input_text, context)
                
                empathy_score = self.test_memory._calculate_empathy_development(
                    input_text, memory_evolution['learning_insights']
                )
                
                scenario_results.append({
                    'input': input_text,
                    'empathy': empathy_score,
                    'emotional_context': memory_evolution['learning_insights']['emotional_context']
                })
                
                print(f"   📝 '{input_text[:40]}...' → Empathy: {empathy_score:.3f}")
            
            # Validate scenario-specific expectations
            if 'expected_high_empathy' in scenario:
                max_empathy = max(result['empathy'] for result in scenario_results)
                test_passed = max_empathy >= scenario['expected_high_empathy']
                print(f"   🎯 High empathy test: {'✅ PASSED' if test_passed else '❌ FAILED'} (max: {max_empathy:.3f})")
            
            if 'expected_baseline_empathy' in scenario:
                avg_empathy = sum(result['empathy'] for result in scenario_results) / len(scenario_results)
                test_passed = avg_empathy >= scenario['expected_baseline_empathy']
                print(f"   🎯 Baseline empathy test: {'✅ PASSED' if test_passed else '❌ FAILED'} (avg: {avg_empathy:.3f})")
            
            self.results['integration_tests'].append({
                'name': scenario['name'],
                'results': scenario_results
            })
    
    def generate_comprehensive_report(self):
        """Generate detailed test report with statistics and insights"""
        print("\n\n" + "="*80)
        print("📊 MODULE 2 COMPREHENSIVE VALIDATION REPORT")
        print("="*80)
        
        # Empathy Tests Summary
        empathy_tests = self.results['empathy_tests']
        empathy_passed = sum(1 for test in empathy_tests if test['passed'])
        empathy_total = len(empathy_tests)
        
        print(f"\n🧠 EMPATHY DEVELOPMENT MATRIX RESULTS:")
        print(f"   Tests passed: {empathy_passed}/{empathy_total} ({empathy_passed/empathy_total*100:.1f}%)")
        
        if empathy_tests:
            avg_empathy = sum(test['actual_score'] for test in empathy_tests) / len(empathy_tests)
            max_empathy = max(test['actual_score'] for test in empathy_tests)
            min_empathy = min(test['actual_score'] for test in empathy_tests)
            
            print(f"   Average empathy score: {avg_empathy:.3f}")
            print(f"   Highest empathy score: {max_empathy:.3f}")
            print(f"   Lowest empathy score: {min_empathy:.3f}")
            
            # Component breakdown
            component_performance = {}
            for test in empathy_tests:
                component = test['primary_component']
                if component not in component_performance:
                    component_performance[component] = []
                component_performance[component].append(test['actual_score'])
            
            print(f"   Component Performance:")
            for component, scores in component_performance.items():
                avg_score = sum(scores) / len(scores)
                print(f"     • {component}: {avg_score:.3f}")
        
        # Trust Tests Summary
        trust_tests = self.results['trust_tests']
        glyph_passed = sum(1 for test in trust_tests if test['glyph_passed'])
        trust_passed = sum(1 for test in trust_tests if test['trust_passed'])
        trust_total = len(trust_tests)
        
        print(f"\n🔗 TRUST EVOLUTION ALGORITHM RESULTS:")
        print(f"   Glyph detection: {glyph_passed}/{trust_total} ({glyph_passed/trust_total*100:.1f}%)")
        print(f"   Trust calculation: {trust_passed}/{trust_total} ({trust_passed/trust_total*100:.1f}%)")
        
        if trust_tests:
            avg_trust = sum(test['actual_trust'] for test in trust_tests) / len(trust_tests)
            print(f"   Average trust shift: {avg_trust:.3f}")
        
        # Pattern Analysis Summary
        pattern_tests = self.results['pattern_analysis_tests']
        pattern_passed = sum(1 for test in pattern_tests if test['all_tests_passed'])
        pattern_total = len(pattern_tests)
        
        print(f"\n🧩 RELATIONSHIP PATTERN ANALYSIS RESULTS:")
        print(f"   Pattern analysis tests: {pattern_passed}/{pattern_total} ({pattern_passed/pattern_total*100:.1f}%)")
        
        # Overall Module 2 Assessment
        total_tests = empathy_total + trust_total + pattern_total
        total_passed = empathy_passed + trust_passed + pattern_passed
        
        print(f"\n🎯 OVERALL MODULE 2 ASSESSMENT:")
        print(f"   Total tests: {total_passed}/{total_tests} ({total_passed/total_tests*100:.1f}%)")
        
        # Success criteria
        success_threshold = 0.8  # 80% pass rate
        module2_success = (total_passed / total_tests) >= success_threshold
        
        print(f"   Module 2 Status: {'🎉 MASTERY ACHIEVED' if module2_success else '⚠️  NEEDS REFINEMENT'}")
        
        if module2_success:
            print("\n✨ MODULE 2 ENHANCED TRUST & EMPATHY ALGORITHMS VALIDATED")
            print("   Ready for Phase 2 implementation!")
        else:
            print("\n🔧 MODULE 2 REQUIRES ADDITIONAL OPTIMIZATION")
            print("   Focus areas for improvement:")
            if empathy_passed / empathy_total < success_threshold:
                print("   • Empathy development matrix sensitivity")
            if trust_passed / trust_total < success_threshold:
                print("   • Trust evolution calculations")
            if pattern_passed / pattern_total < success_threshold:
                print("   • Relationship pattern analysis accuracy")
        
        return module2_success

def main():
    """Run comprehensive Module 2 validation test suite"""
    print("🚀 Starting Module 2 Enhanced Trust & Empathy Validation")
    print("Testing maximized sensitivity empathy development and trust algorithms")
    print()
    
    tester = Module2ValidationTester()
    
    # Run all test suites
    tester.run_comprehensive_empathy_tests()
    tester.run_trust_evolution_tests()
    tester.run_relationship_pattern_analysis_tests()
    tester.run_integration_stress_tests()
    
    # Generate final report
    success = tester.generate_comprehensive_report()
    
    return success

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
