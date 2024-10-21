from random import sample, choice


def randomize_obstacles(graph_dict, obstacles_count=2):
    blocks = []
    starts = sample(list(graph_dict.keys()), k=obstacles_count)
    for start in starts:
        blocks.append([start, choice(graph_dict[start])])
    return blocks


def randomize_car_position(graph_dict, rot_dict):
    position = choice(list(graph_dict.keys()))
    rotation = choice(rot_dict[position])
    return position, rotation
