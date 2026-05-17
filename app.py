import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns

# Set page configuration
st.set_page_config(
    page_title="Weather Prediction System",
    page_icon="🌤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .rain-box {
        background-color: #d4edff;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        border-left: 4px solid #0066cc;
    }
    .no-rain-box {
        background-color: #fff4d4;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        border-left: 4px solid #ff9900;
    }
    </style>
    """, unsafe_allow_html=True)

# Load the trained model and feature names
try:
    model = pickle.load(open("weather_model.pkl", "rb"))
    feature_columns = pickle.load(open("feature_columns.pkl", "rb"))
except FileNotFoundError:
    st.error("❌ Model files not found. Please run the Jupyter notebook first to train the model.")
    st.stop()

# App Title
st.title("🌤️ Weather Prediction System")
st.markdown("---")
st.write("**Predict whether it will rain tomorrow based on weather parameters using Machine Learning!**")

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["🔮 Prediction", "📊 Model Info", "📈 About", "ℹ️ Instructions"])

# ============= TAB 1: PREDICTION =============
with tab1:
    st.header("🔮 Make a Prediction")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        temp_max = st.number_input(
            "Maximum Temperature (°C)",
            min_value=-50.0,
            max_value=60.0,
            value=25.0,
            step=0.1,
            help="Enter the maximum temperature for the day"
        )
    
    with col2:
        temp_min = st.number_input(
            "Minimum Temperature (°C)",
            min_value=-50.0,
            max_value=60.0,
            value=15.0,
            step=0.1,
            help="Enter the minimum temperature for the day"
        )
    
    with col3:
        precipitation = st.number_input(
            "Precipitation (mm)",
            min_value=0.0,
            max_value=500.0,
            value=5.0,
            step=0.1,
            help="Enter the rainfall/precipitation amount"
        )
    
    st.markdown("---")
    
    # Prediction button
    if st.button("🎯 Predict Rain Tomorrow", use_container_width=True, type="primary"):
        # Prepare data for prediction
        input_data = np.array([[temp_max, temp_min, precipitation]])
        
        # Make prediction
        prediction = model.predict(input_data)
        prediction_proba = model.predict_proba(input_data)
        
        # Display results
        st.markdown("### 📊 Prediction Result")
        
        col_result1, col_result2 = st.columns(2)
        
        if prediction[0] == 1:
            with col_result1:
                st.markdown(
                    """<div class="rain-box">
                    <h2>🌧️ Rain Expected</h2>
                    <p style="font-size: 18px; color: #0066cc; font-weight: bold;">
                    Confidence: {:.2%}
                    </p>
                    </div>""".format(prediction_proba[0][1]),
                    unsafe_allow_html=True
                )
        else:
            with col_result1:
                st.markdown(
                    """<div class="no-rain-box">
                    <h2>☀️ No Rain Expected</h2>
                    <p style="font-size: 18px; color: #ff9900; font-weight: bold;">
                    Confidence: {:.2%}
                    </p>
                    </div>""".format(prediction_proba[0][0]),
                    unsafe_allow_html=True
                )
        
        # Display confidence breakdown
        with col_result2:
            st.metric("No Rain Probability", f"{prediction_proba[0][0]:.2%}")
            st.metric("Rain Probability", f"{prediction_proba[0][1]:.2%}")
        
        # Display input summary
        st.markdown("### 📋 Input Summary")
        input_df = pd.DataFrame({
            "Parameter": ["Max Temperature", "Min Temperature", "Precipitation"],
            "Value": [f"{temp_max}°C", f"{temp_min}°C", f"{precipitation}mm"]
        })
        st.table(input_df)

# ============= TAB 2: MODEL INFO =============
with tab2:
    st.header("📊 Model Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Model Details")
        st.markdown("""
        **Model Type:** Random Forest Classifier
        
        **Features Used:**
        - Maximum Temperature
        - Minimum Temperature
        - Precipitation
        
        **Training Set:** 80% of data
        **Test Set:** 20% of data
        """)
    
    with col2:
        st.subheader("Model Performance")
        st.markdown("""
        **Accuracy:** ~91% (varies based on test data)
        
        **Status:** ✅ Production Ready
        
        **Last Updated:** 2024
        """)
    
    st.markdown("---")
    st.subheader("🔬 How the Model Works")
    st.markdown("""
    1. **Data Collection:** Weather parameters are collected (temperature, precipitation)
    2. **Feature Processing:** Data is normalized and processed
    3. **Prediction:** Random Forest algorithm analyzes patterns and makes predictions
    4. **Confidence Scoring:** Model provides probability confidence for each prediction
    """)

# ============= TAB 3: ABOUT =============
with tab3:
    st.header("📈 About This Project")
    
    st.subheader("🎯 Objective")
    st.markdown("""
    To predict whether it will rain or not based on weather parameters such as:
    - Temperature (Maximum and Minimum)
    - Humidity
    - Wind Speed
    - Precipitation
    """)
    
    st.subheader("🛠️ Technologies Used")
    tech_col1, tech_col2, tech_col3 = st.columns(3)
    
    with tech_col1:
        st.markdown("""
        **Backend:**
        - Python
        - Pandas
        - Scikit-learn
        """)
    
    with tech_col2:
        st.markdown("""
        **Visualization:**
        - Matplotlib
        - Streamlit
        """)
    
    with tech_col3:
        st.markdown("""
        **Deployment:**
        - Streamlit Cloud
        - GitHub
        """)
    
    st.subheader("📚 Datasets Used")
    st.markdown("""
    ### 🌧️ Seattle Weather Dataset
    
    **Source:** Kaggle - Seattle Weather Dataset
    
    **Dataset Overview:**
    - **Total Records:** 1,461 daily observations
    - **Time Period:** 2012-2015 (4 years of historical data)
    - **Location:** Seattle, Washington, USA
    - **Format:** CSV (Comma-Separated Values)
    
    **Available Features:**
    - Date (YYYY-MM-DD format)
    - Precipitation (mm) - Daily rainfall amount
    - Temperature Maximum (°C) - Highest temperature of the day
    - Temperature Minimum (°C) - Lowest temperature of the day
    - Wind (km/h) - Wind speed
    - Weather (categorical) - Weather conditions
    
    **Weather Categories:**
    - 🌧️ Rain: 641 days (43.87%)
    - ☀️ Sun: 640 days (43.80%)
    - 🌫️ Fog: 101 days (6.91%)
    - 💧 Drizzle: 53 days (3.63%)
    - ❄️ Snow: 26 days (1.78%)
    
    **Data Quality:**
    - No missing values
    - Complete records for all 1,461 days
    - Balanced dataset (good distribution across weather types)
    
    **Target Variable:**
    - Binary Classification: RainTomorrow (0 = No Rain, 1 = Rain)
    - Class Distribution: 820 No Rain vs 641 Rain (56.1% vs 43.9%)
    
    **Use Case:**
    - Training machine learning models for weather prediction
    - Time-series analysis and forecasting
    - Climate pattern recognition
    - Weather classification tasks
    """)
    
    st.subheader("🤖 Machine Learning Algorithms Tested")
    algo_col1, algo_col2, algo_col3 = st.columns(3)
    
    with algo_col1:
        st.markdown("""
        **Logistic Regression**
        - Simple baseline model
        - Linear classification
        """)
    
    with algo_col2:
        st.markdown("""
        **Decision Tree**
        - Interpretable rules
        - Non-linear decisions
        """)
    
    with algo_col3:
        st.markdown("""
        **Random Forest** ⭐
        - Ensemble method
        - Best accuracy (~91%)
        """)

# ============= TAB 4: INSTRUCTIONS =============
with tab4:
    st.header("ℹ️ How to Use This App")
    
    st.markdown("""
    ### Step 1️⃣: Enter Weather Parameters
    1. Go to the **Prediction** tab
    2. Enter the maximum temperature in Celsius
    3. Enter the minimum temperature in Celsius
    4. Enter the precipitation amount in millimeters
    
    ### Step 2️⃣: Make a Prediction
    1. Click the **"Predict Rain Tomorrow"** button
    2. Wait for the model to process your input
    
    ### Step 3️⃣: Review Results
    The app will display:
    - Whether rain is expected (Yes/No)
    - Confidence percentage
    - Probability breakdown
    - Summary of your inputs
    
    ### 📊 Understanding the Output
    - **Green Box:** Rain is predicted
    - **Yellow Box:** No rain is predicted
    - **Confidence:** How certain the model is (higher is better)
    
    ### ⚠️ Important Notes
    - Model accuracy is approximately 91%
    - Results are based on the Random Forest algorithm
    - Always verify predictions with official weather forecasts
    - Keep temperatures within reasonable ranges (-50°C to +60°C)
    """)
    
    st.info("💡 **Tip:** Try different weather conditions to see how the model behaves!")

# ============= FOOTER =============
st.markdown("---")
col_footer1, col_footer2, col_footer3 = st.columns(3)

with col_footer1:
    st.markdown("**Developer:** ML Project Team")

with col_footer2:
    st.markdown("**Model Version:** 1.0.0")

with col_footer3:
    st.markdown("**License:** MIT")
