# traverse graph and compute number of paths from start to end
#

def create_graph():
    my_graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D', 'E'],
        'D': ['B', 'C', 'E'],
        'E': ['C', 'D']
    }
    return my_graph


def traverse_graph(my_graph, start_node, end_node, path=None):
    if path is None:
        path = []
    path = path + [start_node]
    if start_node == end_node:
        return [path]
    if start_node not in my_graph:
        return []
    paths = []
    for node in my_graph[start_node]:
        if node not in path:
            child_paths = traverse_graph(my_graph, node, end_node, path)
            for child_path in child_paths:
                paths.append(child_path)
    return paths


if __name__ == '__main__':
    graph = create_graph()
    print(graph)
    start = 'A'
    end = 'E'
    paths = traverse_graph(graph, start, end)
    print(f'paths from {start} to {end}: ')
    for path in paths:
        print(path)
    print(f'number of paths from {start} to {end}: {len(paths)}')
    print(f'shortest path from {start} to {end}: {min(paths, key=len)}')