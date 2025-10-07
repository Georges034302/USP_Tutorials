#!/usr/bin/env python3
import sys
import csv
import statistics

# Load CSV into dictionary {city: population}
def load_cities(filename):
    cities = {}
    with open(filename, "r", encoding="utf-8", newline="") as f:
        for row in csv.reader(f):
            if len(row) < 2:
                continue
            city, pop = row[0].strip(), row[1].strip()
            if city and pop:
                cities[city] = pop
    return cities

# Convert to integer safely (remove commas)
def to_int_or_none(s):
    try:
        return int(s.replace(",", "").strip())
    except ValueError:
        return None

# Filter cities with population >= threshold
def match_population(cities, threshold):
    matches = {}
    for city, pop_str in cities.items():
        pop = to_int_or_none(pop_str)
        if pop is not None and pop >= threshold:
            matches[city] = pop
    return matches

# Compute mean, variance, and stdv safely
def compute_stats(values):
    if not values:
        return None, None, None
    mean = statistics.mean(values)
    if len(values) >= 2:
        var = statistics.variance(values)
        stdv = statistics.stdev(values)
    else:
        var = stdv = None
    return mean, var, stdv

# Show the results neatly
def show_results(matches):
    if not matches:
        print("No cities matched the threshold.")
        return
    print("\nMatched Cities (Top 10):")
    for city, pop in sorted(matches.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"{city}: {pop:,}")

    pops = list(matches.values())
    mean, var, stdv = compute_stats(pops)
    print("\nStatistics:")
    print(f"Mean = {mean:,.2f}" if mean else "Mean = N/A")
    print(f"Variance = {var:,.2f}" if var else "Variance = N/A (need ≥2)")
    print(f"STDV = {stdv:,.2f}" if stdv else "STDV = N/A (need ≥2)")

def main():
    if len(sys.argv) < 3:
        print("Usage: python cities_stats.py <file.csv> <population_threshold>")
        print("# Filter cities with population >= threshold (as int)")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        threshold = int(sys.argv[2])
    except ValueError:
        print("Error: population_threshold must be an integer.")
        print("# Filter cities with population >= threshold (as int)")
        sys.exit(1)

    try:
        cities = load_cities(filename)
    except FileNotFoundError:
        print(f"Error: file not found: {filename}")
        print("# Filter cities with population >= threshold (as int)")
        sys.exit(1)

    matches = match_population(cities, threshold)
    show_results(matches)

if __name__ == "__main__":
    main()
