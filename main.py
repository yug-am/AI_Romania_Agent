# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from data import data_prep
from  agentprogram.dfs import depth_first_search
from agentprogram.greedybfs import greedy_best_first_search
from agentprogram.astar import a_star_search
from agentprogram.uniform_search import uniform_search

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Welcome Agent {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('AI')
    places_index_map, index_places_map ,dist_matrix, st_line_dist = data_prep()
    print(places_index_map)
    source = "Arad"
    destination = "Bucharest"
    solution = []
    #solution = greedy_best_first_search(dist_matrix, source, destination, places_index_map,st_line_dist)
    #solution = depth_first_search(dist_matrix, source, destination, places_index_map)
    solution = a_star_search(dist_matrix, source, destination,places_index_map, st_line_dist,)
    #solution = uniform_search(dist_matrix, source, destination, places_index_map)
    for place_index in solution:
        print(index_places_map[place_index])
 # See PyCharm help at https://www.jetbrains.com/help/pycharm/
