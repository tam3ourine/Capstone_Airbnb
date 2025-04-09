import streamlit as st
import pandas as pd
import joblib

# Load trained model
@st.cache_resource
def load_model():
    return joblib.load("xgb_pipeline_best.pkl")  # Make sure this file exists

# Initialize
st.title("Airbnb Price Predictor")
st.write("Fill in the property details to estimate the nightly price.")

model = load_model()

# Collect simplified inputs
month = st.selectbox("Month", list(range(1, 13)))
bedrooms = st.number_input("Bedrooms", min_value=0, step=1)
beds = st.number_input("Beds", min_value=0, step=1)
baths = st.number_input("Baths", min_value=0, step=1)
neighgroup = st.selectbox("Neighborhood Group", ["Bronx", "Brooklyn", "Manhattan", "Queens", "Staten Island"])
room_type = st.selectbox("Room Type", ["Entire home/apt", "Hotel room", "Private room", "Shared room"])
ratings = st.selectbox("Rating", ["3.0", "4.0", "4.2", "4.4", "4.6", "4.8", "5", "New", "No rating", "less3"])

# Create input data with default values for other columns
input_data = {
    'month': month,
    'bedrooms': bedrooms,
    'beds': beds,
    'baths': baths,
    'neighgroup_Bronx': 1 if neighgroup == "Bronx" else 0,
    'neighgroup_Brooklyn': 1 if neighgroup == "Brooklyn" else 0,
    'neighgroup_Manhattan': 1 if neighgroup == "Manhattan" else 0,
    'neighgroup_Queens': 1 if neighgroup == "Queens" else 0,
    'neighgroup_Staten Island': 1 if neighgroup == "Staten Island" else 0,
    'roomtype_Entire home/apt': 1 if room_type == "Entire home/apt" else 0,
    'roomtype_Hotel room': 1 if room_type == "Hotel room" else 0,
    'roomtype_Private room': 1 if room_type == "Private room" else 0,
    'roomtype_Shared room': 1 if room_type == "Shared room" else 0,
    'ratings_3.0': 1 if ratings == "3.0" else 0,
    'ratings_4.0': 1 if ratings == "4.0" else 0,
    'ratings_4.2': 1 if ratings == "4.2" else 0,
    'ratings_4.4': 1 if ratings == "4.4" else 0,
    'ratings_4.6': 1 if ratings == "4.6" else 0,
    'ratings_4.8': 1 if ratings == "4.8" else 0,
    'ratings_5': 1 if ratings == "5" else 0,
    'ratings_New': 1 if ratings == "New" else 0,
    'ratings_No rating': 1 if ratings == "No rating" else 0,
    'ratings_less3': 1 if ratings == "less3" else 0,
    # All other features default to common placeholder values
    'latitude': 40.7128,
    'longitude': -74.0060,
    'minimum_nights': 3,
    'number_of_reviews': 10,
    'reviews_per_month': 1.0,
    'calculated_host_listings_count': 1,
    'availability_365': 180,
    'number_of_reviews_ltm': 5,
    'neighborhood_avgprice': 150,
    'last_review_month': 6,
    'last_review_year': 2024,
    'license_Exempt': 0,
    'license_Has License': 0,
    'license_No License': 1,
}

# Predict button
if st.button("Predict Price"):
    input_df = pd.DataFrame([input_data])
    predicted_price = model.predict(input_df)
    st.success(f"Estimated nightly price: ${predicted_price[0]:.2f}")
