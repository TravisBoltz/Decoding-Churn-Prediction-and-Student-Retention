**<center><span style="font-family:serif; font-size:34px;"> Decoding Student Retention and Churn of Vodafone (Telecel) in KNUST - A Survival Analytics Approach </span>
<a id = "missingvalue" ></a><center>**

<center><span style="font-family:Palatino; font-size:22px;"><i>A comparative analysis between Cox Proportional Hazards, Kaplan Meier <span style="color:#DC143C;"> and</span> Random Survival Forest Model </i> </center>
***
#
**<center><span style="font-family:serif; font-size:34px;"> Survival Analysis Methodologies</span><a id = "missingvalue" ></a><center>**
- In the context of this problem, "methodology" refers to the systematic processes, techniques, and protocols employed in collecting, managing, processing, and analyzing data to ensure its integrity, accuracy, and effectiveness for drawing insights or building machine learning models.
- In this analysis, we employ three methodologies for survival analysis: Kaplan-Meier Estimator, Random Survival Forests (RSF), and Cox Proportional Hazards (CoxPH) model. These methods are used to analyze the time until an event occurs, such as student churn.
## *Model 1: Kaplan-Meier Estimator

**Description:**
The Kaplan-Meier estimator is employed in survival analysis to analyze the time until an event occurs.

**Mathematical Computation:**

The Kaplan-Meier estimator calculates the survival probability at a specific time step by multiplying the probability of surviving each previous time step.

Let $S(t)$ be the survival probability at time $t$. The estimator is computed as:

$$
S(t) = \prod_{t_i \leq t} \left(1 - \frac{d_i}{n_i}\right)
$$

where:
- 
- $t_i$ is the time of the $i$-th unique event (churn)
- $d_i$ is the number of events (churn) at time $i$
- $n_i$ is the number of students at risk just prior to time $i$

The estimator essentially calculates the probability of surviving from one time step to the next, and the product of these probabilities gives the overall survival probability up to time $t$.


Here, $t_1$ would be the time at which the first churn event occurred, $d_1$ would be 1 (since one churn event occurred), and $n_1$ would be the total number of students at that time.

## *Model 2: Random Survival Forests

**Description:**
Random Survival Forests extend the traditional random forest algorithm to the survival analysis setting. They are an ensemble method that combines multiple decision trees to improve predictive performance and handle censored data.

**Mathematical Computation:**

Random Survival Forests use a similar structure to traditional random forests but with modifications to handle right-censored data and to predict survival probabilities.

The predicted survival probability at a specific time $t$ for a new instance can be computed as:

$$
\hat{S}(t) = \frac{1}{B} \sum_{b=1}^{B} \hat{S}_b(t)
$$

where:
- $\hat{S}(t)$ is the predicted survival probability
- $B$ is the total number of trees in the forest
- $\hat{S}_b(t)$ is the predicted survival probability from the $b$-th tree

Each tree is constructed using a bootstrapped sample of the data, and the splitting criteria are based on survival-specific metrics like the log-rank statistic or the log-rank score.

For this model, we would need to build multiple decision trees and calculate the predicted survival probability for each tree.

The hazard function for a specific student can be calculated using the formula.

## *Model 3: Cox Proportional Hazards (Cox PH) Model

**Description:**
The Cox Proportional Hazards model is a popular semi-parametric model for survival analysis. It models the relationship between the survival time and a set of predictor variables, assuming a proportional hazard rate.

**Mathematical Computation:**

The Cox PH model is represented as:

$$
h(t \mid x) = h_0(t) \exp(\beta_1 x_1 + \beta_2 x_2 + \dots + \beta_p x_p)
$$

where:
- $h(t \mid x)$ is the hazard function, i.e., the instantaneous rate of the event occurring at time $t$ given the predictor variables $x$
- $h_0(t)$ is the baseline hazard function, representing the hazard for individuals with all predictor variables equal to zero
- $\beta_1, \beta_2, ..., \beta_p$ are the coefficients for the predictor variables

The coefficients are estimated using maximum likelihood estimation, and the model assumes a proportional hazard ratio, meaning the effect of the predictors on the hazard is constant over time.

## *Concordance Index in Survival Analysis

The Concordance Index, often referred to as the C-index or Harrell's C-index, is a statistical metric used to evaluate the performance of models in survival analysis. It assesses how well a model discriminates between subjects in terms of their event times and predicted risks.

**Description**: The Concordance Index measures the model's ability to correctly order or rank the predicted risks of individuals based on their actual event times. In survival analysis, the goal is often to predict the time until a specific event occurs, such as death, relapse, or failure. The Concordance Index evaluates whether the model's predicted risks align with the observed event times.

**Mathematical Computation**: Let's break down the calculation of the Concordance Index:

**Step 1: Define Pairs of Individuals**
- Create all possible pairs of individuals from the dataset.
- For each pair, compare their predicted risk scores and event times.

**Step 2: Calculate Concordant and Discordant Pairs**

- A pair of individuals (i, j) is concordant if the ordering of their predicted risks aligns with the ordering of their event times: 
  - If $\hat{F}(t_i) > \hat{F}(t_j)$ and $T_i > T_j$
  - If $\hat{F}(t_i) < \hat{F}(t_j)$ and $T_i < T_j$
- A pair is discordant if the ordering of predicted risks is opposite to the ordering of event times.
- Pairs where event times are equal ($T_i = T_j$) are ignored.

**Step 3: Compute the Concordance Index**

The Concordance Index ($C$) is calculated as:

$$
C = \frac{\text{Number of Concordant Pairs}}{\text{Number of Concordant Pairs} + \text{Number of Discordant Pairs}}
$$

**Interpretation**

- $C$ ranges from 0 to 1, where:
  - 0.5 indicates random guessing (no predictive ability)
  - 1 indicates perfect discrimination (perfect predictive ability)
- A $C$ value above 0.5 suggests that the model has predictive ability better than random chance.
- Higher $C$ values indicate better model performance and more accurate risk predictions.

**Extensions**

The Concordance Index can be extended to handle censored data, where individuals may not experience the event of interest during the observation period. Various methods, such as inverse probability of censoring weights (IPCW), can be applied to adjust for censored instances and provide a more accurate assessment of model performance.
***