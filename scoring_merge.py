#
# Scoring Merge
#
# Peter Turney, November 26, 2020
#
# Read in all of the score files, merge them, and
# then sort them.
#
import golly as g
import scoring_functions as sfuncs
import scoring_parameters as sparams
#
# make a list of the score file names
#
log_prefix = sparams.rule_file_prefix + "-CPU"
num_cpus = sparams.num_cpus
#
log_file_list = []
#
for cpu_num in range(num_cpus):
  log_file_name = log_prefix + str(cpu_num + 1) + ".txt"
  log_file_list.append(log_file_name)
#
# the target rule
#
target_rule = sparams.target_rule
#
# read the vector files into a list of vectors
#
vector_list = []
#
for log_file in log_file_list:
  log_handle = open(log_file, "r")
  for line in log_handle:
    # if the line starts with "B" then ...
    if (line[0] == "B"):
      # split line string into a vector
      vector = line.rstrip().split("\t")
      # add the vector to the list
      vector_list.append(vector)
  # close the file
  log_handle.close()
#
# open a file for writing results
#
sorted_file_name = sparams.sorted_file_name
sorted_handle = open(sorted_file_name, "w", 0)
#
# find the target rule in the list
#
target_vector = []
#
for vector in vector_list:
  # separate the rule from the rest of the vector
  rule = vector[0]
  # is this the rule we're looking for?
  if (rule == target_rule):
    target_vector = vector
    break
#
# if target rule was not found, then write an error
# message and close the file
#
if (target_vector == []):
  line = "\n\nThe target rule " + target_rule \
       + "was not found in any of the input files.\n\n"
  sorted_handle.write(line)
  sorted_handle.close()
#
# if the target rule was found, the sort all of the
# vectors by their similarity to the target rule
#
else:
  # make a list of scored tuples
  score_list = []
  # score each rule by its distance from the target rule
  for vector in vector_list:
    # calculate the distance from the target vector
    # - need to skip over first item (rule)
    dist = sfuncs.distance(target_vector[1:], vector[1:])
    # attach the distance to the beginning of the vector
    new_vector = [dist] + vector
    # add to score_list
    score_list.append(new_vector)
  #
  # sort the list in order of decreasing scores and
  # sequentially number the items in the list
  #
  # - distance: reverse=False (sort in order of increasing distance)
  #
  sorted_tuples = sorted(score_list, key=lambda x: x[0], \
                         reverse=False)
  #
  # write the list to a file
  #
  item_num = 1
  #
  for tuple in sorted_tuples:
    # add item_num to the beginning of the tuple
    new_tuple = [item_num] + tuple
    # convert items in tuple to strings, then join them with tabs
    line = "\t".join(map(str, new_tuple)) + "\n"
    # write line to file
    sorted_handle.write(line)
    # update item_num
    item_num = item_num + 1
  #
  sorted_handle.close()
  #
#
#