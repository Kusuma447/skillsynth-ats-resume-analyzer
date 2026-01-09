from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    job_desc = data.get("job_desc", "")

    keywords = ["python", "java", "sql", "flask", "api", "html", "css", "javascript"]
    found = [k for k in keywords if k in job_desc.lower()]
    missing = [k for k in keywords if k not in job_desc.lower()]

    ats_score = min(len(found) * 12, 100)
    match_percentage = min(len(found) * 10, 100)

    return jsonify({
        "ats_score": ats_score,
        "match_percentage": match_percentage,
        "missing_keywords": missing
    })

if __name__ == "__main__":
    app.run(debug=True)
