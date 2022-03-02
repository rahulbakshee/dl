# This repo has some works on AutoEncoders and it's applications in Fraud Detection,Aanomaly Detection, Rare event Detection, Class Imbalance


There are some ususal recommendations for working on Class Imbalance such as:

### Buy or Create more data
- not always possible in real world
### Data Level
- Oversampling the minority class.
- Undersampling the majority class.
- Combination of OverSampling and UnderSampling.
- Synthesize new minority classes.(SMOTE)
### Algorithm Level
- Use class weights (higher weights for minority class)
- Use different classification threshold rather tha default 0.5
- Use complex tree based algorithms like XGBoost / LightGBM etc.
- Focus on specific metric (Precision/Recall/F1-Score).
- Ensemble of Algorithms.
- Cross Validation strategy with StratifiedKFold.
- Neural Networks and Deep Learning.
### Semi-Supervised Learning
- Instead of Classification, reframe problem as Anomaly detection, a.k.a. outlier detection
- AutoEncoders to the rescue

etc....



In our approach, we will use AutoEncoders, which has two aspects:-

We will be using the power of autoencoders to understand the hidden representation of the data. This part is also called `unsupervised learning`
Then using the representation we can transform the data and predict(on test set) using simple linear algorithms and the lables given to us in .csv file. This part is called `supervised learning`

