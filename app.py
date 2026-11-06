
import streamlit as st
import joblib

# Load trained model
model = joblib.load(
    "models/customer_support_model.pkl"
)

st.title("Customer Support Ticket Classification")

st.write(
    "Enter a customer support message "
    "to predict the responsible department."
)

ticket = st.text_area(
    "Enter Customer Support Ticket"
)

if st.button("Predict Category"):

    if ticket.strip():

        prediction = model.predict([ticket])

        st.success(
            f"Predicted Department: {prediction[0]}"
        )

    else:

        st.warning("Please enter a customer message.")
