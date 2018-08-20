import uuid
import datetime


questions = []

class Question():
    """ 
    class to represent question model
    """
    def __init__(self, Topic, Description):
        self.questionId = uuid.uuid4().hex
        self.Topic = Topic
        self.Description = Description
        self.datetimeCreated = datetime.datetime.now()
        self.answers = []


    @staticmethod
    def get_questions():
        """
        :return: all questions in memory
        """
        if questions:
            return questions 
     
    @staticmethod
    def get_question(questionId):
        """
        method to get a specific question by questionId
        :param questionId: Question id
        :return: question (dict) or none
        """
        for question in questions:
            if question['questionId']== questionId:
                return question
        
    def add_question(self):
        """
        method to add a new question
        :return: question created(dict)
        """
        new_question = {
            'questionId': self.questionId,
            'Topic': self.Topic,
            'Description': self.Description,
            'datetimeCreated': self.datetimeCreated,
            'answers': self.answers
        }
        questions.append(new_question)
        return new_question

class Answer():
    """
    class to represent answer model
    """

    def __init__(self, answer, accepted):
        self.answerId = uuid.uuid4().hex
        self.answer = answer
        self.accepted = accepted
        self.datetimeCreated = datetime.datetime.now()
        self.comments = []


    def add_answer(self, questionId):
        """
        method to add a new answer to a question
        :param questionId: of question to add answers
        :return: answer created(dict) or question is none
        """
        for question in questions:
            if question['questionId']== questionId:
                new_answer = {
                    'answerId': self.answerId,
                    'answer': self.answer,
                    'accepted': self.accepted,
                    'datetimeCreated': self.datetimeCreated,
                    'comments': self.comments
                }
                question['answers'].append(new_answer)
                return new_answer