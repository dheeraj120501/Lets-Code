# Introduction

In the applications that require good interpretability of the model, Descision trees work very well especially if they are of small depth.

However, descision trees with real-world datasets can have large depths making them more prone to overfitting and thus lead to higher variance in the model. This shortcoming of DTs is explored by the Random Forest model.

In the Random Forest model, the original training data is randomly sampled-with-replacement generating small subsets of data known as bootstrap samples.

- These bootstrap samples are then fed as training data to many DTs of large depths.
- Each of these DTs is trained separately on these bootstrap samples. This aggregation of DTs is called the Random Forest ensemble.

The concluding result of the ensemble model is determined by counting a majority vote from all the DTs. This concept is known as Bagging or Bootstrap Aggregation.

- Since each DT takes a different set of training data as input, the deviations in the original training dataset do not impact the final result obtained from the aggregation of DTs.
- Therefore, bagging as a concept reduces variance without changing the bias of the complete ensemble.

# Out of Bag (OOB) score

Out of bag (OOB) score is a way of validating the Random forest model.

The rows which are left out or not used for training a particular descision tree in Random Forest is called the Out of Bag sample of that DT.

Each of the OOB sample rows is passed through every DT that did not contain the OOB sample row in its bootstrap training data and a majority prediction is noted for each row.

- As a result only a subset of DTs is used for determining the OOB score.

The OOB score is computed as the number of correctly predicted rows from the out of bag sample.

## OOB score VS Validation score

Validation score and OOB score are unalike, computed in a different manner and should not be thus compared.

OOB score is computed on data that was not necessarily used in the analysis of the model. Whereas for calculation validation score, a part of the original training dataset is actually set aside before training the models.

OOB score is calculated using only a subset of DTs not containing the OOB sample in their bootstrap training dataset. While the validation score is calculated using all the DTs of the ensemble.

## When to use it

In general, validation on a full ensemble of DTs is better than a subset of DT for estimating the score.

In cases where we do not have a large dataset and want to consume it all as the training dataset and can't afford a validation dataset, the OOB score provides a good trade-off.

In an ideal case, about 36.8% of total training data are available as OOB sample for each DT and hence it can be used for evaluating or validating the random forest model.
