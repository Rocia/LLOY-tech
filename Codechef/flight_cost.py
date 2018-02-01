"""
Nikhil’s slogan has won the contest conducted by Drongo Airlines and he is entitled to a free ticket between any two destinations served by 
the airline. All cities served by Drongo Airlines can be reached from each other by some sequence of connecting flights. Nikhil is allowed 
to take as many connecting flights as needed, but he must take the cheapest route between his chosen destinations.

Each direct flight between two cities has a fixed price. All pairs of cities connected by direct flights have flights in both directions and 
the price is the same in either direction. The price for a sequence of connecting flights is the sum of the prices of the direct flights along 
the route.

Nikhil has information about the cost of each direct flight. He would like to maximize the value of his prize, so he would like to choose a 
pair of cities on the network for which the cost of the cheapest route is as high as possible.

For instance, suppose the network consists of four cities {1, 2, 3, 4}.

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
    #line1 = ip1()
    line1 = [4, 4]
    C, F = line1[0], line1[1]
    val = make_pairs(C, F)
    paths, dests = val[0], val[1]
    
    #line2 = ip2(C, F)
    line2 = {'(1, 2)':3,'(1, 3)':5,'(2, 3)':7,'(3, 4)':9, '(2, 1)':3,'(3, 1)':5,'(3, 2)':7,'(4, 3)':9}
    process_paths(paths, line2)
    
    
def ip1():
    string = input("Enter C and F: ")
    split = string.split(' ')
    try:
        if len(split) == 2 and isinstance(int(split[0]), int) and isinstance(int(split[1]), int):
            return int(split[0]), int(split[1])
    except:
        sys.exit("ERROR")
        
def ip2(C, F):
    res = {}
    for i in range (0, F):
        string = input("Enter X, Y and P (eg : 3 4 5): ")
        split = string.split(' ')
        print(split)
        try:
            if len(split) == 3 and isinstance(int(split[0]), int) and isinstance(int(split[1]), int) and isinstance(int(split[2]), int):
                res[str((int(split[0]), int(split[1])))]= int(split[2])
        except:
            sys.exit("ERROR")
    return res

def make_pairs(C,F):
    psbl, psbl_dest = [], []
    for i in range(1,C+1):
        for j in range(1,C+1):
            if i != j and (j, i) not in psbl:
                psbl.append(((i,j)))
                psbl_dest.append((i,j))
            for k in range(1,C+1):
                if i != j and j != k and i != k and (i, j, k) not in psbl:
                    psbl.append(((i,j),(j,k)))
                for l in range(1,C+1):
                    if i != j != k != l and i != k and j != l and i != l and (i, j, k, l) not in psbl:
                        psbl.append(((i, j),(j, k),(k, l)))
    return psbl, psbl_dest

def process_paths(pathslist, pathdict):
    #print(pathslist, pathdict)
    cost_per_path = {}
    lst = list(pathdict.keys())
    #print(lst)
    for path in pathslist:
        if str(path) in lst and len(path) == 2 and isinstance(path[0], int):
            cost_per_path[path] = {"path":path,"cost":pathdict[str(path)]}
        elif str(path[0]) in lst and str(path[1]) in lst and len(path) == 2:
            cost_per_path[(path[0][0], path[0][1], path[1][1])] = {"path":path,"cost":int(pathdict[str(path[0])]) +  int(pathdict[str(path[1])])}
        elif str(path[0]) in lst and str(path[1]) in lst and str(path[2]) in lst  and len(path) == 3:
            cost_per_path[(path[0][0], path[0][1], path[2][0], path[2][1])] = {"path":path,"cost":int(pathdict[str(path[0])]) +  int(pathdict[str(path[1])])+  int(pathdict[str(path[2])])}

    check_cost(cost_per_path)
    
def check_cost(pathcost):
    cummulation, finallst = {}, []
    lstofpaths = list(pathcost.keys())
    for path in lstofpaths:
        revpath = list(path)
        revpath.reverse()
        if tuple(revpath) in lstofpaths:
            lstofpaths.remove(tuple(revpath))
        
    for path in lstofpaths:
        entry = []
        pth  = pathcost[path]['path']
        if isinstance(pth[0],int):
            source = 'S'+str(pth[0])
            dest = 'D'+str(pth[-1])
        else:
            source = 'S'+str(pth[0][0])
            dest = 'D'+str(pth[-1][-1])            
        entry.append(pathcost[path])
        
        if source+dest not in list(cummulation.keys()):
            cummulation[source+dest] = [path, entry]
        else:
            data = cummulation[source+dest][1]
            if data[0]['cost']<pathcost[path]['cost']:
                data[0] = pathcost[path]
            cummulation[source+dest] = [cummulation[source+dest][0], data]
    for entry in list(cummulation.keys()):
        data = cummulation[entry]
        finallst.append(data)
    #print(finallst)
    check_max(finallst)

def check_max(lst):
    maxim, routes = 0 , []
    for entr in lst:
        entry = entr[1][0]
        if entry['cost'] > maxim:
            maxim = entry['cost']
            route = entry
            combo = entr[0]
    #lst.remove(route)
    for entr in lst:
        entry = entr[1][0]
        if entry != route and route['cost'] == entry['cost']:
            routes.append([combo,route])
            routes.append([entr[0],entry])
    if len(routes) == 0:
        routes.append([combo,route])
    print_result(routes)
    
def print_result(paths):
    print('Number of possible routes that Nikhil can take is',len(paths),'that costs',paths[0][1]['cost'],'dollars.')
    
    for pathog in paths:
        path = pathog[1]
        if len(path['path']) == 1:
            print('From:',path['path'][0], '\nTo:',path['path'][-1],'\nRoute:',path )
        else:
            print('From:',path['path'][0][0], '\nTo:',path['path'][-1][-1],'\nRoute:',pathog[0] )
       
if __name__ == "__main__":
    take_input()