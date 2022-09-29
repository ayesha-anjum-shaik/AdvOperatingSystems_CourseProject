#Project : DFS vs BFS
#Name : Ayesha Anjum Shaik
#RID : R11800013
import concurrent.futures
import multiprocessing
from multiprocessing import Process
import psutil
import time
import dfs
import bfs
DFS = dfs.dfs()
BFS = bfs.bfs()

class Multi_Process():
    #method to initiate multiprocessing
    def Concurrent_Processing(self):
        proc1 = multiprocessing.Process(target=DFS.getDfsOutput)
        proc2 = multiprocessing.Process(target=BFS.getBfsOutput)
        # Doing this will execute the programs one after the other
        proc1.start()
        proc2.start()
        proc1.join()
        proc2.join()
