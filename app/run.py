import json
from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

# Läs in API-nyckeln från creds.json
with open("creds.json") as f:
    creds = json.load(f)
    openai.api_key = creds.get("openai_api_key")

@app.route('/')
def index():
    return render_template('jobad-generator.html')

@app.route('/generate', methods=['POST'])
def generate_job_ad():
    data = request.get_json()
    job_title = data.get("jobTitle")
    job_description = data.get("jobDescription")

    prompt = f"Create a professional job ad for the position: {job_title}. Description: {job_description}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are an AI specialized in writing professional job ads."},
                      {"role": "user", "content": prompt}]
        )
        job_ad = response['choices'][0]['message']['content']
        return jsonify({"jobAd": job_ad})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
