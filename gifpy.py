import cv2
import numpy as np
import imageio
import pyautogui
import datetime

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
        converted_choice = int(input_choice)
        
        # Record screen
        if converted_choice == 1:
            output = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*"XVID"), 10.0, (640, 480))
            if not output.isOpened():
                print("Cannot start screen recording; Try again")
                continue

        # Record webcam
        elif converted_choice == 2:
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                print("Cannot open camera; Try again")
                continue

        # From video file
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
print("Press 'a' to add a single frame( or hold to add multiple frames")
print("Press any key to move to the next frame")
print("Press 'q' to stop recording")
while True:

    if converted_choice == 1:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output.write(frame)
    else:
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
if converted_choice == 1:
    output.release()
else:
    cap.release()
cv2.destroyAllWindows()