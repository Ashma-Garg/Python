#User function Template for python3
from collections import deque, defaultdict
class Solution:
    def findOrder(self, n, m, prerequisites):
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