# Introduction

Principal component analysis (PCA) is a statistical technique that is widely used to reduce the dimensionality of large data sets while preserving as much of the information as possible.

The goal of PCA is to identify the underlying structure of the data by finding the directions of maximum variance, also known as principal components.

- These principal components are used to transform the original data into a new set of uncorrelated variables, called principal component scores.

The theory of PCA is based on the eigenvectors and eigenvalues of the covariance matrix of the data.

- Eigenvectors of the covariance matrix represent the directions of maximum variance in the data and eigenvalues represent the amount of variance in those directions.
- These eigenvectors and eigenvalues are used to create the principal components, which are used to transform the original data into a new set of uncorrelated variables.

PCA is widely used in many fields, including pattern recognition, image and speech processing, and bioinformatics. Benifits of using PCA:

- Data compression: PCA can be used to reduce the dimensionality of the data while retaining the most important information.
- Feature extraction: PCA can be used to identify the underlying features of the data, which can then be used as input to other machine learning algorithms.
- Visualization: PCA can be used to create two-dimensional or three-dimensional plots of the data, which can be used to identify patterns and clusters in the data.

Some of the drawbacks of PCA include:

- PCA is sensitive to the scaling of the data and outliers.
- PCA can’t handle categorical variables, which must be encoded in some way before performing the analysis.
- PCA can’t handle missing data, which must be imputed or removed before performing the analysis.

## Issue with real world data

In real-world data, the variables are often correlated.

This correlation can lead to the failure of PCA because the eigenvectors of the covariance matrix will not represent the true directions of maximum variance in the data. Instead, the eigenvectors will represent the directions of maximum variance in the correlated data, which may not be the same as the true directions of maximum variance.

The impact of correlation on PCA can be seen in the results of the analysis.

When the variables are correlated, the principal components may not represent the true underlying structure of the data.

This can lead to a loss of important information and a decrease in the interpretability of the results. In addition, the explained variance and the loadings of the principal components may not accurately reflect the patterns in the data.

One way to mitigate the impact of correlation on PCA is to use regularization techniques, such as ridge regression or principal component regression (PCR).

- These techniques add a penalty term to the eigenvalue problem, which reduces the impact of correlation on the eigenvectors and eigenvalues.

Another approach is to use other dimensionality reduction techniques, such as independent component analysis (ICA) or non-negative matrix factorization (NMF), which do not assume uncorrelated variables.

# Understanding PCA

Steps involved in PCA are:

- Standardization of Data
- Computing Covariance Matrix
- Computing Eigenvectors and Eigenvalues
- Choosing Principal Components
- Computing Principal component scores
- Interpretation of the analysis

The first step in PCA is to **standardize the data** by subtracting the mean and dividing by the standard deviation.

- This is done to ensure that all the variables are on the same scale, which is necessary for PCA.
- The standardized data is denoted as X.

The next step is to **compute the covariance matrix** of the standardized data.

- The covariance matrix is a square matrix that contains the pairwise covariances between the variables.

The **eigenvectors and eigenvalues** of the covariance matrix are computed next.

- The eigenvectors represent the directions of maximum variance in the data, while the eigenvalues represent the amount of variance in those directions.

The **principal components** are the eigenvectors corresponding to the largest eigenvalues.

- They represent the directions of maximum variance in the data.
- The number of principal components is typically chosen to be less than or equal to the number of variables in the original data.

The **principal component scores** are the projections of the original data onto the principal components.

- They are computed by multiplying the original data by the matrix of eigenvectors.

The explained variance and loadings of the principal components can be used to interpret the results of PCA.

- The explained variance is the proportion of the total variance in the data that is explained by each principal component.
- The loadings are the coefficients that describe the linear combination of the original variables that make up each principal component.
