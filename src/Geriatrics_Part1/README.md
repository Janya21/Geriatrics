# Geriatrics_Part1
This repository contains the the code for fall detection.

# Instructions

### Command to clone this repository: </br> 
git clone https://github.com/Janya21/Geriatrics.git </br>
 
### To extract the video into frames: </br> 
Create an Images folder with test and train as subfolders. Inside each one of them, create not_safe and safe as subfolders. Also, create a file named datafile.csv in the Images folder. </br>
Then, move to the Images directory and run the following line in the terminal - </br>
python extract_files.py mp4
</br>
### To train your model: </br> 
Then move to the Geriatrics_Part2 directory and run the following line in the terminal - </br>
python train.py 50 2 480 640 </br>

### To test the model: </br> 
python rt_classification.py 50 2 480 640 'model_021_0.289_0.384.hdf5' 'Video/test/Fall/cam181.mp4' </br>
python rt_classification.py 50 2 480 640 'model_021_0.289_0.384.hdf5' 'Video/test/Regular_Activity/cam184mp4' </br>

The output video with the classification (safe/not safe) printed on each frame would be stored in the same directory with the name 'result.avi'.




