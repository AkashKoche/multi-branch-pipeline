import sys
sys.path.append('src')
from app import hello

def test_hello():
    assert hello() == "Hello, Jenkins!"

if __name__ == "__main__":
    test_hello()
    print("Tests passed!")
