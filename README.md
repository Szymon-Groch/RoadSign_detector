<h1>Application for recognizing vertical road signs</h1>

This applicationserves as my [engineering thesis project](https://drive.google.com/file/d/12cyChpgL3MY6eKqPUHhkvFxemR-PhZbd/view?usp=drive_link)

It utilizes [Yolov8](https://github.com/ultralytics/ultralytics) AI model pretrained for detection of <b>selected polish road signs</b> via webcam or from selected video file. 

![image](https://github.com/Szymon-Groch/RoadSign_detector/assets/171821030/901d447f-ee45-41bf-b063-c531e9ccb13b)



used modules are:
- ultralytics 
- OpenCV
- math


Detected sings are:
- "Agatka" T-27
- highway D-9
- speed limit  B-33
- parking D-18
- priority road D-1
-  go straight C-5
-  pedestrian crossing D-6
-  stop B-20
-  give way A-7

<h2>How to use</h2>
To use either select open main.py, then follow the instructions in the console
or choose:
- camera.py to detect signs from <b>default</b> webcam.
- wideo.py to detect signs from video file. In console write a path to the wideo you want detect sings from (preferably in .mp4).





click <b>Q</b> to end detection.
