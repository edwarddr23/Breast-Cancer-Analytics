Pyspark project created for Big Data Programming course (Spring 2024).
_____________________________________________________________________________
Data Information:
First column represents months. Second column represents a temperature on a certain day.
The output files here are what results from running these scripts.
_____________________________________________________________________________
How to run the python file:
1. For simplicity, create a dataproc Linux VM environment (Google cloud has tools available).
2. Upload these files into the VM's root: input.txt, assignment8_part1.py, and assignment8_part2.py.
3. Type the following commands into the terminal:
   hdfs dfs -put input.txt input
   spark-submit [name of python file here]
5. Wait for the script to fully run until it successfully writes to output/output.txt.
6. Type the following command (you can choose the name of the output file):
   hdfs dfs -getmerge output/* [name of output file].txt
8. This output text file will hold the output attached to this repository.
