from sanic import Sanic
from sanic.response import json
from sanic_jwt import Initialize, exceptions, protected
import logging
from utils import normalize_json

app = Sanic("hire_me")


class User:
    def __init__(self, id, username, password):
        self.user_id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return "User(id='{}')".format(self.user_id)

    def to_dict(self):
        return {"user_id": self.user_id, "username": self.username}


users = {"user1": User(1, "user1", "secret")}


async def authenticate(request, *args, **kwargs):
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    logging.info(f"Auth: username: {username}, password: {password}")

    if not username or not password:
        logging.exception("Either username or password not supplied in request")
        raise exceptions.AuthenticationFailed("Wrong username or password")

    user = users.get(username)
    if user is None:
        logging.exception(f"Couldn't find user {username} in DB")
        raise exceptions.AuthenticationFailed("Wrong username or password")

    if password != user.password:
        logging.exception(f"Invalid password for user {username}: {password}")
        raise exceptions.AuthenticationFailed("Wrong username or password")

    return user


@app.route("/api/normalize", methods=["POST"])
@protected()
async def normalize(request):
    if not request.json:
        raise exceptions.InvalidPayload("No json to normalize")
    return normalize_json(request.json)


if __name__ == '__main__':
    Initialize(app, authenticate=authenticate, url_prefix='/api/login')
    app.run()
