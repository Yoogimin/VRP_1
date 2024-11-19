import heapq

def dijkstra(start):
    # 최단 거리를 저장할 딕셔너리. 모든 값을 무한대로 초기화
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # 모든 노드의 최단 경로를 저장할 딕셔너리 
    paths = {node: [] for node in graph}
    paths[start] = [start]

    # 모든 노드를 처리할 때까지 반복
    queue = [(0, start)]
    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # 현재 노드의 최단 거리가 이미 갱신된 경우
        if current_distance > distances[current_node]:
            continue

        # 인접 노드 처리
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            # 최단 거리 갱신
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))
                paths[adjacent] = paths[current_node] + [adjacent]

    return distances, paths

# 그래프 예시
graph = {
    'A':{'B': 4, 'C': 2},
    'B':{'C': 5, 'D': 10},
    'C':{'D': 3, 'E': 2},
    'D':{'E': 4},
    'E':{}
}

distances, paths = dijkstra('A')
print("Distances:", distances)
print("Paths:", paths)
