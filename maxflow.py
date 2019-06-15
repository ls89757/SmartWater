import queue
edge = []
parent = []
def BFS(source,to):
	visited = []
	for i in range(0,vertex_num):
		visited.append(0)
	for i in range(0,vertex_num):
		parent[i] = -1
	q = queue.Queue()
	visited[source] = 1
	q.put(source)
	while(q.qsize()>0):
		# print(q.queue)
		u = q.get()
		for j in range(0,vertex_num):
			if ((not visited[j]) and edge[u][j]>0):
				q.put(j)
				visited[j]= 1
				parent[j] = u
	# print(parent) 
	return visited[to]
while True:
	try:
		edge_num,vertex_num = map(int,input().split())
		for i in range(0,vertex_num):
			parent.append(-1)
		for i in range(0,vertex_num):
			edge.append([])
			for j in range(0,vertex_num):
				edge[i].append(0)
		for i in range(0,vertex_num):
			edge[i][i] = -1
		for i in range(0,edge_num):
			from_vertex,to_vertex,rest=map(int, input().split())
			edge[from_vertex-1][to_vertex-1] = rest
		maxflow = 0
		while(BFS(0,vertex_num-1)):
			pathflow = 1000000000
			v = vertex_num-1
			while(v!=0):
				u = parent[v]
				if pathflow>edge[u][v]:
					pathflow = edge[u][v]
				v = parent[v]
	# print(pathflow)
			v = vertex_num -1 
			while(v!=0):
				u = parent[v]
				edge[u][v] = edge[u][v] - pathflow
				edge[v][u] = edge[v][u] + pathflow
				v = parent[v]
			maxflow = maxflow + pathflow
		print(maxflow)

	except Exception as e:
		break;


# for i in range(0,vertex_num):
# 	edge.append([])
# 	for j in range(0,vertex_num):
# 		edge[i].append(0)
# for i in range(0,vertex_num):
# 	edge[i][i] = -1
# for i in range(0,edge_num):
# 	from_vertex,to_vertex,rest=map(int, input().split())
# 	edge[from_vertex-1][to_vertex-1] = rest
# # print(edge)
# maxflow = 0
# while(BFS(0,vertex_num-1)):
	
# 	pathflow = 1000000000
# 	v = vertex_num-1
# 	while(v!=0):
# 		u = parent[v]
# 		if pathflow>edge[u][v]:
# 			pathflow = edge[u][v]
# 		v = parent[v]
# 	# print(pathflow)
# 	v = vertex_num -1 
# 	while(v!=0):
# 		u = parent[v]
# 		edge[u][v] = edge[u][v] - pathflow
# 		edge[v][u] = edge[v][u] + pathflow
# 		v = parent[v]
# 	maxflow = maxflow + pathflow
# print(maxflow)
