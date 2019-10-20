class Solution {
  private static class Node {
    String val;
    Node left;
    Node right;

    Node(String val) {
      Node(val, null, null);
    }

    Node(String val, Node left, Node right) {
      this.val = val;
      this.left = left;
      this.right = right;
    }

  }
}