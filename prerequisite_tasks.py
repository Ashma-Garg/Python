#User function Template for python3
from collections import deque, defaultdict
class Solution:
    """
    Determines whether it's possible to finish all tasks in a given course schedule
    and returns a valid ordering of tasks if one exists, otherwise an empty list
    is returned. It takes three inputs: number of courses, total prerequisite
    relationships between courses, and prerequisites for each course.

    """
    def findOrder(self, n, m, prerequisites):
        """
        Determines whether it's possible to finish all tasks based on given
        prerequisites, and if so, returns their order of completion. It takes as
        input the number of tasks (n), the number of edges (m), and a list of
        prerequisite pairs.

        Args:
            n (int): Specified as the number of tasks or nodes in the directed
                graph. It represents the size of the graph, where each task has
                an index from 0 to n-1.
            m (int): Not used within the function, it seems to be an unused variable.
                It might be a leftover from another implementation or a mistake.
            prerequisites (List[tuple[int, int]]): Used to represent the dependencies
                between tasks. It contains pairs of tuples where each tuple
                represents a pair (pre-requisite task ID, dependent task ID).

        Returns:
            list[int]: A valid order for taking courses given the prerequisites,
            or an empty list if no such order exists.

        """
        # Code here
        degree = [0]*n
        df_dict = defaultdict(list)
        
        for p in prerequisites:
            task, pre = p
            df_dict[pre].append(task)
            degree[task] += 1 
            
        no_pre_tasks = deque([i for i in range(n) if degree[i] == 0])
        order=[]
        
        while no_pre_tasks:
            npt = no_pre_tasks.popleft()
            order.append(npt)
            
            for t in df_dict[npt]:
                degree[t] -= 1
                if degree[t] == 0:
                    no_pre_tasks.append(t)
                
        if len(order) == n:
            return order
        else:
            return []