
# coding: utf-8

# In[28]:

import sys
import re
import os
import collections
import numpy as np
import operator
import math



class pagerank:
    def pagerank(self, input_file, alpha, diff):
        #start = time.time()


        File = open(os.path.join(input_file, "test-1.txt"), "r") 
        alpha = 0.14
        diff = 0.007
        i = 0
        for line in File:
            if i == 0:
                # It takes the initial value from the text file, which is the first line and store in length. 
                # Length contains the total number of states in integer.
                self.length = int(line)
                
                #Initial Adjacency matrix created of lenth of number states with all the values as zero.
                AdjacencyMatrix = [[0 for x in range(self.length)]
                for y in range(self.length)]
                i += 1
            elif i == 1:
                i += 1
            else:
                # From line 3. We will check the number of outlinks. 
                arr = line.split()
                numberofones1 = int(arr[0])
                # contains the number of ones in each row
                positionofones2 = int(arr[1])
                # contains the positions of ones w.r.t. each row
                AdjacencyMatrix[numberofones1][positionofones2] = 1
        
        
        
        print("Adjacency Matrix: ", "\n", np.matrix(AdjacencyMatrix))
        
        i = 0
        temp_array = list()
        
        #adjacency matrix created
        
        for rows in AdjacencyMatrix:
            np_row = np.array(rows)
            if np_row.nonzero():
                outgoingLinksLen = np_row.sum()
                np_row = np_row * ((1 - alpha) / outgoingLinksLen)
                np_row = np_row + (alpha / self.length)
            row = list(np_row)
            temp_array.append(row)
        self.TeleportationMatrix = np.matrix(temp_array)
        self.Teleport = np.around(self.TeleportationMatrix,4)
        print("Transition Matrix with teleportation:", "\n ", np.matrix(self.Teleport))
        # Transition Matrix with teleportation is created
        
        
        #Power Iteration starts here.
        
        x_previous = np.array([alpha for x in range(self.length)])
        y = self.TeleportationMatrix
        new = np.array([0 for x in range(self.length)])
        x = np.array([0 for x in range(self.length)])
        count = 0
        x = x_previous.copy()
        
        while np.sum(np.abs (new - x_previous)) >= diff:
            if count > 1000:
                break
            x_previous = x.copy()
            x = np.dot(x, y)
            x = np.around(x,3)
            new=x.copy()
            count = count +1
        
        print ("The pagerank value after convergence is :" +str(new) )
        
        
        

        #it will create a text file with the name text_output with the pagerank values of different pages.
        file = open("text_output.txt","w")
        i=0
        for item in np.nditer(new):
                i+=1
                file.write("D"+str(i)+"\t: "+str(item)+"\n")
        file.close()
        
        #end = time.time()
        #print ('PageRank value calculated in '+str(end-start) +' sec.')



        
#~~~~~~~~~~~~~~~~~~~~Execution~~~~~~~~~~~~~~~~~~~~~~~
            
path = 'D:\Study\Sem-2\IR\Assignment 4'

obj = pagerank()

obj.pagerank(path, 0.15,0.007)


# In[ ]:



