import requests
import os
import unittest

url = os.getenv('APP_URL', 'http')


class TestCase(unittest.TestCase):
    def test_is_alive(self):
        response = requests.get(url)
        assert response.status_code == 200

if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='API-test-reports'))
    unittest.main()