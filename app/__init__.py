from flask import Flask
from flask import Blueprint

from instance.config import app_config

def create_app(config_name):
    """create and configure app object"""
    
    app = Flask(__name__)

    # testing the app instance creation
    
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    """
    registering the questions_bp and answers_bp blueprints
    """
    from resources.questions import questions_bp
    from resources.answers import answers_bp

    app.register_blueprint(questions_bp, url_prefix='/StackOverflow-lite/api/v1')
    app.register_blueprint(answers_bp, url_prefix='/StackOverflow-lite/api/v1')
    
    return app

app = create_app()
app.config.from_object(app_config['development'])