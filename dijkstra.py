import sys

def dijkstra(vertice_count,graph,start_node):
	# shortest distance - index is node, value is distance
	shortest_distance = [0 if i==start_node else float('inf') for i in range(vertice_count)]
	# unvisited_nodes - value keeps track of unvisited nodes
	unvisited_nodes = [i for i in range(vertice_count)]
	current_node = start_node

	# run once for each node, determines a minimum path for a node in each iteration
	unvisited_nodes_distances=[1]
	loop_a_time = 0
	loop_b_time = 0
	while_loop_start_time=time.time()
	while len(unvisited_nodes)>0 and set(unvisited_nodes_distances)!={float('inf')}:
		loop_a_start_time = time.time()
		for edge,weight in graph.items():
			if current_node in edge:
				end_node=edge[0] if current_node == edge[1] else edge[1]
				if end_node in unvisited_nodes and (shortest_distance[current_node] + weight<shortest_distance[end_node]):
					shortest_distance[end_node]=shortest_distance[current_node] + weight
		loop_a_time += time.time() - loop_a_start_time
		unvisited_nodes.remove(current_node)
		unvisited_nodes_distances= [shortest_distance[unvisited_nodes[i]] for i in range(len(unvisited_nodes))]
		if len(unvisited_nodes)>0 and min(shortest_distance)!=float('inf'):
			loop_b_start_time = time.time()
			min_value = float('inf')
			for i in range(len(unvisited_nodes)):
				if shortest_distance[unvisited_nodes[i]]!= float('inf') and  shortest_distance[unvisited_nodes[i]]< min_value:
					min_value = shortest_distance[unvisited_nodes[i]]
					current_node = unvisited_nodes[i]
			loop_b_time += time.time() - loop_b_start_time
	shortest_distance.remove(0)
	print (*shortest_distance)

# # for running code in hackerrank
n = int(input())
for x in range(n):
	v,e=map(int,input().split())
	graph = {}
	for i in range(e):
	    edge = list(map(int,input().split()))
	    if (edge[0]-1,edge[1]-1) in graph:
	    	if edge[2] < graph[edge[0]-1,edge[1]-1]:
	    		graph[edge[0]-1,edge[1]-1]=edge[2]
	    else:
	    	graph[edge[0]-1,edge[1]-1]=edge[2]
	start_node = int(input())-1
	dijkstra(v,graph,start_node)