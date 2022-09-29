#Project : DFS vs BFS
#Name : Ayesha Anjum Shaik
#RID : R11800013
#Program to execute the "Breadth First Search" Algorithm
import psutil
import time
import numpy as np
import matplotlib.pyplot as plt
p2=psutil.Process()
# Input graph taken as follows
input_graph={
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}
startTime = time.time()

class bfs:
    # method to traverse the graph using "Breadth First Search" algorithm
    def getBfsOutput(self, graph, input_node):
        searched = []
        queue = [input_node]
        while queue:
            vertex = queue.pop(0)
            if vertex not in searched:
                searched.append(vertex)
                queue.extend(graph[vertex])
        return searched

    # method to print the System level Information
    def printBfsOutput(self):
        print("The output when executed using Breadth First Search is : ")
        print(bfs.getBfsOutput(self, input_graph, 'A'))
        print("BFS System-Level Information")
        CPU_Usage = psutil.cpu_percent(interval=2) / psutil.cpu_count()
        print("CPU_Usage : ", CPU_Usage, "%")
        Memory_Usage = p2.memory_percent()
        print("Memory_Usage : ", Memory_Usage, "%")
        HardDrive_Usage = psutil.disk_usage('/')[3]
        print("HardDrive_Usage : ", HardDrive_Usage, "%")
        RSS = p2.memory_info()[0]
        print("RSS : ", RSS)
        VMS = p2.memory_info()[1]
        print("VMS: ", VMS)
        NoOfPageFaults = p2.memory_info()[2]
        print("NoOfPageFaults :", NoOfPageFaults)
        BFS_values = [CPU_Usage, Memory_Usage, HardDrive_Usage, RSS, VMS, NoOfPageFaults]

        # BFS_values = [psutil.cpu_percent(interval=2) / psutil.cpu_count(), p2.memory_percent(), psutil.disk_usage('/')[3],p2.memory_info()[0], p2.memory_info()[1], p2.memory_info()[2]]
        return BFS_values

    # method to display the execution time of the program
    def displayRunningTime(self):
        print("BFS User-Level Information")
        print("Program started execution at : "+ time.ctime(startTime))
        endTime = time.time()
        print("Program ended execution at : "+ time.ctime(endTime))
        executionTime = endTime-startTime
        print("Program execution running time(in seconds) is : "+ str(executionTime))

    # method to represent the data in the bar graph
    def BfsDataRepresentation(self):
        bfsbar_width = 0.4
        bfsbar_label = ["CPU_Usage", "Memory_Usage", "HardDrive_Usage"]
        bfsbar_values = [psutil.cpu_percent(interval=2) / psutil.cpu_count(), p2.memory_percent(), psutil.disk_usage('/')[3]]
        bfsbar = np.arange(len(bfsbar_label))
        plt.bar(bfsbar, bfsbar_values, bfsbar_width, label="BFS Bar Graph Representation")
        plt.ylabel("Percentage value")
        plt.xticks(bfsbar, bfsbar_label)
        plt.title("BFS Bar Graph Representation")
        #plt.show()
        plt.savefig("BFS_Bar_Graph.png")

#main method indicating the start of execution
if __name__ == "__main__":
    BFS = bfs()
    BFS.printBfsOutput()
    BFS.displayRunningTime()
    BFS.BfsDataRepresentation()