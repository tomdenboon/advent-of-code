def dfs(node, graph, visited):
    if node == 'end':
        return 1
    if node.islower():
        if node not in visited:
            visited[node] = True
        else:
            return 0
    reached_end = 0
    for next_node in graph[node]:
        reached_end += dfs(next_node, graph, visited.copy())
    return reached_end


graph = {}
for line in open('input'):
    node1, node2 = line.strip().split('-')
    if node1 not in graph:
        graph[node1] = []
    if node2 not in graph:
        graph[node2] = []
    graph[node1].append(node2)
    graph[node2].append(node1)
print(dfs('start', graph, {}))
