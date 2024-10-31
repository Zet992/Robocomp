import basic_control_module as bcm


class CurrentPath:
    def __init__(self, path, end):
        self.end = end
        if type(path) == Vertex:
            self.path = [path]
            self.weight = 0
        else:
            self.path = path.path.copy()
            self.weight = path.weight

    def add_points(self, point, weight, graph):
        self.path.append(graph[point - 1])
        self.weight += weight

    def last_point(self):
        return self.path[-1]

    def check(self):
        return self.path[-1] == self.end

    def print(self):
        print(*list(map(lambda x: x.number, self.path)), "=", self.weight)


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
        temp_all_paths = []
        for path in all_paths:
            if checked_copy(path.path[1:]):
                all_paths.remove(path)
                continue

            current_vertex = path.last_point()
            neighbours = current_vertex.neighbours
            for vertex in neighbours:
                current_path = CurrentPath(path, end)
                current_path.add_points(vertex[0], vertex[1], graph)
                temp_all_paths.append(current_path)
                if current_path.check():
                    if len(graph) == len(set(current_path.path)):
                        answer_paths.append(current_path)
        all_paths = temp_all_paths.copy()

    shortest_answer = answer_paths[0]
    for path in answer_paths[1:]:
        if path.weight < shortest_answer.weight:
            shortest_answer = path

    return list(map(lambda x: x.number, shortest_answer.path))


def double_rotate():
    rover.rot_right()
    rover.rot_right()


def main():
    graph = bcm.Graph()
    rover = bcm.Rover(cur_pos=7, cur_rot=180, graph=graph)
    graph_dict = graph.GraphDict
    weight_dict = graph.WeightDict
    rot_dict = graph.RotDict
    rot_to_func = {
        0: lambda x: x,
        90: rover.rot_left,
        180: double_rotate,
        270: rover.rot_right,
    }

    ggraph = Graph(graph.GraphDict, graph.WeightDict).Graph
    vertex_start = cycles[0][0]
    start = ggraph[vertex_start]
    end = ggraph[vertex_start]
    route = perebor(graph=ggraph, start=start, end=end)
    print(f"Our route is {route}")

    prev_point = route[0]
    length = 0
    for i in route[1:]:
        cur_point_index = graph_dict[prev_point].index(i)
        rotation = (rot_dict[prev_point][cur_point_index] - model.cur_rot) % 360
        print("Point:", i, "Rotation:", rotation)
        rot_to_func[rotation]()
        rover.go_to_forward_node()
        length += weight_dict[prev_point][cur_point_index]
        prev_point = i
    print("The total length:", length)


if __name__ == "__main__":
    main()
