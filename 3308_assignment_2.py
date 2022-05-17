# 3308
import sys
import random 
class Graph():
	
	# Dijstra's for Single Source
	# Prim's
	# Kruskal's
	def __init__(self, vertices): 
		self.V = vertices
		self.graph_matrix = [[0 for column in range(vertices)]for row in range(vertices)]
		self.graph_edges = []
		
	def convert_matrix_to_edges(self):
		for i in range(len(self.graph_matrix)):
			
			for j in range(len(self.graph_matrix[i])):
				if self.graph_matrix[i][j] != 0:
					self.addEdge(i,j,self.graph_matrix[i][j])
		print("final graph as adjaceny list is\n",self.graph_edges)

	def convert_edges_to_matrix(self):
		for i in self.graph_edges:
			self.graph_matrix[i[0]][i[1]] = i[2]

	def addEdge(self, u, v, w):
		self.graph_edges.append([u, v, w])
		
	def minKey(self, key, mstSet):
		min = sys.maxsize
		for v in range(self.V):
			if key[v] < min and mstSet[v] == False:
				min = key[v]
				min_index = v
		print("minimum cost unvisited node is",min_index)
		return min_index
	def PrimMST(self):
		key = [sys.maxsize] * self.V
		key[0] = 0
		parent = [None] * self.V 
		mstSet = [False] * self.V
		parent[0] = -1 # no parent for root
		for cout in range(self.V):
			u = self.minKey(key, mstSet)
			mstSet[u] = True
			for v in range(self.V):
				if self.graph_matrix[u][v] > 0 and mstSet[v] == False and key[v] > self.graph_matrix[u][v]:
						print("havent prcoessed edge from ",u,"to" ,v, " it has potential for better connections")
						key[v] = self.graph_matrix[u][v]
						parent[v] = u
						print("parent of ",v ,"is set to",u)
		print("final parent structure is")
		print(parent)

	def find(self, parent, i):
		if parent[i] == i:
			return i
		k = self.find(parent, parent[i])
		return k


	def union(self, parent, rank, x, y):# Union find with rank 
		xroot = self.find(parent, x)
		yroot = self.find(parent, y)
		print("parent of ",x," is ",xroot)
		print("parent of ",y," is ",yroot)
		if rank[xroot] < rank[yroot]:
			parent[xroot] = yroot
		elif rank[xroot] > rank[yroot]:
			parent[yroot] = xroot
		else:
			parent[yroot] = xroot
			rank[xroot] += 1
		print("setting parent of ",xroot ,"to",parent[xroot])
		print("setting parent of ",yroot ,"to",parent[yroot])
		print("new ranks are xroot =",rank[xroot],"yroot =",rank[yroot])

	def KruskalMST(self):
		result = [] 
		i = 0
		e = 0
		self.graph_edges = sorted(self.graph_edges,key=lambda item: item[2])

		parent = []
		rank = []
		for node in range(self.V):
			parent.append(node)
			rank.append(0)
		
		while e < self.V - 1:
			u, v, w = self.graph_edges[i]
			i = i + 1
			x = self.find(parent, u)
			print("parent of ",u," is ",x)
			y = self.find(parent, v)
			print("parent of ",v," is ",y)
			if x != y:
				print("parents of",u,v,"are not the same finding the better ranked parent to assign to both" )
				e = e + 1
				result.append([u, v, w])
				self.union(parent, rank, x, y)
		
		print(result)
	def Dijkstra(self, src):
		print("source node is ",src)
		dist = [sys.maxsize] * self.V
		dist[src] = 0
		sptSet = [False] * self.V

		for cout in range(self.V):
			x = self.minKey(dist, sptSet)# its a priority queue
			sptSet[x] = True
			for y in range(self.V):
				if self.graph_matrix[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + self.graph_matrix[x][y]:
					print("path from" ,x , "to",y , "is shorter using this now")
					dist[y] = dist[x] + self.graph_matrix[x][y]
		print("distances from source",src, "to all nodes is")
		print(dist)

if __name__ == '__main__':
	n = int(input("input size of graph:"))
	g = Graph(n)
	default = raw_input("use all default?[y/n] ")
	if default in ["Y","y"]:
		for i in range(n):
			for j in range(n):
				if  random.randint > .6:
					g.graph_matrix[i][j] = random.randrange(1,100)
				else:
					g.graph_matrix[i][j] = 0
	else:
		for i in range(n):
			for j in range(n):
				print("weight for edge from" ,i, "to", j)
				w = int(input())
				if type(w) == float:
					g.graph_matrix[i][j] = w 
				else: 
					g.graph_matrix[i][j] = default[i][j]
					print("input invalid using default value")
				print("entered ",default[i][j])
	print("final graph is ", g.graph_matrix)
	print("commencing conversion to adjacency matrix ")
	g.convert_matrix_to_edges()
	print("coversion finished")
	print("Prims MST is")
	g.PrimMST()
	print("Kruskals MST is")
	g.KruskalMST()
	print("Dijkstra's is")
	g.Dijkstra(0)