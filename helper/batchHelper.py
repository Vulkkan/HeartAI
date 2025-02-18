import streamlit as st
from helper import preprocessor, individualHelper


batch_data = st.session_state['data'] if 'data' in st.session_state else None

def submitAndPredictBatch(data):
    if data is not None:
        if data.empty:
            st.error("Uploaded dataset is empty!")
            return False
        
        # data  # Use the entire uploaded dataset

        model = preprocessor.model
        df = data

        patients, df = preprocessor.encodeBatch(df)

        # Make predictions
        predictions = model.predict(df)
        probabilities = model.predict_proba(df)
        results = []

        for i in range(len(df)):
            # Predictions & explanations
            prediction = f"{patients[i]} is predicted to be at low risk" if predictions[i] == 1 else f"{patients[i]} is predicted to be at high risk"

            insights = individualHelper.get_insights(df.iloc[[i]])

            x_prob = probabilities[i][1] * 100
            y_prob = probabilities[i][0] * 100
            
            results.append({
                "Patient": patients[i],
                "Prediction": prediction,
                "X_Probability": x_prob,
                "Y_Probability": y_prob,
                "Insights": insights
            })

        return results


