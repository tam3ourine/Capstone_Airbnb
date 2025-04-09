import streamlit as st
import pandas as pd
import joblib
from streamlit.components.v1 import html

# Load trained model
@st.cache_resource
def load_model():
    return joblib.load("xgb_pipeline.pkl")  # Make sure this file exists

# Set page config
st.set_page_config(page_title="Airbnb Price Predictor", layout="centered")

# Custom CSS for Airbnb-like styling
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
            font-family: 'Helvetica Neue', sans-serif;
        }
        .stButton button {
            background-color: #FF5A5F;
            color: white;
            border-radius: 6px;
            padding: 0.6em 1.2em;
            font-size: 16px;
            border: none;
        }
        .stSelectbox, .stNumberInput {
            margin-bottom: 16px;
        }
        .block-container {
            padding-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Title and instructions
st.title("Airbnb Price Predictor")
st.markdown("""
This tool estimates the **nightly price** of an Airbnb listing based on property details. 
Fill in the form below and click **Predict Price** to get your estimate.
""")

model = load_model()

# Layout for inputs
st.subheader("Listing Information")
col1, col2 = st.columns(2)

with col1:
    bedrooms = st.number_input("Bedrooms", min_value=0, max_value=10, step=1)
    beds = st.number_input("Beds", min_value=0, max_value=20, step=1)
    baths = st.number_input("Baths", min_value=0, max_value=10, step=1)
    ratings = st.selectbox("Rating", ["5", "4.8", "4.6", "4.4", "4.2", "4.0", "3.0", "0-3", "New", "No rating"])

with col2:
    import calendar
    month = st.selectbox("Month", list(calendar.month_name)[1:])
    neighgroup = st.selectbox("Neighborhood Group", ["Bronx", "Brooklyn", "Manhattan", "Queens", "Staten Island"])
    room_type = st.selectbox("Room Type", ["Entire home/apt", "Hotel room", "Private room", "Shared room"])
    num_reviews = st.selectbox("Number of Reviews", ["0", "1-10", "11-30", "31-100", "100+"])


# Predict button
if st.button("Predict Price"):
    input_data = pd.DataFrame([{
        'latitude': 40.7128,
        'longitude': -74.0060,
        'minimum_nights': 3,
        'number_of_reviews': 10,
        'reviews_per_month': 1.0,
        'calculated_host_listings_count': 1,
        'availability_365': 180,
        'number_of_reviews_ltm': 5,
        'bedrooms': bedrooms,
        'beds': beds,
        'baths': baths,
        'month': list(calendar.month_name).index(month),
        'neighborhood_avgprice': 150,
        'last_review_month': 6,
        'last_review_year': 2024,
        'neighgroup_Bronx': 1 if neighgroup == "Bronx" else 0,
        'neighgroup_Brooklyn': 1 if neighgroup == "Brooklyn" else 0,
        'neighgroup_Manhattan': 1 if neighgroup == "Manhattan" else 0,
        'neighgroup_Queens': 1 if neighgroup == "Queens" else 0,
        'neighgroup_Staten Island': 1 if neighgroup == "Staten Island" else 0,
        'roomtype_Entire home/apt': 1 if room_type == "Entire home/apt" else 0,
        'roomtype_Hotel room': 1 if room_type == "Hotel room" else 0,
        'roomtype_Private room': 1 if room_type == "Private room" else 0,
        'roomtype_Shared room': 1 if room_type == "Shared room" else 0,
        'license_Exempt': 0,
        'license_Has License': 0,
        'license_No License': 1,
        'ratings_3.0': 1 if ratings == "3.0" else 0,
        'ratings_4.0': 1 if ratings == "4.0" else 0,
        'ratings_4.2': 1 if ratings == "4.2" else 0,
        'ratings_4.4': 1 if ratings == "4.4" else 0,
        'ratings_4.6': 1 if ratings == "4.6" else 0,
        'ratings_4.8': 1 if ratings == "4.8" else 0,
        'ratings_5': 1 if ratings == "5" else 0,
        'ratings_New': 1 if ratings == "New" else 0,
        'ratings_No rating': 1 if ratings == "No rating" else 0,
        'ratings_less3': 1 if ratings == "0-3" else 0,
    }])

    predicted_price = model.predict(input_data)

    st.markdown(f"""
    <div style='background-color: #fff; padding: 1.5rem; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); margin-top: 1rem;'>
                <div class="prediction-info">
            <h2 style='color: #FF5A5F;'>${predicted_price[0]:,.2f} / night</h2>
            <p><strong>{room_type}</strong> in <strong>{neighgroup}</strong></p>
            <p>{bedrooms} bedroom(s), {beds} bed(s), {baths} bath(s)</p>
            <p>Month: {month}</p>
            <p>Guest Rating: {ratings}</p>
            <p>Number of Reviews: {num_reviews}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)