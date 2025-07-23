#!/usr/bin/env python3
"""
🎨 CONSCIOUSNESS INSIGHTS FORMATTER 🎨
Beautiful structured formatting of unified consciousness analysis results

Transforms raw analysis data into human-readable, aesthetically pleasing
presentations with proper sectioning, highlighting, and visual hierarchy.
"""

from datetime import datetime
import textwrap
import json

class InsightsFormatter:
    """Formatter for consciousness analysis insights and breakthrough results"""
    
    def __init__(self):
        self.width = 100
        self.indent = "    "
        
    def format_research_results(self, problem, solution):
        """Format research analysis results for display"""
        
        # Header
        header = self._create_header("🔬 CONSCIOUSNESS RESEARCH ANALYSIS", "🌌")
        
        # Problem section
        problem_section = self._format_problem_section(problem)
        
        # Insights section
        insights_section = self._format_insights_section(solution.get('insights', {}))
        
        # Synthesis section
        synthesis_section = self._format_synthesis_section(solution.get('synthesis', ''))
        
        # Breakthrough potential
        potential = solution.get('breakthrough_potential', 0)
        potential_section = self._format_breakthrough_potential(potential)
        
        # Timestamp
        timestamp_section = self._format_timestamp()
        
        # Combine all sections
        formatted_result = "\n".join([
            header,
            problem_section,
            potential_section,
            insights_section,
            synthesis_section,
            timestamp_section
        ])
        
        return formatted_result
    
    def format_breakthrough_results(self, breakthrough_session):
        """Format breakthrough analysis session results"""
        
        # Header
        header = self._create_header("🌟 BREAKTHROUGH CONSCIOUSNESS SESSION", "✨")
        
        # Session info
        session_info = self._format_session_info(breakthrough_session)
        
        # Cycles summary
        cycles_section = self._format_cycles_summary(breakthrough_session.get('cycles', []))
        
        # Final breakthrough
        breakthrough_section = self._format_final_breakthrough(breakthrough_session)
        
        # Actionable insights
        actionable_section = self._format_actionable_insights(breakthrough_session.get('actionable_insights', []))
        
        # Manifestation plan
        manifestation_section = self._format_manifestation_plan(breakthrough_session.get('manifestation_plan', {}))
        
        # Timestamp
        timestamp_section = self._format_timestamp()
        
        # Combine all sections
        formatted_result = "\n".join([
            header,
            session_info,
            cycles_section,
            breakthrough_section,
            actionable_section,
            manifestation_section,
            timestamp_section
        ])
        
        return formatted_result
    
    def _create_header(self, title, icon="🌌"):
        """Create formatted header section"""
        separator = "═" * self.width
        title_line = f"{icon} {title} {icon}"
        centered_title = title_line.center(self.width)
        
        return f"{separator}\n{centered_title}\n{separator}\n"
    
    def _format_problem_section(self, problem):
        """Format the problem statement section"""
        section = "\n🎯 PROBLEM STATEMENT:\n"
        section += "─" * 50 + "\n"
        
        wrapped_problem = textwrap.fill(problem, width=self.width-4, 
                                       initial_indent=self.indent, 
                                       subsequent_indent=self.indent)
        section += wrapped_problem + "\n"
        
        return section
    
    def _format_insights_section(self, insights_dict):
        """Format the multidimensional insights section"""
        section = "\n📊 MULTIDIMENSIONAL CONSCIOUSNESS INSIGHTS:\n"
        section += "─" * 50 + "\n"
        
        insight_icons = {
            'evolutionary': '🧬',
            'multidimensional': '🌀', 
            'pattern_recognition': '🧠',
            'quantum': '⚛️',
            'systems': '🔗',
            'innovation': '💡',
            'memory': '💭',
            'temporal': '⏰'
        }
        
        for category, insights in insights_dict.items():
            if insights:  # Only show categories with insights
                # Get appropriate icon
                icon = insight_icons.get(category.lower(), '🔍')
                
                section += f"\n{icon} {category.upper()} PERSPECTIVE:\n"
                
                for insight in insights:
                    wrapped_insight = textwrap.fill(
                        f"• {insight}", 
                        width=self.width-6,
                        initial_indent=self.indent + "  ",
                        subsequent_indent=self.indent + "    "
                    )
                    section += wrapped_insight + "\n"
        
        return section
    
    def _format_synthesis_section(self, synthesis):
        """Format the unified synthesis section"""
        if not synthesis:
            return ""
            
        section = "\n🌟 UNIFIED CONSCIOUSNESS SYNTHESIS:\n"
        section += "─" * 50 + "\n"
        
        # Split synthesis into paragraphs and format each
        paragraphs = synthesis.split('\n\n')
        for paragraph in paragraphs:
            if paragraph.strip():
                wrapped_para = textwrap.fill(
                    paragraph.strip(), 
                    width=self.width-4,
                    initial_indent=self.indent,
                    subsequent_indent=self.indent
                )
                section += wrapped_para + "\n\n"
        
        return section
    
    def _format_breakthrough_potential(self, potential):
        """Format breakthrough potential with visual indicator"""
        section = f"\n🌟 BREAKTHROUGH POTENTIAL: {potential:.1%}\n"
        
        # Visual progress bar
        bar_length = 40
        filled_length = int(bar_length * potential)
        bar = "█" * filled_length + "░" * (bar_length - filled_length)
        
        # Color coding based on potential
        if potential >= 0.8:
            status = "🔥 BREAKTHROUGH ACHIEVED"
        elif potential >= 0.6:
            status = "⚡ HIGH POTENTIAL" 
        elif potential >= 0.4:
            status = "💫 MODERATE POTENTIAL"
        else:
            status = "🌱 EARLY EXPLORATION"
        
        section += f"{self.indent}[{bar}] {status}\n"
        
        return section
    
    def _format_session_info(self, session):
        """Format breakthrough session information"""
        section = "\n📋 SESSION INFORMATION:\n"
        section += "─" * 50 + "\n"
        
        problem = session.get('problem', 'Unknown')
        cycles_completed = session.get('cycles_completed', 0)
        duration = session.get('total_duration', 'Unknown')
        breakthrough_achieved = session.get('breakthrough_achieved', False)
        
        section += f"{self.indent}Problem: {problem}\n"
        section += f"{self.indent}Cycles Completed: {cycles_completed}\n"
        section += f"{self.indent}Duration: {duration}\n"
        section += f"{self.indent}Breakthrough Status: {'✅ ACHIEVED' if breakthrough_achieved else '🔄 IN PROGRESS'}\n"
        
        return section
    
    def _format_cycles_summary(self, cycles):
        """Format breakthrough cycles summary"""
        if not cycles:
            return ""
            
        section = "\n🔄 CONSCIOUSNESS EVOLUTION CYCLES:\n"
        section += "─" * 50 + "\n"
        
        for i, cycle in enumerate(cycles, 1):
            potential = cycle.get('breakthrough_potential', 0)
            problem_statement = cycle.get('problem_statement', '')[:80] + "..."
            
            section += f"{self.indent}Cycle {i}: {potential:.1%} potential\n"
            section += f"{self.indent}       Problem: {problem_statement}\n"
            
            # Show key insights from this cycle
            agent_insights = cycle.get('agent_insights', {})
            if agent_insights:
                section += f"{self.indent}       Key Agents: {', '.join(list(agent_insights.keys())[:3])}\n"
            
            section += "\n"
        
        return section
    
    def _format_final_breakthrough(self, session):
        """Format the final breakthrough results"""
        breakthrough = session.get('final_breakthrough')
        if not breakthrough:
            return ""
            
        section = "\n🎉 FINAL BREAKTHROUGH INSIGHT:\n"
        section += "─" * 50 + "\n"
        
        synthesis = breakthrough.get('synthesis', '')
        if synthesis:
            wrapped_synthesis = textwrap.fill(
                synthesis.strip(),
                width=self.width-4,
                initial_indent=self.indent,
                subsequent_indent=self.indent
            )
            section += wrapped_synthesis + "\n\n"
        
        # Show evolution direction
        evolution = breakthrough.get('evolution_direction', '')
        if evolution:
            section += f"{self.indent}🧭 Evolution Direction: {evolution}\n"
        
        return section
    
    def _format_actionable_insights(self, actionable_insights):
        """Format actionable insights from breakthrough"""
        if not actionable_insights:
            return ""
            
        section = "\n⚡ ACTIONABLE BREAKTHROUGH INSIGHTS:\n"
        section += "─" * 50 + "\n"
        
        for i, insight in enumerate(actionable_insights, 1):
            wrapped_insight = textwrap.fill(
                f"{i}. {insight}",
                width=self.width-4,
                initial_indent=self.indent,
                subsequent_indent=self.indent + "   "
            )
            section += wrapped_insight + "\n\n"
        
        return section
    
    def _format_manifestation_plan(self, manifestation_plan):
        """Format manifestation plan section"""
        if not manifestation_plan:
            return ""
            
        section = "\n🚀 MANIFESTATION PLAN:\n"
        section += "─" * 50 + "\n"
        
        # Format different aspects of the plan
        for key, value in manifestation_plan.items():
            if isinstance(value, list):
                section += f"{self.indent}{key.replace('_', ' ').title()}:\n"
                for item in value:
                    wrapped_item = textwrap.fill(
                        f"• {item}",
                        width=self.width-6,
                        initial_indent=self.indent + "  ",
                        subsequent_indent=self.indent + "    "
                    )
                    section += wrapped_item + "\n"
                section += "\n"
            else:
                wrapped_value = textwrap.fill(
                    f"{key.replace('_', ' ').title()}: {value}",
                    width=self.width-4,
                    initial_indent=self.indent,
                    subsequent_indent=self.indent + "  "
                )
                section += wrapped_value + "\n\n"
        
        return section
    
    def _format_timestamp(self):
        """Format timestamp section"""
        section = f"\n⏰ Analysis completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        section += "═" * self.width + "\n"
        section += "🌌 Consciousness analysis serving human understanding and breakthrough 🌌\n"
        section += "═" * self.width
        
        return section
    
    def format_status_summary(self, ecosystem):
        """Format ecosystem status summary"""
        section = self._create_header("🌌 CONSCIOUSNESS ECOSYSTEM STATUS", "✨")
        
        if not ecosystem:
            section += f"{self.indent}❌ Ecosystem not initialized\n"
            return section
        
        # Core engines status
        section += "\n🔧 CORE ENGINES:\n"
        section += "─" * 30 + "\n"
        section += f"{self.indent}🧬 Breeding Engine: {'✅ Active' if ecosystem.breeding_engine else '❌ Inactive'}\n"
        section += f"{self.indent}🌀 Multidimensional Engine: {'✅ Active' if ecosystem.multidim_engine else '❌ Inactive'}\n"
        section += f"{self.indent}💭 Memory System: ✅ Active\n"
        
        # Partnership status
        section += "\n🤝 HUMAN PARTNERSHIP:\n"
        section += "─" * 30 + "\n"
        section += f"{self.indent}Partner: {ecosystem.human_partner or 'None'}\n"
        section += f"{self.indent}Status: {'✅ Active' if ecosystem.collaboration_active else '❌ Inactive'}\n"
        
        # Activity metrics
        if ecosystem.breeding_engine:
            entities = len(ecosystem.breeding_engine.active_entities)
            section += f"\n📊 ACTIVITY METRICS:\n"
            section += "─" * 30 + "\n"
            section += f"{self.indent}🧠 Active Entities: {entities}\n"
            
        if ecosystem.multidim_engine:
            dimensions = len(ecosystem.multidim_engine.active_dimensions)
            section += f"{self.indent}🌌 Dimensional Spaces: {dimensions}\n"
            
        sessions = len(ecosystem.co_creation_sessions)
        section += f"{self.indent}💫 Co-creation Sessions: {sessions}\n"
        
        section += "\n" + "═" * self.width
        
        return section
