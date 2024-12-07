import pytest
import unittest
import flask
import sqlite3
import app

class TestApi(unittest.TestCase):
    
    def setUp(self):
        self.testapp=app.app
        self.tester = self.testapp.test_client(self)
        
        
        return self
    
    def tearDown(self):
        return super().tearDown()
   
   
    def test_okresponse_on_homepage(self):
      response=self.tester.get('/')
      statuscode =response.status_code
      self.assertEqual(statuscode, 200)
      
    def test_okresponse_on_login(self):
        response=self.tester.get('/login') 
        statuscode =response.status_code
        self.assertEqual(statuscode, 200)
        
    def test_account_create(self):
        response=self.tester.get('/account_create')
        statuscode =response.status_code
        self.assertEqual(statuscode, 200)
        
    def test_news_portal(self):
        response=self.tester.get('/news_portal')
        statuscode =response.status_code
        self.assertEqual(statuscode, 200)
    
      
if __name__=="__main__":
    unittest.main()