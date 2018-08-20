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

   
    def tearDown(self):
        """teardown initialised variables"""
        self.question = {}
        self.answer = {}
        self.partial_qn = {}

if __name__ =='__main__':
    unittest.main()
