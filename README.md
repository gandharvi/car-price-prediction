# Car Price Predictor

This repository contains the code for a car price prediction model and a Streamlit application. The model predicts the price of a car based on various features such as Manufacturer, Model, Category, Leather Interior, Fuel Type, Gear Box Type, Drive Wheels, Wheel, Color, Levy, Engine Volume, Mileage, Cylinders, Airbags, and Age.

## Dataset

The dataset is from kaggle

### InconsistentVersionWarning

If you encounter the `InconsistentVersionWarning`:

```
InconsistentVersionWarning: Trying to unpickle estimator DecisionTreeRegressor from version 1.2.2 when using version 1.5.1.
```

This indicates a version mismatch between the version used to save the model and the version used to load the model. Ensure you are using `scikit-learn==1.2.2`.

