import sys
sys.path.append("./refactorci")

from node_n_ll import Node


def test_add():
    node = Node(1)
    assert str(node) == "(1, None)"

def test_obv(): 
    assert 1 == 1.0