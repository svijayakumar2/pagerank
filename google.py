import numpy as np
import collections
import matplotlib.pyplot as plt 


filename = 'google.txt'
network = collections.defaultdict(list)
with open(filename, 'r') as f:
	mylist = f.read().splitlines()
	for line in mylist:
		data = [int(x) for x in line.split(' ')]
		network[data[0]].append(data[1])


edges = 0
n = len(set(open('google.txt').read().split()))
print n #or len(network)

for k in network.keys():
	edges += len(network[k])
#average out degree 
print float(edges)/float(n) 

###################
pr = {}
for i in range(n):
    pr[i] = (float(1/float(n)))
###################

def pageRankIter(g,d):
	d_new = {}
	for i in d.keys():
		if g[i] == []:
			d_new[i] = d[i]
		else:
			deg = len(g[i])
			if not d_new.has_key(i):
				d_new[i] = 0
			for edge in g[i]:
				d_new[edge] = d_new.get(edge,0)+float(d[i])/(deg)
	return d_new	


def basicPR(g,d,k):
	d_new = pageRankIter(g,d)
	for i in range(1,k):
		d_new = pageRankIter(g,d_new)
	return d_new


def scaledPR(g,d,k,s):
	d_new = pageRankIter(g,d)

	for j in range(1,k):
		d_new = pageRankIter(g,d_new)
		for i in d_new.keys():
			d_new[i] *= s
			d_new[i] = float(d_new.get(i,0)) + (float(1-s)/float(n))
			
	return d_new


def plot(d):
	plt.hist(d_new.values(),bins=np.linspace(0.,0.000025, num=50),edgecolor='black')
	plt.show()
	#plt.savefig('basicPR50.png')

#width = 100000.0
#
d_new = pageRankIter(network, pr)
#d_new = basicPR(network,pr,200)
#d_new = scaledPR(network,pr,10,.85)
#print d_new
#plot(d_new)

filename2 = 'links.txt'
link_graph = collections.defaultdict(list)

with open(filename2, 'r') as f:
	mylist = f.read().splitlines()
	for line in mylist:
		data = [(x) for x in line.split(' ')]
		link_graph[int(data[0])].append(data[1]) #hope this works 


#print link_graph

def RaynorSearch():
	substring = '34'
	list34 = [] 
	top5 = []
	top5links = []
	d_new = scaledPR(network,pr,100,.85)
	counter = 0
	#print d_new[387734]
	for key, value in link_graph.iteritems():
		if substring in value[0]:
			print key
			print value
			try:
				list34.append(d_new[key]) #also want key
			except:
				list34.append(0)
				counter+=1
	
	print counter
	#sorted(list34.keys(), key=lambda x: x[1], reverse=True)
	list34.sort()
	print list34
	top5 = list34[-5:] #key
	d2 = dict((v, k) for k, v in d_new.iteritems())
	for t in top5: #nodes of the top five 
		key = d2[t] #get key at value -- gives you node not pr scre 
		top5links.append(link_graph[key]) #gets link at node 

	print top5links
	print top5
	return top5


#RaynorSearch()
			


		#return the max of the values of the d_new after running scaled 



