import os
import openai
from flask import Blueprint, request, jsonify

# Blueprint för AI-funktioner
ai_routes = Blueprint('ai_routes', __name__)

# Läs in API-nyckeln
openai.api_key = os.getenv("OPENAI_API_KEY")

@ai_routes.route('/generate', methods=['POST'])
def generate_job_ad():
    data = request.get_json()
    job_title = data.get("jobTitle")
    job_description = data.get("jobDescription")

    if not job_title or not job_description:
        return jsonify({"error": "Job title and description are required"}), 400

    prompt = f"Create a professional job ad for the position: {job_title}. Description: {job_description}"

    try:
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI specialized in writing professional job ads."},
                {"role": "user", "content": prompt}
            ]
        )
        job_ad = response.choices[0].message.content
        return jsonify({"jobAd": job_ad})
    except Exception as e:
        return jsonify({"error": str(e)}), 500