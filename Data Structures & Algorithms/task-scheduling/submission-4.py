from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        counter = 0

        freq = {}
        for task in tasks:
            if task not in freq:
                freq[task] = 1
            else:
                freq[task] += 1
        
        # build the heap and prefill it with each of the unique tasks

        heap = []
        for task in freq:   # need to use it as a max heap
            heapq.heappush(
                heap, (-freq[task], task)
            )
        
        q = deque() # empty queue which will be used for cooldown tasks (need to run, but cant yet)

        while q or heap:
            if q:
                task, remaining, run_at = q[0]
                if counter == run_at + 1: # this task can now be run
                    heapq.heappush(
                        heap, (remaining, task)
                    )
                    q.popleft()
            
            if heap:
                popped = heapq.heappop(heap)
                remaining = -popped[0] - 1
                task = popped[1]
                
                run_at = counter + n

                if remaining > 0:
                    q.append(
                        (task, -remaining, run_at)
                    )
            counter += 1
        
        return counter
                


        


        































