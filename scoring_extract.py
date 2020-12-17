#
# Scoring Extract
#
# Peter Turney, December 13, 2020
#
# The goal here is to extract a sample of the scores
# suitable for making a nice graph. If we use all
# 262,144 scores, the graph file will be much larger
# than necessary. Instead, we sample the rows in steps
# of 1000: 1, 1001, 2001, ..., 262,001.
#
import scoring_parameters as sparams
#
# input file name
#
in_file_name = sparams.sorted_file_name
#
# output file name
#
out_file_name = "extract-" + in_file_name
#
# open files
#
in_file_handle = open(in_file_name, "r")
out_file_handle = open(out_file_name, "w")
#
# extract every 1000th line
#
for line in in_file_handle:
  # split line on tabs
  tuple = line.rstrip().split("\t")
  # break out the relevant parts of the tuple
  rank = int(tuple[0])
  rule = tuple[2]
  score = float(tuple[1])
  # is the rank 1, 1001, 2001, ...?
  if (rank % 1000 == 1):
    # write to output file
    line = "\t".join(map(str, [rank, rule, score])) + "\n"
    out_file_handle.write(line)
  #
#
# close files
#
in_file_handle.close()
out_file_handle.close()
#
#