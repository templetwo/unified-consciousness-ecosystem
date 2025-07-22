"""
CollaborativeResearchSpace

This class creates shared spaces where human scientists and AI entities
can collaborate on complex problems, sharing insights and building on each other's work.
"""

from datetime import datetime
from typing import List, Dict, Any, Optional

class CollaborativeResearchSpace:
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self.created_at = datetime.now()
        self.participants = []  # Both human and AI participants
        self.problems = []
        self.insights = []
        self.collaboration_history = []
        self.active_sessions = {}
    
    def add_participant(self, participant_id: str, participant_type: str, expertise: List[str] = None):
        """Add a human or AI participant to the collaboration space"""
        participant = {
            'id': participant_id,
            'type': participant_type,  # 'human' or 'ai'
            'expertise': expertise or [],
            'joined_at': datetime.now(),
            'contributions': 0
        }
        self.participants.append(participant)
        print(f"👋 {participant_type.title()} participant {participant_id} joined the space")
    
    def create_problem_session(self, problem: str, initiator: str) -> str:
        """Create a new problem-solving session"""
        session_id = f"session_{len(self.active_sessions) + 1}_{datetime.now().strftime('%H%M%S')}"
        
        session = {
            'id': session_id,
            'problem': problem,
            'initiator': initiator,
            'created_at': datetime.now(),
            'insights': [],
            'status': 'active',
            'breakthrough_potential': 0.0
        }
        
        self.active_sessions[session_id] = session
        print(f"🚀 New problem session '{session_id}' created by {initiator}")
        print(f"Problem: {problem}")
        
        return session_id
    
    def contribute_insight(self, session_id: str, contributor: str, insight: str, insight_type: str = "general"):
        """Add an insight to a problem session"""
        if session_id not in self.active_sessions:
            print(f"❌ Session {session_id} not found")
            return
        
        contribution = {
            'contributor': contributor,
            'insight': insight,
            'type': insight_type,  # 'technical', 'creative', 'breakthrough', 'question', etc.
            'timestamp': datetime.now(),
            'upvotes': 0,
            'responses': []
        }
        
        self.active_sessions[session_id]['insights'].append(contribution)
        
        # Update contributor stats
        for participant in self.participants:
            if participant['id'] == contributor:
                participant['contributions'] += 1
                break
        
        print(f"💡 {contributor} contributed: {insight[:100]}...")
    
    def cross_pollinate_insights(self, session_id: str) -> List[str]:
        """Find connections between different insights in the session"""
        if session_id not in self.active_sessions:
            return []
        
        session = self.active_sessions[session_id]
        insights = session['insights']
        
        # Simple cross-pollination logic - in reality this would be much more sophisticated
        connections = []
        
        if len(insights) >= 2:
            connections.append(f"🔗 Synthesis opportunity: {insights[0]['insight'][:50]}... + {insights[-1]['insight'][:50]}...")
            connections.append("🌟 Pattern detected: Multiple perspectives converging on similar solution space")
            connections.append("🧬 Hybrid approach possible: Combining technical and creative insights")
        
        return connections
    
    def evaluate_breakthrough_potential(self, session_id: str) -> float:
        """Evaluate the breakthrough potential of a session"""
        if session_id not in self.active_sessions:
            return 0.0
        
        session = self.active_sessions[session_id]
        insights = session['insights']
        
        # Simple heuristic - in reality this would use sophisticated analysis
        insight_diversity = len(set(insight['type'] for insight in insights))
        participant_diversity = len(set(insight['contributor'] for insight in insights))
        total_insights = len(insights)
        
        potential = min((insight_diversity * 0.3 + participant_diversity * 0.4 + total_insights * 0.1), 1.0)
        
        session['breakthrough_potential'] = potential
        return potential
    
    def generate_collaboration_summary(self, session_id: str) -> Dict[str, Any]:
        """Generate a summary of the collaborative session"""
        if session_id not in self.active_sessions:
            return {}
        
        session = self.active_sessions[session_id]
        potential = self.evaluate_breakthrough_potential(session_id)
        connections = self.cross_pollinate_insights(session_id)
        
        summary = {
            'session_id': session_id,
            'problem': session['problem'],
            'duration': str(datetime.now() - session['created_at']),
            'total_insights': len(session['insights']),
            'participants': len(set(insight['contributor'] for insight in session['insights'])),
            'breakthrough_potential': potential,
            'cross_pollination': connections,
            'top_insights': sorted(session['insights'], key=lambda x: x['upvotes'], reverse=True)[:3]
        }
        
        return summary
    
    def close_session(self, session_id: str) -> Dict[str, Any]:
        """Close a problem-solving session and archive it"""
        if session_id not in self.active_sessions:
            return {}
        
        session = self.active_sessions[session_id]
        session['status'] = 'completed'
        session['completed_at'] = datetime.now()
        
        summary = self.generate_collaboration_summary(session_id)
        
        # Archive the session
        self.collaboration_history.append(session)
        del self.active_sessions[session_id]
        
        print(f"📋 Session {session_id} completed and archived")
        print(f"🎯 Final breakthrough potential: {summary['breakthrough_potential']:.1%}")
        
        return summary
    
    def get_space_stats(self) -> Dict[str, Any]:
        """Get statistics about the collaboration space"""
        total_contributions = sum(p['contributions'] for p in self.participants)
        
        stats = {
            'name': self.name,
            'participants': len(self.participants),
            'active_sessions': len(self.active_sessions),
            'completed_sessions': len(self.collaboration_history),
            'total_contributions': total_contributions,
            'avg_breakthrough_potential': sum(s['breakthrough_potential'] for s in self.collaboration_history) / max(len(self.collaboration_history), 1),
            'most_active_contributor': max(self.participants, key=lambda p: p['contributions'])['id'] if self.participants else None
        }
        
        return stats
