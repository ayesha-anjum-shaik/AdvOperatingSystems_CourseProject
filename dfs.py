#Project : DFS vs BFS
#Name : Ayesha Anjum Shaik
#RID : R11800013
#Program to execute the "Depth First Search" Algorithm
import psutil
import time
import matplotlib.pyplot as plt
import numpy as np
p1 = psutil.Process()
# Input graph taken as follows
input_graph = {
    'A': ['B', 'S'],
    'B': ['A'],
    'C': ['D', 'E', 'F', 'S'],
    'D': ['C'],
    'E': ['C', 'H'],
    'F': ['C', 'G'],
    'G': ['F', 'S'],
    'H': ['E', 'G'],
    'S': ['A', 'C', 'G']
}

searched = [] #considered a global variable to display the visited graph
startTime = time.time() #program execution start time

class dfs:
    #method to traverse the graph using "Depth First Search" algorithm
    def getDfsOutput(self, graph, input_node):
        global searched
        if input_node not in searched:
            searched.append(input_node)
            for n in graph[input_node]:
                dfs.getDfsOutput(self, graph, n)
        return searched

    #method to print the System level Information
    def printDfsOutput(self):
        print("The output when executed using Depth First Search is : ")
        print(dfs.getDfsOutput(self, input_graph, 'A'))
        print("DFS System-Level Information")
        CPU_Usage = psutil.cpu_percent(interval=2) / psutil.cpu_count()
        print("CPU_Usage : ", CPU_Usage, "%")
        Memory_Usage = p1.memory_percent()
        print("Memory_Usage : ", Memory_Usage, "%")
        HardDrive_Usage = psutil.disk_usage('/')[3]
        print("HardDrive_Usage : ", HardDrive_Usage, "%")
        RSS = p1.memory_info()[0]
        print("RSS : ", RSS)
        VMS = p1.memory_info()[1]
        print("VMS: ", VMS)
        NoOfPageFaults = p1.memory_info()[2]
        print("NoOfPageFaults :", NoOfPageFaults)
        DFS_values = [CPU_Usage, Memory_Usage, HardDrive_Usage, RSS, VMS, NoOfPageFaults]
        # DFS_values = [psutil.cpu_percent(interval=2) / psutil.cpu_count(),p1.memory_percent(),psutil.disk_usage('/')[3],p1.memory_info()[0],p1.memory_info()[1],p1.memory_info()[2]]
        return DFS_values

    # method to display the execution time of the program
    def displayRunningTime(self):
        print("DFS User-Level Information")
        print("Program started execution at : "+ time.ctime(startTime))
        endTime = time.time()
        print("Program ended execution at : "+ time.ctime(endTime))
        executionTime = endTime-startTime
        print("Program execution running time(in seconds) is : "+ str(executionTime))

    #method to represent the data in the bar graph
    def DfsDataRepresentation(self):
        dfsbar_width = 0.4
        dfsbar_label = ["CPU_Usage", "Memory_Usage", "HardDrive_Usage"]
        dfsbar_values = [psutil.cpu_percent(interval=2) / psutil.cpu_count(), p1.memory_percent(), psutil.disk_usage('/')[3]]
        dfsbar = np.arange(len(dfsbar_label))
        plt.bar(dfsbar, dfsbar_values, dfsbar_width, label="DFS Bar Graph Representation")
        plt.ylabel("Percentage value")
        plt.xticks(dfsbar, dfsbar_label)
        plt.title("DFS Bar Graph Representation")
        #plt.show()
        plt.savefig("DFS_Bar_Graph.png")

#main method indicating the start of execution
if __name__ == "__main__":
    DFS = dfs()
    DFS.printDfsOutput()
    DFS.displayRunningTime()
    DFS.DfsDataRepresentation()

#To take the input from the user
# def getInput(self):
#     wb = openpyxl.load_workbook(r'C:\Users\18062\Desktop\Input_Data.xlsx')
#     sheet = wb['Sheet1']
#     graph_input = {}
#     for i in range(2, 10):
#         vertex = sheet.cell(row=i, column=1).value
#         nodes = sheet.cell(row=i, column=2).value.split()
#         print(nodes)
#         if not vertex in graph_input:
#             graph_input[vertex] = []
#         #graph_input[vertex].append(nodes)
#
#     print(graph_input)
#     x = sheet.cell(row=2, column=1).value
#     print(str(x))
#     return graph_input