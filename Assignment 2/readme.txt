								CS 429 - Information Retrieval
							 	 Assignment Ranked Retrieval
----------------------------------------------------------------------------------------------------------------------------------------------------------
Motivation: To implement vector space model and cosine similarity for retrieving top k documents from the collection of document provided.
----------------------------------------------------------------------------------------------------------------------------------------------------------
There are three parts in the project: 
Part A - Exact top k retrieval. 
In exact top k retrieval all the documents in the collection are scored and cosine score is calculated to find the top k documents which is method 1.

Part B - It consits of three methods.
Method 2 : Champion list, Implement a champion list method which will produce, for each term, a list of r documents that is based on the weighted term frequency.Come up with a formula for r. 
Method 3 : Index Elimination, Implement index elimination by using only half the queries terms sorted in decreasing order of their IDF values.
Method 4:Method 4 Simple Cluster pruning: You will randomly pick v?? leaders (where N is the number of documents in the collection) and then use them to implement the cluster pruning.

Execution:

Steps for execution:
Set the path where all the files are kept in below mentioned query.
obj = index('D:\Study\Sem-2\IR\Assignment 1\collection')

 

