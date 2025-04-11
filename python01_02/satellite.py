#!/bin/env python3

# Determine the speed (v) of a satellite 
#         at a distance d from the Earth.
# Read in first the distance of the satellite from STDIN 
# Then calculate and print the satellite speed (v).

# Use the following constants:
# Gravity value G = 6.67*10-11Nm2/kg2
# Earth mass    M = 5.9722 x 10^24 kilograms
# Earth radius  R = 6,371 km

# Sample I/O:

#     Satellite distance(KM) = <value of d>
#     Satellite speed v = <speed value>
import math as m

G = 6.67*pow(10,-11)  # Nm2/kg2
M = 5.9722*pow(10,24)  # kg
R = 6371*pow(10,3)  # m

d = float(input("Satellite distance(KM) = "))
d = d * 1000  # Convert to meters

v = m.sqrt(G * M / (R + d))
print(f'Satellite speed v = {v:.2f} m/s')