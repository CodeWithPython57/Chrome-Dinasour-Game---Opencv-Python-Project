import playing_dinasour
import cv2  
import math 
import numpy as np 
import pyautogui

# Capture frames from the camera
capture = cv2.VideoCapture(0)
ret, frame = capture.read()

while capture.isOpened():
	playing_dinasour.draw_rectangle()
	playing_dinasour.apply_blur_effect()
	playing_dinasour.apply_morphological_transformations()
	playing_dinasour.apply_blur_threshold()
	playing_dinasour.apply_contour()
	playing_dinasour.show_images()
	if cv2.waitKey(1)==ord('q'):
		break


capture.release()

cv2.destroyAllWindows()