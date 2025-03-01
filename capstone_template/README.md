
------------------------------------------------------------------------------

## Project Title
=========================

### Executive Summary

Area of Interest:
Airbnb is a major homestay booking service. In 2024*, there were an estimated 490 million bookings of nights and experiences, giving Airbnb an estimated 83 billion market capitalization, and generating about 11 billion dollar revenue in 2024. Airbnb has listings worldwide, with over 5 million hosts, listing an estimated 7.7 million listings. There is an opportunity to help with better pricing, more transparency, and better customization.

Problem:
Pricing can be tricky. Hosts may not know the best price for their property, they can under-price and lose out on revenue, or over-price and lose out on bookings. There are dynamic pricing tools, but they tend to take a black-box approach, and hosts usually do not know how the pricing is calculated.

Data Science Application:
Using Airbnb’s NYC 2024 Listings data and the use of machine learning tools such as linear regression, classification, and content recommender to give host information to choose a best-fit price so that hosts and renters can experience a fairer price. Likely linear regression on the prediction of price. Optionally a classification on whether a listing will be rented. Optionally a recommender system on similar listings.

Impact:
More transparency and control for hosts, allowing them more competitive rates and increased revenue. Fairer prices for renters, allowing them more freedom of travel. Better pricing efficiencies and satisfaction for Airbnb.

Dataset:
The dataset contains 20,758 observations, with 22 columns (including: listing name, neighborhood, room type, bedrooms, number of reviews, rating, etc.) The target variable is price. An optional backup target variable could be rating.


### Demo

<img width="957" alt="Screenshot 2025-02-28 at 11 52 11 PM" src="https://github.com/user-attachments/assets/de4c4ebe-19be-41a8-9afd-e6ec66c47055" />

<img width="959" alt="Screenshot 2025-02-28 at 11 52 25 PM" src="https://github.com/user-attachments/assets/5bd6f997-1c50-4d5c-8a78-53152c976824" />


### Methodology

The dataset will be analyzed in 3 Sprints. With an initial exploratory analysis. A pre-processing with feature engineering. Machine learning models, such as linear regression will also be used to predict listing price and offer recommendation of best-fit price.  


### Organization

#### Repository 

* `data` 
    - contains link to copy of the dataset (stored in a publicly accessible cloud storage)
    - saved copy of aggregated / processed data as long as those are not too large (> 10 MB)

* `model`
    - `joblib` dump of final model(s)

* `notebooks`
    - contains all final notebooks involved in the project

* `docs`
    - contains final report, presentations which summarize the project

* `references`
    - contains papers / tutorials used in the project

* `src`
    - Contains the project source code (refactored from the notebooks)

* `.gitignore`
    - Part of Git, includes files and folders to be ignored by Git version control

* `capstone_airbnb.yml`
    - Conda environment specification

* `README.md`
    - Project landing page (this page)

* `LICENSE`
    - Project license

#### Dataset

... Google Drive links to datasets and pickled models

### Credits & References

... Include any personal learning
