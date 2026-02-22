# CO2-EMISSION-PREDICTION

## ✅ Problem Statement

Predicting vehicle CO₂ emissions accurately is critical for environmental monitoring and regulatory compliance.
Traditional approaches rely on multiple vehicle parameters such as fuel type, fuel consumption, and engine characteristics. However, this creates challenges in real-world deployment:

Data collection becomes complex and time-consuming.

Many features are unavailable in real-time systems.

High model complexity increases latency and reduces scalability.

Maintaining consistency between training and deployment pipelines is difficult.

Therefore, there is a need for a lightweight, interpretable, and fast prediction system that can estimate CO₂ emissions using minimal input features while maintaining reasonable accuracy.

## ✅ Problem Faced During Deployment

During model deployment using FastAPI, a feature mismatch error occurred because:

1. The model was trained using multiple features including fuel consumption and encoded fuel type.

2. The deployed API was designed to accept only ENGINE SIZE and CYLINDERS.

3. This caused runtime errors since the model expected the same feature set used during training.

4. This highlighted a common real-world issue in machine learning:
👉 Inconsistency between training and inference pipelines.

## ✅ Solution Implemented

To solve this problem:

### ✔ Feature Simplification

The model was retrained using only:

ENGINE SIZE

CYLINDERS

This reduced model complexity and made it suitable for real-time use.

### ✔ Model Retraining

A new regression model was trained with the selected features to ensure:

Consistent feature input

Reduced risk of deployment errors

Faster predictions

### ✔ End-to-End Deployment

The solution was deployed as a REST API using FastAPI, enabling:

Real-time prediction

Scalable integration with applications

Easy testing via Swagger UI

### ✔ Robust System Design

The deployment pipeline ensured:

Consistent preprocessing

Structured API input validation

Production-ready architecture

## ✅ Key Results and Impact

Reduced model complexity and input requirements

Improved system interpretability

Enabled real-time prediction with low latency

Solved feature mismatch and deployment challenges

Created a scalable and lightweight CO₂ prediction system

## ✅ Business Value

This solution can help:

Environmental agencies estimate emissions quickly

Automotive companies evaluate eco-friendliness

Smart city platforms monitor vehicle pollution

Policy makers design sustainable transportation strategies

## LIVE : https://co2-emission-prediction-j4w5.onrender.com/docs

# 🙎‍♂️ AUTHOR 
## Aryan Narendra Harke
