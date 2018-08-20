from flask import Flask
from flask import Blueprint


def create_app():
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

    app.register_blueprint(questions_bp, url_prefix='/StackOverflow-lite/api/v1')
    
    return app


if __name__ == '__main__':
    
    app = create_app()
    app.run(debug=True)

 