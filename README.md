<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# [Project Name] 🎯

## Basic Details

### Team Name: CodeNova

### Team Members
- Member 1: Swetha C R - Muthoot Institute of Technology and Science
- Member 2: Aarathi Krishna - Muthoot Institute of Technology and Science

### Hosted Project Link
(https://github.com/Aarathi-K/RiskEd-student-dropout-preediction.git)

### Project Description
RiskEd is a Machine Learning powered web application that predicts whether a student is at risk of dropping out based on academic and behavioral indicators. It provides a risk classification along with a probability score to enable early intervention.

### The Problem statement
RiskEd is a Machine Learning powered web application that predicts whether a student is at risk of dropping out based on academic and behavioral indicators. It provides a risk classification along with a probability score to enable early intervention.

### The Solution
We built a predictive analytics web app using Logistic Regression that:

  --Analyzes attendance, marks, fee delays, backlogs, and extracurricular participation
  --Predicts dropout risk (High / Low)
  --Provides probability percentage
  --Enables early intervention strategies

This shifts institutions from reactive to predictive decision-making.

## Technical Details
### Technologies/Components Used

**For Software:**
🖥 For Software
Languages Used:
Python
HTML
CSS

Frameworks Used:
Flask

Libraries Used:
pandas
numpy
scikit-learn
pickle

Tools Used:
VS Code
Git
GitHub

Render (Deployment)

## Features

List the key features of your project:
Feature 1: Predicts dropout risk using ML
Feature 2: Displays probability percentage
Feature 3: Clean, responsive UI
Feature 4: Deployable on cloud platforms

---

## Implementation

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


## Project Documentation

### For Software:

#### Screenshots (Add at least 3)

Home page of our website
<img width="1920" height="1080" alt="Screenshot (175)" src="https://github.com/user-attachments/assets/d38915a6-d589-4f3f-b053-2c86da0f4f50" />



User entering inputs
<img width="1920" height="1080" alt="Screenshot (176)" src="https://github.com/user-attachments/assets/c92a484c-1760-490b-a9e9-8b8699cfbaf4" />


High risk prediction
<img width="1920" height="1080" alt="Screenshot (178)" src="https://github.com/user-attachments/assets/0a5b7e59-b2c3-432c-9f84-ca1e8c35b45d" />


Low risk prediction

<img width="1920" height="1080" alt="Screenshot (177)" src="https://github.com/user-attachments/assets/ba96188e-04dc-4ba8-8b1d-5b984d76367b" />


#### Diagrams

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
(https://github.com/Aarathi-K/RiskEd-student-dropout-preediction.git)
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
[Drive link](https://drive.google.com/file/d/1aIKkHqC1nLGKvGMpMuuugMjHqaMyxhf0/view)

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

