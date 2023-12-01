from flask import Flask
from web_app.routes.pages import mainpage_bp, menu_bp, services_bp, blog_bp, about_bp, contact_bp
import os

app = Flask(__name__, template_folder=os.path.join(
    os.path.dirname(__file__), 'web_app/templates'),
    static_folder=os.path.join(os.path.dirname(__file__), 'web_app/static'))


# Register all bp's
app.register_blueprint(mainpage_bp)
app.register_blueprint(menu_bp)
app.register_blueprint(services_bp)
app.register_blueprint(blog_bp)
app.register_blueprint(about_bp)
app.register_blueprint(contact_bp)

if __name__ == "__main__":
    app.run(debug=True)
