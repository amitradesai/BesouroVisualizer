from episode import Episode
def main():
	ep1  = Episode(123, "TDD")
	ep2  = Episode(122, "TDD")
	ep1_duration = ep1.duration(ep2)
	print ep1_duration