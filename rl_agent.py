
import rospy
from agent_move import move
# from map_msgs import GoalStatusArray
from move_base_msgs.msg import *
from std_msgs.msg import String
import numpy as np

class State:

    def __init__(self,enemy_goal,enemy_location,enemy_path_len,dirty_location):
        self.enemy_goal = enemy_goal
        self.enemy_location = enemy_location
        self.enemy_path_len = enemy_path_len
        self.dirty_location = dirty_location


class rl_agent:
    def __init__(self,agent_id,init_location):
        self.agent_id = agent_id
        self.states = None
        self.last_position = None
        self.move_new_location = move
        self.init_location = init_location
        self.dirty_location = None
        rospy.Subscriber('/tb3_{}/move_base/goal'.format(1-agent_id), MoveBaseActionGoal, self.update_enemy_goal)
        rospy.Subscriber('/tb3_{}/move_base/feedback'.format(1-agent_id), MoveBaseActionFeedback, self.update_enemy_location)
        rospy.Subscriber('dirt'.format(1-agent_id), String, self.update_dirty_location)
        self.dirty_location_msg = None
        self.robot_enemy_location_msg = None
        self.update_enemy_goal_msg = None
        self.dirty_location = []
        # /tb3_1/move_base_simple/goal

    def update_dirty_location(self,msg):
        # print('dirty location')
        self.dirty_location_msg = msg
        self.dirty_location = []
        string_dirty_list = eval(str(self.dirty_location_msg).split(':')[1]).split(']')
        # print(self.dirty_location_msg)
        for index in range(0, len(string_dirty_list) - 1):
            val = string_dirty_list[index].split('[')[1].split(',')
            loc = np.array([float(val[0]), float(val[1])])
            # print(loc)
            self.dirty_location.append(loc)

    def update_enemy_location(self,msg):
        # print('the enemy location is!!!!')
        self.robot_enemy_location_msg = msg
        # print(self.robot_enemy_location_msg)

    def update_enemy_goal(self,msg):
        # print('goal_goal_im_now_his_goal!!')
        self.update_enemy_goal_msg = msg
        # print(self.update_enemy_goal_msg)
    # ADD ITAI CODE


    def position_to_chunk(self,position):
        pass

    def chunk_to_position(self,chunk):
        pass

    def step(self,position):
        self.move_new_location(**position)
        # pass

    def learning(self):
        # move to new position
        while self.update_enemy_goal_msg is None:
           pass

        while self.dirty_location_msg is not None:
            position = dict()
            position['agent_id'] = self.agent_id

            # position['x'] = 0
            # position['y'] = 0.8
            # position['w'] = 1.0
            # self.step(position)
            #
            # position['x'] = 1
            # position['y'] = 0.8
            # position['w'] = 1.0
            # self.step(position)
            position['x'] = 0
            position['y'] = 0.5
            position['w'] = 1.0

            self.step(position)
            print('dirty location are {}',self.dirty_location)


        # finish to learn, return to init location
        self.move_new_location(**self.init_location)


        # finish to
        # x = 1.0, y = 0.5, w = 1.0)
        # postion_1 = (0, x=1.0, y=0.5, w=1.0):

    def move_new_location(self,location):
        # do step to the next chunk
        pass


    def training_loop(self, model_info, laser_info):
        pass




if __name__ == '__main__':
    pass