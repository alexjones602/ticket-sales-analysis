# Ticket Sales Analysis & Forecasting

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

```text
ticket-sales-analysis/
│
├── data/
|
|   ├── cleaned/              # Cleaned datasets used for analysis
│   ├── raw/                  # Original source data
│   └── toy/                  # Small datasets used for testing
|
├── docs/                     # Project documentation
│   └── technical_report.pdf  # Final technical report
|
├── models/                   # Statistical model
│
├── notebooks/                # Jupyter notebooks documenting the analysis
|
├── outputs/
│   ├── cleaned_data/         # Processed datasets
│   └── plots/                # Analysis visualisations
│
├── src/                      # Reusable Python code
│
├── requirements.txt          # Python dependencies
├── .gitignore                # Files excluded from version control
└── README.md                 # Project documentation
```

The project follows an organised workflow from the inital data preperation through to exploratory analysis, statistical testing and regression analysis. Notebooks provide a reproducible record of the whole analytical process in the project, whereas the src section contains reusable Python code.

## Technical Report

The following report shows an explaination of the project in methodology, anaylsis and results terms. Covering the following:

- **Introduction** – project context, objectives and analytical approach
- **Business Problem** – business context and key analytical questions
- **Dataset** – data source, variables and dataset characteristics
- **Data Cleaning** – preparation, validation and transformation
- **Exploratory Data Analysis** – descriptive statistics, relationships and visualisations
- **Statistical Testing** – hypotheses, statistical tests and interpretation
- **Regression Modelling** – model development, predictors and performance
- **Model Comparison** – comparison of predictive approaches
- **Key Findings** – the most important insights from the analysis
- **Business Implications** – how the findings could support decision-making
- **Limitations** – limitations of the data and methodology
- **Future Improvements** – potential improvements to the analysis and modelling
- **Conclusion** – overall conclusions

**[Read the Technical Report](docs/technical_report.pdf)**
