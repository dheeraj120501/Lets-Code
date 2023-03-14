# Introduction

Linear regression is unbounded, and this brings logistic regression into picture. Their value strictly ranges from 0 to 1.

Logistic Regression is used when the dependent variable(target) is categorical.

## Model

The output from the hypothesis is the estimated probability. This is used to infer how confident can predicted value be actual value when given an input X.

To predict which class a data belongs, a threshold can be set.

- Based upon this threshold, the obtained estimated probability is classified into classes.
- This is called descision boundary.
- Decision boundary can be linear or non-linear.
- Polynomial order can be increased to get complex decision boundary.

Output = {0, 1}

Hypothesis => Z = WX + B

hΘ(x) = sigmoid (Z)

If ‘Z’ goes to infinity, Y(predicted) will become 1 and if ‘Z’ goes to negative infinity, Y(predicted) will become 0.

The output from the hypothesis is the estimated probability. This is used to infer how confident can predicted value be actual value when given an input X.

The basic working can be thought of as, we take the output of the linear function and squash the value within the range of [0,1] using the sigmoid function.

- If the squashed value is greater than a threshold value(0.5) we assign it a label 1, else we assign it a label 0.

# Types of Logistic Regression

**Binary Logistic Regression**: The categorical response has only two 2 possible outcomes.

- Example: Spam or Not

**Multinomial Logistic Regression**: Three or more categories without ordering.

- Example: Predicting which food is preferred more (Veg, Non-Veg, Vegan)

**Ordinal Logistic Regression**: Three or more categories with ordering.

- Example: Movie rating from 1 to 5

# Cost Function

Linear regression uses mean squared error as its cost function.

- If it is used for logistic regression, then it will be a non-convex function of parameters (theta).
- Gradient descent will converge into global minimum only if the function is convex.

# Confusion Metrix

Recall, Precision and F1 Score
