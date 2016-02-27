import sys
import subprocess
import json

class Streamer(object):
	def __init__(self):
		self.config = self.getConfig()
		self.start()

	def getConfig(self):
		if len(sys.argv) == 1:
			print 'must specify a config as parameter, aborting...'
			exit()

		configUrl = sys.argv[1]
		try:
			with open(configUrl) as confFile:
				try:
					return json.loads(confFile.read())
				except ValueError:
					print 'config is not json, aborting...'
					exit()
		except IOError:
			print 'ethminer.conf not found, aborting...'
			exit()

	def start(self):
		destinationUrl = self.config['destination-url']
		isWebcam = self.config['use-webcam']

		cmd = ''
		if isWebcam:
			webcamDev = self.config['webcam-dev']
			webcamFramerate = self.config['webcam-framerate']
			webcamResolution = self.config['webcam-resolution']
			cmd = 'avconv -f video4linux2 -r {webcamFramerate} -s {webcamResolution} -i /dev/{webcamDev} -f flv {destinationUrl}'.format(
				webcamFramerate = webcamFramerate,
				webcamResolution = webcamResolution,
				webcamDev = webcamDev,
				destinationUrl = destinationUrl
			)
		else:
			streamUrl = self.config['stream-url']
			cmd = 'avconv -i "{streamUrl}" -c:v copy -c:a copy -f flv {destinationUrl}'.format(
				streamUrl = streamUrl,
				destinationUrl = destinationUrl
			)
		print cmd, '\n'
		subprocess.Popen(cmd, shell=True).communicate()
		exit()

Streamer()