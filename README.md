Pyspark project created for Big Data Programming course (Spring 2024).
_____________________________________________________________________________
Data Information:
First column represents age (years). Second column represents a biological sex (Male = 0, Female - 1).
The output file (out.txt) here are what results from running these scripts.
_____________________________________________________________________________
How to run the python file:
1. For simplicity, create a dataproc Linux VM environment (Google cloud has tools available).
2. Upload these files into the VM's root: input.txt, main.py
3. Type the following commands into the terminal:
   hdfs dfs -put input.txt input
   spark-submit [name of python file here]
5. Wait for the script to fully run until it successfully writes to output/output.txt.
6. Type the following command (you can choose the name of the output file):
   hdfs dfs -getmerge output/* [name of output file].txt
8. This output text file will hold the output attached to this repository.
