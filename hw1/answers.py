r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

# ==============
# Part 1 answers

part1_q1 = r"""
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


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part3_q2 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part3_q3 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

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
