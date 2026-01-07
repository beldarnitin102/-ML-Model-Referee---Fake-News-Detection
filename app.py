#!/usr/bin/env python3
"""
Simple Flask app for ML Model Referee
Perfect for hackathon showcase!
"""

from flask import Flask, render_template
import webbrowser
import threading
import time

app = Flask(__name__)

@app.route('/')
def index():
    """Main page with the interactive questionnaire"""
    return render_template('index.html')

def open_browser():
    """Open browser after a short delay"""
    time.sleep(1.5)
    webbrowser.open('http://localhost:5000')

if __name__ == '__main__':
    print("🚀 Starting ML Model Referee Web Interface...")
    print("📱 Opening in your browser at: http://localhost:5000")
    print("🎯 Perfect for your hackathon showcase!")
    print("\n" + "="*50)
    print("DEMO INSTRUCTIONS:")
    print("1. Answer the 3 questions on the web page")
    print("2. Get instant model recommendations")
    print("3. See detailed comparisons and trade-offs")
    print("4. Perfect for showing to judges!")
    print("="*50 + "\n")
    
    # Open browser automatically
    threading.Thread(target=open_browser).start()
    
    # Run Flask app
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)