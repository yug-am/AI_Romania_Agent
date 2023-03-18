places=['Arad','Timisoara','Zerind','Oradea','Lugoj','Mehadia','Dobreta',
'Sibiu','Rimnicu Vilcea','Craiova','Fagaras','Pitesti','Giurgiu',
'Bucharest','Urziceni','Vaslui','Iasi','Neamt','Hirsova','Eforie',
        ]
St_line_dist_bucharest={
    'Arad':366,
    'Timisoara':329,
    'Zerind':374,
    'Oradea':380,
    'Lugoj':244,
    'Mehadia':241,
    'Dobreta':242,
    'Sibiu':253,
    'Rimnicu Vilcea':193,
    'Craiova':160,
    'Fagaras':176,
    'Pitesti':100,
    'Giurgiu':77,
    'Bucharest':0,
    'Urziceni':80,
    'Vaslui':199,
    'Iasi':226,
    'Neamt':234,
    'Hirsova':151,
    'Eforie':161,
}
places_dist={
    "Arad_Zerind":75,
    "Arad_Timisoara":118,
    "Timisoara_Lugoj":111,
    "Lugoj_Mehadia":70,
    "Mehadia_Dobreta":75,
    "Dobreta_Craiova":120,
    "Zerind_Oradea":71,
    "Oradea_Sibiu":151,
    "Arad_Sibiu":140,
    "Sibiu_Fagaras":99,
    "Sibiu_Rimnicu Vilcea":80,
    "Rimnicu Vilcea_Pitesti":97,
    "Rimnicu Vilcea_Craiova":146,
    "Fagaras_Bucharest":211,
    "Pitesti_Bucharest":101,
    "Craiova_Pitesti":138,
    "Bucharest_Giurgiu":90,
    "Bucharest_Urziceni":85,
    "Urziceni_Hirsova":98,
    "Hirsova_Eforie":86,
    "Urziceni_Vaslui":142,
    "Vaslui_Iasi":92,
    "Iasi_Neamt": 87,
}
st_line_dist={}
places.sort()
#for test
#places.sort(reverse=True)
places_index_map={}
index_places_map={}
def data_prep():
    print(places)
    for i, place in enumerate(places):
        index_places_map[i]=place
        places_index_map[place]=i
        #print(i,place)
    num_places = len(places)
    dist_matrix = [[-1] * num_places for _ in range(num_places)]
    for k, dist in places_dist.items():
        places_in_key = k.split("_")
        place_source = places_in_key[0]
        place_destination = places_in_key[1]
        dist_matrix[places_index_map[place_source]][places_index_map[place_destination]] = dist
        print("{src} to {des} is {distance}".format(src = place_source, des = place_destination, distance = dist))
    places_short = [place[:3]for place in places  ]
    print("    ",end="")
    print(places_short)
    for location, dist in St_line_dist_bucharest.items():
        st_line_dist[places_index_map[location]]=dist
    for i, dist_vect in enumerate(dist_matrix):
        #print(index_places_map[i] ,end=" ")
        dist_vect_temp = [str(dst)+(" ") for dst in dist_vect]
        #print(dist_vect_temp)
    #print("Edge count is {}".format(len(places_dist)))
    return [places_index_map, index_places_map ,dist_matrix, st_line_dist]
    #print(places_map)
