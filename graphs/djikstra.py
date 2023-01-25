def initialize_graph_cost(input_graph: dict) -> dict:
    cost = {}
    for node in input_graph.keys():
        cost[node] = float('inf')

    for start_node in input_graph['start'].keys():
        cost[start_node] = input_graph['start'][start_node]

    return cost

def initialize_parents(input_graph: dict) -> dict:
    parent = {}

    for node in input_graph.keys():
        parent[node] = None

    for start_node in input_graph['start'].keys():
        parent[start_node] = 'start'

    return parent

def get_lower_not_processed_cost_node_to_reach(cost: dict, processed_nodes: list) -> dict:
    lower_node_to_reach = None
    lower_edge = float('inf')

    for node in cost.keys():
        if node in processed_nodes:
            continue

        if cost[node] < lower_edge:
            lower_node_to_reach = node
            lower_edge = cost[node]

    return lower_node_to_reach


def get_total_cost(input_graph: dict) -> int:
    cost = initialize_graph_cost(input_graph)
    parent = initialize_parents(input_graph)
    processed_nodes = ['start']   

    while(set(processed_nodes) != set(input_graph.keys())):
        node = get_lower_not_processed_cost_node_to_reach(cost, processed_nodes)

        for neighboor in input_graph[node]:
            total_cost_to_reach_neighboor = cost[node] + input_graph[node][neighboor]

            if total_cost_to_reach_neighboor < cost[neighboor]:
                cost[neighboor] = total_cost_to_reach_neighboor
                parent[neighboor] = node

        processed_nodes.append(node)

    return cost['end']







