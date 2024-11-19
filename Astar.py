import heapq
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
# import data


def a_star_algorithm(start, end):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0 + heuristics[start], start, [start])]

    while priority_queue:
        current_cost, current_node, route = heapq.heappop(priority_queue)

        if current_node == end:
            return route

        for adjacent, weight in graph[current_node].items():
            new_cost = current_cost + weight - heuristics[current_node] + heuristics[adjacent]
            if new_cost < distances[adjacent]:
                distances[adjacent] = new_cost
                heapq.heappush(priority_queue, (new_cost, adjacent, route + [adjacent]))

    return None


def draw_graph_from_panda():
    plt.figure(figsize=(15, 9))
    g = nx.from_pandas_edgelist(df, 'from', 'to', 'weight', create_using=nx.DiGraph())
    pos = nx.spring_layout(g)
    nx.draw(g, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=15)

    # 휴리스틱 값 라벨 추가
    heuristic_labels = {k: f"\n\n({v})" for k, v in heuristics.items()}
    nx.draw_networkx_labels(g, pos, labels=heuristic_labels)
    print(g)
    edge_labels = nx.get_edge_attributes(g, 'weight')
    print(edge_labels)
    nx.draw_networkx_edge_labels(g, pos)

    # 경로 강조
    print(path)
    if path:
        edges_in_path = [(path[n], path[n + 1]) for n in range(len(path) - 1)]
        nx.draw_networkx_edges(g, pos, edgelist=edges_in_path, edge_color='red', width=2)

    plt.title("A* Algorithm: Path Visualization")
    plt.show()


def draw_graph():
    plt.figure(figsize=(15, 9))
    g = nx.DiGraph(graph)
    pos = nx.spring_layout(g)
    nx.draw(g, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=15)

    # 휴리스틱 값 라벨 추가
    heuristic_labels = {k: f"\n\n({v})" for k, v in heuristics.items()}
    nx.draw_networkx_labels(g, pos, labels=heuristic_labels)

    # 경로 강조
    if path:
        edges_in_path = [(path[n], path[n + 1]) for n in range(len(path) - 1)]
        nx.draw_networkx_edges(g, pos, edgelist=edges_in_path, edge_color='red', width=2)

    plt.title("A* Algorithm: Path Visualization")
    plt.show()


# 예시 그래프
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3},
    'C': {'D': 1, 'E': 6},
    'D': {'F': 2},
    'E': {'F': 2},
    'F': {}
}

df = pd.DataFrame({'from': ['A', 'A', 'B', 'C', 'C', 'D', 'E'],
                   'to': ['B', 'C', 'D', 'D', 'E', 'F', 'F'],
                   'weight': [1, 3, 3, 1, 6, 2, 2]})

# 휴리스틱 값
heuristics = {'A': 9, 'B': 7, 'C': 8, 'D': 5, 'E': 3, 'F': 0}

# A* 알고리즘 실행
path = a_star_algorithm('A', 'F')

# 그래프 시각화
draw_graph_from_panda()
# draw_graph()
