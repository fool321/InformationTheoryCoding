class TreeNode(object):

    """Node with an arbitrary number of children."""

    def __init__(self, key, data, children=[]):
        """Create the node with the given key, data, and children.

        :key: Any object that can be compared.
        :data: Any object.
        :children: Possibly empty list of TreeNodes.

        """
        self.key = key
        self.data = data
        self.children = children

    def print(self):
        """Print the tree rooted at the node in tabular form.
        :returns: Nothing.

        """
        def _print(node, level):
            print("\t"*level + str((node.key, node.data)))
            for child in node.children:
                _print(child, level + 1)
        _print(self, 0)

    def __eq__(self, other):
        """equal--Test equality with another node."""
        return self.key == other.key

    def __ne__(self, other):
        """not equal--Test inequality with another node."""
        return self.key != other.key

    def __lt__(self, other):
        """less than--Test the less than inequality with another node."""
        return self.key < other.key

    def __le__(self, other):
        """less and equal--Test the less than or equal to inequality with another node."""
        return self.key <= other.key

    def __gt__(self, other):
        """greater than--Test the greater than inequality with another node."""
        return self.key > other.key

    def __ge__(self, other):
        """greater and equal--Test the greater than or equal to inequality with another node."""
        return self.key >= other.key
