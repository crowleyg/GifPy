import cv2
import numpy as np
import imageio

print("**********GIF Creator**********")
print("How would you like to create your GIF?")
print("1. Record your screen")
print("2. Record your webcam")
print("3. From a video file")
while True:
    input_choice = input("Enter your choice(1/2/3): ")
    if input_choice != "1" and input_choice != "2" and input_choice != "3":
        print("Invalid choice!")
    else:
        break
    
cap = cv2.VideoCapture(0)