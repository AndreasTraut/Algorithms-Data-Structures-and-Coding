# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 10:06:17 2021

@author: Andreas Traut


Problem: 
Assume, that we have a weighted, directed graph with a source (origin) and 
further nodes. Each path from one node to another node has a weight 
(the time-delay). The quesion is: if a signal is starting from the source 
(origin): how long will it take to transmit this signal to all nodes?

Input
1. num_nodes, e.g. ${num}_{nodes}=4$
2. edges with weights, e.g. $edges = [(2,1,1),(2,3,1),(3,4,1)]$
3. source, e.g. $source = 0$

Output
1. network-delay-time, e.g. 2

Solution: 
1. Create a class for the weighted, directed graph based on the num_nodes 
    and edges information.
2. Start at the source node. Implement the Depth-first search algorithm: 
    recursively go to all leaves and add weight until the end of a branch is 
    reached. 
3. Return the maximum of these sums of weight. This is the network-delay-time.

"""
#%% Define some testcases

# Testcase 1: One source and two possible targets
test = {
    'input': {
        'num_nodes': 4, 
        'edges': [(0,1,1), (0,2,1), (2,3,1)], 
        'source': 0
    },
    'output': 2
}

tests = []
tests.append(test)

# Testcase 2: Two targets with same delay time
tests.append({
    'input': {
        'num_nodes': 3,
        'edges': [(0, 1, 1), (0, 2, 1)],
        'source': 0
    },
    'output': 1
})

# Testcase 3: One branch with two nodes but short delay time. One branch with one node and long delay time.
tests.append({
    'input': {
        'num_nodes': 5,
        'edges': [(0, 1, 1), (0, 2, 1), (0, 4, 5), (2, 3, 3)],
        'source': 0
    },
    'output': 5
})

# Testcase 4: Two path to the same node.
tests.append({
    'input': {
        'num_nodes': 5,
        'edges': [(0, 1, 1), (0, 2, 1), (0, 4, 5), (2, 3, 3), (3, 4, 2)],
        'source': 0
    },
    'output': 6
})

# Testcase 5: Use another source
tests.append({
    'input': {
        'num_nodes': 5,
        'edges': [(1, 0, 1), (2, 0, 1), (4, 0, 5), (2, 3, 3), (3, 4, 2), (2, 1, 4)],
        'source': 2
    },
    'output': 10
})


#%% Define a Graph class

class Graph:
    def __init__(self, num_nodes, edges, directed=False, weighted=False): 
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = weighted
        self.data =[[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)]
        
        for edge in edges: 
            if self.weighted: 
                # include weights
                node1, node2, weight = edge
                self.data[node1].append(node2)                
                self.weight[node1].append(weight)
                
                if not directed: 
                    self.data[node2].append(node1)
                    self.weight[node2].append(weight)
            else: 
                # work without weights
                node1, node2 = edge
                self.data[node1].append(node2)
                
                if not directed: 
                    self.data[node2].append(node1)
    
    def __repr__(self): 
        result = ""
        if self.weighted:
            for i, (nodes, weights) in enumerate(zip(self.data, self.weight)): 
                result += "{}: {}\n".format(i, list(zip(nodes, weights)))
        else: 
            for i, nodes in enumerate(self.data): 
                result += "{}: {}\n".format(i, nodes)
        return result
    
   
#%% Define the solving algorithm (a recursion)

def delay_time_recursion(graph, edge, current, max_delay):
    idx = 0 
    if not graph.data[edge]: 
        if current > max_delay:
                max_delay = current            
        return max_delay
                
    for e in graph.data[edge]:            
            c = delay_time_recursion(graph, e, current + graph.weight[edge][idx], max_delay) 
            if c > max_delay:
                max_delay = c
            idx += 1
    
    return max_delay

def delay_time(num_nodes, edges, source): 
    graph = Graph(num_nodes, edges, directed=True, weighted=True)
    current = 0
    max_delay = 0    
    return delay_time_recursion(graph, source, current, max_delay)

#%% Perform the tests

idx = 0
while idx < len(tests):     
    print('Testcase {}:'.format(idx))
    num_nodes, edges, source = tests[idx]['input']['num_nodes'], tests[idx]['input']['edges'], tests[idx]['input']['source']
    expected = tests[idx]['output']    
    print('num_nodes = {}'.format(num_nodes))
    print('edges = {}'.format(edges))
    print('source = {}'.format(source))
    print('expected = {}'.format(expected))    
    if expected == delay_time(num_nodes, edges, source): 
        print('Test passed\n')
    else:
        print('Test failed\n')
    idx += 1