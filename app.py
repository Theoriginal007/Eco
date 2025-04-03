import streamlit as st
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

# ========== CSS STYLING ========== #
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
        
        :root {
            --primary: #2E8B57;
            --accent: #FFD700;
            --alert: #FF6B6B;
        }
        
        body {
            font-family: 'Inter', sans-serif;
            background: #F5FFFA;
        }
        
        .header {
            background: linear-gradient(135deg, var(--primary) 0%, #3CB371 100%);
            color: white;
            padding: 3rem;
            border-radius: 0 0 30px 30px;
            box-shadow: 0 10px 30px rgba(46, 139, 87, 0.2);
        }
        
        .verification-card {
            background: white;
            border-radius: 20px;
            padding: 2.5rem;
            box-shadow: 0 15px 40px rgba(46, 139, 87, 0.1);
            border-left: 8px solid var(--primary);
            transition: transform 0.3s;
        }
        
        .verification-card:hover {
            transform: translateY(-5px);
        }
        
        .feature-badge {
            background: rgba(46, 139, 87, 0.1);
            border-radius: 50px;
            padding: 0.8rem 1.5rem;
            font-weight: 600;
        }
        
        .points-badge {
            background: var(--accent);
            color: #333;
            border-radius: 50px;
            padding: 0.5rem 1.5rem;
            font-weight: 800;
            display: inline-block;
            box-shadow: 0 4px 15px rgba(255, 215, 0, 0.3);
        }
        
        .fraud-alert {
            border-left: 8px solid var(--alert) !important;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(255, 107, 107, 0.4); }
            70% { box-shadow: 0 0 0 15px rgba(255, 107, 107, 0); }
            100% { box-shadow: 0 0 0 0 rgba(255, 107, 107, 0); }
        }
        
        .metric-box {
            background: white;
            border-radius: 15px;
            padding: 1.5rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05);
            color: #333 !important; /* Force dark text */
        }
        
        .metric-box h3 {
            color: var(--primary) !important;
        }
        
        .section-title {
            color: #2E8B57;
            margin-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

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
            
            <div style="margin-top: 3rem;">
                <h3>📍 Current Location</h3>
                <p>Tokyo Station (Verified Eco-Spot)</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"], label_visibility="collapsed")
    
    if uploaded_file:
        with st.spinner('🔍 Verifying eco-action...'):
            time.sleep(2)
            
            # Simulate verification
            verification_result = np.random.choice(["success", "fraud"], p=[0.9, 0.1])
            confidence = np.random.randint(85, 98)
            current_time = datetime.now(pytz.timezone('Asia/Tokyo')).strftime("%Y-%m-%d %H:%M:%S")
            
            st.markdown(f"""
                <div class="verification-card {'fraud-alert' if verification_result == 'fraud' else ''}" style="margin-top: 1rem;">
                    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem;">
                        <span style="font-size: 3rem;">{'✅' if verification_result == 'success' else '❌'}</span>
                        <div>
                            <h2 style="margin: 0; color: {'var(--primary)' if verification_result == 'success' else 'var(--alert)'}">
                                {'Eco-Action Verified!' if verification_result == 'success' else 'Potential Fraud Detected'}
                            </h2>
                            <p style="margin: 0;">{current_time} • Tokyo Station</p>
                        </div>
                    </div>
                    
                    <img src="{uploaded_file}" style="width: 100%; border-radius: 10px; margin-bottom: 1.5rem;">
                    
                    <div style="display: flex; gap: 2rem; margin-bottom: 1.5rem;">
                        <div>
                            <h4 style="margin: 0;">Confidence Score</h4>
                            <p style="font-size: 1.5rem; margin: 0;">{confidence}%</p>
                        </div>
                        <div>
                            <h4 style="margin: 0;">AI Analysis</h4>
                            <p style="margin: 0;">{'✅ Real recycling bin detected' if verification_result == 'success' else '❌ Edited image suspected'}</p>
                        </div>
                    </div>
                    
                    {'<div class="points-badge">+50 EcoPoints</div>' if verification_result == 'success' else ''}
                </div>
            """, unsafe_allow_html=True)

# ========== METRICS DASHBOARD ========== #
st.markdown("""
    <div style="margin: 3rem 0;">
        <h2 class="section-title">📊 Pilot Metrics</h2>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.5rem; margin-top: 1.5rem;">
            <div class="metric-box">
                <h3>12,489</h3>
                <p>Verified Actions</p>
            </div>
            <div class="metric-box">
                <h3>92%</h3>
                <p>Accuracy Rate</p>
            </div>
            <div class="metric-box">
                <h3>1,203</h3>
                <p>Fraud Attempts Blocked</p>
            </div>
            <div class="metric-box">
                <h3>62%</h3>
                <p>User Engagement Increase</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# ========== TECHNOLOGY SHOWCASE ========== #
st.markdown("""
    <div style="margin: 3rem 0;">
        <h2 class="section-title">🛡️ Triple-Layer Verification</h2>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; margin-top: 1.5rem;">
            <div class="metric-box">
                <h3>📸 AI Vision</h3>
                <p>TensorFlow Lite model detects real bins with 90%+ accuracy</p>
            </div>
            <div class="metric-box">
                <h3>📍 Location Lock</h3>
                <p>GPS confirms presence at 50,000+ verified eco-spots</p>
            </div>
            <div class="metric-box">
                <h3>⏱️ Time Seal</h3>
                <p>Blockchain-style hashing prevents photo reuse</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# ========== FOOTER ========== #
st.markdown("""
    <div style="text-align: center; margin-top: 3rem; color: #666; padding: 2rem 0;">
        <p>© 2023 EcoWander | Aligned with Japan's 2050 Carbon Neutrality Goals</p>
    </div>
""", unsafe_allow_html=True)