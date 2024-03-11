from itertools import cycle
import heapq  

pq=[]
heapq.heappush(pq,(5,("rb",6)))
heapq.heappush(pq,(2,("rd",4)))

# while pq:
#     x,(y,z)=heapq.heappop(pq)
#     print(y,z)
d={"a":1,"b":4}
print(d.values())

print(heapq)