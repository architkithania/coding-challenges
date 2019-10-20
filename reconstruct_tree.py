from typing import List, Optional


class Node:
    def __init__(self, val: str, left: "Node" = None, right: "Node" = None):
        self.val = val
        self.left = left
        self.right = right


def reconstruct_tree(pre_order: List[str], in_order: List[str]) -> Optional[Node]:  # noqa: E501
    if len(pre_order) == 0:
        return None
    if len(pre_order) == 1:
        return Node(pre_order[0])
    root_index = in_order.index(pre_order[0])
    left_subtree = reconstruct_tree(
        pre_order[1:root_index + 1], in_order[:root_index])
    right_subtree = reconstruct_tree(
        pre_order[root_index + 1:], in_order[root_index + 1:])
    return Node(pre_order[0], left_subtree, right_subtree)
