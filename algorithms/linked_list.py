


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.child: Node = None
        self.parent: Node = None

    def append_to_tail(self, data: int):
        end_node = Node(data)
        node = self

        while node.child != None:
            node = node.child

        node.child = end_node
        end_node.parent = node
        return end_node

    def delete_node(self, node: "Node"):
        if node.parent != None:
            node.parent.child = node.child
        
        if node.child != None:
            node.child.parent = node.parent
        
    def remove_dupes(self, head: "Node"):
        node_pointer: Node = head
        cache = []

        while True:
            if node_pointer.data in cache:
                head.delete_node(node_pointer)
            
            cache.append(node_pointer.data)
            
            if node_pointer.child == None:
                break
            else:
                node_pointer = node_pointer.child
