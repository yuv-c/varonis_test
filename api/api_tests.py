from api import app
import unittest
import logging

logging.basicConfig(level=logging.INFO)

"""
Test do not work and i am out of time as i need to configure it to run synchronous client (instead of the default async).
I tested manually with curl. I wrote them so you would get the general idea:
"""


class TestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client

    def test_protected_route(self):
        req, res = self.client.post(
            "/api/normalize", data=[dict(foo="baz", a="b")]
        )
        logging.info(res)
        assert res.status_code == 401
        args = {"username": "user1", "password": "secret"}
        req, res = self.client.get(
            "/api/login",
            args=args
        )
        assert res.status_code == 200
        assert res.json.get("access_toekn") is not None

    def test_normalize(self):
        test_json = [
            {
                "name": "device",
                "strVal": "Iphone",
                "metaData": "dfdsf"
            },
            {
                "name": "isAuthorized",
                "strVal": False,
                "lastSeen": "ghjgvjty"
            }
        ]
        args = {"username": "user1", "password": "secret"}
        req, res = self.client.get(
            "/api/login",
            args=args
        )
        req, res = self.client.post(
            "/api/normalize",
            args=test_json
        )
        assert len(res.json.keys()) == 2
        assert res.json.get("device") == "Iphone"
        assert res.json.get("isAuthorized") is False
