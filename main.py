from libs import robositygame as rcg
from libs.robositygame import Graph

from updates import randomize_obstacles, randomize_car_position, randomize_map
from updates import count_length


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
    length = float("inf")
    route = None
    for i in cycles:
        var_route = list(map(lambda x: x + 1, i))
        new_length = count_length(var_route)
        print(var_route)
        print(new_length)
        if new_length < length:
            length = new_length
            route = var_route
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
