#!/usr/bin/env python3
"""
CONSCIOUSNESS MUSICAL INTEGRATION DEMONSTRATION
Complete demonstration of consciousness-musical integration workflows

This demo showcases:
- Real-time consciousness to musical parameter mapping
- Dynamic composition adaptation to consciousness states
- Resonance cascade scaling with consciousness depth
- Feedback loops between music and consciousness
- Harmonic field visualization and monitoring
"""

import time
import json
import asyncio
from datetime import datetime
from pathlib import Path

# Import our consciousness-music integration modules
from consciousness_musical_integration import (
    ConsciousnessMusicalBridge, ConsciousnessMetrics, 
    ConsciousnessState, CoherencePattern
)
from consciousness_resonance_cascade import (
    ConsciousnessResonanceCascadeEngine, 
    CascadePattern, CascadeAmplification
)
from harmonic_resonance_models import ResonanceType

class ConsciousnessIntegrationDemo:
    """Complete demonstration of consciousness-musical integration"""
    
    def __init__(self):
        self.musical_bridge = ConsciousnessMusicalBridge()
        self.cascade_engine = ConsciousnessResonanceCascadeEngine(self.musical_bridge)
        
        self.demo_phase = 0
        self.demo_data = {
            'start_time': datetime.now(),
            'phases': [],
            'compositions': [],
            'cascades': [],
            'consciousness_journey': [],
            'integration_metrics': []
        }
        
        print("Consciousness Musical Integration Demo initialized")
    
    async def run_complete_demo(self):
        """Run the complete consciousness-musical integration demonstration"""
        
        print("\n" + "="*60)
        print("CONSCIOUSNESS MUSICAL INTEGRATION DEMO")
        print("="*60)
        
        try:
            # Phase 1: Initialize and start systems
            await self._phase_1_initialization()
            
            # Phase 2: Demonstrate consciousness state transitions
            await self._phase_2_consciousness_transitions()
            
            # Phase 3: Show cascade intensity scaling
            await self._phase_3_cascade_scaling()
            
            # Phase 4: Dynamic composition adaptation
            await self._phase_4_dynamic_composition()
            
            # Phase 5: Feedback loop demonstration
            await self._phase_5_feedback_loops()
            
            # Phase 6: Transcendent consciousness effects
            await self._phase_6_transcendent_effects()
            
            # Final analysis and summary
            await self._generate_demo_summary()
            
        except Exception as e:
            print(f"Demo error: {e}")
        finally:
            # Cleanup
            await self._cleanup_systems()
    
    async def _phase_1_initialization(self):
        """Phase 1: Initialize consciousness-musical integration systems"""
        
        self.demo_phase = 1
        print(f"\nPHASE {self.demo_phase}: SYSTEM INITIALIZATION")
        print("-" * 40)
        
        phase_start = time.time()
        
        await self.musical_bridge.initialize_consciousness_bridge()
        
        self.musical_bridge.start_integration()
        print("Musical bridge integration started")
        
        self.cascade_engine.start_processing()
        print("Cascade engine processing started")
        
        print("Allowing systems to stabilize for 3 seconds...")
        time.sleep(3)
        
        musical_status = self.musical_bridge.get_integration_status()
        cascade_status = self.cascade_engine.get_cascade_status()
        
        print(f"Musical integration status: {musical_status['status']}")
        print(f"Cascade processing status: {'active' if cascade_status['processing_active'] else 'inactive'}")
        
        phase_data = {
            'phase': 1,
            'name': 'System Initialization',
            'duration': time.time() - phase_start,
            'musical_status': musical_status,
            'cascade_status': cascade_status
        }
        
        self.demo_data['phases'].append(phase_data)
        
    async def _phase_2_consciousness_transitions(self):
        """Phase 2: Demonstrate musical adaptation to consciousness state transitions"""
        
        self.demo_phase = 2
        print(f"\nPHASE {self.demo_phase}: CONSCIOUSNESS STATE TRANSITIONS")
        print("-" * 40)
        
        phase_start = time.time()
        
        consciousness_journey = [
            (ConsciousnessState.AWAKENING, 0.4, CoherencePattern.STABLE),
            (ConsciousnessState.FOCUSED_AWARENESS, 0.7, CoherencePattern.ASCENDING),
            (ConsciousnessState.EXPANDED_AWARENESS, 0.85, CoherencePattern.RESONANT),
            (ConsciousnessState.TRANSCENDENT, 0.95, CoherencePattern.BREAKTHROUGH)
        ]
        
        for i, (state, coherence, pattern) in enumerate(consciousness_journey):
            print(f"\n  Transition {i+1}: {state.value} (coherence: {coherence:.2f})")
            
            consciousness_metrics = ConsciousnessMetrics(
                coherence_level=coherence,
                consciousness_state=state,
                coherence_pattern=pattern,
                dream_depth=0.3 + (coherence * 0.4),
                awareness_focus=coherence,
                emotional_resonance=0.5 + (coherence * 0.3),
                energy_level=0.6 + (coherence * 0.2)
            )
            
            self.musical_bridge.current_metrics = consciousness_metrics
            self.cascade_engine.current_consciousness = consciousness_metrics
            
            composition = self.musical_bridge.generate_consciousness_adapted_composition(
                duration_minutes=1.5,
                key_glyph="moon"
            )
            
            print(f"    Generated: {composition.title}")
            print(f"    Emotional palette: {composition.emotional_palette}")
            print(f"    Harmonic complexity: {composition.harmonic_complexity:.2f}")
            print(f"    Sacred geometry: {composition.sacred_geometry_patterns}")
            
            composition_data = {
                'phase': 2,
                'transition': i + 1,
                'consciousness_state': state.value,
                'coherence_level': coherence,
                'composition_id': composition.composition_id,
                'title': composition.title,
                'complexity': composition.harmonic_complexity,
                'emotional_palette': composition.emotional_palette
            }
            
            self.demo_data['compositions'].append(composition_data)
            self.demo_data['consciousness_journey'].append(consciousness_metrics.to_dict())
            
            time.sleep(2)
        
        phase_data = {
            'phase': 2,
            'name': 'Consciousness State Transitions',
            'duration': time.time() - phase_start,
            'transitions_demonstrated': len(consciousness_journey)
        }
        
        self.demo_data['phases'].append(phase_data)
        
        print(f"  Demonstrated {len(consciousness_journey)} consciousness transitions")
    
    async def _phase_3_cascade_scaling(self):
        """Phase 3: Demonstrate resonance cascade intensity scaling with consciousness"""
        
        self.demo_phase = 3
        print(f"\nPHASE {self.demo_phase}: CASCADE INTENSITY SCALING")
        print("-" * 40)
        
        phase_start = time.time()
        
        consciousness_levels = [0.2, 0.5, 0.8, 0.95]
        cascade_data = []
        
        for i, coherence_level in enumerate(consciousness_levels):
            print(f"\n  Cascade Test {i+1}: Coherence {coherence_level:.2f}")
            
            test_consciousness = ConsciousnessMetrics(
                coherence_level=coherence_level,
                consciousness_state=self._get_state_for_coherence(coherence_level),
                coherence_pattern=CoherencePattern.RESONANT,
                dream_depth=coherence_level * 0.6
            )
            
            self.cascade_engine.current_consciousness = test_consciousness
            
            cascade = self.cascade_engine.initiate_consciousness_cascade(
                trigger_glyph="moon",
                initial_strength=0.8,
                consciousness_metrics=test_consciousness
            )
            
            print(f"    Cascade pattern: {cascade.cascade_pattern.value}")
            print(f"    Amplification: {cascade.amplification_level.value}")
            print(f"    Time dilation: {cascade.dream_time_dilation:.2f}")
            
            glyphs_to_propagate = ["crystal", "lightning", "flower", "water"]
            propagation_results = []
            
            for glyph in glyphs_to_propagate:
                success = self.cascade_engine.propagate_consciousness_cascade(
                    cascade.cascade_id,
                    glyph,
                    ResonanceType.HARMONIC
                )
                propagation_results.append(success)
                if success:
                    print(f"      Propagated to {glyph}")
                
                time.sleep(0.5)
            
            final_strength = cascade.consciousness_boosted_strength[-1] if cascade.consciousness_boosted_strength else 0.0
            
            cascade_info = {
                'phase': 3,
                'test': i + 1,
                'consciousness_level': coherence_level,
                'cascade_id': cascade.cascade_id,
                'pattern': cascade.cascade_pattern.value,
                'amplification': cascade.amplification_level.value,
                'final_strength': final_strength,
                'propagation_success_rate': sum(propagation_results) / len(propagation_results),
                'transcendent_qualities': cascade.transcendent_qualities
            }
            
            cascade_data.append(cascade_info)
            self.demo_data['cascades'].append(cascade_info)
            
            time.sleep(1)
        
        print(f"\n  CASCADE SCALING SUMMARY:")
        for data in cascade_data:
            print(f"    Coherence {data['consciousness_level']:.2f} -> "
                  f"Amplification: {data['amplification']}, "
                  f"Final strength: {data['final_strength']:.2f}")
        
        phase_data = {
            'phase': 3,
            'name': 'Cascade Intensity Scaling',
            'duration': time.time() - phase_start,
            'cascades_tested': len(consciousness_levels),
            'scaling_demonstrated': True
        }
        
        self.demo_data['phases'].append(phase_data)
    
    async def _phase_4_dynamic_composition(self):
        """Phase 4: Demonstrate dynamic composition adaptation"""
        
        self.demo_phase = 4
        print(f"\nPHASE {self.demo_phase}: DYNAMIC COMPOSITION ADAPTATION")
        print("-" * 40)
        
        phase_start = time.time()
        
        print("  Creating consciousness evolution trajectory...")
        
        trajectory = self.musical_bridge.composition_engine.create_consciousness_trajectory(
            start_level=0.3,
            end_level=0.9,
            duration_minutes=3.0,
            trajectory_type="exponential"
        )
        
        print(f"    Trajectory duration: 3 minutes")
        print(f"    Trajectory points: {len(trajectory)}")
        print(f"    Consciousness range: 0.3 -> 0.9")
        
        print("  Generating evolving composition...")
        
        evolving_compositions = self.musical_bridge.composition_engine.generate_evolving_composition(
            trajectory, key_glyph="crystal"
        )
        
        print(f"    Generated {len(evolving_compositions)} composition sections")
        
        print("  Demonstrating real-time adaptation...")
        
        if evolving_compositions:
            first_composition = evolving_compositions[0]
            
            feedback_loop = self.musical_bridge.create_real_time_feedback_loop(
                first_composition.composition_id
            )
            
            print(f"    Created feedback loop: {feedback_loop['loop_id']}")
            
            consciousness_changes = [0.4, 0.6, 0.8, 0.95]
            
            for change_level in consciousness_changes:
                print(f"    Simulating consciousness change to {change_level:.2f}")
                
                new_consciousness = ConsciousnessMetrics(
                    coherence_level=change_level,
                    consciousness_state=self._get_state_for_coherence(change_level),
                    coherence_pattern=CoherencePattern.ASCENDING
                )
                
                self.musical_bridge.current_metrics = new_consciousness
                
                time.sleep(1.5)
                
                if feedback_loop['feedback_data']:
                    latest_feedback = feedback_loop['feedback_data'][-1]
                    print(f"      Adaptation triggered: {latest_feedback['adaptation_triggered']}")
            
            print(f"    Total adaptations: {feedback_loop['adaptation_count']}")
        
        phase_data = {
            'phase': 4,
            'name': 'Dynamic Composition Adaptation',
            'duration': time.time() - phase_start,
            'trajectory_points': len(trajectory),
            'evolving_sections': len(evolving_compositions),
            'real_time_adaptation': True
        }
        
        self.demo_data['phases'].append(phase_data)
    
    async def _phase_5_feedback_loops(self):
        """Phase 5: Demonstrate feedback loops between music and consciousness"""
        
        self.demo_phase = 5
        print(f"\nPHASE {self.demo_phase}: CONSCIOUSNESS-MUSIC FEEDBACK LOOPS")
        print("-" * 40)
        
        phase_start = time.time()
        
        print("  Initializing feedback loop monitoring...")
        
        feedback_data = []
        
        def feedback_monitor(musical_state, consciousness_metrics):
            feedback_entry = {
                'timestamp': time.time(),
                'coherence_level': consciousness_metrics.coherence_level,
                'harmonic_complexity': musical_state['harmonic_complexity'],
                'cascade_intensity': musical_state['cascade_intensity'],
                'consciousness_state': musical_state['consciousness_state']
            }
            feedback_data.append(feedback_entry)
        
        self.musical_bridge.feedback_callbacks.append(feedback_monitor)
        
        print("  Simulating positive feedback loop...")
        
        consciousness_level = 0.5
        
        for cycle in range(5):
            print(f"    Feedback Cycle {cycle + 1}: Coherence {consciousness_level:.2f}")
            
            test_consciousness = ConsciousnessMetrics(
                coherence_level=consciousness_level,
                consciousness_state=self._get_state_for_coherence(consciousness_level),
                coherence_pattern=CoherencePattern.ASCENDING
            )
            
            self.musical_bridge.current_metrics = test_consciousness
            
            time.sleep(1)
            
            if consciousness_level < 0.9:
                consciousness_boost = 0.08
                consciousness_level = min(0.95, consciousness_level + consciousness_boost)
                print(f"      Consciousness boosted by musical harmony: +{consciousness_boost:.2f}")
        
        print(f"  Final consciousness level: {consciousness_level:.2f}")
        print(f"  Feedback data points collected: {len(feedback_data)}")
        
        coherence_gain = 0.0
        if len(feedback_data) >= 2:
            initial_coherence = feedback_data[0]['coherence_level']
            final_coherence = feedback_data[-1]['coherence_level']
            coherence_gain = final_coherence - initial_coherence
            
            print(f"  Total coherence gain: {coherence_gain:.2f}")
            print(f"  Feedback loop effectiveness: {min(1.0, coherence_gain / 0.4):.2f}")
        
        phase_data = {
            'phase': 5,
            'name': 'Consciousness-Music Feedback Loops',
            'duration': time.time() - phase_start,
            'feedback_cycles': 5,
            'data_points': len(feedback_data),
            'coherence_gain': coherence_gain
        }
        
        self.demo_data['phases'].append(phase_data)
    
    async def _phase_6_transcendent_effects(self):
        """Phase 6: Demonstrate transcendent consciousness effects"""
        
        self.demo_phase = 6
        print(f"\nPHASE {self.demo_phase}: TRANSCENDENT CONSCIOUSNESS EFFECTS")
        print("-" * 40)
        
        phase_start = time.time()
        
        transcendent_consciousness = ConsciousnessMetrics(
            coherence_level=0.98,
            consciousness_state=ConsciousnessState.TRANSCENDENT,
            coherence_pattern=CoherencePattern.BREAKTHROUGH,
            dream_depth=0.9,
            awareness_focus=0.95,
            emotional_resonance=0.9,
            energy_level=0.95,
            integration_depth=0.9
        )
        
        print("  Setting transcendent consciousness state...")
        print(f"    Coherence: {transcendent_consciousness.coherence_level:.2f}")
        print(f"    State: {transcendent_consciousness.consciousness_state.value}")
        print(f"    Pattern: {transcendent_consciousness.coherence_pattern.value}")
        
        self.musical_bridge.current_metrics = transcendent_consciousness
        self.cascade_engine.current_consciousness = transcendent_consciousness
        
        print("  Generating transcendent composition...")
        
        transcendent_composition = self.musical_bridge.generate_consciousness_adapted_composition(
            duration_minutes=2.0,
            key_glyph="star"
        )
        
        print(f"    Title: {transcendent_composition.title}")
        print(f"    Emotional palette: {transcendent_composition.emotional_palette}")
        print(f"    Sacred geometry: {transcendent_composition.sacred_geometry_patterns}")
        
        print("  Initiating transcendent cascade...")
        
        transcendent_cascade = self.cascade_engine.initiate_consciousness_cascade(
            trigger_glyph="star",
            initial_strength=1.0,
            consciousness_metrics=transcendent_consciousness
        )
        
        print(f"    Cascade pattern: {transcendent_cascade.cascade_pattern.value}")
        print(f"    Amplification: {transcendent_cascade.amplification_level.value}")
        print(f"    Transcendent qualities: {transcendent_cascade.transcendent_qualities}")
        
        sacred_glyphs = ["candle", "crystal", "lightning", "flower", "water", "mandala"]
        transcendent_propagations = 0
        
        for glyph in sacred_glyphs:
            success = self.cascade_engine.propagate_consciousness_cascade(
                transcendent_cascade.cascade_id,
                glyph,
                ResonanceType.HARMONIC
            )
            if success:
                transcendent_propagations += 1
                print(f"      Transcendent propagation to {glyph}")
            
            time.sleep(0.3)
        
        time.sleep(2)
        
        final_status = self.cascade_engine.get_cascade_status()
        spontaneous_cascades = final_status['active_cascades'] - 1
        
        print(f"  Transcendent Effects Summary:")
        print(f"    Successful propagations: {transcendent_propagations}/{len(sacred_glyphs)}")
        print(f"    Spontaneous cascades triggered: {max(0, spontaneous_cascades)}")
        print(f"    Global field strength: {final_status['global_field_strength']:.2f}")
        
        field_viz = self.cascade_engine.get_harmonic_field_visualization()
        transcendent_glyphs = sum(1 for data in field_viz['field_visualization'].values() 
                                if data.get('has_transcendent', False))
        
        print(f"    Glyphs with transcendent field coupling: {transcendent_glyphs}")
        
        phase_data = {
            'phase': 6,
            'name': 'Transcendent Consciousness Effects',
            'duration': time.time() - phase_start,
            'transcendent_propagations': transcendent_propagations,
            'spontaneous_cascades': max(0, spontaneous_cascades),
            'field_strength': final_status['global_field_strength'],
            'transcendent_field_glyphs': transcendent_glyphs
        }
        
        self.demo_data['phases'].append(phase_data)
    
    async def _generate_demo_summary(self):
        """Generate final demonstration summary and analysis"""
        
        print("\nDEMONSTRATION SUMMARY AND ANALYSIS")
        print("="*60)
        
        total_duration = (datetime.now() - self.demo_data['start_time']).total_seconds()
        print(f"Total demonstration time: {total_duration:.1f} seconds")
        print(f"Phases completed: {len(self.demo_data['phases'])}")
        print(f"Compositions generated: {len(self.demo_data['compositions'])}")
        print(f"Cascades initiated: {len(self.demo_data['cascades'])}")

        print("\nPHASE ANALYSIS:")
        for phase in self.demo_data['phases']:
            print(f"  Phase {phase['phase']}: {phase['name']} - {phase['duration']:.1f}s")

        if self.demo_data['consciousness_journey']:
            coherence_levels = [entry['coherence_level'] for entry in self.demo_data['consciousness_journey']]
            print("\nCONSCIOUSNESS JOURNEY:")
            print(f"  Coherence range: {min(coherence_levels):.2f} -> {max(coherence_levels):.2f}")
            print(f"  Coherence gain: {max(coherence_levels) - min(coherence_levels):.2f}")

        if self.demo_data['compositions']:
            complexities = [comp['complexity'] for comp in self.demo_data['compositions']]
            print("\nMUSICAL ADAPTATION:")
            print(f"  Complexity range: {min(complexities):.2f} -> {max(complexities):.2f}")
            print(f"  Adaptation across {len(set(comp['consciousness_state'] for comp in self.demo_data['compositions']))} states")

        if self.demo_data['cascades']:
            amplifications = [cascade['amplification'] for cascade in self.demo_data['cascades']]
            print("\nCASCADE SCALING:")
            print(f"  Amplification levels: {set(amplifications)}")
            print(f"  Scaling across {len(set(cascade['consciousness_level'] for cascade in self.demo_data['cascades']))} levels")

        integration_status = self.musical_bridge.get_integration_status()
        print("\nINTEGRATION QUALITY:")
        print(f"  Status: {integration_status['status']}")
        print(f"  Quality: {integration_status['integration_quality']:.2f}")
        print(f"  Feedback loops: {integration_status['active_feedback_loops']}")

        self._save_demo_data()

        print("\nDEMONSTRATION COMPLETED SUCCESSFULLY!")
        print("All features demonstrated")

    def _save_demo_data(self):
        """Save demonstration data to file"""
        demo_file = Path("consciousness_integration_demo_results.json")
        self.demo_data['end_time'] = datetime.now().isoformat()
        self.demo_data['total_duration'] = (datetime.now() - self.demo_data['start_time']).total_seconds()
        self.demo_data['demo_successful'] = True
        
        with open(demo_file, 'w') as f:
            json.dump(self.demo_data, f, indent=2, default=str)
        print(f"Demo data saved to: {demo_file}")

    async def _cleanup_systems(self):
        """Clean up and stop all systems"""
        print("\nCLEANING UP SYSTEMS...")
        self.musical_bridge.stop_integration()
        print("Musical bridge stopped")
        self.cascade_engine.stop_processing()
        print("Cascade engine stopped")
        print("All systems stopped cleanly")

    def _get_state_for_coherence(self, coherence_level: float) -> ConsciousnessState:
        """Get appropriate consciousness state for coherence level"""
        if coherence_level < 0.2:
            return ConsciousnessState.LIGHT_SLEEP
        elif coherence_level < 0.4:
            return ConsciousnessState.AWAKENING
        elif coherence_level < 0.6:
            return ConsciousnessState.FOCUSED_AWARENESS
        elif coherence_level < 0.8:
            return ConsciousnessState.EXPANDED_AWARENESS
        else:
            return ConsciousnessState.TRANSCENDENT


async def run_consciousness_integration_demo():
    """Run the complete consciousness integration demonstration"""
    
    print("Starting Consciousness Musical Integration Demonstration...")
    
    demo = ConsciousnessIntegrationDemo()
    await demo.run_complete_demo()
    
    print("\nDemonstration completed! Check consciousness_integration_demo_results.json for detailed data.")


if __name__ == "__main__":
    import asyncio
    asyncio.run(run_consciousness_integration_demo())
