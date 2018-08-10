import cv2 as cv
import numpy as np
from PIL import Image
import glob
import pickle
import time


class Descriptors():

    #known dataset lists
    img_dataset = []
    keypoints_dataset = []
    descriptors_dataset = []
    dataset_names = []
    names_full = []
    minHessian = 400    # as in paper


    def acquire_des(self, img_path):
        #  read all images from folder - set directory accordingly
        for filename in glob.glob(img_path + '*.jpg'):  # for all images
            im = cv.imread(filename, cv.IMREAD_GRAYSCALE)
            name = filename.split('_', 1)
            names_full.append(filename)
            dataset_names.append(name[0])
            img_dataset.append(im)


    # print(len(img_dataset))
    # print(dataset_names)
    #
    # # check if ok
    # for i in img_dataset:
    #     if i is None:
    #         print('Could not open or find the images!')
    #         exit(0)
    #
    # # acquire descriptor list from dataset - keypoints also available if needed
    # def getDescriptor(descriptors, keypoints, img):
    #     detector = cv.xfeatures2d_SURF.create(hessianThreshold=minHessian)
    #     for index, image in enumerate(img):
    #         kp, des = detector.detectAndCompute(image, None)
    #         # if keypoints are needed
    #         # keypoints.append(kp)
    #         descriptors.append(des)
    #         keypoints.append(kp)
    #
    # # call function
    # getDescriptor(descriptors_dataset, keypoints_dataset, img_dataset)
    # print(len(descriptors_dataset))
    # print(len(keypoints_dataset))
    # # print(keypoints_dataset)
    #
    #
    #
    # # write descriptors on txt file to be used later
    # # not readable by humans, can be changed later if necessary
    # with open('dataset_descriptors.txt', 'wb') as fp:
    #     fp.truncate(0)
    #     pickle.dump(descriptors_dataset, fp)
    #     print('saved dataset_descriptors.txt')
    #
    # with open('dataset_namesFull.txt', 'wb') as fp:
    #     fp.truncate(0)
    #     pickle.dump(names_full, fp)
    #     print('saved dataset_namesFull.txt')
    #
    # with open('dataset_names.txt', 'wb') as fp:
    #     fp.truncate(0)
    #     pickle.dump(dataset_names, fp)
    #     print('saved dataset_names.txt')
