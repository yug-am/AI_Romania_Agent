from queue import LifoQueue
def stack_empty_check(stack):
    return len(stack) == 0
def pick_next_place_index(current_index, visited_places_index, dist_matrix):
    #print("Pick next index call")
    curr_dist_arr = dist_matrix[current_index]
    #print(curr_dist_arr)
    index = 0
    for distance in curr_dist_arr:
        #print(str(index)+" "+str(distance))
        if (distance != -1 and index not in visited_places_index):
            print("Found "+str(index))
            return index
        index+=1
    return -1
def depth_first_search(dist_matrix, source, destination, places_index_map):
    #print(dist_matrix)
    print("Source is "+source)
    print("Destination is " + destination)
    source_index = places_index_map[source]
    destination_index = places_index_map[destination]
    visited_places_index = []
    stack = []
    stack.append(source_index)
    visited_places_index.append(source_index)
    while (len(stack)>0):
        top_index = stack[-1]
        print("Top index is "+str(top_index))
        picked_index = pick_next_place_index(top_index, visited_places_index, dist_matrix)
        print("Got "+str(picked_index))
        if (picked_index == destination_index):
            stack.append(destination_index)
            print("Solution found!!")
            return stack
        elif(picked_index==-1):
            print("No options here, popping")
            stack.pop()
        else:
            stack.append(picked_index)
            visited_places_index.append(picked_index)
            print("pushed "+str(picked_index))