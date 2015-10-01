'''implements directed graph examples and functions to generate a complete directed
graph of n points, determine in-degrees of directed graphs and in-degree 
distribution of directed graphs'''
from collections import Counter

EX_GRAPH0 = {0:{1,2},
            1:set(),
            2:set()}

EX_GRAPH1 = {0:{1,4,5},
            1:{2,6},
            2:{3},
            3:{0},
            4:{1},
            5:{2},
            6:set()}

EX_GRAPH2 = {0:{1,4,5},
            1:{2,6},
            2:{3,7},
            3:{7},
            4:{1},
            5:{2},
            6:set(),
            7:{3},
            8:{1,2},
            9:{0,3,4,5,6,7}}

def make_complete_graph(num_nodes):
    '''given a number of nodes, returns a dictionary representation
    of a complete directed graph with the specified number of nodes.
    returns an empty dict if an invalid number of nodes is given'''
    if num_nodes <= 0:
        return dict()
    else:
        nodes = set(range(num_nodes))
        return {node: set(neighbor for neighbor in nodes - {node})
                for node in nodes}

def dict_value_counts(dictionary):
    '''given a dictionary, returns a new dict with values of the original
    as keys and the count of each original value as the new value'''
    return dict(Counter(value for key in dictionary for value in dictionary[key]))
    
def compute_in_degrees(digraph):
    '''given a directed graph digraph, computes the in-degrees for
    each node in the graph. returns a dictionary with the same keys
    as the digraph and a count of edges with that node as a head'''
    count = dict_value_counts(digraph)
    for key in digraph:
        if key not in count:
            count[key] = 0
    return count

def in_degree_distribution(digraph):
    '''given a directed graph digraph, computes the unnormalized
    distribution of the in-degrees of the graph. returns a dict
    with keys equal to the in-degrees of nodes in the graph.'''
    in_degrees = compute_in_degrees(digraph)
    return dict(Counter(in_degrees.values()))