

import rospy
from rl_agent import rl_agent
from map import MapService
import numpy as np
import multiprocessing

X_init_pose_id_0 = -0.0
y_init_pose_id_0 = 0.0


class Env:

    def __init__(self,init_position_robot_first,
                 init_position_robot_second
                 ):
        rospy.init_node('movebase_client_py')

        # load the map
        # self.map = MapService()


        self.first_agent_rl_agent_id = 0
        self.second_agent_rl_agent_id = 1
        self.first_agent_rl_agent = rl_agent(
            agent_id=self.first_agent_rl_agent_id,
            init_location=init_position_robot_first
        )
        self.second_agent_rl_agent = rl_agent(
            agent_id=self.second_agent_rl_agent_id,
            init_location=init_position_robot_second
        )

    def first_model(self):
        self.first_agent_rl_agent.learning()

    def second_model(self):
        self.second_agent_rl_agent.learning()

    def learning(self):
        # to it parnell
        #worker_1 = multiprocessing.Process(name='first model', target=self.first_model)
        # worker_2 = multiprocessing.Process(name='second model', target=self.second_model)

        # worker_1.start()
        # worker_2.start()
        # worker_1.join()
        # worker_2.join()
        self.first_agent_rl_agent.learning()
        # self.second_agent_rl_agent.learning()

if __name__ == '__main__':
    # map_service = MapService()
    init_position_robot_first = dict()
    init_position_robot_first['agent_id'] = 0
    # init_position_robot_first['x'], init_position_robot_first['y'] = map_service.position_to_map(np.array([0,0]))


    init_position_robot_first['x'], init_position_robot_first['y'] = 0, 0
    init_position_robot_first['w'] = 1

    init_position_robot_second = dict()
    init_position_robot_second['agent_id'] = 1
    # init_position_robot_second['x'], init_position_robot_second['y'] = map_service.position_to_map(np.array([0,1]))
    init_position_robot_second['x'], init_position_robot_second['y'] = 1.0, 0
    init_position_robot_second['w'] = 1

    env = Env(init_position_robot_first=init_position_robot_first,
              init_position_robot_second=init_position_robot_second
              )

    env.learning()