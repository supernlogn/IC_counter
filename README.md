# IC_counter
Information Criterions Counter Example
---

This repository contains counterexamples for not using the information criteria.
Every scientist who uses information criteria should not rely only on them,
because they may lead to a false analysis.

At the same time, because no scientist could be base its approximation only with
these criteria, so no computer algorithm should also not do. Trying to figure out the
right model by using only these criteria produces many errors not only at the final model, but even during its estimation. That is because if the worng type of model is peaked then there may be namy numerical instabilities in the computation.

For example in the notebook given we cannot use an `ARIMA(2,1,2)` because for MA term equal to 2
it results in a numerically anstable approximation.
