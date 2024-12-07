import pytest
import unittest
import flask
import sqlite3
import app

class TestApi(unittest.TestCase):
    
    def setUp(self):
        self.testapp=app.app
        self.tester = self.testapp.test_client(self)
        self.connection=app.get_db_connection()
        self.cursor=self.connection.cursor()
        
        return self
    
    def tearDown(self):
        pass
   
   
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
        
    def test_valid_user(self):
        username='admin1'
        password=username
        self.cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?',  (username, password))
        l=self.cursor.fetchone()
        self.assertEqual(l["username"], "admin1")
        self.assertEqual(l["password"], "admin1")
        
if __name__=="__main__":
    unittest.main()