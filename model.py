
import pandas as pd
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


# Load the hospital feedback dataset
DATASET_PATH = Path(__file__).with_name("dataset.csv")


def train_model():
    # Read dataset
    data = pd.read_csv(DATASET_PATH)

    # Check dataset columns
    required_columns = {"feedback", "label"}

    if not required_columns.issubset(data.columns):
        raise ValueError("Dataset must contain feedback and label columns.")

    # Remove empty rows
    data = data.dropna(subset=["feedback", "label"])

    X = data["feedback"].astype(str)
    y = data["label"].astype(str)

    # Create machine learning pipeline
    model = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
        ("classifier", LogisticRegression(
            max_iter=1000,
            class_weight="balanced"
        ))
    ])

    # Train model
    model.fit(X, y)

    return model


def predict_feedback(model, feedback):
    if not feedback or not feedback.strip():
        raise ValueError("Please enter patient feedback.")

    prediction = model.predict([feedback.strip()])

    return prediction[0]


# Test the model
if __name__ == "__main__":
    model = train_model()

    test_feedback = [
        "The doctors were very kind and helpful",
        "The hospital service was very poor",
        "I visited the hospital yesterday"
    ]

    print("HOSPITAL FEEDBACK CLASSIFICATION")
    print("--------------------------------")

    for feedback in test_feedback:
        result = predict_feedback(model, feedback)

        print("Feedback:", feedback)
        print("Prediction:", result)
        print()
