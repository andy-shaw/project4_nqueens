'''
Andy Shaw

This script will analyze runtimes for the genetic algorithm and attempt to find
the best population sizes for difference sizes.
'''

import time
import geneticAlgorithmAgent as agent
from solution import solution

verbose = False
filename = 'outputs.txt'

def main():
	boardSize = 6
	mutationRate = 0.008
	populationSize = 50
	times = []
	avgTimes = []
	runsPerPopSize = 50

	f = open(filename, 'w')
	f.write('This is the output for populationSizeFinder.py\n')
	f.write('Each timing is averaged over ' + str(runsPerPopSize) + ' runs per population size\n\n')

	for bsize in range(6,12):
		boardSize = bsize
		if verbose: print 'running test boardSize:', boardSize
		first = True

		for size in range(50, 501, 50):
			populationSize = size
			for i in range(runsPerPopSize): 
				times.append(timeAgent(boardSize, mutationRate, populationSize))
			avgTimes.append(sum(times)/len(times))
			times = []

			if verbose and first: print 'completed pop:', ; first = False
			if verbose: print populationSize, '\t',

		if verbose: print '\nwriting times for boardSize', boardSize, 'to file\n'
		#write raw times to file
		f.write('boardSize: ' + str(boardSize).ljust(3))
		f.write('\n-----------------------------------')
		for x in range(0, len(avgTimes)):
			f.write('\npopulationSize: ' + str((x+1)*50).ljust(5))
			f.write('\tavg: ' + str(avgTimes[x]))

		#write analysis to file
		f.write('\n===================================\n')
		f.write('Best populationSize: ' + str((avgTimes.index(min(avgTimes))+1) * 50) + '\n\n')
		avgTimes = []


	f.close()

def timeAgent(boardSize, mutationRate, populationSize):
	start = time.time()
	#run the agent until the correct answer is found
	while 1:

		answer = agent.geneticAlgorithmAgent(boardSize, mutationRate, populationSize, True)

		if solution(answer) == 0:
			finish = time.time()
			return finish - start

def parseOutputFile(filename):
	import re
	output = open('outputs.txt', 'r')
	parsed = open(filename, 'w')

	#read in lines
	lines = output.readlines()
	output.close()

	#for every line, if it contains a time, pull it out, and add it to parsed file
	for line in lines:
		#if the line is a boardsize, then it will be it's own line in the parsed
		if line[:5] == 'board':
			m = re.search('\d+', line)
			parsed.write(m.group(0) + '\n')
		if line[:5] == 'popul':
			m = re.findall('populationSize: (\d+)\s+avg: (\d+\.\d+)', line)
			s = '\t'.join(m[0])
			parsed.write(s + '\n')

	parsed.close()
	print 'Parsing of output.txt is complete'
	exit()

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser(description='Analysis of population sizes')
	parser.add_argument('-v', '--verbose', action='store_true')
	parser.add_argument('-o', '--output-file', action='store', dest='output-file', help='Parse output.txt to a new csv format .txt file')
	args = vars(parser.parse_args())

	if args['verbose']: verbose = True

	if args['output-file']: parseOutputFile(args['output-file'])


	main()