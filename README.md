# 🍽️ AI Food Nutrition Analyzer

An AI-powered food analysis application that allows users to upload images of their meals and get detailed nutritional insights including calories, macronutrients, and daily health tracking.

---

## 🚀 Features

* 📸 Upload food images (supports complex plates)
* 🤖 AI-based food detection using Google Gemini Vision
* 🧾 Nutrition analysis (calories, protein, fat, carbs)
* 📊 Daily dashboard with:

  * Total calories consumed
  * Calories burned (via steps)
  * Net calorie balance
  * Macronutrient breakdown
* 🗂️ Meal logging with timestamps
* ⚡ Fast and interactive UI using Streamlit

---

## 🧠 How It Works

```text
User uploads image
        ↓
Gemini Vision API detects food items
        ↓
Nutrition API calculates calories & macros
        ↓
Data stored in database
        ↓
Dashboard displays daily analytics
```

---

## 🛠️ Tech Stack

* **Frontend/UI:** Streamlit
* **Backend:** Python
* **AI Model:** Google Gemini Vision API
* **Nutrition API:** Edamam / USDA
* **Database:** CSV / SQLite
* **Libraries:** pandas, requests, Pillow

---

## 📂 Project Structure

```
ai_food_tracker/
│
├── app.py              # Main Streamlit app
├── ai_engine.py        # AI food detection logic (Gemini)
├── utils.py            # Nutrition + helper functions
├── database.py         # Meal storage & retrieval
├── data/               # Database files
├── uploads/            # Uploaded images
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/ai-food-tracker.git
cd ai-food-tracker
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Set environment variables

Create a `.env` file in the root directory and add:

```env
GEMINI_API_KEY=your_gemini_api_key
EDAMAM_APP_ID=your_app_id
EDAMAM_APP_KEY=your_app_key
```

---

### 4️⃣ Run the application

```bash
streamlit run app.py
```

---

## 📊 Example Output

* Detected foods: *rice, grilled chicken, salad*
* Calories: **520 kcal**
* Protein: **32g**
* Fat: **18g**
* Carbs: **55g**

Dashboard shows:

* Total calories consumed
* Calories burned (steps × 0.04)
* Net calorie balance
* Macronutrient chart

---

## 🧪 Sample Use Case

1. Upload your meal image
2. App detects food items using AI
3. Nutrition is calculated automatically
4. View your daily health summary

---

## ⚠️ Limitations

* Accuracy depends on image quality
* Nutrition values are approximate
* Requires internet for AI inference (Gemini API)

---

## 🔮 Future Improvements

* 🔍 Multi-food detection with bounding boxes (YOLO)
* 📱 Mobile app (Flutter / React Native)
* 🧠 AI diet recommendations
* 📅 Weekly & monthly analytics
* 🧑‍⚕️ Health scoring system

---

## 🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## ⭐ Acknowledgements

* Google Gemini API
* Edamam Nutrition API
* Streamlit

---

## 💡 Author

Built with ❤️ as an AI-powered health tracking project.
