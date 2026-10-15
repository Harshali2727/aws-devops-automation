import json
import subprocess
import sys
import time
import unittest
from urllib.request import urlopen


class TestApplication(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server = subprocess.Popen(
            [sys.executable, "app/app.py"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.server.terminate()
        cls.server.wait(timeout=5)

    def test_home_page(self):
        with urlopen("http://127.0.0.1:8000/") as response:
            self.assertEqual(response.status, 200)
            content = response.read()
            self.assertIn(b"AWS DevOps Automation", content)

    def test_health_endpoint(self):
        with urlopen("http://127.0.0.1:8000/health") as response:
            self.assertEqual(response.status, 200)
            data = json.loads(response.read())
            self.assertEqual(data["status"], "healthy")
            self.assertEqual(
                data["project"], "AWS DevOps Automation"
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)