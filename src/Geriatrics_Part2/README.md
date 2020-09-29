# Geriatrics_Part2
This repository contains the the code for detecting if an elderly patient got out of his/her bed.

# Instructions

### Command to clone this repository: </br> 
git clone https://github.com/Janya21/Geriatrics_Part2.git </br>
 
### To extract the video into frames: </br> 
Create an Images folder with test and train as subfolders. Inside each one of them, create not_safe and safe as subfolders. </br>
Then, run this line: </br>
python extract_files.py mp4
</br>
### To train your model: </br> 
python train.py 50 2 480 640 </br>

### To test the model: </br> 
python rt_classification.py 50 2 480 640 'model_004_0.169_0.158.hdf5' 'Video/test/not_safe/video3.mp4' </br>
python rt_classification.py 50 2 480 640 'model_004_0.169_0.158.hdf5' 'Video/test/safe/video21.mp4'


