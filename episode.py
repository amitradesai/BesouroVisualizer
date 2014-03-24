import math
class Episode(object):
	"""docstring for Episode"""
	duration = 0
	def __init__(self, timestamp, type):
		super(Episode, self).__init__()
		self.timestamp = timestamp
		self.type = type

	def calculate_duration(self, other_episode):
		self.duration = math.fabs(self.timestamp - other_episode.timestamp) / 60
		 