import streamlit as st
import pandas as pd
import joblib


# ---------------------------------------------------------
# Load the saved final MLP pipeline
# ---------------------------------------------------------

PIPELINE_FILE = "final_mlp_pipeline.joblib"

model_pipeline = joblib.load(PIPELINE_FILE)


# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="Serious Crime Risk Predictor",
    page_icon="🇿🇦",
    layout="wide"
)


# ---------------------------------------------------------
# Title and introduction
# ---------------------------------------------------------

st.title("🇿🇦 Serious Violent Crime Risk Predictor")

st.write(
    """
    This application predicts whether a police station-year observation
    is classified as **Higher Risk** or **Lower Risk** for serious violent
    crime in the following financial year.
    """
)

st.info(
    """
    Enter the crime and geographic information for a police station-year.
    The saved machine-learning pipeline will automatically perform the
    required preprocessing before generating the prediction.
    """
)


# ---------------------------------------------------------
# Get the exact features expected by the saved pipeline
# ---------------------------------------------------------

feature_columns = list(model_pipeline.feature_names_in_)

categorical_features = ["loc_mn", "dc_mn"]

numeric_features = [
    feature for feature in feature_columns
    if feature not in categorical_features
]


# ---------------------------------------------------------
# Get the categorical values learned during training
# ---------------------------------------------------------

preprocessor = model_pipeline.named_steps["preprocessor"]

categorical_pipeline = next(
    transformer
    for name, transformer, columns in preprocessor.transformers_
    if name == "cat"
)

encoder = categorical_pipeline.named_steps["encoder"]

loc_options = list(encoder.categories_[0])
dc_options = list(encoder.categories_[1])


# ---------------------------------------------------------
# Helper function for readable labels
# ---------------------------------------------------------

def readable_label(feature):
    return feature.replace("_", " ").title()


# ---------------------------------------------------------
# Input section
# ---------------------------------------------------------

st.header("1. Enter Station Information")

col1, col2 = st.columns(2)

with col1:
    loc_mn = st.selectbox(
        "Municipality",
        loc_options
    )

with col2:
    dc_mn = st.selectbox(
        "District",
        dc_options
    )


# ---------------------------------------------------------
# Geographic information
# ---------------------------------------------------------

st.header("2. Geographic Information")

geo_col1, geo_col2, geo_col3 = st.columns(3)

with geo_col1:
    latitude = st.number_input(
        "Latitude",
        value=0.0,
        format="%.6f"
    )

with geo_col2:
    longitude = st.number_input(
        "Longitude",
        value=0.0,
        format="%.6f"
    )

with geo_col3:
    start_year = st.number_input(
        "Financial Year",
        min_value=2005,
        max_value=2024,
        value=2024,
        step=1
    )


# ---------------------------------------------------------
# Crime information
# ---------------------------------------------------------

st.header("3. Crime Information")

st.caption(
    "Enter the number of reported cases for each crime category."
)

user_inputs = {}

crime_columns = st.columns(3)

crime_features = [
    feature for feature in numeric_features
    if feature not in ["latitude", "longitude", "start_year"]
]


for index, feature in enumerate(crime_features):

    column = crime_columns[index % 3]

    with column:
        user_inputs[feature] = st.number_input(
            readable_label(feature),
            min_value=-1.0,
            value=0.0,
            step=1.0
        )


# ---------------------------------------------------------
# Prediction button
# ---------------------------------------------------------

st.divider()

predict_button = st.button(
    "🔍 Predict Crime Risk",
    type="primary",
    use_container_width=True
)


# ---------------------------------------------------------
# Prediction
# ---------------------------------------------------------

if predict_button:

    # Basic validation

    negative_crimes = [
        feature
        for feature, value in user_inputs.items()
        if value < 0
    ]

    if negative_crimes:

        st.error(
            "Invalid input: Crime counts cannot be negative. "
            "Please enter values of 0 or greater."
        )

    elif latitude == 0.0 or longitude == 0.0:

        st.warning(
            "Please enter valid latitude and longitude values."
        )

    else:

        try:

            # Build one input row
            input_data = {}

            # Add crime features
            input_data.update(user_inputs)

            # Add categorical features
            input_data["loc_mn"] = loc_mn
            input_data["dc_mn"] = dc_mn

            # Add geographic features
            input_data["longitude"] = longitude
            input_data["latitude"] = latitude
            input_data["start_year"] = start_year

            # Create DataFrame in EXACT feature order
            input_df = pd.DataFrame(
                [input_data],
                columns=feature_columns
            )

            # Make prediction
            prediction = model_pipeline.predict(input_df)[0]

            # Get probability
            probabilities = model_pipeline.predict_proba(input_df)[0]

            confidence = probabilities[int(prediction)]


            # -------------------------------------------------
            # Display result
            # -------------------------------------------------

            st.header("Prediction")

            if prediction == 1:

                st.error("🔴 HIGHER RISK")

                st.write(
                    "The model classifies this station-year "
                    "observation as **Higher Risk**."
                )

            else:

                st.success("🟢 LOWER RISK")

                st.write(
                    "The model classifies this station-year "
                    "observation as **Lower Risk**."
                )


            st.metric(
                "Model Confidence",
                f"{confidence * 100:.1f}%"
            )


            # -------------------------------------------------
            # Plain-language explanation
            # -------------------------------------------------

            st.subheader("What does this mean?")

            if prediction == 1:

                st.write(
                    """
                    Based on the crime and geographic information entered,
                    the model identifies this station-year observation as
                    having a higher predicted level of serious violent
                    crime risk for the following financial year.
                    """
                )

            else:

                st.write(
                    """
                    Based on the crime and geographic information entered,
                    the model identifies this station-year observation as
                    having a lower predicted level of serious violent
                    crime risk for the following financial year.
                    """
                )


            # -------------------------------------------------
            # Responsible-use notice
            # -------------------------------------------------

            st.warning(
                """
                **Responsible-use notice:** This prediction is intended
                for analytical decision support only. It should not be
                used as the sole basis for policing decisions, resource
                allocation, or decisions about individuals or communities.
                """
            )


        except Exception as error:

            st.error(
                "The prediction could not be completed."
            )

            st.write(
                "Please check that all inputs are valid."
            )

            st.caption(
                f"Technical details: {error}"
            )