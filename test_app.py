from app import app
import unittest 
import json

class ConverterTests(unittest.TestCase): 

    @classmethod
    def setUpClass(cls):
        pass 

    @classmethod
    def tearDownClass(cls):
        pass 

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def tearDown(self):
        pass 

    def test_converter(self):
        response = self.app.get('/converter', follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        response.data = response.data.decode('utf8').replace("'", '"')
        data = json.loads(response.data)
        self.assertIn('yen', data.keys())
        self.assertIn('dollar', data.keys())
        self.assertIn('euro', data.keys())


if __name__ == "__main__":
    unittest.main()