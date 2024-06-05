<h1>Application for recognizing vertical road signs</h1>

This application uses [Yolov8](https://github.com/ultralytics/ultralytics) AI model pretrained to allows for detectection of <b>selected polish road signs</b> via webcam or from video file. 

used modules are:
- ultralytics 
- OpenCv2
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
