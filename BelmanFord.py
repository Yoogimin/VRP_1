def bellman_ford(start):
    distance = {node: float('infinity') for node in graph}
    distance[start] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbour, weight in graph[node]:
                if distance[node] + weight < distance[neighbour]:
                    distance[neighbour] = distance[node] + weight

    for node in graph:
        for neighbour, weight in graph[node]:
            if distance[node] + weight < distance[neighbour]:
                return "Graph contains a negative weight cycle"
    return distance


# 예시 그래프
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', -3), ('D', 2)],
    'C': [('D', 3)],
    'D': []
}

# 벨만-포드 알고리즘 실행
distances = bellman_ford('A')
print(distances)