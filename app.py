import streamlit as st
import pandas as pd
import datetime
from PIL import Image
import os

import database as db
import ai_engine as ai
import utils

st.set_page_config(page_title="AI Food & Fitness Tracker", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Upload Meal", "Log Steps", "Dashboard", "Meal History"], index=2)

today = datetime.date.today().strftime("%Y-%m-%d")

if page == "Dashboard":
    st.title("Daily Dashboard 📊")
    st.write(f"**Date:** {today}")
    
    meals_today = db.get_meals_by_date(today)
    steps_today = db.get_steps(today)
    
    total_calories_in = sum(m['calories'] for m in meals_today)
    total_protein = sum(m['protein'] for m in meals_today)
    total_carbs = sum(m['carbs'] for m in meals_today)
    total_fat = sum(m['fat'] for m in meals_today)
    
    calories_burned = utils.calculate_calories_burned(steps_today)
    net_calories = total_calories_in - calories_burned
    
    # 1. Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Calories Consumed", f"{total_calories_in:.0f} kcal")
    col2.metric("Calories Burned", f"{calories_burned:.0f} kcal", f"{steps_today} steps")
    col3.metric("Net Calories", f"{net_calories:.0f} kcal")
    
    st.markdown("---")
    
    col4, col5, col6 = st.columns(3)
    col4.metric("Protein Intake", f"{total_protein:.0f} g")
    col5.metric("Carbs Intake", f"{total_carbs:.0f} g")
    col6.metric("Fat Intake", f"{total_fat:.0f} g")
    
    st.markdown("---")
    
    # 2. Charts
    if meals_today:
        st.subheader("Macronutrients Breakdown")
        macro_data = pd.DataFrame({
            'Macro': ['Protein', 'Carbs', 'Fat'],
            'Grams': [total_protein, total_carbs, total_fat]
        })
        st.bar_chart(macro_data.set_index('Macro'))
    else:
        st.info("No meals logged today. Upload a meal to see your macros!")
    
    # 3. Meals Eaten Today
    st.subheader("Meals Eaten Today")
    if meals_today:
        df_meals = pd.DataFrame(meals_today)
        st.dataframe(df_meals[['food_item', 'calories', 'protein', 'carbs', 'fat']])
        
        st.subheader("Food Images History")
        cols = st.columns(4)
        for idx, meal in enumerate(meals_today):
            if meal['image_filename']:
                img_path = utils.get_image_path(meal['image_filename'])
                if os.path.exists(img_path):
                    try:
                        img = Image.open(img_path)
                        cols[idx % 4].image(img, caption=meal['food_item'], use_container_width=True)
                    except Exception as e:
                        pass
    else:
        st.write("No meals to display.")

elif page == "Upload Meal":
    st.title("Upload Meal 📸")
    st.write("Take a picture of your food to automatically detect items and estimate nutrition.")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
        
        if st.button("Analyze Food"):
            with st.spinner("Analyzing with Gemini AI..."):
                filename, filepath = utils.save_uploaded_image(uploaded_file)
                
                # Analyze image
                result = ai.analyze_food_image(filepath)
                
                if result and "foods" in result:
                    st.success("Analysis Complete!")
                    st.subheader("Detected Foods")
                    
                    df_foods = pd.DataFrame(result["foods"])
                    st.dataframe(df_foods)
                    
                    # Log to database
                    for food in result["foods"]:
                        db.add_meal(
                            date=today,
                            food_item=food["name"],
                            calories=food["calories"],
                            protein=food["protein"],
                            carbs=food["carbs"],
                            fat=food["fat"],
                            image_filename=filename
                        )
                    st.info("Meals successfully logged to your daily dashboard!")
                else:
                    st.error("Failed to analyze image. Please ensure your Gemini API key is valid and the image is clear.")

elif page == "Log Steps":
    st.title("Log Daily Steps 🚶‍♂️")
    st.write("Track your activity to calculate calories burned.")
    
    current_steps = db.get_steps(today)
    steps = st.number_input("Enter number of steps walked today", min_value=0, value=current_steps, step=100)
    
    if st.button("Save Steps"):
        db.log_steps(today, steps)
        calories_burned = utils.calculate_calories_burned(steps)
        st.success(f"Successfully logged {steps} steps! (Estimated {calories_burned:.0f} kcal burned)")

elif page == "Meal History":
    st.title("Meal History 🗓️")
    st.write("All your logged meals across all days.")
    
    all_meals = db.get_all_meals()
    if all_meals:
        df_all = pd.DataFrame(all_meals)
        st.dataframe(df_all[['date', 'food_item', 'calories', 'protein', 'carbs', 'fat']])
    else:
        st.info("No meals logged yet.")
