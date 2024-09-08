<h1>Application for recognizing vertical road signs</h1>

This application serves as my engineering thesis.

It utilizes [Yolov8](https://github.com/ultralytics/ultralytics) AI model pretrained for detection of <b>selected polish road signs</b> via webcam or from selected video file. 

![image](https://github.com/Szymon-Groch/RoadSign_detector/assets/171821030/901d447f-ee45-41bf-b063-c531e9ccb13b)

Program was written in python language

<h3>Used modules are:</h3>
<ul>
<li> <b>ultralytics:</b> - used for YOLOv8 model inference
<li> <b>OpenCV:</b> - video vapture, drawing bounding boxes and postprocessing for roadsign detection
<li> <b>math:</b> for roadsign detection confidence calculation
</ul>

<h3>Detected sings are:</h3>
<ul>
<li> "Agatka" T-27
<li> highway D-9
<li> speed limit  B-33
<li> parking D-18
<li> priority road D-1
<li>  go straight C-5
<li>  pedestrian crossing D-6
<li>  stop B-20
<li>  give way A-7
</ul>

<h2>How to use</h2>
Run "main.py" via terminal, then follow the instructions in the console
or run:
- camera.py to detect signs from <b>default</b> webcam.
- wideo.py to detect signs from video file. In console write a path to the wideo you want detect sings from (preferably in .mp4).

click <b>Q</b> to end detection.

<h3>Important notes</h3>
<ul>
<li> <b> For webcam detection make sure you have one connected </b>
<li> <b>Make sure pretrained YOLOv8 AI model named "znaki.pt" is in the same directory as .py scripts </b>. Alternatively modify the argument in the 'model' variable to match the file's current directory.
<li> For example video extract .zip file in "wideo" folder
</ul>
