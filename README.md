# Using Machine Learning to Identify High-Risk Police Stations for Serious Violent Crime in South Africa
 
## 1. Project Overview
 
This project develops an end-to-end machine-learning solution to identify South African police stations that may be classified as higher-risk for serious violent crime in the following financial year.
 
The project was completed for the IDA117V Introduction to Data Science group project.
 
### Stakeholder
 
The intended stakeholder is the South African Police Service (SAPS).
 
### Problem
 
The project uses historical police-station crime records to predict whether a police station will fall into a higher-risk or lower-risk category for serious violent crime in the following financial year.
 
The prediction task is defined at the:
 
**Police station × financial year**
 
level.
 
The model is intended as a decision-support tool for identifying stations that may require further investigation, monitoring or resource-planning attention. It should not replace human decision-making.
 
---
 
## 2. Target Definition
 
The serious violent crime score is based on the following crime categories:
 
- Murder

- Attempted murder

- Rape

- Sexual assault

- Assault GBH

- Kidnapping
 
The target represents whether the following financial year's serious violent crime score is classified as:
 
- `0` = Lower Risk

- `1` = Higher Risk
 
The classification threshold was determined using the 75th percentile of the training data.
 
The prediction uses information available for the current financial year to predict the risk category for the following financial year.
 
---
 
## 3. Dataset
 
The project uses the South African Police Service Annual Crime Records dataset.
 
Dataset citation:
 
South African Police Service. South African Police Service Annual Crime Records 2005-2026 [dataset]. Version 1.4. Pretoria: South African Police Service (SAPS) [producers], 2026. Pretoria: DataFirst [distributor], 2026.
 
DOI:
 
South Africa - South African Police Service Annual Crime Records 2005-2026
 
The dataset contains annual crime records at police-station level.
 
The dataset includes crime variables together with geographic/location information.
 
---
 
## 4. Data Dictionary
 
### Identification and time variables
 
| Variable | Description |

|---|---|

| station | Police station identifier/name |

| year | Financial year of the crime record |

| start_year | Starting calendar year extracted from the financial year |
 
### Geographic variables
 
| Variable | Description |

|---|---|

| loc_mn | Local municipality |

| dc_mn | District municipality |

| longitude | Police station longitude |

| latitude | Police station latitude |
 
### Crime variables
 
The crime variables represent reported crime counts recorded for each police station and financial year.
 
The model uses the available crime categories as predictive features, including:
 
- Murder

- Attempted murder

- Rape

- Sexual assault

- Assault GBH

- Kidnapping

- Sexual offences

- Other recorded crime categories contained in the dataset
 
Invalid negative crime counts were treated as missing values during preprocessing.
 
---
 
## 5. Data Preparation and Preprocessing
 
The data preparation process follows a chronological design because the task predicts a future financial year.
 
The data were divided into:
 
- Training: 2005–2021

- Validation: 2022–2023

- Test: 2024
 
The test set was kept separate and was used only for the final evaluation of the locked model.
 
The preprocessing pipeline includes:
 
1. Conversion of invalid negative crime counts to missing values.

2. Median imputation for numerical variables.

3. Most-frequent imputation for categorical variables.

4. Standardisation of numerical variables using `StandardScaler`.

5. One-hot encoding of categorical location variables.

6. Handling of unseen categorical values using `handle_unknown="ignore"`.
 
Preprocessing transformations are fitted using the training data within the machine-learning pipeline to reduce the risk of data leakage.
 
---
 
## 6. Reproducibility
 
The project uses fixed random seeds to make the experiments reproducible.
 
The primary random seed used throughout the project is:
 
**random_state = 42**
 
The same train, validation and test partitions were used for model comparisons and controlled ablation experiments.
 
The test set was not used during model selection or hyperparameter tuning.
 
---
 
## 7. Models
 
The project compares multiple machine-learning approaches.
 
### Traditional models
 
- Logistic Regression

- Random Forest
 
### Neural models
 
- Multi-Layer Perceptron (MLP)

- Lightweight Tabular Transformer
 
A naïve DummyClassifier baseline was also used for comparison.
 
The final selected model was the MLP with:
 
- Hidden layers: `(64, 32)`

- Activation: ReLU

- Optimiser: Adam

- Batch size: 32

- Maximum iterations: 100

- Early stopping: enabled

- Validation fraction: 0.1

- Random state: 42
 
---
 
## 8. Model Optimisation
 
The strongest validation model was optimised using GridSearchCV.
 
The optimisation search considered:
 
- Hidden layer sizes

- Alpha regularisation

- Learning rate

- Batch size
 
The optimisation used macro-F1 as the scoring metric.
 
The held-out test set was not used during hyperparameter optimisation.
 
After comparing the original and optimised configurations, the original MLP configuration was retained as the final locked model because it achieved the stronger validation macro-F1 score.
 
---
 
## 9. Final Model Performance
 
The final MLP achieved the following performance on the held-out 2024 test set:
 
| Metric | Test Performance |

|---|---:|

| Accuracy | 0.9709 |

| Precision | 0.9392 |

| Recall | 0.9567 |

| Macro-F1 | 0.9638 |

| Weighted-F1 | 0.9710 |

| ROC-AUC | 0.9935 |

| PR-AUC | 0.9879 |
 
The test set was evaluated only once after the final model and pipeline were locked.
 
---
 
## 10. Ablation Analysis
 
Three controlled ablation experiments were performed while keeping the split, random seed and evaluation procedure fixed.
 
The experiments investigated:
 
1. Removing geographic features.

2. Removing categorical location variables.

3. Removing StandardScaler.
 
The results showed that geographic information contributed meaningfully to model performance, while categorical location information and feature scaling also had measurable effects.
 
---
 
## 11. Statistical Comparison
 
The final MLP was compared with the strongest traditional comparator, Random Forest, using the same held-out 2024 test cases.
 
McNemar's exact test was used because the predictions were paired on identical test observations.
 
The test produced:
 
- Discordant cases: 22

- McNemar statistic: 11.0

- Exact p-value: 1.0

- Significance level: α = 0.05
 
The null hypothesis was not rejected. Therefore, there was no statistically significant difference in error rates between the two models on the paired test cases.
 
---
 
## 12. Streamlit User Interface
 
The project includes a Streamlit user interface for making predictions using the saved final pipeline.
 
The interface:
 
- Accepts police-station and crime-related inputs.

- Validates user input.

- Rejects negative crime counts.

- Runs the saved preprocessing and model pipeline.

- Displays the predicted risk class.

- Displays prediction probability/confidence.

- Provides a brief explanation.

- Includes responsible-use and limitation information.
 
### Run the application
 
Install the required dependencies and run:
 
    streamlit run app.py
 
The application will then open in a local browser.
 
---
 
## 13. Repository Structure
 
```text

crime-prediction-model/

│

├── Crime rate prediction model.ipynb

├── app.py

├── transformers.py

├── final_mlp_pipeline.joblib

├── requirements.txt

├── README.md

└── data/

    └── saprac-2005-2026-v1.4.csv
South Africa - South African Police Service Annual Crime Records 2005-2026
In accordance with the Section 218 (f) of the Interim Constitution of the Republic of South Africa, 1993 (Act No. 200 of 1993), the South African Police Service (SAPS) should enable the provision o...
 
