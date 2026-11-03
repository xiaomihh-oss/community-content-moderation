
import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestModerationAPI(unittest.TestCase):

    def test_home(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_health(self):
        response = client.get("/health")
        self.assertEqual(response.status_code, 200)

    def test_normal_content(self):
        response = client.post(
            "/moderate",
            json={"text": "今天天气真好"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()["result"], "审核通过"
        )

    def test_ad_content(self):
        response = client.post(
            "/moderate",
            json={"text": "加微信扫码进群"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()["result"], "人工复核"
        )

    def test_empty_content(self):
        response = client.post(
            "/moderate",
            json={"text": ""}
        )
        self.assertEqual(response.status_code, 422)

    def test_multiple_risks(self):
        response = client.post(
            "/moderate",
            json={
                "text": "加微信扫码进群，联系13812345678"
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()["risk_level"], "高风险"
        )


if __name__ == "__main__":
    unittest.main()
