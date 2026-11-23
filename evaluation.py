
import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)


# Load the hospital feedback dataset
DATASET_PATH = Path(__file__).with_name("dataset.csv")


def evaluate_model():

    print("\nHOSPITAL FEEDBACK MODEL EVALUATION")
    print("=" * 45)

    # Read dataset
    data = pd.read_csv(DATASET_PATH)

    # Validate dataset
    required_columns = {"feedback", "label"}

    if not required_columns.issubset(data.columns):
        raise ValueError("Dataset must contain feedback and label columns.")

    data = data.dropna(subset=["feedback", "label"])

    if len(data) < 12:
        raise ValueError("Not enough feedback records for evaluation.")

    X = data["feedback"].astype(str)
    y = data["label"].astype(str)

    # Check available categories
    expected_labels = {"Positive", "Negative", "Neutral"}

    if set(y.unique()) != expected_labels:
        raise ValueError("Dataset must contain Positive, Negative and Neutral labels.")

    # Split training and testing data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y
    )

    print("\nDATASET INFORMATION")
    print("-" * 45)
    print("Total records:", len(data))
    print("Training records:", len(X_train))
    print("Testing records:", len(X_test))

    # Create machine learning pipeline
    model = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
        ("classifier", LogisticRegression(
            max_iter=1000,
            class_weight="balanced"
        ))
    ])

    # Train model
    model.fit(X_train, y_train)

    # Predict test data
    y_pred = model.predict(X_test)

    # Calculate evaluation metrics
    print("\nMODEL PERFORMANCE")
    print("-" * 45)

    print("Accuracy:",
          round(accuracy_score(y_test, y_pred), 4))

    print("Precision:",
          round(precision_score(
              y_test, y_pred, average="macro", zero_division=0
          ), 4))

    print("Recall:",
          round(recall_score(
              y_test, y_pred, average="macro", zero_division=0
          ), 4))

    print("F1-Score:",
          round(f1_score(
              y_test, y_pred, average="macro", zero_division=0
          ), 4))

    # Classification report
    print("\nCLASSIFICATION REPORT")
    print("-" * 45)

    print(classification_report(
        y_test,
        y_pred,
        labels=["Positive", "Negative", "Neutral"],
        zero_division=0
    ))

    # Confusion matrix
    print("\nCONFUSION MATRIX")
    print("-" * 45)

    print(confusion_matrix(
        y_test,
        y_pred,
        labels=["Positive", "Negative", "Neutral"]
    ))

    # Show evaluation examples
    print("\nEVALUATION EXAMPLES")
    print("-" * 45)

    for feedback, actual, predicted in zip(X_test, y_test, y_pred):

        print("\nFeedback:", feedback)
        print("Expected:", actual)
        print("Predicted:", predicted)

        if actual == predicted:
            print("Status: Correct")
        else:
            print("Status: Incorrect")

    # Identify failure cases
    print("\nFAILURE CASE ANALYSIS")
    print("-" * 45)

    failures = []

    for feedback, actual, predicted in zip(X_test, y_test, y_pred):

        if actual != predicted:
            failures.append((feedback, actual, predicted))

    if failures:
        for feedback, actual, predicted in failures:
            print("\nFeedback:", feedback)
            print("Expected:", actual)
            print("Predicted:", predicted)
    else:
        print("No incorrect predictions in this test split.")

    print("\nEvaluation completed successfully!")


if __name__ == "__main__":

    try:
        evaluate_model()

    except FileNotFoundError:
        print("Error: dataset.csv was not found.")

    except Exception as error:
        print("Evaluation Error:", error)
