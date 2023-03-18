def pick_next_place_index(current_index, visited_places_index, dist_matrix):
    #print("Pick next index call")
    curr_dist_arr = dist_matrix[current_index]
    #print(curr_dist_arr)
    index = 0
    possible_places=[]
    for distance in curr_dist_arr:
        #print(str(index)+" "+str(distance))
        if (distance != -1 and index not in visited_places_index):
            print("Found "+str(index))
            possible_places.append(index)
        index+=1
    sorted(range(len(possible_places)), key=possible_places.__getitem__)
    return possible_places
def uniform_search(dist_matrix, source, destination, places_index_map):
    #print(dist_matrix)
    print("Source is "+source)
    print("Destination is " + destination)
    source_index = places_index_map[source]
    destination_index = places_index_map[destination]
    visited_places_index = []
    queue = []
    queue.append(source_index)
    visited_places_index.append(source_index)
    parent={}
    solution = []
    while (len(queue)>0):
        top_index = queue[0]
        print("Top index is " + str(top_index))
        #visited_places_index.append(source_index)
        if (top_index == destination_index):
            #queue.append(destination_index)
            print("Solution found!!")
            curr = top_index
            solution.append(curr)
            while( curr != source_index):
                temp = parent[curr]
                solution.append(temp)
                curr = temp
            return solution[::-1]

        picked_indexes = pick_next_place_index(top_index, visited_places_index, dist_matrix)
        if(len(picked_indexes)==0):
            print("No options here, popping")
            queue.remove(queue[0])
        else:
            for index in picked_indexes:
                visited_places_index.append(index)
                queue.append(index)
                parent[index]=top_index


