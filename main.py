from libs import robositygame as rcg
from libs.robositygame import Graph
from updates_libs import *

from updates import randomize_obstacles, randomize_car_position, randomize_map


def main():
    graph, model, cycles = randomize_map()
    graph_dict = graph.GraphDict
    weight_dict = graph.WeightDict
    rot_dict = graph.RotDict
    rot_to_func = {
        0: model.mov_to_front_point,
        90: model.mov_to_left_point,
        180: model.mov_to_back_point,
        270: model.mov_to_right_point,
    }
    ggraph = Graph(graph.GraphDict, graph.WeightDict).Graph
    vertex_start = cycles[0][0]
    start = ggraph[vertex_start]
    end = ggraph[vertex_start]
    route = perebor(graph=ggraph, start=start, end=end)
    print(f"Our route is {route}")
    if cycles:
        prev_point = route[0]
        length = 0
        for i in route[1:]:
            cur_point_index = graph_dict[prev_point].index(i)
            rotation = (rot_dict[prev_point][cur_point_index] - model.cur_rot) % 360
            print(rotation, i)
            rot_to_func[rotation]()
            length += weight_dict[prev_point][cur_point_index]
            prev_point = i
    else:
        print("This track cannot be completed! Change base_info!")
    rcg.finalize(model=model, graph=graph)


if __name__ == "__main__":
    main()
