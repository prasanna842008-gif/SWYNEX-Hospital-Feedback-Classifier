
from flask import Flask, request, render_template_string
from model import train_model, predict_feedback

app = Flask(__name__)
model = train_model()


def get_details(result):
    if result == "Positive":
        return {
            "icon": "😊",
            "message": "Positive Feedback",
            "description": "The feedback expresses satisfaction with the hospital experience.",
            "action": "Continue providing excellent patient care.",
            "color": "#15966b",
            "background": "#e9f8f1"
        }

    elif result == "Negative":
        return {
            "icon": "⚠️",
            "message": "Negative Feedback",
            "description": "The feedback indicates dissatisfaction with the hospital experience.",
            "action": "Review the patient's concerns and improve hospital services.",
            "color": "#dc4545",
            "background": "#fff0f0"
        }

    else:
        return {
            "icon": "ℹ️",
            "message": "Neutral Feedback",
            "description": "The feedback does not express a clear positive or negative opinion.",
            "action": "Record the feedback for future reference.",
            "color": "#2878c8",
            "background": "#edf5ff"
        }


HTML = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>CareSense AI | Hospital Feedback Analysis</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f1f6fb;
            color: #23364d;
        }

        header {
            background: #075985;
            color: white;
            padding: 18px 7%;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .logo {
            font-size: 25px;
            font-weight: bold;
        }

        .logo span {
            color: #8de2ee;
        }

        header .status {
            font-size: 13px;
            background: #ffffff20;
            padding: 9px 15px;
            border-radius: 20px;
        }

        .hero {
            min-height: 360px;
            background:
                linear-gradient(90deg,
                rgba(3, 47, 76, 0.92),
                rgba(3, 47, 76, 0.35)),
                url("https://images.unsplash.com/photo-1586773860418-d37222d8fce3?auto=format&fit=crop&w=1600&q=85");

            background-size: cover;
            background-position: center;
            display: flex;
            align-items: center;
            padding: 55px 9%;
            color: white;
        }

        .hero-content {
            max-width: 650px;
        }

        .hero-tag {
            background: #ffffff25;
            padding: 9px 15px;
            border-radius: 20px;
            font-size: 12px;
            letter-spacing: 1px;
        }

        .hero h1 {
            font-size: 42px;
            margin: 25px 0 12px;
        }

        .hero p {
            font-size: 16px;
            line-height: 1.8;
            color: #e5f2f8;
        }

        .main {
            max-width: 1150px;
            margin: 35px auto;
            padding: 0 20px;
        }

        .section-heading {
            margin-bottom: 22px;
        }

        .section-heading h2 {
            color: #075985;
            margin-bottom: 7px;
        }

        .section-heading p {
            color: #718096;
        }

        .content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 25px;
        }

        .card {
            background: white;
            padding: 28px;
            border-radius: 17px;
            box-shadow: 0 5px 25px rgba(30, 70, 100, 0.08);
        }

        .card h2 {
            color: #075985;
            margin-top: 0;
        }

        .card-description {
            color: #718096;
            font-size: 14px;
            line-height: 1.6;
        }

        textarea {
            width: 100%;
            height: 155px;
            margin-top: 15px;
            padding: 16px;
            border: 1px solid #d5e0ea;
            border-radius: 12px;
            font-size: 15px;
            font-family: Arial;
            resize: vertical;
            outline: none;
        }

        textarea:focus {
            border-color: #0784b5;
            box-shadow: 0 0 0 3px #0784b520;
        }

        button {
            width: 100%;
            padding: 15px;
            margin-top: 17px;
            border: none;
            border-radius: 10px;
            background: #087cae;
            color: white;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
        }

        button:hover {
            background: #075985;
        }

        .result-box {
            padding: 22px;
            margin-top: 18px;
            border-radius: 14px;
            border-left: 6px solid {{ color }};
            background: {{ background }};
        }

        .result-icon {
            font-size: 43px;
            margin-bottom: 8px;
        }

        .result-label {
            color: #718096;
            font-size: 11px;
            font-weight: bold;
            letter-spacing: 1.5px;
        }

        .result-title {
            color: {{ color }};
            font-size: 25px;
            margin: 10px 0 18px;
        }

        .result-text {
            font-size: 14px;
            line-height: 1.7;
            overflow-wrap: anywhere;
        }

        .action-box {
            background: white;
            padding: 15px;
            border-radius: 10px;
            margin-top: 18px;
            line-height: 1.6;
            font-size: 14px;
        }

        .empty-result {
            text-align: center;
            padding: 40px 10px;
            color: #718096;
        }

        .empty-result img {
            width: 100%;
            height: 145px;
            object-fit: cover;
            border-radius: 12px;
            margin-bottom: 15px;
        }

        .features {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 18px;
            margin-top: 28px;
        }

        .feature {
            background: white;
            padding: 20px;
            border-radius: 13px;
            text-align: center;
            box-shadow: 0 4px 15px #00000008;
        }

        .feature h3 {
            color: #075985;
            font-size: 16px;
        }

        .feature p {
            color: #718096;
            font-size: 13px;
            line-height: 1.5;
        }

        footer {
            margin-top: 40px;
            padding: 25px;
            text-align: center;
            background: #063d5b;
            color: white;
            font-size: 13px;
        }

        @media(max-width: 750px) {
            .content {
                grid-template-columns: 1fr;
            }

            .hero h1 {
                font-size: 31px;
            }

            .features {
                grid-template-columns: 1fr;
            }

            header {
                padding: 16px 5%;
            }
        }
    </style>
