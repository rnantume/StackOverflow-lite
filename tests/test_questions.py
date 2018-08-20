 import unittest
import json

from app import app, create_app
from instance.config import app_config

class QuestionsTestCase(unittest.TestCase):
    """class to represent questions test case"""

    def setUp(self):
        """setup test variables"""
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()
        
        self.question = {'Topic':'Sample Topic', 'Description':"Sample Description"}
        self.answer = {'answer':"Sample Answer", 'accepted':True}
        self.partial_qn = {'Topic':'Sample Topic'}

    def test_hello(self):
        """Test API can get hello function"""
        res = self.client().get('/hello')
        self.assertEqual(res.status_code, 200)

    
    def test_api_can_get_all_questions(self):
        """Test API can get all questions (GET request)."""
        res = self.client().post('/questions', data=self.question)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/questions')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Description', str(res.data))

    def test_add_question(self):
        """Test API can add new question"""
        res = self.client().post('/questions', data=self.question,
                                 content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn('Sample Description', str(res.data))

    def test_api_can_get_question_by_id(self):
        """Test API can get a question by using it's questionId."""
        res = self.client().post('/questions', data=self.question)
        self.assertEqual(res.status_code, 201)
        result_in_json = json.loads(res.data.decode('utf-8').replace("'", "\""))
        result = self.client().get(
                '/questions/{}'.format(result_in_json['questionId']))
        self.assertEqual(result.status_code, 200)
        self.assertIn('Sample description', str(result.data))