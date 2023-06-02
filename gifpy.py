import cv2
import numpy as np
import imageio
import pyautogui

# Display menu
print("**********GifPy - Gif Creator**********")
print("How would you like to create your GIF?")
print("1. Record your screen")
print("2. Record your webcam")
print("3. From a video file")

# Get user choice
while True:
    input_choice = input("Enter your choice(1/2/3): ")
    if input_choice != "1" and input_choice != "2" and input_choice != "3":
        print("Invalid choice!")
    else:
        break
converted_choice = int(input_choice)

# Record screen
if converted_choice == 1:
    output = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*"XVID"), 10.0, (640, 480))
    # frames = []
    # image_count = 0
    # while True:
    #     img = pyautogui.screenshot()
    #     frame = np.array(img)
    #     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #     output.write(frame)
    #     cv2.imshow("GifPy", frame)
    #     key = cv2.waitKey(0)
    #     if key == ord("a"):
    #         image_count += 1
    #         frames.append(frame)
    #         print("Adding new frame: ", image_count)
    #     elif key == ord("q"):
    #         break
    # print("Total frames: ", image_count)

    # print("Saving GIF...")
    # with imageio.get_writer("output.gif", mode="I") as writer:
    #     for frame in frames:
    #         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #         writer.append_data(rgb_frame)
    # print("GIF Saved!")
    # exit()

# Record webcam
elif converted_choice == 2:
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

# From video file
elif converted_choice == 3:
    input_file = input("Enter the file name: ")
    cap = cv2.VideoCapture(input_file)


# Record frames
frames = []
image_count = 0
while True:

    if converted_choice == 1:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output.write(frame)
    else:
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        ret, frame = cap.read()


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
print("Saving GIF...")
with imageio.get_writer("output.gif", mode="I") as writer:
    for frame in frames:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        writer.append_data(rgb_frame)
print("GIF Saved!")

# Release the capture
if converted_choice == 1:
    output.release()
else:
    cap.release()
cv2.destroyAllWindows()