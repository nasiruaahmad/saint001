from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from PIL import Image
import io

app = Flask(__name__)

# Configure Google Gemini API
GOOGLE_API_KEY = "AIzaSyCHp9n4X24A3d3dgaW8o1ENgVtev2cxeBY"
genai.configure(api_key=GOOGLE_API_KEY)

# Set up the model
model = genai.GenerativeModel('gemini-pro')
vision_model = genai.GenerativeModel('gemini-1.5-flash-latest')

def is_agricultural_query(query):
    """Check if the query is related to agriculture using Gemini AI"""
    prompt = f"""Determine if this query is related to agriculture, farming, livestock, crops, weather in farming context, or agricultural market analysis. 
    Only respond with 'yes' or 'no'.
    Query: {query}"""
    
    response = model.generate_content(prompt)
    return response.text.strip().lower() == 'yes'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    try:
        question = request.form.get('question')
        
        # First, verify if the question is agriculture-related
        if not is_agricultural_query(question):
            return jsonify({
                'error': 'Please ask questions related to agriculture, farming, livestock, crops, weather, or agricultural market analysis only.'
            }), 400

        # Create a context-aware prompt
        prompt = f"""As an AI agricultural expert, please provide a detailed response to this farming-related question. 
        If applicable, include practical advice and best practices.
        Question: {question}"""

        response = model.generate_content(prompt)
        return jsonify({'response': response.text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/analyze-image', methods=['POST'])
def analyze_image():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image uploaded'}), 400

        image_file = request.files['image']
        if image_file.filename == '':
            return jsonify({'error': 'No image selected'}), 400

        # Read and process the image
        img_bytes = image_file.read()
        img = Image.open(io.BytesIO(img_bytes))

        prompt = """Analyze this crop/plant image and provide:
        1. Identification of the crop/plant
        2. Assessment of plant health
        3. Identification of any visible issues (diseases, pests, nutrient deficiencies)
        4. Recommended treatments or solutions if problems are detected
        5. General care advice
        Be specific and practical in your recommendations."""

        response = vision_model.generate_content([prompt, img])
        return jsonify({'response': response.text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
