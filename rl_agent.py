
import rospy
from agent_move import move
# from map_msgs import GoalStatusArray
from move_base_msgs.msg import *
from std_msgs.msg import String
import numpy as np
from nav_msgs.msg import Odometry
from map import CostmapUpdater
#
# class State:
#
#     def __init__(self,enemy_goal,enemy_location,serial_num,my_location):
#         self.enemy_goal = enemy_goal #tuple (int,int)
#         self.enemy_location = enemy_location #tuple (int,int)
#         self.my_location = my_location
#         # self.enemy_path_len = enemy_path_len #int
#         self.serial_num = serial_num
#
#     def get_serial_num(self):
#         return self.serial_num
#
# class Action:
#     def __init__(self, who_did, new_location):
#         self.who_did_the_action = who_did
#         self.new_location = new_location
#
#
# class Environment:
#     def __init__(self, map_size_x, map_size_y, dirty_location):
#         self.states = self.prepare_states(map_size_x, map_size_y)
#         self.dirty_location = dirty_location
#         self.init_dirty_location = dirty_location
#         self.cur_state = None
#         self.actions = []
#
#     def prepare_states(self,map_size_x,map_size_y):
#         index = 0
#         states_list = []
#         for x_enemy_goal in range(0,map_size_x):
#             for y_enemy_goal in range(0,map_size_y):
#                 enemy_goal=(x_enemy_goal,y_enemy_goal)
#                 for x_enemy_location in range(0, map_size_x):
#                     for y_enemy_location in range(0, map_size_y):
#                         enemy_location=(x_enemy_location,y_enemy_location)
#                         for x_my_location in range(0, map_size_x):
#                             for y_my_location in range(0, map_size_y):
#                                 my_location = (x_my_location, y_my_location)
#                                 states_list.append(State(enemy_goal=enemy_goal,enemy_location=enemy_location,serial_num=index,my_location=my_location))
#                                 index += 1
#         return states_list
#
#     def update_dirty_location(self, dirty_location):
#         self.dirty_location = dirty_location
#
#
#
#     def step(self, action):
#         pass
#
#     def reset(self):
#         pass



class rl_agent:
    def __init__(self,agent_id,init_location):

        # prepare the map
        self.map_service = CostmapUpdater(agent_id)

        # get the shape of the map
        self.width, self.height = self.map_service.get_shape()

        # get the valid places where to go
        self.valid_locations = self.map_service.get_valid_locations_map()
        self.static_map = self.map_service.get_static_map()




        self.agent_id = agent_id
        self.states = None
        self.last_position = None
        self.move_new_location = move
        self.init_location = init_location
        self.dirty_location = None

        # my location
        # rospy.Subscriber('/tb3_{}/move_base/feedback'.format(agent_id), MoveBaseActionFeedback, self.update_my_location)
        rospy.Subscriber('/tb3_{}/odom'.format(agent_id), Odometry, self.update_my_location)
        self.robot_my_location_msg = None
        self.robot_my_location_gazebo = dict()
        self.robot_my_location_map = dict()

        # enemy location
        rospy.Subscriber('/tb3_{}/odom'.format(1-agent_id), Odometry, self.update_enemy_location)
        self.robot_enemy_location_msg = None
        self.robot_enemy_location_gazebo = dict()
        self.robot_enemy_location_map = dict()

        # enemy goal
        rospy.Subscriber('/tb3_{}/move_base/goal'.format(1-agent_id), MoveBaseActionGoal, self.update_enemy_goal)
        rospy.Subscriber('dirt'.format(1-agent_id), String, self.update_dirty_location)

        # enemy plan
        

        self.dirty_location_msg = None

        self.update_enemy_goal_msg = None
        self.dirty_location = []
        # /tb3_1/move_base_simple/goal



    def update_my_location(self,msg):
        self.robot_my_location_msg = msg
        pose = self.robot_my_location_msg.pose.pose.position

        self.robot_my_location_gazebo['x'] = pose.x
        self.robot_my_location_gazebo['y'] = pose.y
        self.robot_my_location_gazebo['w'] = self.robot_my_location_msg.pose.pose.orientation.w

        self.robot_my_location_map['w'] = self.robot_my_location_gazebo['w']

        self.robot_my_location_map['x'], self.robot_my_location_map['y'] = self.map_service.position_to_map(np.array([self.robot_my_location_gazebo['x'],self.robot_my_location_gazebo['y']]))
        # print (self.robot_my_location_map['x'], self.robot_my_location_map['y'])
        #print( self.robot_my_location_msg)

    def update_enemy_location(self,msg):
        self.robot_enemy_location_msg = msg
        pose = self.robot_enemy_location_msg.pose.pose.position

        self.robot_enemy_location_gazebo['x'] = pose.x
        self.robot_enemy_location_gazebo['y'] = pose.y
        self.robot_enemy_location_gazebo['w'] = self.robot_enemy_location_msg.pose.pose.orientation.w

        self.robot_enemy_location_map['w'] = self.robot_enemy_location_gazebo['w']

        self.robot_enemy_location_map['x'], self.robot_enemy_location_map['y'] = self.map_service.position_to_map(np.array([self.robot_enemy_location_gazebo['x'],
                                                                                                                            self.robot_enemy_location_gazebo['y']]))
        # print (self.robot_enemy_location_map['x'], self.robot_enemy_location_map['y'])


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
            # print('dirty location are {}',self.dirty_location)


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