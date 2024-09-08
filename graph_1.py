from collections import deque

class GraphNode:
	"""
	Initializes an object to represent a node in a graph. It has two attributes:
	`val`, which stores the value of the node, and `neighbors`, which is a list of
	neighboring nodes connected to it. The node's neighbors are initialized as an
	empty list by default.

	Attributes:
	    val (Union[int,str]): Initialized to a default value of 0. It represents the
	        value associated with a node in a graph.
	    neighbors (List[GraphNode]|List[int]): Initialized as an empty list by default.
	        It represents a collection of neighboring nodes or their values, allowing
	        for either node references or just their IDs in adjacency representation
	        graphs.

	"""
	def __init__(self, val=0, neighbors=[]):
		"""
		Initializes an object with a value and a list of neighboring nodes. The value
		defaults to 0, and the neighbors list defaults to an empty list if no value is
		provided when creating a new node instance.

		Args:
		    val (int | float): 0 by default if not provided when instantiating an object
		        from this class. It represents the value of the node being created.
		    neighbors (List[Node | None]): Specified to be an empty list by default.
		        This allows for the initialization of nodes with or without neighboring
		        nodes.

		"""
		self.val = val
		self.neighbors = neighbors

def cloneGraph(src: GraphNode) -> GraphNode:
	"""
	Creates a deep copy of a graph, where each node in the original graph is replaced
	by a new identical node with the same value and neighbors. The copied nodes are
	stored in a dictionary for efficient lookup.

	Args:
	    src (GraphNode): Used as an input to the cloning process, representing the
	        source graph from which a clone will be created. It denotes the starting
	        point for the graph traversal.

	Returns:
	    GraphNode: A deep copy of the input graph represented by src, containing all
	    nodes and their corresponding neighbors.

	"""
	# A Map to keep track of all the
	# nodes which have already been created
	m = {}
	q = deque()

	# Enqueue src node
	q.append(src)
	node = None

	# Make a clone Node
	node = GraphNode()
	node.val = src.val

	# Put the clone node into the Map
	m[src] = node
	while q:
		# Get the front node from the queue
		# and then visit all its neighbors
		u = q.popleft()
		v = u.neighbors
		for neighbor in v:
			# Check if this node has already been created
			if neighbor not in m:
				# If not then create a new Node and
				# put into the HashMap
				node = GraphNode()
				node.val = neighbor.val
				m[neighbor] = node
				q.append(neighbor)

			# Add these neighbors to the cloned graph node
			m[u].neighbors.append(m[neighbor])

	# Return the address of cloned src Node
	return m[src]

# Build the desired graph
def buildGraph() -> GraphNode:
	"""
	Given Graph:
	1--2
	| |
	4--3
	"""
	node1 = GraphNode(1)
	node2 = GraphNode(2)
	node3 = GraphNode(3)
	node4 = GraphNode(4)
	node1.neighbors = [node2, node4]
	node2.neighbors = [node1, node3]
	node3.neighbors = [node2, node4]
	node4.neighbors = [node3, node1]
	return node1

# A simple bfs traversal of a graph to
# check for proper cloning of the graph
def bfs(src: GraphNode):
	"""
	Performs a breadth-first search traversal of a graph, starting from the source
	node `src`. It visits each node in the graph level by level, printing its value
	and address, and adding unvisited neighbors to a queue for further processing.

	Args:
	    src (GraphNode): Used to initialize the Breadth-First Search traversal from
	        this node. It represents the source or starting node for the algorithm.

	"""
	visit = {}
	q = deque()
	q.append(src)
	visit[src] = True
	while q:
		u = q.popleft()
		print(f"Value of Node {u.val}")
		print(f"Address of Node {u}")
		v = u.neighbors
		for neighbor in v:
			if neighbor not in visit:
				visit[neighbor] = True
				q.append(neighbor)

if __name__ == "__main__":
	src = buildGraph()
	print("BFS Traversal before cloning")
	bfs(src)
	clone = cloneGraph(src)
	print("\nBFS Traversal after cloning")
	bfs(clone)

	# This code is contributed by vikramshirsath177
