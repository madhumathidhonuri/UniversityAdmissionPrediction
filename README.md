# 🎓 University Admission Predictor (Machine Learning + Django)

This is a full-stack web application that predicts a student's chance of university admission based on their academic profile.

It combines a machine learning model (trained on a graduate admission dataset) with a Django backend and a simple HTML/CSS frontend.



## Key Components

* **Machine Learning Model:** A Jupyter Notebook (`AdmissionModel.ipynb`) that explores the data, compares 4 different regression models (Linear Regression, Ridge, Lasso, Random Forest), and selects the best-performing model.
* **Django Web App:** A user-friendly web form where you can enter academic scores (GRE, TOEFL, CGPA, etc.) and receive an instant admission chance prediction.

## 🤖 Machine Learning Model Insights

The final model selected was a **Linear Regression** model, as it provided the best performance for this linear dataset.

* **Best R² Score:** **0.8188** (The model can explain ~81.9% of the variance in admission chances.)
* **Best MAE:** **0.0427** (On average, the model's predictions are only off by ~4.3%.)

### Feature Importance
The analysis showed that `CGPA` is by far the most important factor in predicting admission, followed by `GRE Score` and `TOEFL Score`.
<img width="1366" height="746" alt="image" src="https://github.com/user-attachments/assets/a2b4c08b-4f2b-4de8-91d6-9027c94e72c6" />

## 🛠️ Tech Stack

* **Backend:** Django
* **Machine Learning:** Scikit-learn, Pandas, NumPy, Joblib
* **Data Analysis:** Jupyter Notebook, Matplotlib, Seaborn

## 🚀 How to Run This Project Locally

Follow these steps to get the project running on your local machine.

### 1. Clone the Repository

```bash
git clone [https://github.com/madhumathidhonuri/UniversityAdmissionPrediction.git](https://github.com/madhumathidhonuri/UniversityAdmissionPrediction.git)
cd UniversityAdmissionPrediction
