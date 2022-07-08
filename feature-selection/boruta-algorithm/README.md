## Boruta Algorithm

Boruta is a feature selection algorithm based on a statistical approach. It relies in two principles: `shadow features` and `binomial distributions`.

**1. Shadow Features:**

The first step of the Boruta algorithm is to evaluate the feature importances. This is usually done in tree-based algorithms, but on Boruta the features do not compete among themselves, they compete with their randomized versions called “shadow features”, for instance:

<p align="center">
  <img src="https://miro.medium.com/max/700/1*zStvS_9GpDEJJFZb0AvG4Q.png">
</p>

Now we evaluate the feature importances of all 6 features using any method of preference, as a DecisionTree, RandomForest, XGBoost or any other. The idea of the Boruta algorithm is that a feature is useful only if it’s capable of doing better than the best randomized feature, represented here by the shadow features, so we compare the importances of the original features with the **highest feature importance of the shadow features**. Every time a feature has a higher importance than this threshold, we call it a “hit”. For the above example, we would have:

<p align="center">
  <img src="https://miro.medium.com/max/700/1*btH1CNb6lQ62zakBxYECYg.png">
</p>

The threshold in this example is the maximum of 11%, 14%, 9%. `age` and `height` made a hit. Due that the importance of `weight` is below the threshold, we could think keep only the hits and discard the other, but what if it was an unlucky run for `weight`?

Here is where the second principle of Boruta into play, which is based on iterations.

**2. Binomial distribution:**

All features will have only two outcomes: "hit" or "not hit", therefore we can perform the previous step several times and build a binomial distribution for each feature, where the maximum level of uncertainty about the feature is expressed by a probability of 50%. In the current example, we perform the step 1, 20 times and we obtain the following results:

<p align="center">
  <img src="https://miro.medium.com/max/700/1*Zly3ZYolDDsvn8x8_MeIeg.png">
</p>

In Boruta, there is not a hard threshold between a refusal and an acceptance area. Instead, there are 3 areas:

1. Refusal area / Features to drop (the red area): the features that end up here are considered as noise, so they are dropped;
2. Irresolution area / Features to keep tentatively (the blue area): Boruta is indecisive about the features that are in this area;
3. Acceptance area / Features to keep (the green area): the features that are here are considered as predictive, so they are kept.

The areas are defined by selecting two extreme portions (something like significance level), in our example is 1% (each tail has 0.5% of the distribution).

<p align="center">
  <img src="https://miro.medium.com/max/700/1*yqAUlMtPUiFyr8gYLFagTA.png">
</p>

Finally, in this example we can see that `age` is predictive and should be kept, `weight` should be dropped and the decision of `height` is up to us.

## Examples

We use the Sisben III 2019 data in order to explain how to use boruta:

1. [Data preparation](https://github.com/sebasjp/data-science-applications/blob/master/feature-selection/boruta-algorithm/notebooks/01-prepare_data.ipynb)
2. [Boruta from scratch](https://github.com/sebasjp/data-science-applications/blob/master/feature-selection/boruta-algorithm/notebooks/02-boruta-from-scratch.ipynb)
3. [Boruta packages (BorutaPy and BorutaShap)](https://github.com/sebasjp/data-science-applications/blob/master/feature-selection/boruta-algorithm/notebooks/03-BorutaPy-BorutaShap.ipynb)

## References

* Credits about the Boruta explination: https://towardsdatascience.com/boruta-explained-the-way-i-wish-someone-explained-it-to-me-4489d70e154a
* https://www.jstatsoft.org/article/view/v036i11
* https://towardsdatascience.com/boruta-shap-an-amazing-tool-for-feature-selection-every-data-scientist-should-know-33a5f01285c0
