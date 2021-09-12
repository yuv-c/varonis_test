from api import app
import unittest
import logging

logging.basicConfig(level=logging.INFO)

# For my manual test
static_dict = [
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


class TestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client

    async def test_protected_route(self):
        req, res = await self.client.post(
            "/api/normalize", data=[dict(foo="baz", a="b")]
        )
        logging.info(res)
        assert res.status_code == 401

    # I would have added a test for the login method and the normalize, but had no time to figure it out.
    # Tested manually.
