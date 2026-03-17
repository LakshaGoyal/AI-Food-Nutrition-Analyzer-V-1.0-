# AI Food & Fitness Tracker

An MVP application using Python, Streamlit, and Google Gemini Vision API to track meals, estimate calories, and monitor daily steps.

## Features
- Upload food images for automatic nutrition estimation (Calories, Protein, Carbs, Fat)
- Log daily steps to estimate calories burned
- View meal history and daily dashboard

## Project Structure
```
ai_food_tracker/
├── app.py
├── ai_engine.py
├── database.py
├── utils.py
├── requirements.txt
├── .env.example
├── README.md
├── data/
│   └── meals.db
└── uploads/
    └── food_images/
```

## Installation

1. Extract this repository.
2. Navigate to the project directory:
   ```bash
   cd ai_food_tracker
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and configure your API key:
   ```bash
   cp .env.example .env
   # Or manually rename .env.example to .env and edit it
   ```
   Add your `GEMINI_API_KEY` to the `.env` file. You can obtain a free API key from [Google AI Studio](https://aistudio.google.com/).

## How to Run

Start the Streamlit application:
```bash
streamlit run app.py
```

## Screenshots
*Placeholder for app screenshots*
