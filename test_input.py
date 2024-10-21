from random import randint

from libs import robositygame as rcg
from libs.robositygame import Graph
from updates import randomize_obstacles, randomize_car_position


graph_dict = Graph.GraphDict
rot_dict = Graph.RotDict
blocks = randomize_obstacles(graph_dict, obstacles_count=randint(1, 3))
#  Влево - 0 градусов и дальше против часовой стрелки
position, rotation = randomize_car_position(graph_dict, rot_dict)
print(f"Start position: {position}\nStart rotation: {rotation}\n")

graph, model, com_flag = rcg.init_game(position, rotation, blocks)
if com_flag:
    # ЗДЕСЬ НАЧИНАЮТСЯ ВАШИ КОММАНДЫ/АЛГОРИТМ
    model.mov_to_front_point()
    model.mov_to_front_point()
    model.mov_to_right_point()
    model.mov_to_right_point()
    model.mov_to_front_point()
    model.mov_to_front_point()
    model.mov_to_right_point()
    model.mov_to_left_point()
    model.mov_to_front_point()
    model.mov_to_right_point()
    model.mov_to_right_point()
    model.mov_to_front_point()
    model.mov_to_front_point()
    model.mov_to_right_point()
    model.mov_to_front_point()
    #ЗДЕСЬ ЗАКАНЧИВАЮТСЯ ВАШИ КОМАНДЫ/АЛГОРИТМ
else:
    print("This track cannot be completed! Change base_info!")
rcg.finalize(model=model, graph=graph)
