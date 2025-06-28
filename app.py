
import streamlit as st
import pickle
import pandas as pd

# Load model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)
    


# Set page config with background
st.set_page_config(page_title="Personality Predictor", layout="centered")
# Custom CSS for background image
st.markdown("""
    <style>
    .stApp {
        background-image: url("");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 Personality Prediction App")
st.markdown("🚀 This app uses a Machine Learning model to analyze your social behavior and predict whether you're an Extrovert or an Introvert.")

# --- Input Section ---
col1, col2 = st.columns(2)

with col1:
    Time_spent_Alone= st.slider("🕒 Time Spent Alone (1-24) in Hours", 0, 24, 5)
    Social_event_attendance= st.slider("🎉 How Many Social Event You Attended Recently (1-15)", 0, 15, 5)
    Friends_circle_size = st.slider("👥 Friends Circle Size", 0, 5, 50)
    Post_frequency = st.slider("📱 How Much Post You Upload On Social Media Recently", 0, 20, 5)

with col2:
    Going_outside = st.slider("🚶 Going Outside (1-10)", 0, 10, 5)
    Stage_fear = st.selectbox("🎤 Do you have stage fear?", ["Yes", "No"])
    Drained_after_socializing = st.selectbox("😩 Do social events make you feel exhausted?", ["Yes", "No"])

# Encode categorical inputs
stage_fear_encoded = 1 if Stage_fear == "Yes" else 0
drained_encoded = 1 if Drained_after_socializing == "Yes" else 0
# --- Predict ---

    # Extrovert Case
if st.button("🔍 Predict Personality"):
    # Prepare input DataFrame
    data = pd.DataFrame([{
        "Time_spent_Alone": Time_spent_Alone,
        "Stage_fear": stage_fear_encoded,
        "Social_event_attendance": Social_event_attendance,
        "Going_outside": Going_outside,
        "Drained_after_socializing": drained_encoded,
        "Friends_circle_size": Friends_circle_size,
        "Post_frequency": Post_frequency
    }])

    # Make prediction
    prediction = model.predict(data)

    # 🎉 Extrovert Case
    if prediction[0] == 0 or prediction[0] == "Extrovert":
        # st.success("✅ You are likely an **Extrovert** 🎉")
        st.markdown("""
<div style='
    background-color: #d4edda;
    color: #155724;
    padding: 20px;
    border-radius: 10px;
    font-size: 32px;
    font-weight: bold;
    text-align: center;
    line-height: 1.6;
'>
✅ You are likely an <strong>Extrovert</strong> 🎉
</div>
""", unsafe_allow_html=True)

        st.balloons()

        st.markdown("""
        <div style='text-align: center;'>
            <style>
            .float-up {
                animation: floatUp 2s ease-in-out forwards;
                font-size: 40px;
                position: relative;
            }

            @keyframes floatUp {
                0% { bottom: -50px; opacity: 0; }
                50% { bottom: 0px; opacity: 1; }
                100% { bottom: 50px; opacity: 0; }
            }
            </style>
            <div class="float-up">🎉😎✨🎊🕺</div>
        </div>
        """, unsafe_allow_html=True)

    # 😌 Introvert Case
    else:
        # st.warning("🔕 You are likely an **Introvert** 😌")
        st.markdown("""
<div style='
    background-color: #f8f9fa;
    color: #343a40;
    padding: 20px;
    border-radius: 10px;
    font-size: 32px;
    font-weight: bold;
    text-align: center;
    line-height: 1.6;
'>
🔕 You are likely an <strong>Introvert</strong> 😌
</div>
""", unsafe_allow_html=True)

        st.snow()

        st.markdown("""
        <div style='text-align: center;'>
            <style>
            .float-up-slow {
                animation: floatSlow 3s ease-in-out forwards;
                font-size: 40px;
                position: relative;
            }

            @keyframes floatSlow {
                0% { bottom: -30px; opacity: 0; }
                50% { bottom: 0px; opacity: 1; }
                100% { bottom: 30px; opacity: 0; }
            }
            </style>
            <div class="float-up-slow">💭🧘‍♂️😶‍🌫️🌙</div>
        </div>
        """, unsafe_allow_html=True)
