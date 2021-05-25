from flask import Blueprint, render_template, request, redirect
from .generator import ai

generator = Blueprint('generator', __name__)

@generator.route('/')
def index():
    # 18. Now add route index 
    return render_template('index.html')

@generator.route('/analyze', methods=['POST'])
def analyze():
    # 7. Explain the render template and import and also how it finds the index
    # 8. Also explain how we need to create a template now
    title = request.form['title']
    text = ai.generate_text(title)

    return render_template('index.html', text=text)