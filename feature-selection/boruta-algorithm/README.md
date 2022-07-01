## Boruta Algorithm

Boruta is a feature selection algorithm based on a statistical approach. It relies in two principles: `shadow features` and `binomial distributions`.

**Shadow Features:**

The first step of the Boruta algorithm is to evaluate the feature importances. This is usually done in tree-based algorithms, but on Boruta the features do not compete among themselves, they compete with their randomized versions called “shadow features”, for instance:

![dataset](https://miro.medium.com/max/700/1*zStvS_9GpDEJJFZb0AvG4Q.png)
