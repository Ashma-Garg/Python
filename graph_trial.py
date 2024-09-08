from collections import deque

class GraphNode:
    """
    Initializes an object representing a node in a graph data structure. It has
    two attributes: `val`, which stores the node's value, and `neighbour`, which
    is a list storing references to adjacent nodes. The constructor accepts optional
    arguments for initializing these attributes.

    Attributes:
        val (Union[int,float]|None): Initialized with a default value of 0,
            representing the value associated with each node in the graph. It holds
            integer or floating point values.
        neighbour (List[GraphNode]): Initialized as an empty list. It represents
            a node's adjacent nodes in a graph, allowing for efficient traversal
            and connection between nodes.

    """
    def __init__(self, val=0, neighbour = []):
        """
        Initializes the object with two attributes: `val`, which represents the
        node's value, and `neighbour`, a list that stores references to adjacent
        nodes. The parameters have default values for flexibility in usage.

        Args:
            val (Union[int, float]): 0 by default if no value is provided to it
                during object initialization. It represents a scalar value associated
                with an instance of this class.
            neighbour (List[any] | Dict[Any, Any]): Initialized with an empty list
                by default. It appears to be intended for storing neighboring
                values or data points associated with each instance.

        """
        self.val = val
        self.neighbour = neighbour

def bfs(src: GraphNode):
    """
    Performs a breadth-first search traversal on a graph, starting from the given
    source node (`src`). It prints the values of visited nodes and marks them as
    visited to avoid revisiting. The search continues until all reachable nodes
    have been processed.

    Args:
        src (GraphNode): Initialized to represent the source node for the breadth-first
            search algorithm. It represents the starting point of the traversal.

    """
    visit = {}
    a = deque()
    a.append(src)
    visit[src] = True

    while a:
        node = a.popleft()
        print(node.val)
        neigh = node.neighbour
        for n in neigh:
            if n not in visit:
                a.append(n)
                visit[n] = True


def buildGraph():
    """
    Initializes a directed graph with four nodes and their corresponding neighbors.
    Each node is represented as an object, and its neighboring nodes are assigned
    through their respective attributes. The function returns the first node of
    the graph.

    Returns:
        GraphNode: A reference to a graph with four nodes and their respective
        neighbours. The returned node has ID 1 and references to all other nodes
        in the graph through its neighbour attribute.

    """
    node1 = GraphNode(1)
    node2 = GraphNode(2)
    node3 = GraphNode(3)
    node4 = GraphNode(4)
    node1.neighbour = [node2, node4]
    node2.neighbour = [node1, node3]
    node3.neighbour = [node2, node4]
    node4.neighbour = [node1, node3]

    return node1


graph = buildGraph()
bfs(graph)
j = {"name": "Ashma", "class": "fisrt"}
print("cla" in j)