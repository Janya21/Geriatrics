import os
import sys
import cv2
import numpy as np
from data import DataSet
from extractor import Extractor
from keras.models import load_model
from imutils.video import VideoStream

if (len(sys.argv) == 6):
    seq_length = int(sys.argv[1])
    class_limit = int(sys.argv[2])
    height = int(sys.argv[3])
    width = int(sys.argv[4])
    saved_model = sys.argv[5]
else:
    seq_length = 99
    class_limit = 2
    height = 180
    width = 480
    saved_model = 'model_021_0.002.hdf5'
    video_file = 'video1.mp4'

print('\n')
print('\n')
video_file = input('Enter the Path of the Video for Prediction: ')

capture = cv2.VideoCapture(os.path.join(video_file))
# capture = VideoStream().start()

video_writer = cv2.VideoWriter('result.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (width,height))

# Get the dataset.
data = DataSet(seq_length=seq_length, class_limit=class_limit, image_shape=(height, width, 3))

# get the model.
extract_model = Extractor(image_shape=(height, width, 3))
saved_LSTM_model = load_model(saved_model)

sequence = []
frame_count = 1
while True:
    ret, frame = capture.read()
    # Bail out when the video file ends
    if not ret:
        break
    # frame = capture.read()

    # Save each frame of the video to a list
    frame = cv2.resize(frame, (width, height))

    features = extract_model.extract_image(frame)
    sequence.append(features)

    if frame_count <= seq_length:
        frame_count += 1
        video_writer.write(frame)
        continue
    else:
        sequence.pop(0)

    # Clasify sequence
    prediction = saved_LSTM_model.predict(np.expand_dims(sequence, axis=0))
    print(prediction)
    values = data.print_class_from_prediction(np.squeeze(prediction, axis=0))

    # Add prediction to frames and write them to new video
    for i in range(len(values)):
        cv2.putText(frame, values[i], (40, 40 * i + 40), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), lineType=cv2.LINE_AA)
    # print("\n\nwriting")
    video_writer.write(frame)
    # cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break


video_writer.release()

