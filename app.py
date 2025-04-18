from flask import Flask, render_template, request
from config import Config
from blueprints.user import user_bp
from blueprints.admin import admin_bp
from flask_babel import Babel

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.cookies.get('language') or request.accept_languages.best_match(app.config['LANGUAGES'])

app.register_blueprint(user_bp)
app.register_blueprint(admin_bp, url_prefix='/admin')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
