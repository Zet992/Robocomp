class CurrentPath:
    def __init__(self, path, end):
        self.end = end  # Бесполезная переменная, нигде не используется
        if type(path) == Vertex:
            self.path = [path]
            self.weight = 0
        else:
            self.path = path.path.copy()
            self.weight = path.weight

    def add_points(self, point, weight, graph):
        self.path.append(graph[point-1])
        self.weight += weight

    def last_point(self):
        return self.path[-1]
    
    def check(self):
        return self.path[-1] == self.path[0]
    
    def print(self):
        print(*list(map(lambda x: x.number, self.path)), "=" , self.weight)


class Vertex:
    def __init__(self, n):
        self.number = n
        self.neighbours = []

    def add_neighbours(self, n, weight):
        self.neighbours.append((n, weight))


class Graph:
    def __init__(self, graph, weight):
        self.Graph = []
        for i in range(len(graph.keys())):
            n = list(graph.keys())[i]
            vertex = Vertex(n)
            for j in range(len(graph[n])):
                vertex.add_neighbours(graph[n][j], weight[n][j])
            self.Graph.append(vertex)


def checked_copy(l1):
    s1 = list(set(l1))
    for i in s1:
        if l1.count(i) > 2:
            return True


def perebor(graph, start, end):
    all_paths = [CurrentPath(start, end)]
    answer_paths = []
    n = 0

    while n <= len(graph) or len(answer_paths) == 0:
        n += 1
        temp_all_paths = []  # Нужен, т.к. all_paths в цикле изменять нельзя
        for path in all_paths:
            # Проверка на Гамильтонов цикл (вершину проехать можно только один раз)
            if checked_copy(path.path[1:]):  # Если вершину проехали больше 2 раз
                all_paths.remove(path)  # Удаляем путь из списка всех путей
                continue  # И больше не рассматриваем данный маршрут

            current_vertex = path.last_point()
            neighbours = current_vertex.neighbours  # список с кортежами сосед. вершин (номер, вес)
            for vertex in neighbours:
                current_path = CurrentPath(path, end)  # Создаем новой путь
                current_path.add_points(vertex[0], vertex[1], graph)  # И добавляем текущую вершину
                temp_all_paths.append(current_path)
                if current_path.check():  # Если путь вернулся в начало
                    if (len(graph) == len(set(current_path.path))):  # И длина равна количеству вершин
                        answer_paths.append(current_path)  # Получаем подходящий путь
        all_paths = temp_all_paths.copy()
    maxs = [answer_paths[0]]

    for path in answer_paths:
        if len(set(path.path)) > len(set(maxs[0].path)):
            maxs = [path]
        elif len(set(path.path)) == len(set(maxs[0].path)):
            maxs.append(path)
    answer = maxs

    # Выбираем наименее длинный
    shortest_answer = answer[0]
    for path in answer[1:]:
        if path.weight < shortest_answer.weight:
            shortest_answer = path

    return list(map(lambda x: x.number, shortest_answer.path))
