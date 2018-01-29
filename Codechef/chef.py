#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 18:40:17 2018

@author: root
"""
"""
Nikhil’s slogan has won the contest conducted by Drongo Airlines and he is entitled to a free ticket between any two destinations served by 
the airline. All cities served by Drongo Airlines can be reached from each other by some sequence of connecting flights. Nikhil is allowed 
to take as many connecting flights as needed, but he must take the cheapest route between his chosen destinations.

Each direct flight between two cities has a fixed price. All pairs of cities connected by direct flights have flights in both directions and 
the price is the same in either direction. The price for a sequence of connecting flights is the sum of the prices of the direct flights along 
the route.

Nikhil has information about the cost of each direct flight. He would like to maximize the value of his prize, so he would like to choose a 
pair of cities on the network for which the cost of the cheapest route is as high as possible.

For instance, suppose the network consists of four cities {1, 2, 3, 4}, connected as shown on the right.

In this case, Nikhil should choose to travel between 1 and 4, where the cheapest route has cost 19. You can check that for all other pairs of 
cities, the cheapest route has a smaller cost. For instance, notice that though the direct flight from 1 to 3 costs 24, there is a cheaper 
route of cost 12 from 1 to 2 to 3.
"""


"""
input format

    Line 1 : Two space-separated integers, C and F . C is the number of cities on the network, numbered 1, 2, . . . , C. 
    F is the number of pairs of cities connected by a direct flight.
    Lines 2 to F + 1 : Each line describes one direct flight between a pair of cities and consists of three integers, x, y and p, 
    where x and y are the two cities connected by this flight and p is the price of this
"""
import sys


def take_input():
    line1 = ip1()
    C, F = int(line1[0]), int(line1[1])
    print(C, F)
    line2 = ip2(C, F)
    print(line2)
    
def ip1():
    string = input("Enter C and F: ")
    split = string.split(' ')
    try:
        if len(split) == 2 and isinstance(int(split[0]), int) and isinstance(int(split[1]), int):
            return split
    except:
        sys.exit("ERROR")
        
def split_res():
    string = input("Enter X, Y and P (eg : x y z): ")
    split = string.split(' ')
    print(split)
    
def ip2(C, F):
    res = []
    for i in range (0, F-1):

        try:
            if len(split) == 3 and isinstance(int(split[0]), int) and isinstance(int(split[1]), int) and isinstance(int(split[2]), int):
                check = check_validity(split)
                if check:
                    res.append(split)
                else:
                    
        except:
            sys.exit("ERROR")
    return res

def check_validity(res):
    unqs = list(set(result).union(res))
    for unq in set(unqs):
        if unqs.count(unq) > 2:
            return False
        
result = []
if __name__ == "__main__":
    take_input()