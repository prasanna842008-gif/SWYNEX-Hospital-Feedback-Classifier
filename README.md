# SWYNEX – Hospital Feedback Classification Using Machine Learning

## 1. Project Overview

SWYNEX Hospital Feedback Classifier is a Machine Learning-based application designed to analyse hospital patient feedback and classify it into three categories:

- **Positive** – Feedback expressing satisfaction with hospital services.
- **Negative** – Feedback expressing dissatisfaction with hospital services.
- **Neutral** – Feedback containing general or objective information.

The project demonstrates how Artificial Intelligence and Machine Learning can help organise and understand patient feedback.

## 2. Problem Statement

Hospitals receive feedback from patients about doctors, nurses, facilities, waiting times and overall services. Manually reviewing large amounts of feedback can be time-consuming.

This project aims to develop a simple Machine Learning application that automatically classifies hospital feedback into Positive, Negative and Neutral categories.

## 3. Methodology

The application uses the following Machine Learning approach:

1. **Data Collection:** A dataset containing 120 hospital feedback examples, with 40 examples in each category.
2. **Data Preprocessing:** Feedback text and labels are loaded and prepared for model training.
3. **Feature Extraction:** TF-IDF (Term Frequency–Inverse Document Frequency) converts text into numerical features. Unigrams and bigrams are used.
4. **Model Training:** Logistic Regression is used to train the classification model.
5. **Prediction:** The trained model predicts the sentiment category of new feedback.
6. **Evaluation:** The model is evaluated using Accuracy, Precision, Recall, F1-score, a classification report and a confusion matrix.

### Technologies Used

- Python
- Flask
- Pandas
- Scikit-learn
- TF-IDF
- Logistic Regression
- HTML and CSS

## 4. Application Features

- Classifies feedback into three sentiment categories.
- Provides a simple web interface.
- Accepts patient feedback for analysis.
- Displays prediction results and related messages.
- Handles empty feedback input.
- Handles excessively long feedback.
- Includes model evaluation and failure-case analysis.

## 5. Demo – How to Run the Application

### Requirements

- Python installed on your computer.
- Required Python libraries.

### Installation

Clone the repository:

```bash
git clone https://github.com/prasanna842008-gif/SWYNEX-Hospital-Feedback-Classifier.git
```

Open the project folder:

```bash
cd SWYNEX-Hospital-Feedback-Classifier
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

Enter hospital feedback and click the analysis button to view the predicted category.

### Model Evaluation

The model was evaluated using a stratified train-test split:

- Total records: 120
- Training records: 90
- Testing records: 30

**Evaluation Results:**

| Metric | Result |
|---|---:|
| Accuracy | 53.33% |
| Precision (Macro) | 49.47% |
| Recall (Macro) | 53.33% |
| F1-score (Macro) | 50.39% |

### Confusion Matrix

Label order: Positive, Negative, Neutral.

| Actual / Predicted | Positive | Negative | Neutral |
|---|---:|---:|---:|
| Positive | 2 | 4 | 4 |
| Negative | 4 | 5 | 1 |
| Neutral | 1 | 0 | 9 |

The evaluation also identifies incorrect predictions to help understand the model's weaknesses.

## 6. Limitations

- The dataset is small and contains only 120 feedback examples.
- The dataset is an educational dataset and may not represent real-world hospital feedback.
- The model may incorrectly classify feedback containing complex language, mixed sentiments or context-dependent expressions.
- The evaluation results show that the model needs further improvement.
- The application does not understand the full clinical context of patient experiences.
- Performance may vary when new or different feedback is provided.

## 7. Ethics and Responsible AI

- Patient privacy should be protected when handling feedback.
- Personal and confidential medical information should not be uploaded to public datasets.
- The system should be used responsibly and should not make medical decisions.
- Predictions should be reviewed by a human before any important action is taken.
- The model may produce incorrect predictions, so its output should not be treated as completely reliable.
- This project is developed for educational and demonstration purposes only.

## 8. Future Enhancements

- Increase the size and diversity of the dataset.
- Improve model accuracy and classification performance.
- Test with properly anonymised real-world feedback.
- Explore advanced Natural Language Processing techniques.
- Improve the user interface and reporting features.

## 9. Project Structure

```text
SWYNEX-Hospital-Feedback-Classifier/
│
├── app.py
├── model.py
├── dataset.csv
├── evaluation.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 10. Conclusion

The SWYNEX Hospital Feedback Classifier demonstrates the use of Machine Learning for automatic hospital feedback classification. The project includes a Flask-based interface, text processing, model prediction, input validation, error handling and model evaluation.

It also highlights the importance of identifying model limitations and developing responsible AI applications.

**Project developed as part of the SWYNEX Technologies Internship.**

