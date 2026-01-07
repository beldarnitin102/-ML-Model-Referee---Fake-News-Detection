# 🏆 ML Model Referee - Fake News Detection

**The smart way to choose machine learning models - no more guessing!**

## 🎯 The Problem

Choosing the right ML model for fake news detection is hard:
- Different models have different strengths
- Trade-offs between accuracy, speed, and resources
- No "one-size-fits-all" solution
- Users have different constraints (budget, hardware, expertise)

## 💡 Our Solution

**ML Model Referee** - A comparison-based recommendation system that:
- ✅ Shows trade-offs transparently instead of giving one answer
- ✅ Considers your specific constraints (data size, hardware, priorities)
- ✅ Explains reasoning behind recommendations
- ✅ Helps you make informed decisions

## 🤖 AI Assistance Used

This project was developed with the help of **Kiro AI (AWS)** as a decision-support tool.

Kiro was used to:
- Compare multiple ML models (Logistic Regression, Naive Bayes, BERT)
- Analyze trade-offs between accuracy, speed, and explainability
- Improve model selection strategy for fake news detection

Kiro acted as an AI referee rather than a single-answer generator.


## 🚀 HOW TO RUN THE PROJECT

### 🌐 **MAIN DEMO** (For Hackathon Judges)
```bash
python app.py
```
**Then open browser and go to: http://localhost:5000**

### 🖥️ **Terminal Demo** (Alternative)
```bash
python showcase_demo.py
```

## 📊 Model Comparison

| Model | Accuracy | Speed | Memory | Interpretability | Best For |
|-------|----------|-------|---------|------------------|----------|
| **Logistic Regression** | 82% | 0.5ms | 50MB | 9/10 | Balanced needs |
| **Naive Bayes** | 78% | 0.3ms | 30MB | 8/10 | Speed & Simplicity |
| **BERT** | 94% | 45ms | 2GB | 3/10 | Maximum Accuracy |

## 🎮 How It Works

### 3 Simple Questions:
1. **Dataset Size**: Small, Medium, or Large?
2. **Priority**: Speed, Accuracy, or Simplicity?
3. **Hardware**: CPU only or GPU available?

### Smart Recommendations:
- **CPU + Speed** → Naive Bayes
- **GPU + Accuracy + Large Data** → BERT
- **Balanced Needs** → Logistic Regression
- **Explainable AI** → Logistic Regression

## 🏗️ Project Files

```
📁 ML Model Referee (Essential Files Only)
├── 🌐 app.py                 # Main web interface (START HERE)
├── 🖥️ showcase_demo.py       # Terminal demo for presentation
├── 🧠 simple_referee.py      # Core logic
├── �  templates/index.html   # Web UI
├── � trequirements.txt       # Dependencies
└── 📖 README.md             # This file
```

## 🎯 Key Features

### 1. **Comparison-Based Approach**
- No single "best" model
- Shows all options with trade-offs
- Builds trust through transparency

### 2. **3 Simple Questions**
1. **Dataset Size**: Small, Medium, or Large?
2. **Priority**: Speed, Accuracy, or Simplicity?
3. **Hardware**: CPU only or GPU available?

### 3. **Smart Recommendations**
- **CPU + Speed** → Naive Bayes
- **GPU + Accuracy + Large Data** → BERT
- **Balanced Needs** → Logistic Regression

## 🛠️ Setup & Installation

```bash
# 1. Install dependencies
pip install flask

# 2. Run the main project
python app.py

# 3. Open browser to: http://localhost:5000
```

## 🎪 For Hackathon Judges

**Perfect demo flow:**
1. Run `python app.py`
2. Open http://localhost:5000 in browser
3. Let judges try the 3 questions
4. Show different scenarios and recommendations
5. Explain why comparison > single answer

## 🏆 Why This Project Wins

- ✅ **Solves Real Problem**: Model selection is genuinely difficult
- ✅ **Interactive & Beautiful**: Professional web interface
- ✅ **Smart Logic**: Considers user constraints
- ✅ **Easy to Demo**: Works immediately, no complex setup
- ✅ **Practical Value**: Actually helps developers

---

**Built for hackathon success! 🎯**
*Ready to impress judges with smart ML model selection.*
