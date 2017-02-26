# Results

## Chris vs Sara emails ("Enron emails" training set)

| Lesson  | Classifier Algorithm | Accuracy | Training set <sup id="a5">[5](#f5)</sup> | Feature set <sup id="a3">[3](#f3)</sup> | Training time | Prediction time |
| :-----: | :------------------: | :------: | :----------: | :---------: | :-----------: | :-------------: |
| Naive Bayes | Gaussian Naive Bayes | 0.97326 | 100% | 10%% | 2.58s | 0.321s    |
| SVM | SVM (Kernel <sup id="a1">[1](#f1)</sup>: Linear) | 0.98407 | 100% | 10%% | 232.457s | 24.674s |
| SVM | SVM (Kernel: Linear) | 0.88452 | 10% | 10%% | 0.239s | 1.966s |
| SVM | SVM (Kernel: Radial Basis Function (RBF)) | 0.61604 | 10% | 10%% | 0.162s | 1.927s |
| SVM | SVM (Kernel: RBF, C=10 <sup id="a2">[2](#f2)</sup>) | 0.61604 | 10% | 10%% | 0.148s | 1.642s |
| SVM | SVM (Kernel: RBF, C=100) | 0.61604 | 10% | 10%% | 0.163s | 1.582s |
| SVM | SVM (Kernel: RBF, C=1K) | 0.82138 | 10% | 10%% | 0.147s | 1.482s |
| SVM | SVM (Kernel: RBF, C=10K) | 0.89249 | 10% | 10%% | 0.146s | 1.317s |
| SVM | SVM (Kernel: RBF, C=10K) | 0.99089 | 100% | 10%% | 184.227s | 18.85s |
| Decision Trees | Decision Tree (Min. Sample Split: 40) | 0.97554 | 100% | 10%% | 123.371s | 0.077s |
| Decision Trees | Decision Tree (Min. Sample Split: 40) | 0.96700 | 100% | 1%% <sup id="a4">[4](#f4)</sup> | 7.522s | 0.004s |

## Terrain classification

| Lesson  | Classifier Algorithm | Accuracy | Training set <sup id="a6">[6](#f6)</sup> | Feature set <sup id="a7">[7](#f7)</sup> | Training time | Prediction time |
| :-----: | :------------------: | :------: | :----------: | :---------: | :-----------: | :-------------: |
| Naive Bayes | Gaussian Naive Bayes | 0.884 | 100% | 2 | **0.001s** | **0.001s** |
| SVM | SVM (RBF kernel, C=10k) | 0.932 | 100% | 2 | 0.034s | 0.003s |
| Decision Trees | Decision Tree (Min. Sample Split: 40) | 0.912 | 100% | 2 | 0.002s | **0.001s** |
| Choose your own Algorithm | K-Nearest Neighbors (default) | 0.92 | 100% | 2 | **0.001s** | 0.002s |
| Choose your own Algorithm | AdaBoost (default) | 0.924 | 100% | 2 | 0.158s | 0.006s |
| Choose your own Algorithm | AdaBoost (200 estimators) | 0.916 | 100% | 2 | 0.584s | 0.021s |
| Choose your own Algorithm | Random Forest (default) | 0.912 | 100% | 2 | 0.034s | 0.009s |
| Choose your own Algorithm | Random Forest (Min. Sample Split: 40) | 0.924 | 100% | 2 | 0.04s | 0.014s |
| Choose your own Algorithm | Random Forest (10 estimators, no max depth, Min. Sample Split: 2) | 0.932 | 100% | 2 | 0.044s | 0.012s |
| Choose your own Algorithm | Extremely Randomized Trees (default) | 0.936 | 100% | 2 | 0.036s | 0.05s |
| Choose your own Algorithm | Extremely Randomized Trees (Min. Sample Split: 30) | 0.924 | 100% | 2 | 0.041s | 0.009s |
| Choose your own Algorithm | Extremely Randomized Trees (10 estimators, no max depth, Min. Sample Split: 2) | **0.944** | 100% | 2 | 0.034s | 0.012s |

## Footnotes

* <sup id="f1">1</sup> A simple example of the behavior of _linear_ vs _poly_ vs _rbf_ kernels,
  offered by this algorithm can be found
  [here](http://scikit-learn.org/stable/auto_examples/svm/plot_svm_regression.html). [↩](#a1)
* <sup id="f2">2</sup> The C parameter tells the SVM optimization how much you want to avoid
  misclassifying each training example: it's a penalty parameter. [↩](#a2)
* <sup id="f3">3</sup> `10` percentile of the Features set is `3785`. [↩](#a3)
* <sup id="f4">4</sup> `1` percentile of the Features set is `379`. [↩](#a4)
* <sup id="f5">5</sup> Training set contains `15820` data points. [↩](#a5)
* <sup id="f6">6</sup> Training set contains `750` data points, and Test set contains `250` data points: all auto-generated. [↩](#a6)
* <sup id="f7">7</sup> Every data point has 2 features: road _grade_ and road _bumpy(ness)_. [↩](#a7)
