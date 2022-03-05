import numpy as np


class State:

    def __init__(self, my_location, enemy_location,
                 enemy_goal, enemy_path, dirty_location,
                 valid_locations, state_serial_num,static_map
                 ):
        """

        :param my_location: center location by (int,int)
        :param enemy_location: center location by (int,int)
        :param enemy_goal: center goal by (int,int)
        :param dirty_location: center location of the dirty by [(int,int),..]
        :param valid_locations: valid locations by [(int,int)....]
        :param enemy_path: valid location by [(int,int)....]
        :param state_serial_num: num
        """

        # create a state that is 3d array - first np array


        # create the first layout- my place is 1, opp place is -1, empty cells 0.
        self.dirty_location = dirty_location
        self.enemy_goal = enemy_goal  # tuple (int,int)
        self.enemy_location = enemy_location  # tuple (int,int)
        self.my_location = my_location
        # self.enemy_path_len = enemy_path_len #int
        self.serial_num = state_serial_num

    def get_serial_num(self):
        return self.serial_num

class Action:
    def __init__(self, who_did, new_location):
        self.who_did_the_action = who_did
        self.new_location = new_location


class Environment:
    def __init__(self, map_size_x, map_size_y, dirty_location):
        # self.states = self.prepare_states(map_size_x, map_size_y)
        self.dirty_location = dirty_location
        self.init_dirty_location = dirty_location
        self.cur_state = None
        self.actions = []

    # def prepare_states(self ,map_size_x ,map_size_y):
    #     index = 0
    #     states_list = []
    #     for x_enemy_goal in range(0 ,map_size_x):
    #         for y_enemy_goal in range(0 ,map_size_y):
    #             enemy_goal =(x_enemy_goal ,y_enemy_goal)
    #             for x_enemy_location in range(0, map_size_x):
    #                 for y_enemy_location in range(0, map_size_y):
    #                     enemy_location =(x_enemy_location ,y_enemy_location)
    #                     for x_my_location in range(0, map_size_x):
    #                         for y_my_location in range(0, map_size_y):
    #                             my_location = (x_my_location, y_my_location)
    #                             states_list.append \
    #                                 (State(enemy_goal=enemy_goal ,enemy_location=enemy_location ,serial_num=index
    #                                       ,my_location=my_location))
    #                             index += 1
    #    return states_list

    def update_dirty_location(self, dirty_location):
        self.dirty_location = dirty_location



    def step(self, action):
        pass

    def reset(self):
        pass


if __name__ == '__main__':

    my_location = {'w': 0.9999871423089662, 'x': 199.0, 'y': 200.0}
    enemy_location = {'w': 0.9997237807525646, 'x': 219.0, 'y': 200.0}
    dirty_location = [(1,1),(1,2),(1,3),(1,10)]
    static_map = np.load("static_map.npy")
    s = State(
        my_location=my_location,
        enemy_location=enemy_location,
        static_map=static_map,
        enemy_goal=None,
        enemy_path=None,
        dirty_location=dirty_location
    )

    pass

