# Face-Detector

Face Detection is a tool capable of detecting faces of people in both webcam and video. It was built in Python using mainly OpenCV.

#How it works?

The program takes each frame of the video or webcam and passes to the detector, a Haar cascade
classifier serialized as an XML file, after which a rectangle is drawn around the faces
detected. Optionally, the detection display can be recorded.

##Preview

![](gifs/preview.gif)

#Installation

*  `git clone https://github.com/wesleymonte/Face-Detector.git`

*  `cd Face-Detector`

*  `pip install -r requirements.txt`

#How to Run?

There are 4 optional arguments:
--face: Path to where the face cascade resides, defined by the standard that comes with the project
--video: In the case where you want to analyze a video, the path to your file is passed through this argument
--record: If you want to record the detection pass the filename of the video file with the extension mp4 by this argument
--resolution: Argument to set both the webcam resolution and the resolution of the recording. Receives "480p", "720p", "1080p" or "4k. (with recording errors)

##Examples

Using webcam only
*  `python main.py`

Using the webcam and recording it
*  `python main.py -r record.mp4`

Using a video
*  `python main.py -v faces.mp4`

Using a video and recording in 720p
*  `python main.py -v faces.mp4 -r record.mp4 -re 720p`
