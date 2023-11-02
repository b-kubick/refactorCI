import sys
sys.path.append("./refactorci")

from node_n_ll import Node
from node_n_ll import DoublyLinkedList
from node_n_ll import twenties





def test_add():
    node = Node(1)
    assert str(node) == "(1, None)"

def test_doubly_linked_list_creation():
    dL = DoublyLinkedList()
    for i in range(4):
        dL.add_last(Node(i))
    assert str(dL) == "(0, (1, (2, (3, ('Trailer', None)))))"

def test_size_method():
    dL = DoublyLinkedList()
    for i in range(4):
        dL.add_last(Node(i))
    assert dL.size() == 4

def test_is_empty_method():
    dL = DoublyLinkedList()
    dL2 = DoublyLinkedList()
    dL.add_last(Node(1))
    assert not dL.is_empty()
    assert dL2.is_empty()

def test_get_first_last_methods():
    dL = DoublyLinkedList()
    for i in range(4):
        dL.add_last(Node(i))
    # Testing normal behavior
    assert str(dL.get_first()) == "(0, (1, (2, (3, ('Trailer', None)))))"
    assert str(dL.get_last()) == "(3, ('Trailer', None))"

    # Testing behavior with an empty list
    dL_empty = DoublyLinkedList()
    # Testing edge cases
    try:
        dL_empty.get_first()
        assert False, "Expected an exception for get_first on empty list"
    except Exception as e:
        assert str(e) == "List is empty"

    try:
        dL_empty.get_last()
        assert False, "Expected an exception for get_last on empty list"
    except Exception as e:
        assert str(e) == "List is empty"



def test_get_previous_next_methods():
    dL = DoublyLinkedList()
    for i in range(4):
        dL.add_last(Node(i))
    assert str(dL.get_last().get_previous()) == "(2, (3, ('Trailer', None)))"
    assert str(dL.get_first().get_next()) == "(1, (2, (3, ('Trailer', None))))"


def test_add_before_after_methods():
    dL = DoublyLinkedList()
    for i in range(4):
        dL.add_last(Node(i))
    dL.add_after(Node(42), dL.get_first())
    dL.add_before(Node(34), dL.get_last())
    assert str(dL) == "(0, (42, (1, (2, (34, (3, ('Trailer', None)))))))"

def test_add_first_last_methods():
    dL = DoublyLinkedList()
    for i in range(4):
        dL.add_last(Node(i))
    dL.add_first(Node(7))
    dL.add_last(Node(-1))
    assert str(dL) == "(7, (0, (1, (2, (3, (-1, ('Trailer', None)))))))"

def test_remove_method():
    dL = DoublyLinkedList()
    for i in range(4):
        dL.add_last(Node(i))
    dL.remove(dL.get_first())
    assert dL.get_first().get_element() == 1


def test_map_method():
    dL = DoublyLinkedList()
    for i in range(4):
        dL.add_last(Node(i))
    dL.map(lambda x: x ** 2)

    assert str(dL) == "(0, (1, (4, (9, ('Trailer', None)))))"

def test_iteration():
    dL = DoublyLinkedList()
    for i in range(4):
        dL.add_last(Node(i))
    
    elements = [node.get_element() for node in dL]
    assert elements == [0, 1, 2, 3]

def test_add_two():
    LL = DoublyLinkedList()
    for t in range(20, 30):
        LL.add_last(Node(t))
    LL.map(lambda x: x + 2)
    assert str(LL) == "(22, (23, (24, (25, (26, (27, (28, (29, (30, (31, ('Trailer', None)))))))))))"

def test_multiply_by_five():
    doubleDigits = twenties()
    doubleDigits.map(lambda x: x * 5)

    # Collect nodes to be removed
    nodes_to_remove = [node for node in doubleDigits if node.get_element() % 4 == 0]

    # Remove the collected nodes
    for node in nodes_to_remove:
        doubleDigits.remove(node)

    # Expected result should be all numbers from 20 to 29, multiplied by 5,
    # with those divisible by 4 removed
    expected_result = [x * 5 for x in range(20, 30) if (x * 5) % 4 != 0]
    actual_result = [node.get_element() for node in doubleDigits]
    assert actual_result == expected_result


def test_remove_multiples_of_three():
    doubleDigits = twenties()
    doubleDigits.map(lambda x: x * 5)

    current = doubleDigits.get_first()
    while current and current != doubleDigits.get_last().get_next():
        next_node = current.get_next()
        if current.get_element() % 3 == 0:
            doubleDigits.remove(current)
        current = next_node

    # Expected result should be all numbers from 20 to 29, multiplied by 5,
    # with those divisible by 3 removed
    expected_result = [x * 5 for x in range(20, 30) if (x * 5) % 3 != 0]
    actual_result = [node.get_element() for node in doubleDigits]
    assert actual_result == expected_result

def test_remove_odd_numbers():
    doubleDigits = twenties()
    doubleDigits.map(lambda x: x * 5)

    current = doubleDigits.get_first()
    while current and current != doubleDigits.get_last().get_next():
        next_node = current.get_next()
        if current.get_element() % 2 == 1:
            doubleDigits.remove(current)
        current = next_node

    # Expected result should be all numbers from 20 to 29, multiplied by 5,
    # with odd numbers removed
    expected_result = [x * 5 for x in range(20, 30) if (x * 5) % 2 == 0]
    actual_result = [node.get_element() for node in doubleDigits]
    assert actual_result == expected_result

