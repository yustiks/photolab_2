from mtcnn.mtcnn import MTCNN
import cv2
from datetime import datetime

t = datetime.now()
img = cv2.imread("alena.jpeg")
detector = MTCNN()
result = detector.detect_faces(img)

left_eye = result[0]['keypoints']['left_eye']
right_eye = result[0]['keypoints']['right_eye']
mouth_left = result[0]['keypoints']['mouth_left']
mouth_right = result[0]['keypoints']['mouth_right']
nose = result[0]['keypoints']['nose']
#cv2.rectangle(img,(left_eye[0]-2,left_eye[1]-2),(left_eye[0]+2,left_eye[1]+2),(0,255,0),3)
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
print(result)
print(datetime.now() - t)