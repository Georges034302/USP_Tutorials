#!/bin/env python3
import csv 
import statistics as stat
import sys
# step 1: define a function to return a dictiory of cities
def csv_dictionary(filename):
    with open(filename, 'r',encoding='utf8') as fin:
        cities = dict(filter(None,csv.reader(fin)))
    return cities  

# step 2: define a function to match cities by population >= population
def match_population(cities, population):
    matches = {} # dictionary to hold matches
    for key in cities:
        if(len(cities[key].strip()) > 0): # check if the value is empty
            if int(cities[key]) >= population: # check if a city population is a match
                matches[key] = cities[key]
    return matches # return the dictionary of matches
    
# step 3: define a function to return mean, variance, and standard deviation
def stats(cities):
    # convert the dictionary to a list of integers
    pop_list = [int(cities[key]) for key in cities]
    # calculate mean
    mean = stat.mean(pop_list)
    # calculate variance
    variance = stat.variance(pop_list)
    # calculate standard deviation
    stddev = stat.stdev(pop_list)
    return mean, variance, stddev # return the mean, variance, and standard deviation

# step 4: main function
def main():
    filename = sys.argv[1] # get the filename from the command line
    population = int(sys.argv[2]) # get the population from the command line
    cities = csv_dictionary(filename) # get the dictionary of cities
    # print(cities)
    matches = match_population(cities, population) # get the matches
    mean, variance, stddev = stats(matches) # get the statistics
    # print the results
    print(f"Mean: {mean}")
    print(f"Variance: {variance}")
    print(f"Standard Deviation: {stddev}")

main() # call the main function