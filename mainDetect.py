from yolo.detect import *
import cv2

import sys

cfg = 'yolo/model/yolo-drone.cfg'
data = 'yolo/model/yolo-drone.data'
weights = 'yolo/model/yolo-drone_190000_49.weights'
images = 'Input'
img_size = 416
conf_thres = 0.15
nms_thres = 0.1
fourcc = 'mp4v'
output = 'output'

# img = cv2.imread('InputImages/test7a.jpg')
# detector = Frame_detecter( cfg, data, weights, output, img_size = 416)
# DetectFlag, BBox, probability = detector.divideAndDetectFrame(img)
# a=1
# img = cv2.imread('InputImages/test1b.jpg')
#
# BBox, probability = detector.detectFrame(img)




if __name__ == "__main__":
    vide_name = sys.argv[1]
    detection_video('Input/'+vide_name, cfg=cfg, data = data, weights = weights, save_output = True, show_output = True)
    