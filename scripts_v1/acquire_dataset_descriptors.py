import cv2 as cv
import numpy as np
from PIL import Image
import glob
import pickle
import time
import os


class Descriptors():

    #known dataset lists
    img_dataset = []
    keypoints_dataset = []
    descriptors_dataset = []
    dataset_names = []
    names_full = []
    minHessian = 400    # as in paper
    # dataset_path = 'dataset/'

    def getDescriptor(self, dataset_path, img_path, Hessian_val, descriptors):
        names_full = []
        names = []
        img_dataset = []
        #  read all images from folder - set directory accordingly
        for filename in glob.glob(img_path + '*.jpg'):  # for all images
            im = cv.imread(filename, cv.IMREAD_GRAYSCALE)
            head, tail = os.path.split(filename)
            name = tail.split('_', 1)
            print(tail)
            names_full.append(filename)
            names.append(name[0])
            img_dataset.append(im)

        # print(len(img_dataset))
        # check if ok
        for i in img_dataset:
            if i is None:
                print('Could not open or find the images!')
                exit(0)

        # acquire descriptor list from dataset - keypoints also available if needed
        detector = cv.xfeatures2d_SURF.create(hessianThreshold=Hessian_val)
        for index, image in enumerate(img_dataset):
            kp, des = detector.detectAndCompute(image, None)
            # if keypoints are needed - add list to function
            # keypoints.append(kp)
            descriptors.append(des)
        # print(len(descriptors))

        # write descriptors on txt file to be used later
        # not readable by humans, can be changed later if necessary
        with open(img_path + 'descriptors.txt', 'wb') as fp:
            fp.truncate(0)
            pickle.dump(descriptors, fp)
            print('\nsaved descriptors.txt in ' + dataset_path)

        with open(img_path + 'namesFull.txt', 'wb') as fp:
            fp.truncate(0)
            pickle.dump(names_full, fp)
            print('saved namesFull.txt in ' + dataset_path)

        with open(img_path + 'names.txt', 'wb') as fp:
            fp.truncate(0)
            pickle.dump(names, fp)
            print('saved names.txt in ' + dataset_path + '\n')

    # # call function
    # getDescriptor(dataset_path, dataset_path, minHessian, descriptors_dataset)
    # print(len(descriptors_dataset))
    # print(len(keypoints_dataset))
    # # print(keypoints_dataset)
