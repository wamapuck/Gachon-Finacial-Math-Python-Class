import collections, random

cus_in_rest = collections.deque()

for i in range(100):
    
    if random.random() < 0.8:
        cus_in_rest.append(i)
    if random.random() < 0.5 and len(cus_in_rest) > 0:
        cus_in_rest.popleft()
    
    print(f"""
customers in restaurant ephoch: {i+1}
the real time customers: {cus_in_rest}
""")