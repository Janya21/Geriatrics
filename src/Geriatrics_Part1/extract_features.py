"""
This script generates extracted features for each video, which other
models make use of.

You can change you sequence length and limit to a set number of classes
below.

class_limit is an integer that denotes the first N classes you want to
extract features from.
Then set the same number when training models.
"""
import numpy as np
import os.path
from data import DataSet
from extractor import Extractor
from tqdm import tqdm

def extract_features(seq_length=40, class_limit=2, image_shape=(300, 300, 3)):
    # Get the dataset.
    data = DataSet(seq_length=seq_length, class_limit=class_limit, image_shape=image_shape)

    # get the model.
    model = Extractor(image_shape=image_shape)

    # Loop through data.
    pbar = tqdm(total=len(data.data))
    for video in data.data:
        if int(video[3])<seq_length:
            continue

        video_feature_path = os.path.join('Images', 'sequences', video[2] + '-' + str(seq_length) + '-features-' + str(int(video[3])-seq_length)) 
        if os.path.isfile(video_feature_path + '.npy'):
          pbar.update(1)
          continue
          
        # Get the frames for this video.
        frames = data.get_frames_for_sample(video)
        sequence = []
        for image in frames:
            features = model.extract(image)
            sequence.append(features)

        for video_number in range(int(video[3])-seq_length+1):
            # Get the path to the sequence for this video.
            path = os.path.join('Images', 'sequences', video[2] + '-' + str(seq_length) + '-features-' + str(video_number))  # numpy will auto-append .npy

            # Check if we already have it.
            if os.path.isfile(path + '.npy'):
                pbar.update(1)
                continue
            
            current_sequence = sequence[video_number: video_number+seq_length]
            # Save the sequence.
            np.save(path, current_sequence)
            pbar.update(1)

    pbar.close()
