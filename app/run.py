import os
from flask import Flask, render_template
from config import Config
from routes.main_routes import main_routes
from routes.ai_routes import ai_routes
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

print(f"✅ Flask letar efter templates i: {os.path.abspath('../cleo/templates')}")
print(f"Flask letar efter templates i: {os.path.abspath('templates')}")

# Skapa Flask-applikationen
app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.config.from_object(Config)  # Laddar in konfigurationen

# Registrera Blueprints
app.register_blueprint(main_routes)
app.register_blueprint(ai_routes, url_prefix="/api")  # Prefix för API-rutter

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(debug=True, host="0.0.0.0", port=port)
