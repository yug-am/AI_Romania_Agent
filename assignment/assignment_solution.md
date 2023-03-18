# AI assignment

## Algo implementation
 Q.1 Following  search algorithms are implemented to find the path from Arad to Bucharest:

**agentprogram** module has files by respective names:
-  Depth-First search
- Greedy Best-First search
- Uniform-Cost search
- A* search

|  Search algorithm | Python file name  |
|---|---|
| Depth-First search  |  dfs  |
| Greedy Best-First search  | greedybfs|
|Uniform-Cost search   |  uniform_search |
|   A* search |  astar |

## Ordering 
Places are arranged in ascending ordering of name in the distance matrix

## Q.2 Exploration analysis
- ##### Effects of Simulated Annealing on this problem
    Simulated anealing would have followed path along the location with decrease
the distance from destination( i.e. Bucharest) and on deadend would have picked
  a random location again and decreased the probability of taking that path
  by some badness factor b raise to power n  i.e. ```P = P - b^n```.
  
-   **Effects of Genetic Algorithm on this problem**
    Genetic Algorithm would have selected next possible places according to 
  fitness function that would have been like closer to destination ( i.e. Bucharest) 
  and then from choices would have taken intermediate paths and Random exploration
  would have helped in long run like help with future other routes as well.
  
## Q.3 Obervations analysis

- ##### observations about uninformed search
  Uninformed search performed like a generic graph algo which finds path between nodes with backtracking and the values of 
distance would only be used.
   **Uniform-Cost search** performed at par with shorted path

- ##### observations about  informed search
  Informed search gave a mixed results in terms of  as in this case straight line distance was huerisrics but path was not 
there between all nodes.
  
  **A\* Search Algorithm** gave longer path
  
- ##### observations about probabilistic search
  Probabilistic search which penalize deadends may work better for non lead/ dead end
destination as there may be more possibilties of picking them/ moving closer to them

-  ##### observations about  meta-heuristic search
  For Agent to be trained for flexibility in longer run for dynamic routes should served 
  as better exploratory and better learning algorithms.
 
    - Simulated anealing would have followed path along the location with decrease
the distance from destination( i.e. Bucharest) and on deadend would have picked
  a random location again and decreased the probability of taking that path
  by some badness factor b raise to power n.

 
 

[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yug-am/)