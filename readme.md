# Capstone Project: Predicting Used Car Price and Used Car Recommender System

## Problem Statement

The price of used cars has increased after the coronavirus pandemic due to the issue of supply chain ([source](https://www.cnbc.com/2023/09/08/used-vehicle-prices-may-have-bottomed-for-2023.html#:~:text=Used%20vehicle%20prices%20have%20been,high%20prices%20amid%20resilient%20demand.)). Making a decision on buying and selling a car is challenging. As a data scientist, we would like to help buyers and sellers on buying and selling their car. The purpose of this project is to build a model to predict the price of used cars and a used car recommender system. Those models will help sellers when they are planning to sell their car and buyers to have an idea when they are looking for a used car. 

---

## Data Collection

* The data was obtained from Kaggle.
* The data collected by Austin Reese from craigslist ([*Kaggle*](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data/data)) 

### Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|price|float|Used Car Dataset|The sell price of used car| 
|year|float|Used Car Dataset|Year of manufacture |
|manufacturer|object|Used Car Dataset|The manufacturer of car|
|condition|object|Used Car Dataset|Condition of used car|
|cylinders|object|Used Car Dataset|Type of used car cylinder|
|fuel|object|Used Car Dataset|Type of used car fuel| 
|odometer|float|Used Car Dataset|The mile of used car|
|title_status|object|Used Car Dataset|Used car title status|
|transmission|object|Used Car Dataset|Transmission of used car|
|drive|object|Used Car Dataset|Drives used car|
|size|object|Used Car Dataset|Sizes used car|
|type|object|Used Car Dataset|Types of used car|
|paint_color|object|Used Car Dataset|The color of used car|
|state|object|Used Car Dataset|States where used car located|

## Imputing Method
* KNN imputer
* Mean and mode imputer base on different range of price
    * 1000 to 15000
    * 15000 to 50000
    * 50000 to 200000

## Table of Result

|Name of Model|Train score|Test score (R2)|RMSE|
|---|---|---|---|
|Baseline (Null model)|0.00|0.00|14504.270|
|Linear Regression (mean imputer)|0.514|0.521|10081.260| 
|RandomForest Regressor (mean imputer)|0.982|0.874|5172.700|
|ExtraTrees Regresssor (mean imputer)|0.952|0.874|5161.382|
|AdaBoost Regressor (mean imputer)|0.961|0.872|5217.493|
|GradientBoosting Regressor (mean imputer)|0.777|0.775|6913.230|
|RandomForest Regressor(pipeline)|0.982|0.874|5167.861|
|ExtraTrees Regressor(pipeline)|0.999|0.873|5179.484|
|RandomForest Regressor (KNN imputer)|0.925|0.836|5853.053|
|ExtraTrees Regresssor (KNN imputer)|0.941|0.840|5781.103|
|AdaBoost Regressor (KNN imputer)|0.953|0.836|5867.411|



## Discussion

* A large number of used car are belong to 2018, 2017, and 2013.
* The top 5 manufacturers that have highest number of car are:
    * ford - American
    * chevrolet - American
    * toyota - Japanese
    * honda - Japanese
    * nissan - Japanese
* Most of used cars are belong to Sedan and SUV follow by pickup and truck. However, the total average price of pickup and truck are approximately double the total average price of sedan and SUV.
* California, Florida, and Texas are the top 3 states that have highest number of used car are selling.
* White, black and silver are the top three colors that have highest number of car and average of price

## Conclusions and Recommendations

* The best performance model is Extra Trees Regressor with lowest RMSE and highest R2 score on both imputing methods.
* Linear Regression and Gradient Boosting have lowest train score and test score but the different between train and test score are small, those models are less overfit.
* The others models have train score higher than test score, those models are overfit but the test scores are improved.
* Tuning hyperparameters can be apply to help improve the overfit.
* Keep the hyperparameter the same, train score, test score, and RMSE will be slightly different when apply the pipeline and without applying the pipeline.
* Using the same model and hyperparameters, models with KNN imputer are less performance than mean imputer. However, those models with KNN imputer are less overfit than those models with mean imputer.
* Due to the limit of computer memory, the cosine similarity was not be able to run for this dataset. Limit the price of the data to limit the amount of data for cosine similarity. 
* The cosine similarity works when limit the data to a small dataset.
* Brand recommender, Price recommender, and All recommender can be use as a recommender system. Those recommender systems do not provide a perfect result but those recommender systems will give a list of used car base on some features that customers are looking for.






