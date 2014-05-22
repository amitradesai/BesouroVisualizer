from episode import Episode
import re
import csv
import sys
import os.path
DIVIDER_FOR_STANDARD_TIMESTAMP_FORMAT = 1000
def import_from_log(episode_file):
	return [parse_line_episode(line.strip()) for line in open(episode_file)]

def parse_line_episode(line):
	line_array = re.split('\s+', line)
	timestamp = sanitize_timestamp(line_array[0])
	type = line_array[1]
	return  Episode(timestamp, type)

def calculate_durations(episodes):
	for index, elem in enumerate(episodes):
  		if(index > 0 < len(episodes)):
			elem.calculate_duration(episodes[index-1])
	return episodes

def write_to_csv(user_id, output_file, episodes):
	with open(output_file, "a") as f:
		for episode in episodes:
			f.write("{0}; {1}; {2}\n".format(user_id, episode.type, episode.duration))

def sanitize_timestamp(timestamp):
	return int(timestamp) // DIVIDER_FOR_STANDARD_TIMESTAMP_FORMAT

def generate_first_episode(actions_file):
	with open(actions_file) as f:
		start_time_stamp =  f.readline().split()[1]
		return Episode(sanitize_timestamp(start_time_stamp), "dummy")

def main(argv):

	
	separator = os.sep
	user_id = re.search('FS\w+\d+', argv).group()
	zorroEpisodes_file = argv + separator + 'zorroEpisodes.txt'
	actions_file = argv + separator + 'actions.txt'
	output_file = "episodes.csv"
	episodes_without_duration = import_from_log(zorroEpisodes_file)
	first_episode = generate_first_episode(actions_file) #take the starting time of the first episode from the actions file
	episodes_without_duration.insert(0,first_episode) #insert this dummy episode at the beginning of the list
	episodes_with_duration = calculate_durations(episodes_without_duration)
	write_to_csv(user_id, output_file, episodes_with_duration[1:]) #write the list to file excluding the dummy
	print "File written in " + output_file
if  __name__ =='__main__':
		if  len(sys.argv)==1 or sys.argv[1]=="-h":
			print("Usage: python besouro_visualizer path/to/zorroEpisodes.txt")
			sys.exit()
		else: 
			main(sys.argv[1])
