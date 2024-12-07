import pytest
import unittest
import flask
import sqlite3
import app

class TestApi(unittest.TestCase):
    
    def test_okResponse(self):
      testApp=app.app
      tester = testApp.test_client(self)
      response=tester.get('/')
      statuscode =response.status_code
      self.assertEqual(statuscode, 200)
      
      
if __name__=="__main__":
    unittest.main()