class Node:
    def __init__(self, val: str, left: "Node" = None, right: "Node" = None):
        self.val = val
        self.right = right
        self.left = left


def exp_tree(node: Node) -> float:
    # Base Case
    if node.left is None and node.right is None:
        return float(node.val)

    # Different Operations
    if node.val == "+":
        return exp_tree(node.left) + exp_tree(node.right)  # noqa: T484
    elif node.val == "-":
        return exp_tree(node.left) - exp_tree(node.right)  # noqa: T484
    elif node.val == "*":
        return exp_tree(node.left) * exp_tree(node.right)  # noqa: T484
    else:
        return exp_tree(node.left) / exp_tree(node.right)  # noqa: T484


root = Node("*", Node("+", Node("3"), Node("2")),
            Node("+", Node("4"), Node("5")))
