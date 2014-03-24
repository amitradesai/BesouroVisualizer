from episode import Episode
import re
def import_from_log(file):
	
def parse_line_episode(line):
	line_array = re.split('\s+', line)
	timestamp = int(line_array[0]) // 1000
	type = line_array[1]
	ep = Episode(timestamp, type)
def main():
	ep1  = Episode(123, "TDD")
	ep2  = Episode(122, "TDD")
	ep1.calculate_duration(ep2)
	print ep1.duration

if  __name__ =='__main__':main()