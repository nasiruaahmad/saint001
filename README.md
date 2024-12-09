# AI Farmer Assistant

An AI-powered agricultural assistant platform that helps farmers optimize their operations through intelligent insights and recommendations.

## Features

- Agricultural Q&A system
- Crop image analysis
- Disease detection and treatment suggestions
- Weather and market analysis
- Real-time farming insights

## Setup Instructions

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your web browser and navigate to `http://localhost:5000`

## Usage

### Ask Questions
- Enter your agriculture-related questions in the text area
- Click "Ask Question" to get expert answers
- Questions are limited to agriculture, livestock, crops, weather, and market analysis

### Analyze Crops
- Upload an image of your crop or plant
- Click "Analyze Image" to get:
  - Crop identification
  - Health assessment
  - Disease detection
  - Treatment recommendations
  - Care advice

## Technical Details

- Backend: Flask (Python)
- AI: Google Gemini API
- Frontend: HTML, CSS (Bootstrap), JavaScript
- Image Processing: PIL (Python Imaging Library)

## Security Note

The API key in the code should be moved to an environment variable in a production environment.
