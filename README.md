
# CareSense AI – Hospital Feedback Classification

## Project Overview
CareSense AI is a Machine Learning-based application that analyses hospital patient feedback and classifies it into three categories: Positive, Negative and Neutral.

## Features
- Automatic hospital feedback classification.
- Positive, Negative and Neutral predictions.
- Input validation and error handling.
- Model evaluation and performance metrics.
- Confusion matrix.
- Failure-case analysis.
- Simple web interface.

## Technologies Used
- Python
- Flask
- Pandas
- Scikit-learn
- HTML
- CSS

## Project Files
- app.py – Flask web application.
- model.py – Machine Learning model.
- dataset.csv – Hospital feedback dataset.
- evaluation.py – Model evaluation and failure-case analysis.
- requirements.txt – Required Python libraries.
- .gitignore – Files excluded from Git tracking.

## How to Run

1. Install the required libraries:

   `pip install -r requirements.txt`

2. Run the application:

   `python app.py`

3. Open your browser:

   `http://127.0.0.1:5000`

## Model Evaluation

The model was evaluated using a test dataset.

- Accuracy: 53.33%
- Precision: 49.47%
- Recall: 53.33%
- F1-Score: 50.39%

The evaluation includes a classification report, confusion matrix and failure-case analysis.

## Future Improvements
- Increase dataset size and diversity.
- Improve model performance.
- Test with real-world anonymized feedback.
- Enhance the user interface.

## Disclaimer
This project is an educational prototype and is not intended for real clinical decision-making.