</head>

<body>

<header>
    <div class="logo">CareSense <span>AI</span></div>
    <div class="status">● Hospital Feedback System</div>
</header>

<section class="hero">
    <div class="hero-content">
        <span class="hero-tag">ARTIFICIAL INTELLIGENCE IN HEALTHCARE</span>

        <h1>Understanding Patients. Improving Healthcare.</h1>

        <p>
            Analyse hospital feedback using Artificial Intelligence.
            Identify patient sentiment and help healthcare providers
            understand patient experiences.
        </p>
    </div>
</section>

<div class="main">

    <div class="section-heading">
        <h2>Patient Feedback Analysis</h2>
        <p>Enter patient feedback to generate an AI-based sentiment prediction.</p>
    </div>

    <section class="content">

        <div class="card">
            <h2>📝 Submit Feedback</h2>

            <p class="card-description">
                Share the patient's experience with the hospital.
                Our AI model will analyse the feedback.
            </p>

            <form method="POST">
                <textarea
                    name="feedback"
                    placeholder="Example: The doctors were very kind and helpful..."
                    required>{{ feedback }}</textarea>

                <button type="submit">
                    Analyse Patient Feedback →
                </button>
            </form>
        </div>

        <div class="card">
            <h2>📊 AI Prediction</h2>

            {% if result %}

            <div class="result-box">

                <div class="result-icon">{{ details.icon }}</div>

                <div class="result-label">PREDICTED SENTIMENT</div>

                <div class="result-title">
                    {{ details.message }}
                </div>

                <div class="result-text">
                    <b>Patient Feedback</b>
                    <p>{{ feedback }}</p>
                </div>

                <div class="result-text">
                    <b>AI Analysis</b>
                    <p>{{ details.description }}</p>
                </div>

                <div class="action-box">
                    <b>💡 Suggested Hospital Action</b>
                    <p>{{ details.action }}</p>
                </div>

            </div>

            {% else %}

            <div class="empty-result">

                <img
                    src="https://images.unsplash.com/photo-1551076805-e1869033e561?auto=format&fit=crop&w=800&q=80"
                    alt="Healthcare professionals">

                <h3>Waiting for Patient Feedback</h3>

                <p>
                    Submit feedback to see the AI prediction
                    and sentiment analysis here.
                </p>

            </div>

            {% endif %}

        </div>

    </section>

    <section class="features">

        <div class="feature">
            <h3>😊 Positive</h3>
            <p>Identifies patient satisfaction and good experiences.</p>
        </div>

        <div class="feature">
            <h3>😟 Negative</h3>
            <p>Identifies complaints and unsatisfactory experiences.</p>
        </div>

        <div class="feature">
            <h3>😐 Neutral</h3>
            <p>Identifies feedback without a clear positive or negative opinion.</p>
        </div>

    </section>

</div>

<footer>
    CareSense AI | Hospital Feedback Classification Project
    <br><br>
    AI-powered patient feedback analysis
</footer>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():

    feedback = ""
    result = None
    details = None

    color = "#2878c8"
    background = "#edf5ff"

    if request.method == "POST":

        feedback = request.form.get("feedback", "").strip()

        if feedback:
            result = predict_feedback(model, feedback)
            details = get_details(result)

            color = details["color"]
            background = details["background"]

    return render_template_string(
        HTML,
        feedback=feedback,
        result=result,
        details=details,
        color=color,
        background=background
    )


if __name__ == "__main__":
    app.run(debug=False)
