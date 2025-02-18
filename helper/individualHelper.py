import streamlit as st
import helper.preprocessor as preprocessor

def get_insights(df):
    """Generate health insights based on patient data."""
    insights = []

    # Checking fasting blood sugar (fbs_1 indicates high blood sugar)
    if df['fbs_1'].iloc[0] == 1:
        insights.append("Fasting blood sugar is high. Consider reducing sugar intake.")
    elif df['fbs_0'].iloc[0] == 1:
        insights.append("Fasting blood sugar is normal.")

    # Checking cholesterol level
    if df['chol'].iloc[0] > 240:
        insights.append("Cholesterol level is high. Reduce fat intake and exercise.")
    elif df['chol'].iloc[0] < 150:
        insights.append("Cholesterol level is quite low. Add healthy fats to your diet.")

    # Checking resting blood pressure
    if df['trestbps'].iloc[0] > 130:
        insights.append("Blood pressure is elevated. Monitor your sodium intake and manage stress.")
    elif df['trestbps'].iloc[0] < 90:
        insights.append("Blood pressure is low. Probably hydrated, and requires a balanced diet.")

    # Checking heart rate (thalach - maximum heart rate achieved)
    if df['thalach'].iloc[0] < 100:
        insights.append("Heart rate is relatively low. Consider taking cardio exercises.")
    elif df['thalach'].iloc[0] > 180:
        insights.append("Heart rate is quite high. Assessment required.")

    # Checking ST depression (oldpeak - indicates heart stress)
    if df['oldpeak'].iloc[0] > 2:
        insights.append("ST depression level is high, which may indicate heart stress. Cardiologist intervention required.")

    # ✅ Ensure at least one insight is provided
    if not insights:
        insights.append("Health parameters are within normal ranges. Keep maintaining a healthy lifestyle!")

    return insights



def submitAndPredict(patient, df):
    if df is not None:
        df = preprocessor.encode(df)

        # Make predictions
        prediction = preprocessor.model.predict(df)
        probabilities = preprocessor.model.predict_proba(df)

        # Ensure probabilities exist
        if probabilities.shape[0] == 0:
            st.error("Prediction failed. No probability values returned.")
            return None

        prediction_text = f"{patient} is predicted to be at low risk" if prediction[0] == 1 else f"{patient} is predicted to be at high risk"

        # Extract repayment and default probabilities
        x_prob = f"{probabilities[0][1] * 100:.2f}%"
        y_prob = f"{probabilities[0][0] * 100:.2f}%"

        # Generate insights
        insights = get_insights(df)

        return patient, prediction_text, x_prob, y_prob, insights
    
    else:
        return None
