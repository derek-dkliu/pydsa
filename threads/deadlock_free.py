from threading import Lock
from collections import deque

class DeadlockFree:
    def __init__(self, n):
        self.G = Digraph(n)
        self.locks = [Lock() for _ in range(n)]
        self.lockorder = {}

    def declare(self, id, required_locks):
        # add edges to lock graph
        for i in range(len(required_locks) - 1):
            v = required_locks[i]
            w = required_locks[i + 1]
            self.G.add_edge(v, w)

        # remove edges from lock graph if it has cycle
        if self.check_cycle(required_locks):
            for i in range(len(required_locks) - 1):
                v = required_locks[i]
                w = required_locks[i + 1]
                self.G.remove_edge(v, w)
            return False

        # set lock order
        self.lockorder[id] = deque(required_locks)
        return True

    def get_lock(self, id, lockid):
        queue = self.lockorder.get(id)
        if queue and lockid == queue[0]:
            return self.locks[queue.popleft()]
        return None
    
    def check_cycle(self, required_locks):
        self.marked = [False] * self.G.V
        self.onstack = [False] * self.G.V
        for v in required_locks:
            if self._dfs(v):
                return True
        return False

    def _dfs(self, v):
        self.marked[v] = True
        self.onstack[v] = True
        for w in self.G.get_adj(v):
            if not self.marked[w]:
                if self._dfs(w):
                    return True
            elif self.onstack[w]:
                return True
        self.onstack[v] = False
        return False

class Digraph:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [set() for _ in range(V)]

    def add_edge(self, v, w):
        self.adj[v].add(w)
        self.E += 1

    def remove_edge(self, v, w):
        self.adj[v].remove(w)
        self.E -= 1

    def get_adj(self, v):
        return self.adj[v]


df = DeadlockFree(10)
cases = [
    [1,2,3,4],
    [1,3,5],
    [7,5,9,2]
]
# for id, locks in enumerate(cases):
#     print(locks, df.declare(id, locks))
#     lock = df.get_lock(id, locks[0])
#     print(lock)
#     if lock and not lock.locked():
#         lock.acquire()

from concurrent.futures import ThreadPoolExecutor
from threading import Thread, RLock, current_thread
def process(lock, is_locker):
    thread = current_thread()
    if is_locker:
        lock.acquire()
        print(f"{thread.getName()}: acquired lock")
    else:
        lock.release()
        print(f"{thread.getName()}: released lock")
