# 📊 Customer Churn Prediction System (Django + Machine Learning)

This is a web-based AI-powered Customer Churn Prediction System built using **Django** and **Machine Learning**. The system allows businesses to input customer attributes and get predictions about the likelihood of customer churn, helping improve retention strategies.



## 🚀 Features

- 🎯 Predict whether a customer will churn or not
- 📈 Show churn probability percentage
- 🧠 Machine Learning models: Logistic Regression, Decision Tree, Random Forest, XGBoost, ANN
- 📊 EDA Dashboard with insights (visualizations)
- 🌗 Light/Dark Theme toggle
- 🔁 Navigate between prediction and dashboard
- 🎨 Bootstrap-styled UI with enhanced visuals



## 🛠️ Tech Stack

| Technology     | Purpose                             |
|----------------|-------------------------------------|
| Python         | Core programming language           |
| Django         | Backend web framework               |
| scikit-learn   | ML model building & evaluation      |
| XGBoost        | Advanced boosting model              |
| Keras/TensorFlow | ANN model for deep learning       |
| Pandas, NumPy  | Data manipulation                   |
| Matplotlib, Seaborn | Data visualization             |
| Bootstrap 5    | Frontend styling                    |
| SQLite3        | Default Django database             |


## 📂 Project Structure

Customer_Churn_Prediction/
├── churn_project/
│ ├── churn_app/
│ │ ├── templates/churn_app/
│ │ │ ├── form.html
│ │ │ ├── result.html
│ │ │ ├── dashboard.html
│ │ ├── static/images/
│ │ │ └── [EDA and ROC curve plots]
│ │ ├── views.py
│ │ ├── forms.py
│ ├── settings.py
│ ├── urls.py
├── models/
│ ├── churn_model.pkl
│ ├── scaler.pkl
│ ├── model_columns.pkl
├── requirements.txt
├── README.md


## 📌 Notes
You can upload different models in the /models/ folder and update your Django view accordingly.

The model_columns.pkl must match the features used during prediction (especially if you're using engineered features like engagement_score).

## 🤖 ML Models Included

✅ Logistic Regression

✅ Decision Tree

✅ Random Forest

✅ XGBoost

✅ Artificial Neural Network (Keras)

## 📈 Visuals Included

**1)** Churn Distribution

**2)** Churn vs Contract Type

**3)** Churn vs Internet Service

**4)** Churn vs Monthly Charges

**5)** ROC Curves for all models

**6)** Monthly Sales Trend

**7)** Model Performance Comparison

## 🧾 License
This project is licensed under the MIT License.

## 🙋‍♀️ Author

**Archana Pati**

**💼 Data Analyst**

**📍 Bangalore, Karnataka**

**📧 Email:** patiarchana.ap@gmail.com

**🔗 GitHub:** github.com/Archana98-bit

