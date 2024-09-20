# streamlit_app.py
pip install joblib
import streamlit as st
import numpy as np
import joblib
import pandas as pd
import base64
import os


# Load the trained model
model = joblib.load('titanic_survival_model.pkl')

# Function to make a prediction based on user input
def predict_survival(pclass, sex, age, sibsp, parch, fare, embarked):
    input_data = np.array([[pclass, sex, age, sibsp, parch, fare, embarked]])
    prediction = model.predict(input_data)
    return prediction

# Function to Encode Local Image
# Function to get the base and decode the image
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
# Function to use CSS and set the background to be png_file
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)


# Function to explain why the person may not have survived
def explain_death(pclass, sex, age):
    explanation = ""
    if pclass == 3 and age > 50:
        explanation = "You were in 3rd class and older than 50, which had a lower survival rate."
    elif sex == 0 and pclass == 3:
        explanation = "Being a male in 3rd class greatly reduced your chances of survival."
    elif age < 12:
        explanation = "Even though children had a higher chance of survival, other factors might have played a role."
    else:
        explanation = "The combination of your class, age, and other factors may have affected your survival."
    return explanation



# Title and description
st.title("🚢 Titanic Survival Prediction Game")
st.write("""
         Can you survive the Titanic? Enter your details below and find out!
         """)

# Set background image
set_background('images/background_image.jpg')

# Collect user input
pclass = st.selectbox('Passenger Class (Pclass)', options=[1, 2, 3], index=0)
sex = st.selectbox('Gender', options=['Male', 'Female'], index=0)
age = st.slider('Age', min_value=0, max_value=100, value=30)
sibsp = st.number_input('Number of Siblings/Spouses aboard (SibSp)', min_value=0, max_value=10, value=0)
parch = st.number_input('Number of Parents/Children aboard (Parch)', min_value=0, max_value=10, value=0)
fare = st.slider('Fare', min_value=0.0, max_value=500.0, value=50.0)
embarked = st.selectbox('Port of Embarkation', options=['Southampton', 'Cherbourg', 'Queenstown'], index=0)

# Convert user input to model-compatible form
sex = 0 if sex == 'Male' else 1  # Male = 0, Female = 1
embarked_dict = {'Southampton': 2, 'Cherbourg': 0, 'Queenstown': 1}
embarked = embarked_dict[embarked]

# Predict button
if st.button('Will you survive?'):
    prediction = predict_survival(pclass, sex, age, sibsp, parch, fare, embarked)

    # Path to images folder
    image_folder = os.path.join(os.getcwd(), "images")
    
    if prediction[0] == 1:
        st.success("🎉 Congratulations! You survived!")
        # survival_image_path = os.path.join(image_folder, "happy.png")  # Replace with your local image name
        st.image("images/happy.png", caption="You made it!", width=200)
    else:
        st.error("😔 Sorry, you did not survive. Try again!")
        # death_image_path = os.path.join(image_folder, "sad.png")  # Replace with your local image name
        st.image("images/sad.png", caption="You did not make it.", width=200)
        
        # Provide an explanation
        explanation = explain_death(pclass, sex, age)
        st.write(f"**Reason:** {explanation}")

# Interactivity
st.write("#### Want to try different scenarios? Adjust the sliders and try again!")

# Footer
st.markdown("""
---
Made by KeeObom.
""")
