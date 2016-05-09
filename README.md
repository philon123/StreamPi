#StreamPi

Make a raspberry push an ipcam or webcam stream to a remote server, for example Wowza.
Streaming starts automatically after boot.

Find the stream url of your camera at http://www.ispyconnect.com/sources.aspx. For example, for the Tp-Link 942L, the url will be rtsp://USER:PASSWORD@IP/play1.sdp

Start/Stop stream with 'service stream start/stop'. Check for errors by running 'journalctl -fu streampi'

#Install:
* Install fresh Raspian
* apt-get update
* apt-get install libav-tools
* Copy streampi.py and config.json to /opt/streampi
* Copy streampi.service to /etc/systemd/system/streampi.service
* systemctl daemon-reload
* restart raspberry
