# Evaluate your Model using the F-score

* The F-score or F-measure is a metric for indicating the accuracy of a classification model. After obtaining the precision and recall on your test set, you can calculate the F1-score with following formula:

* The maximum possible value is 1, which indicates a perfect model. If either precision or recall is 0, the -score is 0 as well.

* In the formula above, we state that precision is as important as recall for our application; that is why we write . We will use this version of the metric in this template via the scikit-learn's function f1_score(). However, you can also apply weights to the precision or recall with the -score.

* First, we need to convert the probabilities predicted by our model to actual binary predictions. In this example, we will use a threshold of 0.65; predictions under this threshold will be mapped to 0, the other predictions to 1.

* Now we can go ahead and calculate the -score using the scikit-learn package.

* The -score is about 0.7. That is pretty good, but this probably can be increased depending on the threshold that you use. You can change the threshold to try to get a better classification model.
