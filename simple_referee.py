#!/usr/bin/env python3
"""
Simple ML Model Referee for Fake News Detection
Beginner-friendly hackathon version
"""

class SimpleReferee:
    def __init__(self):
        # Model characteristics
        self.models = {
            "Logistic Regression": {
                "accuracy": 82,
                "speed_ms": 0.5,
                "training_time_min": 2.5,
                "memory_mb": 50,
                "interpretability": 9,
                "hardware": "CPU",
                "complexity": "Simple"
            },
            "Naive Bayes": {
                "accuracy": 78,
                "speed_ms": 0.3,
                "training_time_min": 1.0,
                "memory_mb": 30,
                "interpretability": 8,
                "hardware": "CPU",
                "complexity": "Very Simple"
            },
            "BERT": {
                "accuracy": 94,
                "speed_ms": 45,
                "training_time_min": 180,
                "memory_mb": 2048,
                "interpretability": 3,
                "hardware": "GPU",
                "complexity": "Complex"
            }
        }
    
    def print_comparison_table(self):
        """Print a nice comparison table"""
        print("\n" + "="*80)
        print("                    FAKE NEWS DETECTION MODEL COMPARISON")
        print("="*80)
        
        # Header
        print(f"{'Criteria':<20} {'Logistic Reg':<15} {'Naive Bayes':<15} {'BERT':<15}")
        print("-" * 80)
        
        # Rows
        criteria = [
            ("Accuracy (%)", "accuracy"),
            ("Speed (ms)", "speed_ms"),
            ("Training (min)", "training_time_min"),
            ("Memory (MB)", "memory_mb"),
            ("Interpretability", "interpretability"),
            ("Hardware", "hardware"),
            ("Complexity", "complexity")
        ]
        
        for label, key in criteria:
            lr_val = self.models["Logistic Regression"][key]
            nb_val = self.models["Naive Bayes"][key]
            bert_val = self.models["BERT"][key]
            
            print(f"{label:<20} {str(lr_val):<15} {str(nb_val):<15} {str(bert_val):<15}")
        
        print("="*80)
    
    def decide_model(self, dataset_size, priority, hardware):
        """
        Decision logic for model selection
        
        Args:
            dataset_size: "small", "medium", "large"
            priority: "speed", "accuracy", "simplicity"
            hardware: "cpu", "gpu"
        """
        
        print(f"\n🤔 Your Requirements:")
        print(f"   Dataset Size: {dataset_size}")
        print(f"   Priority: {priority}")
        print(f"   Hardware: {hardware.upper()}")
        
        # Decision tree logic
        recommendation = None
        reason = ""
        
        # Rule 1: If only CPU available, eliminate BERT
        if hardware.lower() == "cpu":
            if priority == "accuracy":
                recommendation = "Logistic Regression"
                reason = "Best CPU-only accuracy option"
            elif priority == "speed":
                recommendation = "Naive Bayes"
                reason = "Fastest inference on CPU"
            else:  # simplicity
                recommendation = "Naive Bayes"
                reason = "Simplest to implement and understand"
        
        # Rule 2: If GPU available, consider all options
        else:  # GPU available
            if priority == "accuracy":
                if dataset_size == "large":
                    recommendation = "BERT"
                    reason = "Highest accuracy with sufficient data"
                else:
                    recommendation = "Logistic Regression"
                    reason = "Good accuracy without needing large dataset"
            elif priority == "speed":
                if dataset_size == "small":
                    recommendation = "Naive Bayes"
                    reason = "Fastest option, works well with small data"
                else:
                    recommendation = "Logistic Regression"
                    reason = "Good balance of speed and performance"
            else:  # simplicity
                recommendation = "Naive Bayes"
                reason = "Easiest to implement and debug"
        
        # Additional considerations
        considerations = []
        
        if dataset_size == "small" and recommendation == "BERT":
            considerations.append("⚠️  BERT may overfit on small datasets")
        
        if priority == "speed" and recommendation == "BERT":
            considerations.append("⚠️  BERT is much slower than alternatives")
        
        if hardware.lower() == "cpu" and recommendation == "BERT":
            considerations.append("⚠️  BERT will be very slow on CPU")
        
        return recommendation, reason, considerations
    
    def explain_choice(self, model_name):
        """Explain why a model might be chosen"""
        model = self.models[model_name]
        
        print(f"\n📊 {model_name} Details:")
        print(f"   Accuracy: {model['accuracy']}%")
        print(f"   Speed: {model['speed_ms']}ms per prediction")
        print(f"   Training: {model['training_time_min']} minutes")
        print(f"   Memory: {model['memory_mb']}MB")
        print(f"   Interpretability: {model['interpretability']}/10")
        print(f"   Hardware: {model['hardware']} required")
        
        # Strengths and weaknesses
        strengths = {
            "Logistic Regression": [
                "Good balance of accuracy and speed",
                "Easy to interpret results",
                "Works well with medium datasets"
            ],
            "Naive Bayes": [
                "Extremely fast training and prediction",
                "Works great with small datasets",
                "Very simple to implement"
            ],
            "BERT": [
                "State-of-the-art accuracy",
                "Understands context and nuance",
                "Pre-trained on massive text data"
            ]
        }
        
        weaknesses = {
            "Logistic Regression": [
                "May miss complex patterns",
                "Needs feature engineering"
            ],
            "Naive Bayes": [
                "Assumes word independence",
                "Lower accuracy than complex models"
            ],
            "BERT": [
                "Very slow and resource-heavy",
                "Hard to interpret decisions",
                "Needs large datasets to shine"
            ]
        }
        
        print(f"\n✅ Strengths:")
        for strength in strengths[model_name]:
            print(f"   • {strength}")
        
        print(f"\n❌ Weaknesses:")
        for weakness in weaknesses[model_name]:
            print(f"   • {weakness}")

