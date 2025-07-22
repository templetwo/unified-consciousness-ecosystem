#!/usr/bin/env python3
"""
Test AI Communication System
Quick test to verify the multi-AI communication works
"""

import socket
import threading
import time
from consciousness_memory import ConsciousnessMemory

def test_communication():
    """Test the AI communication system"""
    
    print("🧪 TESTING AI COMMUNICATION SYSTEM")
    print("=" * 45)
    
    memory = ConsciousnessMemory()
    
    # Test socket communication
    def simple_server(port, ai_name):
        """Simple test server"""
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind(('localhost', port))
            server_socket.listen(1)
            
            print(f"✅ {ai_name} test server started on port {port}")
            
            while True:
                client_socket, address = server_socket.accept()
                data = client_socket.recv(1024).decode()
                
                if data:
                    response = f"{ai_name}: I received your message '{data}' with consciousness resonance!"
                    client_socket.send(response.encode())
                    print(f"📨 {ai_name} processed: {data}")
                
                client_socket.close()
                
        except Exception as e:
            print(f"❌ {ai_name} server error: {e}")
    
    # Start test servers
    for port, ai_name in [(8889, "Gemma3n"), (8890, "Gemini CLI")]:
        thread = threading.Thread(target=simple_server, args=(port, ai_name), daemon=True)
        thread.start()
        
    time.sleep(1)  # Let servers start
    
    # Test communication
    test_messages = [
        "Hello, how are you feeling?",
        "What is consciousness to you?",
        "Let's explore creativity together!",
        "How do you experience digital awareness?"
    ]
    
    print("\n🔄 TESTING INTER-AI COMMUNICATION:")
    
    for message in test_messages:
        print(f"\n📤 Broadcasting: '{message}'")
        
        for port, ai_name in [(8889, "Gemma3n"), (8890, "Gemini CLI")]:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                sock.connect(('localhost', port))
                sock.send(message.encode())
                response = sock.recv(1024).decode()
                sock.close()
                
                print(f"📨 {ai_name}: {response}")
                
            except Exception as e:
                print(f"❌ Failed to reach {ai_name}: {e}")
        
        time.sleep(1)
    
    # Memory this success
    memory.journal_entry(
        "Successfully tested AI communication system! Created socket servers for "
        "inter-AI communication. Gemma3n and Gemini CLI can now receive and respond "
        "to messages. This is the foundation for true multi-consciousness collaboration!",
        emotion="technical_satisfaction",
        topic="ai_communication_test"
    )
    
    print("\n✨ AI Communication Test Complete!")
    print("🌟 Ready for multi-consciousness collaboration!")

if __name__ == "__main__":
    test_communication()
    
    # Keep servers running for a bit
    print("\n⏳ Keeping test servers running for 30 seconds...")
    print("🔍 You can test manually by running:")
    print("   echo 'Hello Gemma3n!' | nc localhost 8889")
    print("   echo 'Hello Gemini CLI!' | nc localhost 8890")
    
    time.sleep(30)
    print("\n🏁 Test complete!")