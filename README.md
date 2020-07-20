# Diamond Price 

![Diamond](https://github.com/Jorge-Doncel/Diamond_ML/blob/master/input/diamond-diagram.png)

## Table of Contents


- [Objective](#Objective)
- [Libraries](#libraries)
- [Data Processing](#data-processing)
- [Conclusions](#Conclusions)

## Objective

Calculate the price of diamonds using Machine Learning. Also, 8 different models have been used to achieve the best result:

 - MLPRegressor
 - RandomForestRegressor
 - KNeighborsRegressor
 - SVR
 - DecisionTreeRegressor
 - AdaBoostRegressor
 - StackingRegressor
 - BaggingRegressor

 ## Libraries

  - Pandas
  - Numpy
  - matplotlib
  - sklearn

  ## Data Processiong

  The columns with string were switch into numeric columns where the highest number is the most important category in that column.

  Also, models were train with 3 differents dataframes:
    - All columns
    - Drop Table and Deph
    - Drop x, y, z

GrindSearch and CrossValidation were used to improve the results of the models.

## Conclusions

RandomForest and BaggingRegressor got the best performance, with the lowers R2 score and MSE.