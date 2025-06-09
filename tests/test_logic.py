from src.logic import greet_user

def test_greet_user():
    assert greet_user("Alice") == "Hello, Alice! 👋"
