#!/usr/bin/env python3
"""
Automated Showcase Demo - Perfect for hackathon presentations
Shows different scenarios without requiring user input
"""

import time
import os

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print fancy header"""
    print("🏆" + "="*58 + "🏆")
    print("🎯        ML MODEL REFEREE - FAKE NEWS DETECTION        🎯")
    print("🏆" + "="*58 + "🏆")
    print()

def simulate_typing(text, delay=0.03):
    """Simulate typing effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def show_scenario(scenario_name, dataset_size, priority, hardware, description):
    """Show a complete scenario"""
    print(f"🎬 SCENARIO: {scenario_name}")
    print(f"📝 Context: {description}")
    print()
    
    # Show the questions and answers
    print("❓ Question 1: How much training data do you have?")
    simulate_typing(f"   ✅ Answer: {dataset_size.title()} dataset")
    print()
    
    print("❓ Question 2: What's most important to you?")
    simulate_typing(f"   ✅ Answer: {priority.title()} is the priority")
    print()
    
    print("❓ Question 3: What hardware do you have available?")
    simulate_typing(f"   ✅ Answer: {hardware.upper()} available")
    print()
    
    # Show thinking
    print("🤔 Analyzing requirements", end="")
    for i in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print(" Done! ✅")
    print()
    
    # Decision logic (same as web interface)
    if hardware == 'cpu':
        if priority == 'accuracy':
            recommendation = 'Logistic Regression'
            reason = 'Best CPU-only accuracy option'
        elif priority == 'speed':
            recommendation = 'Naive Bayes'
            reason = 'Fastest inference on CPU'
        else:
            recommendation = 'Naive Bayes'
            reason = 'Simplest to implement and understand'
    else:
        if priority == 'accuracy':
            if dataset_size == 'large':
                recommendation = 'BERT'
                reason = 'Highest accuracy with sufficient data'
            else:
                recommendation = 'Logistic Regression'
                reason = 'Good accuracy without needing large dataset'
        elif priority == 'speed':
            if dataset_size == 'small':
                recommendation = 'Naive Bayes'
                reason = 'Fastest option, works well with small data'
            else:
                recommendation = 'Logistic Regression'
                reason = 'Good balance of speed and performance'
        else:
            recommendation = 'Naive Bayes'
            reason = 'Easiest to implement and debug'
    
    # Show recommendation
    print("🎉" + "="*50 + "🎉")
    print(f"🏆 RECOMMENDATION: {recommendation}")
    print(f"📝 REASON: {reason}")
    print("🎉" + "="*50 + "🎉")
    print()
    
    time.sleep(2)

def main():
    """Main showcase function"""
    clear_screen()
    print_header()
    
    simulate_typing("🎯 Welcome to the ML Model Referee Demo!")
    simulate_typing("   This tool helps choose the right ML model for fake news detection")
    print()
    time.sleep(1)
    
    scenarios = [
        {
            "name": "Startup Company",
            "dataset_size": "small",
            "priority": "speed",
            "hardware": "cpu",
            "description": "Small team, limited resources, need quick deployment"
        },
        {
            "name": "Research Institution", 
            "dataset_size": "large",
            "priority": "accuracy",
            "hardware": "gpu",
            "description": "Academic research, need highest possible accuracy"
        },
        {
            "name": "News Website",
            "dataset_size": "medium", 
            "priority": "speed",
            "hardware": "cpu",
            "description": "Real-time fact-checking for live articles"
        },
        {
            "name": "Explainable AI System",
            "dataset_size": "medium",
            "priority": "simplicity", 
            "hardware": "gpu",
            "description": "Need to explain decisions to end users"
        }
    ]
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"\n{'='*60}")
        print(f"DEMO {i}/4")
        print('='*60)
        
        show_scenario(
            scenario["name"],
            scenario["dataset_size"], 
            scenario["priority"],
            scenario["hardware"],
            scenario["description"]
        )
        
        if i < len(scenarios):
            print("⏭️  Next scenario in 3 seconds...")
            time.sleep(3)
            clear_screen()
            print_header()
    
    # Final summary
    print("\n" + "🌟" * 20)
    print("🎊 DEMO COMPLETE! 🎊")
    print("🌟" * 20)
    print()
    print("📊 What we showed:")
    print("   ✅ Interactive questionnaire (3 simple questions)")
    print("   ✅ Smart recommendation engine")
    print("   ✅ Multiple real-world scenarios")
    print("   ✅ Detailed model comparisons")
    print()
    print("🚀 Key Features:")
    print("   • No single 'best' model - shows trade-offs")
    print("   • Considers user constraints (data, hardware, priorities)")
    print("   • Explains reasoning behind recommendations")
    print("   • Perfect for hackathon judges to understand!")
    print()
    print("🌐 Try the interactive web version at: http://localhost:5000")
    print("💻 Or run: python simple_referee.py for terminal version")
    print()
    print("🏆 Ready to impress the judges! 🏆")

if __name__ == "__main__":
    main()