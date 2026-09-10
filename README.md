# Finance Data Learning - Ticket Sales Analysis & Forecasting

## Project Overview

This project involves the analysis of ticket sales data which is collected from my electronic music event. Such data will be used to investigate factors regarding demand, attendance, revenue and others.

## Analytical Questions

- AQ1 — Relationship

What relationships exist between the key variables in the ticket sales dataset?

- AQ2 — Statistical significance

Are the most important observed relationships statistically significant?

- AQ3 — Prediction

Which variables are most useful for predicting the target outcome?

- AQ4 — Model performance

How effectively can the regression models explain or predict the target outcome?

## Key Findings

- F1 - Marketing Exposure strongly associated with ticket sales

Days advertised had the strongest correlation compared to other variables, with ticket sales with r = 0.896. This implies marketing reach and campaign exposure appear important when understanding demand.

- F2 - Weekend marketing wasn't especially significant regarding growth in event views

Although mean event views were 13.2, compared to a mean of 11.92 on weekdays, the outcome of a hypothesis test produced a p-value of 0.427, showing tgat tge difference was not statistically significant at a 5% significance level.

- F3 - Instagram followers were a positive and strong variable associated with the prediction of ticket sales

When a regression model was ran, the instagram followers variable had a coefficient of 6.979 and a p-value of 0.0046, highlighting a statistically significant postitive correlation with ticket sales after taking taking other predictors into account. Such finding shows that building social mdeia audience reach may be a useful component of a ticket sales strategy.

## Technologies 
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- Scikit-learn

## Repository Structure 

The repository is organised into the following structure to seperate mainly data, analysis, Python code, statistical modelling, outputs and docments.

finance-data-learning/
|
|-- data
|
|-- docs
|
|-- models
|
|-- notebooks
|
|-- outputs
|
|-- src
|
|-- .gitignore
|-- README.md
|-- requirements.txt

The project follows an organised workflow from the inital data preperation through to exploratory analysis, statistical testing and regression analysis. Notebooks provide a reproducible record of the whole analytical process in the project, whereas the src section contains reusable Python code.

## Technical report

The following report shows an explaination of the project in methodology, anaylsis and results terms. Covering the following:

- Introduction
- Business Problem
- Dataset 
- Data Cleaning
- Exploratory Data Analysis 
- Statistical Testing
- Regression Modelling
- Model Comparison
- Key Findings
- Business Implications
- Limitations
- Future Improvements
- Conclusion

Read the Technical report: