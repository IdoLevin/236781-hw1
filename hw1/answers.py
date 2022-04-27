r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

# ==============
# Part 1 answers

part1_q1 = r"""
**Your answer:**

1. False.
 
The test set is used to estimate the out-sample error, 
not the in-sample error which is determined by the training set. 

2. False. 

The split should be random, for the 2 sets to be iid. 
If the split is deterministic, e.g. always taking the first samples as the training set and the last samples as 
the test set, then the distributions of the 2 sets might be different or dependent in each other, 
because of patterns in the dataset order.

Also, the train set should be large, because it is more important to train well than to test well. 
E.g. if the training set would be 10% of the dataset, then the test would be very good but 
the resulting model would not be as good as it could be. 

3. True. 

Cross-validation is using the training set for validation. 
Using the test set would make the out-sample error estimation invalid. 

4. False. 

During cross-validation, we use the validation-set performance to choose the model. <br/>
After cross-validation, we use the test-set performance to estimate the generalization error. 

The validation-set cannot be used to evaluate the model, because it was used to choose it. 
"""

part1_q2 = r"""
**Your answer:**
No.

Our friend decided to use the test set as a validation set, after having used it once as a test set. 
It is fine to use it as a validation set in this case, i.e. in practice, the validation will work well. 

The problem is that he would not have a test set. 
He would have to produce more data in order to test the resulting model. 
To avoid producing more data, he should use cross-validate on the training set, 
and then he will be able to use the test set for testing. 

However, he did already use the test set once, and therefore he would need a new test set anyway.
"""

# ==============
# Part 2 answers

part2_q1 = r"""
**Your answer:**

No, increasing k too much would not result in a model with better generalization. 
Increasing k makes the kNN classifier decide by more far away train set examples, that might be irrelevant for 
the decision because they are too far. 
Consider for instance the extremal example of k=$\infty$, or making k as large as the training set size: 
the classifier decides using the entire training set. 

However, decreasing k too much makes the learner prone to overfitting.
It would be more vulnerable to outliers that do not represent their vicinity well. 
"""

part2_q2 = r"""
**Your answer:**

1. The train-set accuracy is not a good measure of generalization, because it cannot detect overfit classifiers. 

2. Using the test-set for validation contaminates the test-set, so we will not be able to use it afterwards to 
estimate the generalization error. 
"""

# ==============

# ==============
# Part 3 answers

part3_q1 = r"""
**Your answer:**

One can obtain the same model for any $\Delta$, by adjusting $\lambda$. 
The selection of $\Delta$ is arbitrary because it must be selected together with $\lambda$. 

First, note that one can multiply a linear classifier's weights by some scalar, and get 
an equivalent linear classifier, i.e. a classifier that would classify any example by the same way as the original one. 
However, its scores and hence its margin would be multiplied by the scalar.

In this manner, one can escape the penalty for any such 



First, let us explain the meaning of the parameter Delta. 
The soft SVM loss function penalizes for every difference 
$\vectr{w_j} \vec{x_i} - \vectr{w_{y_i}} \vec{x_i}\right$ 
between the ground truth class prediction score and 
a wrong class prediction score, that is too small. Namely, smaller than Delta.  

The effect of making Delta larger, is that more examples are penalized, 

Note that by multiplying the weights of the linear classifier by some scalar, makes an equivalent model   

By multiplying the vector $\vectr{w}$ of the linear classifier by some scalar, 
all of the differences in favor of the ground truth class become larger and escape the penalty. 

What stops the optimization scheme from choosing a large $\vectr{w}$ is the regularization term. 


"""

part3_q2 = r"""
**Your answer:**

1. We know that the class prediction scores are simply weighted sums of the pixel values. 
Every digit has weights. 
Pixels that are often white in images of the digit receive high weights, and those often black receive low weights.
We see that in the weights_as_images visualization. 
Hence, it learns the statistics which pixels are often white, which are often black, 
and which do not affect it. 

Indeed, some wrongly classified images have pixels where they must not have. The 2 classified as a 7 has lines similar 
to lines that images of 7 have. 
The 8 classified as an 6 has few white pixels, and those it does are precisely where the 6 weights put large weights. 

2. In SVM, the score is based on all training images, whereas in KNN it is only based on K training images. 
In SVM, the score is a weighted sum of the test image, whereas in KNN it is its distance from training images.    

"""

part3_q3 = r"""
**Your answer:**

1. We think that our learning rate is pretty good. 
If it were too high, the curve wouldn't be so smooth, it would have some rise and falls along the way, because 
the large steps would skip the minimum. 
If it were too low, the convergence would be too slow, but it seems fine. 
 
 
2. 
The graph shows that the model performs better on the training set, so we may say that it slightly overfits. 
We say only slightly, because it is expected, and the test performance is pretty good. 


"""

# ==============

# ==============
# Part 4 answers

part4_q1 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part4_q2 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part4_q3 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============
