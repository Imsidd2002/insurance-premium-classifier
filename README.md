##Introduction
#Overview
This repository provides an application for predicting insurance premium categories. It combines a FastAPI backend for handling predictions, a Streamlit frontend for user interaction, and a machine learning model trained on insurance data. This project is ideal for:

Data scientists and machine learning engineers looking to build and deploy a prediction model.
Developers interested in learning how to build and integrate FastAPI and Streamlit applications.
Anyone interested in exploring the application of machine learning to insurance premium prediction.

#QuickStart
To get the application up and running quickly:

#Install the required dependencies.
Run the FastAPI backend.
Run the Streamlit frontend.
Interact with the application through the frontend to get insurance premium predictions.

Repository Structure
insurance-premium-classifier/
├── app.py # FastAPI backend
├── frontend.py # Streamlit frontend
├── insurance.csv # Dataset
├── insurnce_model.ipynb # Jupyter notebook
├── model.pkl # Trained machine learning model
└── README.md # This file

Prerequisites
Software:
Python 3.7+
pip (Python package installer)
A web browser
Knowledge:
Basic understanding of Python programming
Familiarity with machine learning concepts (optional)
Basic understanding of APIs and web applications (optional)

Getting Started
Clone the Repository:

bash
git clone https://github.com/Imsidd2002/insurance-premium-classifier.git
cd insurance-premium-classifier

Install Dependencies:

bash
pip install fastapi uvicorn streamlit scikit-learn pandas pydantic requests

Run FastAPI Backend:

bash
uvicorn app:app --reload
(This will start the API, typically on http://localhost:8000)

Run Streamlit Frontend:

bash
streamlit run frontend.py
(This will open the Streamlit application in your web browser, usually at http://localhost:8501
)

Interact:
Access the Streamlit application in your browser and enter the required information to get a predicted insurance premium category.
