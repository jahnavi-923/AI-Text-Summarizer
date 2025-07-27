# app.py

from flask import Flask, render_template, request
from src.summarizer import summarize_text

app = Flask(__name__)

# New: Create a list to store history. This list will be in memory.
summary_history = []

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    if request.method == 'POST':
        article_text = request.form['article']
        if article_text: # Ensure the text is not empty
            results = summarize_text(article_text)
            # New: Add the new result to the beginning of our history list.
            summary_history.insert(0, results)
        
    # Pass the current results and the entire history to the template
    return render_template('index.html', results=results, history=summary_history)

if __name__ == '__main__':
    app.run(debug=True)