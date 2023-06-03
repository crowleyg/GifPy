# GifPy - GIF Creator

GifPy is a Python script that allows you to create GIFs from screen recording, webcam, or video files. It utilizes the OpenCV library for capturing and processing frames, as well as other supporting libraries.

## Requirements

Before running the program, ensure that you have the following dependencies installed:

- Python 3.6 or above
- OpenCV (`cv2`)
- NumPy (`numpy`)
- imageio (`imageio`)
- pyautogui (`pyautogui`)

To install the dependencies, run the following command:

`pip install -r requirements.txt`

Make sure you have pip installed and the requirements.txt file is in the same directory as the script.

## Usage

1. Clone the repository or download the script file.

2. Install the required dependencies using the command mentioned in the "Requirements" section above.

3. Run the script using the following command:

`python gifpy.py`

4. The program will display a menu with options for creating a GIF:
   - Enter `1` to record your screen.
   - Enter `2` to record from your webcam.
   - Enter `3` to create a GIF from a video file.

5. Depending on your choice, the program will start recording frames. Follow the on-screen instructions to add frames, move to the next frame, or stop recording.

6. Once you have recorded the desired frames, the program will save the GIF in the "Saved_Gifs" directory with a unique timestamp as the file name.

7. After saving the GIF, the program will release the capture (if applicable), close any open windows, and remove the temporary video file (if created during screen recording).

8. The saved GIF can be found in the "Saved_Gifs" directory with the filename format: `YYYY-MM-DD-HH-MM-SS.gif`.

## License

This project is licensed under the [MIT License](LICENSE).
