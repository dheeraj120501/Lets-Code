# Introduction

The support vector machine is a model used for both classification and regression problems though it is mostly used to solve classification problems.

- Also known as maximum margin classifier.
- It's a Supervised Machine Learning Algorithm.

The objective of the algorithm is to find a hyperplane in an N-dimensional space(N — the number of features) that distinctly classifies the data points.

- The algorithm creates a decision boundary which separates data into classes.
- To separate the two classes of data points, there can be many possible hyperplanes that could be chosen.
- SVM find a plane that has the maximum margin, i.e the maximum distance between data points of both classes.
- Maximizing the margin distance provides some reinforcement so that future data points can be classified with more confidence.

## SVM vs Logistic Regression

In logistic regression, we take the output of the linear function and squash the value within the range of [0,1] using the sigmoid function.

- If the squashed value is greater than a threshold value(0.5) we assign it a label 1, else we assign it a label 0.

In SVM we take the output of the linear function and if that output is greater than 1, we identify it with one class and if the output is less than -1, we identify is with another class.

- Since the threshold values are changed to 1 and -1 in SVM, we obtain this reinforcement range of values([-1,1]) which acts as margin.

## Equation of Hyperplane

Hyperplanes are decision boundaries that help classify the data points.

Data points falling on either side of the hyperplane can be attributed to different classes.

The dimension of the hyperplane depends upon the number of features.

- If the number of input features is 2, then the hyperplane is just a line.
- If the number of input features is 3, then the hyperplane becomes a two-dimensional plane.
- It becomes difficult to imagine when the number of features exceeds 3.

## Concepts of Support Vectors

Support vectors are data points that are closer to the hyperplane and influence the position and orientation of the hyperplane.

Using these support vectors, we maximize the margin of the classifier.

Deleting the support vectors will change the position of the hyperplane. These are the points that help us build our SVM.

## Constraints and Lagrange Multiplier

## Descision Rule

# Convex Optimization Problem

# Hard margin and Soft Margin SVM

# Regularization

L1 Regularization

# Non-Linear Data and Kernel Trick

Polynomial and Gaussian/RBF Kernel

## Motivation
