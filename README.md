## Telecom Customer Churn Analysis

# Overview

This project aims to analyze customer churn in a telecom company using parametric models and Customer Lifetime Value (CLV) calculations. The main objectives include building Accelerated Failure Time (AFT) models with various distributions, comparing the models, and selecting the final model. Additionally, CLV is calculated based on the chosen model, exploring CLV within different customer segments, and providing insights into factors influencing churn risk.

## Project Inclusions

# Parametric Models:

Developing Accelerated Failure Time (AFT) models with various distributions.
Comparing these models based on relevant metrics.
Visualizing survival curves for all distributions in a single plot.
Selecting the final model, considering factors beyond statistical comparisons.

## Customer Lifetime Value (CLV):

Computing CLV per customer using the chosen model.
Exploring CLV variations within different customer segments..

# Report:

Interpreting coefficients derived from the final model.
Identifying and describing the most valuable customer segments.
Estimating the annual retention budget based on CLV, survival probabilities, and the number of at-risk subscribers.
Providing recommendations for retention strategies beyond the model.

## Project Components

Exponential.py
Defines a class for an Exponential AFT Fitter.
clv_calc.py
Defines the calculate clv function

HW3.ipynb
A report summarizing findings, interpretations, and recommendations.
