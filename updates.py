from random import sample, choice, randint
from copy import deepcopy
import time

from libs import robositygame as rcg


def randomize_obstacles(graph_dict: dict[int, list[int]], obstacles_count: int = 2) -> list[tuple[int, int]]:
    """Случайная генерация препятствий (желтых машин)"""
    blocks = []
    starts = sample(list(graph_dict.keys()), k=obstacles_count)
    for start in starts:
        blocks.append((start, choice(graph_dict[start])))
    return blocks


def randomize_car_position(graph_dict: dict, rot_dict: dict) -> tuple[int, int]:
    """Случайная генерация начальной позиции машинки"""
    position = choice(list(graph_dict.keys()))
    rotation = choice(rot_dict[position])
    return position, rotation


def randomize_map() -> tuple[rcg.Graph, rcg.Rover, list[list[int]]]:
    """Случайная безошибочная генерация препятствий и начального положения машинки.

    Проверка проводится с помощью кода из completion.check.py, который
    написал разработчик этого симулятора. Этот код проверяет возможность машинки
    сделать круг, проехав все точки без пересечений.
    """
    original_graph_dict = deepcopy(rcg.Graph.GraphDict)
    original_weight_dict = deepcopy(rcg.Graph.WeightDict)
    original_rot_dict = deepcopy(rcg.Graph.RotDict)
    blocks = randomize_obstacles(rcg.Graph.GraphDict, obstacles_count=randint(1, 3))
    #  Угол поворота: Влево - 0 градусов и дальше против часовой стрелки (90 - вниз и т.д.)
    position, rotation = randomize_car_position(rcg.Graph.GraphDict, rcg.Graph.RotDict)
    graph, model, cycles = rcg.init_game(position, rotation, blocks)
    randomization_cycle = 1
    while not cycles:
        randomization_cycle += 1
        print(f"Цикл генерации номер: {randomization_cycle}")
        rcg.Graph.GraphDict = deepcopy(original_graph_dict)
        rcg.Graph.WeightDict = deepcopy(original_weight_dict)
        rcg.Graph.RotDict = deepcopy(original_rot_dict)
        blocks = randomize_obstacles(rcg.Graph.GraphDict, obstacles_count=randint(1, 3))
        position, rotation = randomize_car_position(rcg.Graph.GraphDict, rcg.Graph.RotDict)
        graph, model, cycles = rcg.init_game(position, rotation, blocks)
    print()
    print(f"Start position: {position}\nStart rotation: {rotation}\n")
    return graph, model, cycles


def count_length(route: list[int]) -> int:
    length = 0
    prev_point = route[0]
    for point in route[1:]:
        index = rcg.Graph.GraphDict[prev_point].index(point)
        length += rcg.Graph.WeightDict[prev_point][index]
        prev_point = point
    return length