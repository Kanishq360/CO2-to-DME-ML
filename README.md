# CO₂ to DME Prediction using Machine Learning

## Overview

This project focuses on predicting **CO₂ conversion** and **DME selectivity** using machine learning models based on catalyst properties, reaction conditions, and system design parameters.

The objective is to understand complex interactions between catalyst design and reaction performance, and to develop predictive models for improved process optimization.

---

## Dataset

* Experimental dataset collected from literature
* ~650 data points with multiple catalyst and reaction descriptors

### Feature Categories:

* Reaction conditions (temperature, pressure, GHSV, feed ratio)
* Catalyst composition (metal fractions, promoters)
* Acidic properties (Si/Al ratio, acid sites)
* Structural properties (surface area, pore volume, crystallite size)
* System configuration (integration method, zeolite dimensionality)

---

## Modeling Approach

Multiple machine learning models were implemented and compared:

* Random Forest (baseline model)
* Extra Trees Regressor
* HistGradientBoosting Regressor (numeric & full feature sets)
* XGBoost Regressor

Separate models were developed for different target variables, including:

* CO₂ Conversion
* DME Selectivity

---

## Methodology

1. Data preprocessing using a unified pipeline (ColumnTransformer)
2. Handling missing values through imputation techniques
3. Feature encoding (categorical + numerical)
4. Baseline model development (Random Forest)
5. Feature importance analysis (Permutation importance)
6. Training advanced ensemble models
7. Model comparison using cross-validation
8. Hyperparameter tuning (performed in extended workflow)

---

## Evaluation Strategy

Model performance was evaluated using:

* R² Score
* RMSE
* K-Fold Cross-Validation (5-fold and 10-fold)

### Diagnostic Analysis:

* Prediction vs Actual (Parity plots)
* Residual distribution
* Learning curves (bias-variance analysis)

---

## Key Insights

* Reaction conditions (temperature, GHSV) strongly influence CO₂ conversion
* DME selectivity depends on both structural and acidic catalyst properties
* Categorical features (integration method, zeolite dimensionality) significantly impact selectivity prediction
* Tree-based ensemble models effectively capture nonlinear relationships in catalytic systems

---

## Project Structure

```id="projstructure"
CO2-to-DME-ML/
│
├── notebook/
│   └── main.ipynb
│
├── results/
│   ├── plots/
│   └── models/
│
├── data/
│   └── dataset.xlsx
```

---

## Tech Stack

* Python
* Scikit-learn
* XGBoost
* Pandas, NumPy, Matplotlib

---

## Future Work

* Advanced hyperparameter optimization
* Model interpretability (e.g., SHAP analysis)
* Multi-objective optimization (Pareto-based approaches)
* Catalyst design space exploration

---

## Author

Kanishq
Chemical Engineering, IIT Ropar
