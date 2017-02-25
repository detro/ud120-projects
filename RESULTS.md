# Results

## Chris vs Sara emails ("Enron emails" training set)
| Lesson  | Classifier Algorithm | Accuracy | Training set | Feature set | Training time | Prediction time |
| :-----: | :-------: | :------: | :-----------: | :-------------: |
| Naive Bayes | Gaussian Naive Bayes | 0.97326 | 100% <sup id="a5">[5](#f5)</sup> | 10%% <sup id="a3">[3](#f3)</sup> | 2.58s | 0.321s    |
| SVM | SVM (Kernel <sup id="a1">[1](#f1)</sup>: Linear) | 0.98407 | 100% | 10%% | 232.457s | 24.674s |
| SVM | SVM (Kernel: Linear) | 0.88452 | 10% | 10%% | 0.239s | 1.966s |
| SVM | SVM (Kernel: Radial Basis Function (RBF)) | 0.61604 | 10% | 10%% | 0.162s | 1.927s |
| SVM | SVM (Kernel: RBF, C=10 <sup id="a2">[2](#f2)</sup>) | 0.61604 | 10% | 10%% | 0.148s | 1.642s |
| SVM | SVM (Kernel: RBF, C=100) | 0.61604 | 10% | 10%% | 0.163s | 1.582s |
| SVM | SVM (Kernel: RBF, C=1000) | 0.82138 | 10% | 10%% | 0.147s | 1.482s |
| SVM | SVM (Kernel: RBF, C=10000) | 0.89249 | 10% | 10%% | 0.146s | 1.317s |
| SVM | SVM (Kernel: RBF, C=10000) | 0.99089 | 100% | 10%% | 184.227s | 18.85s |
| Decision Trees | Decision Tree (Min. Sample Split: 40) | 0.97554 | 100% | 10%% | 123.371s | 0.077s |
| Decision Trees | Decision Tree (Min. Sample Split: 40) | 0.96700 | 100% | 1%% <sup id="a4">[4](#f4)</sup> | 7.522s | 0.004s |

## Footnotes

* <sup id="f1">1</sup> A simple example of the behavior of _linear_ vs _poly_ vs _rbf_ kernels,
  offered by this algorithm can be found
  [here](http://scikit-learn.org/stable/auto_examples/svm/plot_svm_regression.html). [↩](#a1)
* <sup id="f2">2</sup> The C parameter tells the SVM optimization how much you want to avoid
  misclassifying each training example: it's a penalty parameter. [↩](#a2)
* <sup id="f3">3</sup> `10` percentile of the Features set is `3785`. [↩](#a3)
* <sup id="f4">4</sup> `1` percentile of the Features set is `379`. [↩](#a4)
* <sup id="f5">5</sup> Training set contains `15820` data points. [↩](#a4)
