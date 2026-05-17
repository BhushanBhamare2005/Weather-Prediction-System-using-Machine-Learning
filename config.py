# Configuration file for Weather Prediction ML Project

## Project Settings
PROJECT_NAME = "Weather Prediction System"
PROJECT_VERSION = "1.0.0"
AUTHOR = "Your Name"
EMAIL = "your.email@example.com"

## Model Settings
MODEL_NAME = "weather_model.pkl"
FEATURE_FILE = "feature_columns.pkl"
DATASET_PATH = "seattle-weather.csv"

## Model Parameters
RANDOM_STATE = 42
TEST_SIZE = 0.2
STRATIFY = True

# Random Forest Parameters
RANDOM_FOREST_N_ESTIMATORS = 100
RANDOM_FOREST_MAX_DEPTH = 10

# Decision Tree Parameters
DECISION_TREE_MAX_DEPTH = 10

# Logistic Regression Parameters
LOGISTIC_REGRESSION_MAX_ITER = 1000

## Features
FEATURE_COLUMNS = ['temp_max', 'temp_min', 'precipitation']
TARGET_COLUMN = 'RainTomorrow'

## Streamlit App Settings
STREAMLIT_PAGE_TITLE = "Weather Prediction System"
STREAMLIT_PAGE_ICON = "🌤️"
STREAMLIT_LAYOUT = "wide"

## Expected Model Performance
EXPECTED_ACCURACY = 0.91  # 91%
MIN_ACCEPTABLE_ACCURACY = 0.85  # 85%

## Data Information
DATASET_SIZE = 1461
TRAIN_SIZE = 1168  # 80% of dataset
TEST_SIZE_SAMPLES = 293  # 20% of dataset

## Feature Ranges (for validation)
TEMP_MAX_MIN = -50.0
TEMP_MAX_MAX = 60.0
TEMP_MIN_MIN = -50.0
TEMP_MIN_MAX = 60.0
PRECIPITATION_MIN = 0.0
PRECIPITATION_MAX = 500.0
