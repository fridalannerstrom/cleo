import json
import os
from flask import Flask, request, jsonify, render_template
import openai

# Skapa Flask-app och peka på templates-mappen (i root)
app = Flask(__name__, template_folder="../templates", static_folder="../static")

# Läs in API-nyckeln från miljövariabel
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('/jobad-generator.html')

@app.route('/generate', methods=['POST'])
def generate_job_ad():
    data = request.get_json()
    job_title = data.get("jobTitle")
    job_description = data.get("jobDescription")

    if not job_title or not job_description:
        return jsonify({"error": "Job title and description are required"}), 400

    prompt = f"Create a professional job ad for the position: {job_title}. Description: {job_description}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI specialized in writing professional job ads."},
                {"role": "user", "content": prompt}
            ]
        )
        job_ad = response["choices"][0]["message"]["content"]
        return jsonify({"jobAd": job_ad})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
