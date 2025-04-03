import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import time
import pytz
from datetime import datetime

# ========== PAGE CONFIG ========== #
st.set_page_config(
    page_title="EcoWander Verification Portal",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ========== MODEL LOADING ========== #
@st.cache_resource
def load_model():
    return tf.keras.models.load_model('model.h5')  # Ensure model.h5 is available in the working directory

model = load_model()

# ========== IMAGE PROCESSING ========== #
def preprocess_image(image):
    img = image.resize((224, 224))  # Adjust based on your model's expected input
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

# ========== HEADER SECTION ========== #
st.markdown("""
    <div class="header">
        <div style="text-align: center;">
            <h1 style="font-size: 3rem; margin: 0;">🌿 EcoWander</h1>
            <p style="font-size: 1.5rem; opacity: 0.9;">AI-Powered Eco-Action Verification</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# ========== VERIFICATION DEMO ========== #
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("""
        <div style="margin-top: 2rem;">
            <h2>📱 How It Works</h2>
            <div class="feature-badge">1. User Takes Photo</div>
            <div class="feature-badge" style="margin: 1rem 0;">2. AI Verifies Authenticity</div>
            <div class="feature-badge">3. Earn EcoPoints</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"], label_visibility="collapsed")
    
    if uploaded_file:
        with st.spinner('🔍 Verifying eco-action...'):
            # Load and display the image preview
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image Preview", use_column_width=True)
            
            # Process and predict
            processed_img = preprocess_image(image)
            prediction = model.predict(processed_img)
            confidence = float(prediction[0][0]) * 100
            is_real = confidence > 50  # Assuming your model outputs a probability for real vs fake
            
            current_time = datetime.now(pytz.timezone('Asia/Tokyo')).strftime("%Y-%m-%d %H:%M:%S")
            
            # Simulate fraud detection results
            if is_real:
                scenario = "valid"
            else:
                scenario = np.random.choice(["ai_generated", "edited", "reused"], p=[0.5, 0.3, 0.2])
            
            responses = {
                "valid": {
                    "icon": "✅",
                    "title": "Eco-Action Verified!",
                    "color": "var(--primary)",
                    "analysis": "✅ Authentic photo detected",
                    "reason": "",
                    "points": True
                },
                "ai_generated": {
                    "icon": "❌",
                    "title": "Fraud Detected!",
                    "color": "var(--alert)",
                    "analysis": "❌ AI-generated content detected",
                    "reason": "Image shows signs of synthetic generation (unnatural textures)",
                    "points": False
                },
                "edited": {
                    "icon": "❌",
                    "title": "Fraud Detected!",
                    "color": "var(--alert)",
                    "analysis": "❌ Edited image detected",
                    "reason": "Digital manipulation found in background elements",
                    "points": False
                },
                "reused": {
                    "icon": "❌",
                    "title": "Fraud Detected!",
                    "color": "var(--alert)",
                    "analysis": "❌ Duplicate image detected",
                    "reason": "This photo was previously submitted",
                    "points": False
                }
            }
            
            result = responses[scenario]
            
            st.markdown(f"""
                <div class="verification-card {'fraud-alert' if not is_real else ''}" style="margin-top: 1rem;">
                    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem;">
                        <span style="font-size: 3rem;">{result['icon']}</span>
                        <div>
                            <h2 style="margin: 0; color: {result['color']}">
                                {result['title']}
                            </h2>
                            <p style="margin: 0;">{current_time} • Tokyo Station</p>
                        </div>
                    </div>
                    
                    <div style="display: flex; gap: 2rem; margin-bottom: 1.5rem;">
                        <div>
                            <h4 style="margin: 0;">Confidence Score</h4>
                            <p style="font-size: 1.5rem; margin: 0;">{confidence:.1f}%</p>
                        </div>
                        <div>
                            <h4 style="margin: 0;">AI Analysis</h4>
                            <p style="margin: 0;">{result['analysis']}</p>
                        </div>
                    </div>
                    
                    {f"<div class='fraud-reason'><strong>Reason:</strong> {result['reason']}</div>" if not is_real else ''}
                    
                    {"<div class='points-badge'>+50 EcoPoints</div>" if result['points'] else ''}
                </div>
            """, unsafe_allow_html=True)
