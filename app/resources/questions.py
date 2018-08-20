from flask import request, jsonify, Blueprint
from flask_restful import (Resource, Api, fields,
                            marshal)

import models


question_fields = {
    'Url': fields.Url(absolute=True, scheme='http'),
    'questionId': fields.String,
    'Topic': fields.String,
    'Description': fields.String,
    'datetimeCreated': fields.DateTime,
    'answers': fields.List(cls_or_instance=fields.Raw) 
}

class QuestionList(Resource):
    """
    Shows a list of all questions
    """

    def get(self):
        """
        get all questions
        """
        questions = models.Question.get_questions()
        if questions:
            """serializing the response with JSON"""
            return {'Questions': [marshal(question,question_fields)
                                for question in questions]},200
        else:
            return {'Message': 'No Questions Found'},200

 
questions_bp = Blueprint('resources.questions', __name__)
api = Api(questions_bp)

api.add_resource(QuestionList,
    '/questions',
    endpoint='questions')
