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
     
 