from main import Node
import sys
sys.path.append("./refactorci/")

def test_add():
    node = Node(1)
    assert str(node) == "(1, None)"