from collections import deque

class GraphNode:
    def __init__(self, val=0, neighbour = []):
        self.val = val
        self.neighbour = neighbour

def bfs(src: GraphNode):
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