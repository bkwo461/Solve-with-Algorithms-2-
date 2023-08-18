
import sys

def dijkstra(graph):
    distances = graph[0]
    colour = ['W' for i in range(len(graph))]

    while 'W' in colour:
        u = -1
        for i in range(len(distances)):
            if colour[i] == 'W' and (u == -1 or distances[i] < distances[u]):
                u = i

        colour[u] = 'B'
        for v in range(len(graph)):
            if colour[v] == 'W'  and graph[u][v] != 9999 and distances[u] + graph[u][v] < distances[v]:
                distances[v] = distances[u] + graph[u][v]


    

    return '{:.2f}'.format(distances[len(distances)-1]) if distances[len(distances)-1] != 9999 else -1


lines = sys.stdin.readlines()
for line in lines:
    splittedLine = line.strip().split(",")
    boulders = []
    graph = [ [9999 for j in range(1, len(splittedLine), 2)] for i in range(1, len(splittedLine), 2) ]
    
    dim = float(splittedLine[0].strip())
    for i in range(1, len(splittedLine), 2):
        boulders.append( ( float(splittedLine[i]), float(splittedLine[i+1] ) ) )
    
    for i in range(len(boulders)):
        for j in range(i+1, len(boulders)):
            dist = ((boulders[i][0] - boulders[j][0])**2 + (boulders[i][1] - boulders[j][1])**2)**0.5
            if dist <= 100:
                graph[i][j], graph[j][i] = dist, dist

    print(dijkstra(graph))