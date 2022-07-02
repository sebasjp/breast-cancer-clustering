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


<p align="center">
  <img src="https://miro.medium.com/max/700/1*yqAUlMtPUiFyr8gYLFagTA.png">
</p>




## References

* https://towardsdatascience.com/boruta-explained-the-way-i-wish-someone-explained-it-to-me-4489d70e154a
* https://www.jstatsoft.org/article/view/v036i11
* https://towardsdatascience.com/boruta-shap-an-amazing-tool-for-feature-selection-every-data-scientist-should-know-33a5f01285c0