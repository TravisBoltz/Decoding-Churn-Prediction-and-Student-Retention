---
Final Year Research Project: Churn Prediction
 ---

## Introduction

Customer churn prediction is a critical aspect of business strategy, aiming to identify customers who are likely to stop using a service. In this final year research project, we focus on predicting churn among university students based on various factors such as demographics, usage patterns, and service quality perceptions.

## Objectives

The primary objectives of this research are:

1. To identify key factors contributing to student churn.
2. To build predictive models that can accurately forecast churn.
3. To evaluate the performance of different machine learning models for churn prediction.
4. To provide actionable insights for reducing churn rates.

## Dataset Description

The dataset used for this research includes the following features:
Make changes to the dataset description
- **Gender**: The customer's gender.
- **College**: The specific college within the university.
- **Churn**: Indicates whether the student has churned ("Yes" or "No").
- **Level**: The academic level of the student.
- **Residence**: Whether the student lives on-campus or off-campus.
- **SIM_Usage**: Whether the student uses a SIM card.
- **Usage_Freq**: Frequency of SIM usage.
- **Network_Strength**: Quality of the network (on a scale).
- **Voice_Calls**: Whether the student makes voice calls.
- **Mobile_Data_Internet**: Whether the student uses mobile data.
- **SMS_Text_Messaging**: Whether the student sends SMS texts.
- **Data_Exhaustion**: Whether the student experiences data exhaustion.
- **Other_Networks**: Whether the student uses other networks.
- **Poor_Network_Quality_Coverage**: Whether the student experiences poor network quality.
- **Insufficient_Data_Allowance**: Whether the student's data allowance is insufficient.
- **Unsatisfactory_Customer_Service**: Whether the student is dissatisfied with customer service.
- **High_Costs_Pricing**: Whether the student finds the pricing high.
- **Monthly_Data_Usage**: Amount of data used monthly.

## Methodology

### Data Preprocessing

Data preprocessing steps include handling missing values, encoding categorical variables, and normalizing numerical features to prepare the dataset for model training.

### Survival Analysis


### Model Training

The following machine learning models are utilized for churn prediction:

- Logistic Regression
- Random Forest Classifier
- K-Nearest Neighbors (KNN)
- Support Vector Classifier (SVC)
- Gradient Boosting Classifier
- Multi-Layer Perceptron (MLP)
- LightGBM Classifier

### Hyperparameter Tuning 

Hyperparameter tuning is performed using `RandomizedSearchCV` to identify the best parameters for each model. The hyperparameters for each model are defined as follows:

```python
# Initialize the models
lr = LogisticRegression(random_state=42, solver='liblinear')
rf = RandomForestClassifier(random_state=42)
knn = KNeighborsClassifier()
svm = SVC(random_state=42)
gb = GradientBoostingClassifier(random_state=42)
nn = MLPClassifier(random_state=42, max_iter=1000)
lgbm = LGBMClassifier(random_state=42)
# lightgbm.basic.Booster.silent = True

# List of models
models = [lr,rf,knn, svm, gb, nn, lgbm]
# Define the hyperparameters for each model
hyperparameters = {
    'LogisticRegression': {
        'C': uniform(0.1, 10),
        'penalty': ['l1', 'l2']
    },
    'RandomForestClassifier': {
        'n_estimators': randint(50, 200),
       'max_depth': randint(1, 10)
    },
    'KNeighborsClassifier': {
        'n_neighbors': randint(1, 10)
    },
    'SVC': {
        'C': uniform(0.1, 10),
        'gamma': uniform(0.001, 1)
    },
    'GradientBoostingClassifier': {
        'n_estimators': randint(50, 200),
       'max_depth': randint(1, 10),
        'learning_rate': uniform(0.01, 0.3)
    },
    'MLPClassifier': {
        'hidden_layer_sizes': (randint(10, 100).rvs(), randint(10, 100).rvs()),
        'alpha': uniform(0.0001, 0.1)
    },
    'LGBMClassifier': {
        'n_estimators': randint(50, 200),
       'max_depth': randint(1, 10),
        'learning_rate': uniform(0.01, 0.3)
    }
}

# Perform a randomized search for each model
for model in models:
    model_name = model.__class__.__name__
    print(f"\nTuning {model_name}...")

    # Initialize a RandomizedSearchCV object
    rs = RandomizedSearchCV(rf, hyperparameters['RandomForestClassifier'], n_iter=10, cv=5, random_state=42, n_jobs=-1, error_score='raise')
    # Fit the RandomizedSearchCV object to the data
    rs.fit(X_train, y_train)

    # Print the best parameters and the best score
    print(f"Best parameters: {rs.best_params_}")
    # print(f"Best score: {rs.best_score_}")
```
## Model Evaluation

The performance of each model is evaluated using cross-validation. The best parameters and scores for each model are reported to identify the most effective model for churn prediction.

## Results and Discussion

The results of the model evaluations will be presented, highlighting the performance of each model in terms of accuracy, precision, recall, and F1-score. The discussion will focus on the implications of the findings and how they can be utilized to mitigate churn.

## Conclusion

This research project provides a comprehensive approach to predicting student churn using various machine learning models. The insights gained from this study can help university administrations and service providers to identify at-risk students and take proactive measures to improve retention rates.
