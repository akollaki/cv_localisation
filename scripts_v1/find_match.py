from __future__ import print_function
import cv2 as cv
import sys
import numpy as np
import operator


class FindMatch:

    # acquisition of descriptors of query image
    def getQueryDescriptor(self, descriptors, img):
        detector = cv.xfeatures2d_SURF.create(hessianThreshold=400)
        kp, des = detector.detectAndCompute(img, None)
        descriptors.append(des)
        # keypoints.append(kp)

    # find matches
    def match(self, good_matches, descriptors_dataset, query_descriptors):
        matcher = cv.DescriptorMatcher_create(cv.DescriptorMatcher_FLANNBASED)
        for index, item in enumerate(descriptors_dataset):
            knn_matches = matcher.knnMatch(descriptors_dataset[index], \
            query_descriptors[0], 2)
            #-- Filter matches using the Lowe's ratio test
            ratio_thresh = 0.7
            nr_good_matches = 0
            for m,n in knn_matches:
                if m.distance < ratio_thresh * n.distance:
                    nr_good_matches += 1
            good_matches.append(nr_good_matches)
