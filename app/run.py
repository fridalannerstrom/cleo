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

login_manager = LoginManager()
login_manager.init_app(app)  # Kopplar login_manager till Flask-appen
login_manager.login_view = 'login'  # Bestämmer vilken route som användaren ska omdirigeras till om den inte är inloggad

# Skapa en instans av SQLAlchemy
db = SQLAlchemy(app)

# Den här raden kommer att läsa in databasens URI som vi har satt i config.py
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

# Definiera användarmodellen här som vi gjorde tidigare

@app.route('/test-template')
def test_template():
    return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(debug=True, host="0.0.0.0", port=port)
