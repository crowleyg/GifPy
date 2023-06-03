import cv2
import numpy as np
import imageio
import pyautogui
import datetime
import os

def screen_record():
    file_name = "output.avi"
    fps = 10.0
    out = cv2.VideoWriter(file_name, cv2.VideoWriter_fourcc(*"XVID"), fps, (1920, 1080))
    cv2.namedWindow("GifPy Screen Capture", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("GifPy Screen Capture", 480, 270)
    print("Screen Recording Started; Press 'q' to stop recording")
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        cv2.imshow("GifPy Screen Capture", frame)
        if cv2.waitKey(1) == ord("q"):
            break
    cv2.destroyAllWindows()
    out.release()

# Display menu
print("**********GifPy - Gif Creator**********")
print("How would you like to create your GIF?")
print("1. Record your screen")
print("2. Record your webcam")
print("3. From a video file")

# Get user choice.
while True:
    input_choice = input("Enter your choice(1/2/3): ")
    if input_choice != "1" and input_choice != "2" and input_choice != "3":
        print("Invalid choice!")
    else:
        converted_choice = int(input_choice)
        
        # Screen
        if converted_choice == 1:
            screen_record()
            cap = cv2.VideoCapture("output.avi")

        # Webcam
        elif converted_choice == 2:
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                print("Cannot open camera; Try again")
                continue

        # Video file
        elif converted_choice == 3:
            input_file = input("Enter the file name: ")
            cap = cv2.VideoCapture(input_file)
            if not cap.isOpened():
                print("Cannot open file; Check the file name and try again")
                continue
        break

# Output file name
time_stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
file_name = f"Saved_Gifs/{time_stamp}.gif"

# Record frames
frames = []
image_count = 0
cv2.namedWindow("GifPy", cv2.WINDOW_NORMAL)
cv2.resizeWindow("GifPy", 1280, 720)
print("Press 'a' to add a single frame(or hold to add multiple frames)")
print("Press any key to move to the next frame")
print("Press 'q' to stop recording")
while True:

    ret, frame = cap.read()
    if not ret:
        print("No more frames available; Exiting...")
        break

    cv2.imshow("GifPy", frame)
    key = cv2.waitKey(0)
    if key == ord("a"):
        image_count += 1
        frames.append(frame)
        print("Adding new frame: ", image_count)
    elif key == ord("q"):
        break
print("Total frames: ", image_count)

# Save GIF
if image_count == 0:
    print("No frames added; GIF not saved")
    exit()

print("Saving GIF...")
with imageio.get_writer(f"{file_name}", mode="I") as writer:
    for frame in frames:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        writer.append_data(rgb_frame)
print(f"GIF '{time_stamp}.gif' Saved!")

# Release the capture
cap.release()
cv2.destroyAllWindows()

# Remove the output.avi file
if os.path.exists("output.avi"):
    os.remove("output.avi")

# TODO: Add option to add text to the GIF
# TODO: file compression (100mb = GIPHY limit)
# TODO: remove the output.avi file after saving the GIF