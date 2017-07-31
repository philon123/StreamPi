import sys
import subprocess
import json

class Streamer():
	def __init__(self):
		self.config = self.getConfig()
		self.start()

	def getConfig(self):
		if len(sys.argv) == 1:
			print('must specify a config as parameter, aborting...')
			exit()

		configUrl = sys.argv[1]
		try:
			with open(configUrl) as confFile:
				try:
					return json.loads(confFile.read())
				except ValueError:
					print('config is not json, aborting...')
					exit()
		except IOError:
			print('ethminer.conf not found, aborting...')
			exit()

	def start(self):
		cmd = ''
		if self.config['cam-type'] == 'webcam':
			webcamDev = self.config['webcam-dev']
			webcamFramerate = self.config['webcam-framerate']
			webcamResolution = self.config['webcam-resolution']
			cmd = '{encoder} -f video4linux2 -r {webcamFramerate} -s {webcamResolution} -i /dev/{webcamDev} -f flv {destinationUrl}'.format(
				encoder = self.config['encoder'],
				webcamFramerate = webcamFramerate,
				webcamResolution = webcamResolution,
				webcamDev = webcamDev,
				destinationUrl = self.config['destination-url']
			)
		elif self.config['cam-type'] == 'networkcam':
			streamUrl = self.config['networkcam-url']
			cmd = '{encoder} -i "{streamUrl}" -c:v copy -c:a copy -f flv {destinationUrl}'.format(
				encoder = self.config['encoder'],
				streamUrl = streamUrl,
				destinationUrl = self.config['destination-url']
			)
		print(cmd, '\n')
		subprocess.Popen(cmd, shell=True).communicate()
		exit()

Streamer()
