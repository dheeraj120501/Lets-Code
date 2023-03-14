# Introduction

It is a supervised algorithm and can be used for both classification and regression problems.

- For classification find the most vote of the k nearest neighbour
- For regression find the average of the k nearest neighbour

For KNN regression we can also use the weights which can be inverse of the distance, this way among the k neighbours the one closure will have more effect on the prediction.

The main objective of the KNN algorithm is to predict the classification of a new sample point based on data points that are separated into several individual classes.

- It is useful when you are performing a pattern recognition task for classifying objects based on different features.

A KNN algorithm is based on feature similarity.

There are only two parameters required to implement KNN—the value of K and the distance function (e.g. Euclidean, Manhattan, etc.)

The KNN algorithm is used in the following scenarios:

- Data is labeled
- Data is noise-free
- Dataset is small, as KNN is a lazy learner

The KNN algorithm does not work well with large datasets.

- The cost of calculating the distance between the new point and each existing point is huge, which degrades performance.

Feature scaling (standardization and normalization) is required before applying the KNN algorithm to any dataset. Otherwise, KNN may generate wrong predictions.

# Distance finding Methods

Euclidean Distance
Cosine Distance
Manhattan Distance

# Variation in k

K in KNN is a parameter that refers to the number of nearest neighbors in the majority voting process.

Selecting the right K value is a process called parameter tuning, which is important to achieve higher accuracy.

There is not a definitive way to determine the best value of K. It depends on the type of problem you are solving, as well as the business scenario.

- Small k means low bias, high variance resulting in overfitting.
- Large k means high bias, low variance resulting in underfitting.

To choose the value of K, take the square root of n (sqrt(n)), where n is the total number of data points.

- Usually, an odd value of K is selected to avoid confusion between two classes of data.
- The most preferred value for K is five.
