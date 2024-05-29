import os
import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Hello, Docker!')

    def test_env(self):
        response = self.client.get('/AMBIENTE')
        my_env = os.getenv('AMBIENTE')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), f'AMBIENTE={my_env}')

    def test_started(self):
        response = self.client.get('/STARTED')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'STARTED')

    def test_ready(self):
        response = self.client.get('/READY')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'OK')

    def test_health(self):
        response = self.client.get('/HEALTH')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'OK')

if __name__ == '__main__':
    unittest.main()