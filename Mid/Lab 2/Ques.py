from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()     # The first to arrive now leaves
queue.popleft()     # The second to arrive now leaves

queue()             # Displays the remaining queue