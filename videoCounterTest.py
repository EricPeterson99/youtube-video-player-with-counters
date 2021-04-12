import sys
# sys.path.append(
#     '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages')

# import libraries
import csv
from vidgear.gears import CamGear
import cv2

print("Line Coutner \nKey A - TSA Pre (Z for luggage)\nKey S - CLEAR (X for luggage)\nKey D - Regular (C for luggage)")
print("q - to quit | SPACE to pause")

PLAYBACK_SPEED = int(input("Enter desired playback speed as an int: "))
FPS = 30
INTERVAL_TIME_MINS = 5
line_counts = [0] * 6

# Create Video Steam
# Test link: https://www.youtube.com/watch?v=AnuGSFvKO80
options = {"STREAM_RESOLUTION": "144p", "STREAM_PARAMS": {"no_color": True}}
stream = CamGear(source=sys.argv[1], stream_mode = True, logging=True, **options).start() # YouTube Video URL as input

def read_input(key):
    if key == ord("a"):
        line_counts[0] += 1
    elif key == ord("s"):
        line_counts[1] += 1
    elif key == ord("d"):
        line_counts[2] += 1
    elif key == ord("z"):
        line_counts[3] += 1
    elif key == ord("x"):
        line_counts[4] += 1
    elif key == ord("c"):
        line_counts[5] += 1
    elif key == ord(" "):
        print("Paused, press enter to play")
        input()

def log_data(interval):
    print("Time: ",interval, "| Lanes", line_counts)
    with open(sys.argv[1][32:] + '.csv', mode='a') as line_file:
        line_writer = csv.writer(line_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        line_writer.writerow([interval, line_counts[0], line_counts[3], line_counts[1], line_counts[4], line_counts[2], line_counts[5]])

def main():
    cur_interval_frame_count = 0
    interval = 1

    while True:

        # skip frames to increase playback speed
        for _ in range(0,PLAYBACK_SPEED - 1):
            if stream.read() is None: break
            cur_interval_frame_count+= 1

        frame = stream.read()
        # read frames

        # check if frame is None aka end of video
        if frame is None: break


        cv2.imshow("Output Frame", frame)
        cv2.resizeWindow('Output Frame', (1920, 1080))

        key = cv2.waitKey(1) & 0xFF
        # check for 'q' key-press
        if key == ord("q"): break
        read_input(key)

        if cur_interval_frame_count / (INTERVAL_TIME_MINS * 60 * FPS) > 1:
            log_data(interval)
            interval += 1
            cur_interval_frame_count = 0

        cur_interval_frame_count+= 1


    cv2.destroyAllWindows()
    stream.stop()

    log_data(interval)



# ----------------------------------------------------------------------------

main()
