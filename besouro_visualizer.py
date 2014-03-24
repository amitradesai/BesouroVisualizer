from episode import Episode
import re
def import_from_log(file):
	return [parse_line_episode(line.strip()) for line in open(file)]
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
def main():
	episodes = calculate_durations(import_from_log("zorroEpisodes.txt"))
	print [(episode.duration, episode.type) for episode in episodes]


if  __name__ =='__main__':main()



 