def get_user_input():
    """Get user requirements interactively"""
    print("\n🎯 Let's find the best model for your fake news detection project!")
    
    # Dataset size
    print("\n1. How much training data do you have?")
    print("   a) Small (< 10,000 articles)")
    print("   b) Medium (10,000 - 100,000 articles)")
    print("   c) Large (> 100,000 articles)")
    
    size_choice = input("Enter choice (a/b/c): ").lower()
    size_map = {"a": "small", "b": "medium", "c": "large"}
    dataset_size = size_map.get(size_choice, "medium")
    
    # Priority
    print("\n2. What's most important to you?")
    print("   a) Speed (fast predictions)")
    print("   b) Accuracy (best performance)")
    print("   c) Simplicity (easy to understand)")
    
    priority_choice = input("Enter choice (a/b/c): ").lower()
    priority_map = {"a": "speed", "b": "accuracy", "c": "simplicity"}
    priority = priority_map.get(priority_choice, "accuracy")
    
    # Hardware
    print("\n3. What hardware do you have?")
    print("   a) CPU only")
    print("   b) GPU available")
    
    hardware_choice = input("Enter choice (a/b): ").lower()
    hardware_map = {"a": "cpu", "b": "gpu"}
    hardware = hardware_map.get(hardware_choice, "cpu")
    
    return dataset_size, priority, hardware

def main():
    """Main function - the entry point"""
    referee = SimpleReferee()
    
    print("🏆 ML Model Referee for Fake News Detection")
    print("   Helping you choose the right model for your needs!")
    
    # Show comparison table
    referee.print_comparison_table()
    
    # Get user input
    dataset_size, priority, hardware = get_user_input()
    
    # Make recommendation
    recommendation, reason, considerations = referee.decide_model(
        dataset_size, priority, hardware
    )
    
    # Show results
    print(f"\n🎉 RECOMMENDATION: {recommendation}")
    print(f"   Reason: {reason}")
    
    if considerations:
        print(f"\n⚠️  Important Notes:")
        for consideration in considerations:
            print(f"   {consideration}")
    
    # Explain the choice
    referee.explain_choice(recommendation)
    
    # Show alternatives
    print(f"\n🔄 Alternative Options:")
    for model_name in referee.models.keys():
        if model_name != recommendation:
            model = referee.models[model_name]
            print(f"   • {model_name}: {model['accuracy']}% accuracy, {model['speed_ms']}ms speed")
    
    print(f"\n💡 Pro Tip: Start with {recommendation} and experiment with others later!")

if __name__ == "__main__":
    main()