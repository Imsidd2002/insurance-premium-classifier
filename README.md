## Introduction

This repository provides an application for predicting insurance premium categories. It combines a FastAPI backend for handling predictions, a Streamlit frontend for user interaction, and a machine learning model trained on insurance data. This project is ideal for:



# Install the required dependencies.
Run the FastAPI backend.
Run the Streamlit frontend.
Interact with the application through the frontend to get insurance premium predictions.


# Getting Started
Clone the Repository:

# bash
git clone https://github.com/Imsidd2002/insurance-premium-classifier.git
cd insurance-premium-classifier

# Install Dependencies:

# bash
pip install fastapi uvicorn streamlit scikit-learn pandas pydantic requests

# Run FastAPI Backend:

# bash
uvicorn app:app --reload
(This will start the API, typically on http://localhost:8000)

Run Streamlit Frontend:

bash
streamlit run frontend.py
(This will open the Streamlit application in your web browser, usually at http://localhost:8501
)

Interact:
Access the Streamlit application in your browser and enter the required information to get a predicted insurance premium category.
