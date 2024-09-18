
# 🚢 Titanic Survival Prediction Game

Can you survive the Titanic disaster? This interactive game allows you to enter your details and predict whether you would have survived or not. Based on the classic Titanic dataset, this app uses a trained machine learning model to make the prediction.

---

## 🎮 How to Play

Simply enter your information, such as:
- Passenger Class (Pclass)
- Gender
- Age
- Number of Siblings/Spouses aboard
- Number of Parents/Children aboard
- Fare
- Port of Embarkation

Click **"Will you survive?"** to find out your fate!

- If you survive, 🎉 congratulations will follow!
- If not, 😔 you'll see a reason why and an appropriate image.

---

## 💻 Features

- **Interactive UI**: Enter inputs and get real-time predictions.
- **Fun Design**: Engaging visuals and a background image that sets the mood.
- **Model-based Predictions**: Uses a pre-trained machine learning model to predict survival chances.
- **Feedback & Explanations**: Get personalized feedback on why you may not have survived based on historical trends.

---

## 📂 Project Structure

```
├── images
│   ├── background_image.jpg    # Background image for the app
│   ├── happy.png               # Image displayed on survival
│   ├── sad.png                 # Image displayed on non-survival
├── titanic_survival_model.pkl   # Trained ML model file
├── streamlit_app.py             # Main app file
└── README.md                    # This file
```

---

## 🚀 Getting Started

To run this app locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/titanic-survival-prediction.git
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run streamlit_app.py
    ```

4. Visit `http://localhost:8501` in your browser to start interacting with the app.

---

## 🛠 Dependencies

- **Streamlit**: For building the interactive web app
- **Joblib**: For loading the pre-trained ML model
- **Scikit-learn**: For the machine learning model
- **Pandas**: For data handling
- **Numpy**: For numerical operations

Install all dependencies by running:
```bash
pip install -r requirements.txt
```

---

## 📊 The Model

The model is trained on the famous [Titanic dataset](https://www.kaggle.com/c/titanic/data) using a classification algorithm. The features used for prediction include:
- Passenger Class
- Gender
- Age
- Number of Siblings/Spouses
- Number of Parents/Children
- Fare
- Port of Embarkation

The trained model is saved as `titanic_survival_model.pkl`.

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

Made by **KeeObom**.
