

import rospy
from rl_agent import rl_agent
# from map import MapService
import numpy as np
import multiprocessing

X_init_pose_id_0 = -0.0
y_init_pose_id_0 = 0.0


class Env:

    def __init__(self,init_position_robot,
                 ):
        rospy.init_node('rl_agent__py')

        # load the map
        # self.map = MapService()

        self.agent_rl_agent = rl_agent(
            agent_id=0,
            init_location=init_position_robot,
        )




    def learning(self):
        # to it parnell
        #worker_1 = multiprocessing.Process(name='first model', target=self.first_model)
        # worker_2 = multiprocessing.Process(name='second model', target=self.second_model)

        # worker_1.start()
        # worker_2.start()
        # worker_1.join()
        # worker_2.join()
        self.agent_rl_agent.learning()

if __name__ == '__main__':
    # map_service = MapService()
    init_position_robot = dict()
    init_position_robot['agent_id'] = 0
    # init_position_robot_first['x'], init_position_robot_first['y'] = map_service.position_to_map(np.array([0,0]))


    init_position_robot['x'], init_position_robot['y'] = 0, 0
    init_position_robot['w'] = 1

    init_position_robot_second = dict()
    init_position_robot_second['agent_id'] = 0
    # init_position_robot_second['x'], init_position_robot_second['y'] = map_service.position_to_map(np.array([0,1]))

    env = Env(init_position_robot=init_position_robot)

    env.learning()