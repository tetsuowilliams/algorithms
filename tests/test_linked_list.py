from algorithms.linked_list import Node


def test_linked_list_smoke_test():
    node1 = Node(1)
    node1.append_to_tail(2)
    assert node1.child.data == 2

def test_doubly_linked():
    node1 = Node(1)
    node1.append_to_tail(2)
    assert node1.child.parent.data == 1

def test_delete():
    node1 = Node(1)
    node2 = node1.append_to_tail(2)
    node3 = node1.append_to_tail(3)
    node1.delete_node(node2)
    assert node1.child == node3
    assert node3.parent == node1

def test_remove_dupes():
    node1 = Node(1)
    node1.append_to_tail(2)
    node1.append_to_tail(3)
    node1.append_to_tail(3)
    node1.remove_dupes(node1)

    assert node1.child.child.child == None

