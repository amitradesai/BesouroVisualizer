from episode import Episode
import re
import csv
import sys
def import_from_log(episode_file):
	return [parse_line_episode(line.strip()) for line in open(episode_file)]

def parse_line_episode(line):
	line_array = re.split('\s+', line)
	timestamp = int(line_array[0]) // 1000
	type = line_array[1]
	return  Episode(timestamp, type)

def calculate_durations(episodes):
	for index, elem in enumerate(episodes):
  		if(index +1 < len(episodes)):
			elem.calculate_duration(episodes[index+1])
	return episodes

def write_to_csv(output_file, episodes):
	with open(output_file, "wb") as file:
		for episode in episodes:
			output_file.write("{0}; {1} \n".format(episode.type, episode.duration))

def main(argv):
	output_file = argv.split("\\")[4] + ".csv"
	episodes = calculate_durations(import_from_log(argv + '\\zorroEpisodes.txt'))
	write_to_csv(output_file, episodes)
	print "File written in " + output_file
if  __name__ =='__main__':main(sys.argv[1])
