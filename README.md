
# 🎯 RiskEd – Student Dropout Risk Predictor

---

## Basic Details

**Team Name:** CodeNova

### Team Members

Member 1: Swetha C R – Muthoot Institute of Technology and Science
Member 2: Aarathi Krishna – Muthoot Institute of Technology and Science

---

## 🌐 Hosted Project Link

[https://your-render-link.onrender.com](https://your-render-link.onrender.com)

---

# 📌 Project Description

RiskEd is a Machine Learning powered web application that predicts whether a student is at risk of dropping out based on academic and behavioral indicators. It provides a risk classification along with a probability score to enable early intervention.

---

# ❗ The Problem Statement

Student dropout is a major challenge in educational institutions.
Most institutions take action only after students fail or leave.

There is no early-warning predictive system to identify at-risk students.

---

# 💡 The Solution

We built a predictive analytics web app using Logistic Regression that:

* Analyzes attendance, marks, fee delays, backlogs, and extracurricular participation
* Predicts dropout risk (High / Low)
* Provides probability percentage
* Enables early intervention strategies

This shifts institutions from reactive to predictive decision-making.

---

# ⚙ Technical Details

## Technologies/Components used

## 🖥 For Software

### Languages Used:

* Python
* HTML
* CSS

### Frameworks Used:

* Flask

### Libraries Used:

* pandas
* numpy
* scikit-learn
* pickle

### Tools Used:

* VS Code
* Git
* GitHub
* Render (Deployment)

---

# 🚀 Features

Feature 1: Predicts dropout risk using ML
Feature 2: Displays probability percentage
Feature 3: Clean, responsive UI
Feature 4: Deployable on cloud platforms

---

# 🛠 Implementation

## Installation

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install flask numpy pandas scikit-learn
```

---

## Run

Train model:

```bash
python train_model.py
```

Run app:

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

# 📸 Project Documentation

## Screenshots

### Screenshot 1 – Home Page



### Screenshot 2 - Prediction of high risk



### Screenshot 3 – Prediction of low risk


---

# 🏗 System Architecture

### Architecture Explanation

1. User enters student details via Web UI
2. Flask backend receives input
3. ML model processes data
4. Prediction and probability generated
5. Results rendered on frontend

### Tech Stack Flow

Frontend (HTML/CSS)
⬇
Flask Backend
⬇
Trained ML Model (Logistic Regression)
⬇
Prediction Output

---

# 🔄 Application Workflow

1. User inputs student metrics
2. Data sent to Flask
3. Converted into NumPy array
4. Model predicts risk
5. Probability calculated
6. Result displayed

---

# 📡 API Documentation

Base URL:

```
https://your-render-link.onrender.com
```

---

### GET /

Description: Loads homepage

---

### POST /predict

Description: Predict dropout risk

Request Body (Form Data):

```
attendance
avg_marks
fee_delay
backlogs
extracurricular
```

Response:
Displays rendered HTML page with:

* Risk classification
* Probability %

---

# 🎥 Project Demo

Video:
(Add YouTube or Drive link)

The video demonstrates:

* Entering student data
* Predicting dropout risk
* Displaying probability
* Explanation of ML model logic

---

# 🤖 AI Tools Used (Transparency Section)

Tool Used: ChatGPT

Purpose:

* Code debugging
* Model explanation
* Presentation preparation
* Documentation formatting

Key Prompts Used:

* "Create a Flask ML integration"
* "Explain logistic regression in simple terms"
* "Generate hackathon pitch"

Estimated AI-generated code: ~25% (boilerplate & documentation)

Human Contributions:

* System design
* Model training logic
* Dataset preparation
* UI styling
* Deployment configuration

---

# 👥 Team Contributions

Swetha C R:

* Backend development
* ML model training
* Flask integration

Aarathi Krishna:

* Frontend design
* Testing
* Deployment
* Documentation

---

# 📜 License

This project is licensed under the MIT License.

---

# ❤️ Made with dedication at TinkerHub Hackathon

---

