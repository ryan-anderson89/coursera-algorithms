
def bfs_visited(ugraph, start_node):
    '''takes the provided undirected graph ugraph and the node start_node
    and returns the set consisting of all nodes that are visited by a 
    breadth-first search that starts at start_node'''
    queue = deque()
    visited = {start_node}
    queue.append(start_node)
    while queue:
        next_node = queue.popleft()
        for neighbor in ugraph[next_node]:
            if neighbor not in visited:
                visited.update({neighbor})
                queue.append(neighbor)
    return visited

def cc_visited(ugraph):
    '''takes the undirected graph ugraph and returns a list of sets, where
    each set consists of all the nodes in a connected component. There is one
    set in the list for each connected component in ugraph and nothing else'''
    remaining_nodes = list(ugraph.keys())
    connected_components = []
    while remaining_nodes:
        node = remaining_nodes.pop()
        visited = bfs_visited(ugraph, node)
        connected_components.append(visited)
    return connected_components
    
def largest_cc_size(ugraph):
    '''takes the undirected graph ugraph and returns the size of the largest
    connected component in ugraph'''
    connected_components = cc_visited(ugraph)
    return max([len(component) for component in connected_components])

def compute_resilience(ugraph, attack_order):
    '''takes the undirected graph ugraph and a list of nodes attack_order and
    iterates through the nodes in attack_order. For each node in the list, the
    function removes the given node and its edges from the graph and then
    computes the size of the largest connected compontent for the resulting
    graph. Returns a list whose k+1 entry in the size of the largest connected
    component in the resulting graphs after the removal of the first k nodes
    in attack_order'''
    attack_result = [largest_cc_size(ugraph)]
    for node in attack_order:
        for neighbor in ugraph[node]:
            ugraph[neighbor].remove(node)
        del(ugraph[node])
        attack_result.append(largest_cc_size(ugraph))
    return attack_result