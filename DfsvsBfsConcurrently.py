#Project : DFS vs BFS
#Name : Ayesha Anjum Shaik
#RID : R11800013
#Program to execute the "Depth First Search" and "Breadth First Search" Algorithms concurrently
import numpy as np
import psutil
import time
from matplotlib import pyplot as plt
import Multi_Process
import multiprocessing
p = psutil.Process()
C_Pro = Multi_Process.Multi_Process()
startTime = time.time()
class DfsvsBfsConcurrently:
    #method to create the object for concurrent execution
    def DfsvsBfs(self):
        Concurrent_proc = multiprocessing.Process(target=C_Pro.Concurrent_Processing)
        Concurrent_proc.start()
        Concurrent_proc.join()

    #method to display the System level Information when run the programs concurrently
    def printConcurrentOutput(self):
        print("System level Information for DFS and BFS run Concurrently")
        CPU_Usage = psutil.cpu_percent(interval=2) / psutil.cpu_count()
        print("CPU_Usage : ", CPU_Usage, "%")
        Memory_Usage = p.memory_percent()
        print("Memory_Usage : ", Memory_Usage, "%")
        HardDrive_Usage = psutil.disk_usage('/')[3]
        print("HardDrive_Usage : ", HardDrive_Usage, "%")
        RSS = p.memory_info()[0]
        print("RSS : ", RSS)
        VMS = p.memory_info()[1]
        print("VMS: ", VMS)
        NoOfPageFaults = p.memory_info()[2]
        print("NoOfPageFaults :", NoOfPageFaults)
        DFSvsBfs_values = [CPU_Usage, Memory_Usage, HardDrive_Usage, RSS, VMS, NoOfPageFaults]
        # DFSvsBfs_values = [psutil.cpu_percent(interval=2) / psutil.cpu_count(), p.memory_percent(), psutil.disk_usage('/')[3],p.memory_info()[0], p.memory_info()[1], p.memory_info()[2]]
        return DFSvsBfs_values

    # method to display the execution time of the program
    def displayRunningTime(self):
        print("Concurrent Execution User-Level Information")
        print("Program started execution at : " + time.ctime(startTime))
        endTime = time.time()
        print("Program ended execution at : " + time.ctime(endTime))
        executionTime = endTime - startTime
        print("Program execution running time(in seconds) is : " + str(executionTime))

    # method to represent the data in the bar graph
    def BfsDfsDataRepresentation(self):
        bfsdfsbar_width = 0.4
        bfsdfsbar_label = ["CPU_Usage", "Memory_Usage", "HardDrive_Usage"]
        bfsdfsbar_values = [psutil.cpu_percent(interval=2) / psutil.cpu_count(), p.memory_percent(), psutil.disk_usage('/')[3]]
        bfsdfsbar = np.arange(len(bfsdfsbar_label))
        plt.bar(bfsdfsbar, bfsdfsbar_values, bfsdfsbar_width, label="Concurrent Execution Bar Graph Representation")
        plt.ylabel("Percentage value")
        plt.xticks(bfsdfsbar, bfsdfsbar_label)
        plt.title("Concurrent Execution Bar Graph Representation")
        #plt.show()
        plt.savefig("BFS_DFS_Bar_Graph.png")

#main method indicating the start of execution
if __name__ == "__main__":
    DfsvsBfsObj = DfsvsBfsConcurrently()
    DfsvsBfsObj.printConcurrentOutput()
    DfsvsBfsObj.displayRunningTime()
    DfsvsBfsObj.BfsDfsDataRepresentation()