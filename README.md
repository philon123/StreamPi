#StreamPi

Make a linux mashine push a network camera or webcam stream to a remote server, for example Wowza Streaming Engine.
Streaming starts automatically after boot.

Requires python3

Find the stream url of your camera at http://www.ispyconnect.com/sources.aspx. For example, for the Tp-Link 942L, the url will be rtsp://USER:PASSWORD@IP/play1.sdp

Start/Stop stream with 'service stream start/stop'. Check for errors by running 'journalctl -fu streampi'

##Install
* Install fresh Ubuntu/Raspian
* `apt-get update && apt-get upgrade`
* (Ubuntu) `apt-get install git python3 ffmpeg`
* (Rasberry) `apt-get install git python3 libav-tools`
* `cd /opt && git clone https://github.com/philon123/StreamPi`
* `cp /opt/StreamPi/streampi.service /etc/systemd/system/streampi.service`
* `systemctl enable streampi`
* modify config.json and add correct settings
* restart raspberry

##Config

```
{
	//change this to avconv if you are using a raspberry
	"encoder": "ffmpeg",

	//this is where the rtmp stream will be pushed to
	"destination-url": "rtmp://SERVER URL",

	//change this to 'networkcam' if you are using a network camera
	"cam-type": "webcam",

	//only used if "cam-type" is "webcam". this is the video device of the webcam. video0 is probably correct.
	"webcam-dev": "video0",

	//only used if "cam-type" is "webcam". choose framerate of stream
	"webcam-framerate": "10",

	//only used if "cam-type" is "webcam". choose resolution of stream
	"webcam-resolution": "640x480",

	//only used if "cam-type" is "networkcam". this is the stream url of your network camera
	"networkcam-url": "rtsp://CAM STREAM URL",
}
```

##Changelog

###v1.0.0
* Updated to python3
* Added option for ffmpeg
* Improved Readme

###v0.9.0
Initial Commit




##Sample Config for an Axis P1357 network camera with the service running on an ubuntu server
```
{
	"encoder": "ffmpeg",
	"destination-url": "rtmp://mywowzaserver.test/live/axisP1357",
	"cam-type": "networkcam",
	"networkcam-url": "rtsp://root:root@192.168.1.38/axis-media/media.amp?videocodec=h264&streamprofile=Balanced"
}
```

##Sample Config for a Logitech webcam connected to a raspberry
```
{
	"destination-url": "rtmp://mywowzaserver.test/live/kitchenCam",
	"cam-type": "webcam",
	"webcam-dev": "video0",
	"webcam-framerate": "10",
	"webcam-resolution": "640x480"
}
```
