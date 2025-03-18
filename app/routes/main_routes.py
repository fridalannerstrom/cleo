import os
from flask import Blueprint, render_template

# Blueprint för generella sidor
main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/test')
def test():
    return render_template('index.html')

@main_routes.route('/<page>')
def show_page(page):
    print(f"🔍 Flask försöker ladda: {page}.html")  # Debug
    try:
        return render_template(f"{page}.html")
    except Exception as e:
        print(f"🚨 Fel vid rendering av sidan {page}.html: {e}")
        return f"Sidan {page}.html finns inte", 404