#!/bin/bash

# launch hadoop
start-dfs.sh
start-yarn.sh
jps

# run the mapreduce job
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input /user/ubuntu/books_dataset \
  -output /user/ubuntu/books_dataset_output/mapreduce_genres \
  -mapper mapper.py \
  -reducer reducer.py



# NOTES

# to delete output folder: hdfs dfs -rm -r -skipTrash /user/ubuntu/books_dataset_output/mapreduce_genres 

# to see the folder: hdfs dfs -ls /user/ubuntu/books_dataset/

# Save in local the results (move first in /jupyter/book_reviews):
# hdfs dfs -get /user/ubuntu/books_dataset_output/mapreduce_genres ./path-to-local-folder
#  -file mapper.py \
#  -file reducer.py