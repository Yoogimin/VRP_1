import random
import numpy as np
import matplotlib.pyplot as plt


# 경로 시각화 함수 추가
def plot_path(cities, path):
    fig, ax = plt.subplots()
    x = []
    y = []
    for city in path:
        x.append(cities[city][0])
        y.append(cities[city][1])
        plt.annotate(city, (cities[city][0], cities[city][1]))

    x.append(cities[path[0]][0])  # 출발점으로 돌아오기
    y.append(cities[path[0]][1])

    ax.plot(x, y, c='violet', marker='o')
    plt.show()


# 도시의 좌표를 무작위로 생성
def create_cities(n):
    return {i: (random.uniform(0, 200), random.uniform(0, 200)) for i in range(n)}


# 경로의 총 거리를 계산
def calculate_distance(cities, path):
    total_distance = 0
    for i in range(len(path)):
        total_distance += np.sqrt((cities[path[i]][0] - cities[path[i-1]][0])**2 +
                                  (cities[path[i]][1] - cities[path[i-1]][1])**2)
    return total_distance


# 초기 경로 생성
# def create_initial_population(cities, population_size):
#     return [random.sample(cities.keys(), len(cities)) for _ in range(population_size)]
def create_initial_population(cities, population_size):
    return [random.sample(list(cities.keys()), len(cities)) for _ in range(population_size)]


# 경로 선택 (룰렛 휠 선택)
def select(population, cities, elite_size):
    fitness_results = {}
    for i in range(len(population)):
        fitness_results[i] = calculate_distance(cities, population[i])
    sorted_fitness = sorted(fitness_results.items(), key=lambda x: x[1])
    selected = [population[i[0]] for i in sorted_fitness[:elite_size]]
    return selected


# 교차 (Crossover)
def crossover(parent1, parent2):
    child = []
    child_p1 = []
    child_p2 = []

    gene_a = int(random.random() * len(parent1))
    gene_b = int(random.random() * len(parent1))

    start_gene = min(gene_a, gene_b)
    end_gene = max(gene_a, gene_b)

    for i in range(start_gene, end_gene):
        child_p1.append(parent1[i])

    child_p2 = [item for item in parent2 if item not in child_p1]

    child = child_p1 + child_p2
    return child


# 돌연변이 (Mutation)
def mutate(individual, mutation_rate):
    for swapped in range(len(individual)):
        if random.random() < mutation_rate:
            swap_with = int(random.random() * len(individual))

            city1 = individual[swapped]
            city2 = individual[swap_with]

            individual[swapped] = city2
            individual[swap_with] = city1
    return individual


# 새로운 세대 생성
def create_new_generation(population, elite_size, mutation_rate):
    new_generation = []
    selected = select(population, cities, elite_size)
    for i in range(len(population) - elite_size):
        parent1 = selected[i % len(selected)]
        parent2 = selected[(i+1) % len(selected)]
        child = crossover(parent1, parent2)
        new_generation.append(mutate(child, mutation_rate))
    new_generation.extend(selected)
    return new_generation


# 매개변수 설정
n_cities = 100
population_size = 100
elite_size = 20
mutation_rate = 0.01
n_generations = 500

# 도시 생성 및 초기 세대
cities = create_cities(n_cities)
population = create_initial_population(cities, population_size)

# 유전 알고리즘 실행
for i in range(n_generations):
    population = create_new_generation(population, elite_size, mutation_rate)

# 최적 경로 출력
best_route = select(population, cities, 1)[0]
best_distance = calculate_distance(cities, best_route)
print("Best Route:", best_route)
print("Distance:", best_distance)

# 최적 경로 출력 및 시각화
plot_path(cities, best_route)