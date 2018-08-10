import sys
from geometry_msgs.msg import Twist
import rospy
import operator
from take_photo import TakePhoto
import cv2 as cv
from find_match import FindMatch
import pickle
import time

camera = TakePhoto()
twist = Twist()
find = FindMatch()

query_descriptors = []
query_keypoints = []
good_matches = []
descriptors_dataset = []
dataset_names = []
minHessian = 400


def move():

    # read dataset descriptors and locations
    with open('dataset2/dataset2_descriptors.txt', 'rb') as fp:
        descriptors_dataset = pickle.load(fp)
    with open('dataset2/dataset2_names.txt', 'rb') as fp:
        dataset_names = pickle.load(fp)

    pub = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
    rospy.init_node('teleop_py',anonymous=True)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        good_matches = []
        query_descriptors = []
        query_keypoints = []

        #twist.angular.z = 0.5
        #pub.publish(twist)
        index = 0
        img_title ='query_robot/queryImg.jpg'
        camera.take_picture(img_title)

        queryImg = cv.imread(img_title, cv.IMREAD_GRAYSCALE)
        if queryImg is None:
            print('Could not open or find the query image!')
            exit(0)

        # print(queryImg)
        # call functions for feature extraction
        find.getQueryDescriptor(query_descriptors, query_keypoints, queryImg)
        # print(query_descriptors)
        # print(len(descriptors_dataset))
        find.match(good_matches, descriptors_dataset, query_descriptors)
        # print(len(good_matches))

        # find max number of matches - assume best match
        index, value = max(enumerate(good_matches), key=operator.itemgetter(1))
        best_match = dataset_names[index]
        print('i am in ' + best_match)
        rate.sleep()

    # t0 = time.time()
    # # computation time
    # t1 = time.time()
    # time_taken = t1-t0
    # print('computation time: ' + str(time_taken) + 's')


if __name__ == '__main__':
    try:
        # getReady(dataset_names, descriptors_dataset)

        move()
    except rospy.ROSInterruptException:
        pass

# move()
