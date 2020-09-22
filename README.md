# IC_counter
Information Criteria Counter Examples

---

This repository contains a few counterexamples for not using the information criteria.
Every scientist who uses information criteria should not rely only on them,
because they may lead to false results.

At the same time, because no scientist can base an approximation only on
these criteria, the same holds for computer algorithm. Trying to figure out the
right model by using only these criteria produces many errors both at the final model predictions, and during its estimation. That is because if the wrong type of model (assumption) is picked then many numerical instabilities may appear in its computations.

For example in the notebook provided, an `ARIMA(2,1,2)` process cannot be used, because for MA term equal to 2
it results in a numerically unstable approximation.

---
Many of the data and ideas are adapted from [here](http://www.jakob-aungiers.com/articles/a/Multidimensional-LSTM-Networks-to-Predict-Bitcoin-Price)
