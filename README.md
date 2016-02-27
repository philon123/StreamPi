StreamPi

Make a raspberry push an ipcam or webcam stream to a remote server, for example wowza.
Streaming starts automatically after reboot.

Find the stream url of your camera at http://www.ispyconnect.com/sources.aspx

Start/Stop stream with
	service stream start/stop

Install:
	1: Install fresh raspian
	2: apt-get update
	3: apt-get install libav-tools upstart
	4: Copy stream.py and stream.conf to /opt
	5: Copy initconf to /etc/init/stream.conf
	6: restart raspberry
