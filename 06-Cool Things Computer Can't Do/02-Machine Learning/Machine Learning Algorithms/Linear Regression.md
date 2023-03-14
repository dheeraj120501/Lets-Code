# Introduction

**Linear regression** is a method for finding the straight line or hyperplane that best fits a set of points.

By convention in machine learning, you'll write the equation for a model slightly differently:
![Linear Regression](./img/linear-regression.png "Linear Regression")

- A more sophisticated model might rely on multiple features, each having a separate weight (w1, w2, etc.).
  - For example, a model that relies on three features might look as follows  
    ![Linear Regression](./img/linear-regression-more-feature.png "Linear Regression")

An intercept or offset from an originis called **bias**.

- Bias (also known as the bias term) is referred to as b or w0 in machine learning models.

A coefficient for a feature in a linear model, or an edge in a deep network is called **weight**.

- The goal of training a linear model is to determine the ideal weight for each feature.
- If a weight is 0, then its corresponding feature does not contribute to the model.

In supervised learning, a machine learning algorithm builds a model by examining many examples and attempting to find a model that minimizes loss; this process is called **empirical risk minimization**.

- _loss_ is a number indicating how bad the model's prediction was on a single example.

# Calculate Loss Function

MSE and Gradient Descent

# Overfitting

## Lasso Regression

## Ridge Regression

## Lasso vs Ridge Regression
