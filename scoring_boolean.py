#
# Scoring Boolean
#
# Peter Turney, December 13, 2020
#
# Generate 18-dimensional Boolean vectors for all
# 262,144 semi-totalistic cellular automata rules.
# Sort the list in order of increasing distance from
# a given rule (e.g., B3/S23).
#
import scoring_functions as sfuncs
#
# make a list of B/S rules (born/survive -- outer-totalistic)
#
rules_list = sfuncs.all_BS_rules()
#
# open a file for storing selected rules
#
rule_file_name = "boolean-sorted-B3-S23.txt"
rule_file_handle = open(rule_file_name, "w")
#
# target rule for sorting
#
target_rule = "B3/S23"
target_vec = sfuncs.rule_to_boole(target_rule)
#
# make a list where each element has the following form:
#
# b = born, s = survive, u = unborn, d = die
#
# <distance, rule, b0, b1, ..., b8, s0, s1, ..., s8,
#                  u0, u1, ..., u8, d0, d1, ..., d8>
#
vectors_list = []
#
for rule in rules_list:
  boole_vec = sfuncs.rule_to_boole(rule)
  dist = sfuncs.distance(boole_vec, target_vec)
  # note that each element in vectors_list will be a list
  # that mixes character strings, integers, and reals
  vectors_list.append([dist, rule] + boole_vec)
#
# sort the list in order of increasing distance
#
sorted_vec_list = sorted(vectors_list, key=lambda x: x[0], \
                         reverse=False)
#
# write the sorted list to a file
#
item_num = 1
#
for vec in sorted_vec_list:
  # add item_num to the beginning of vec
  new_vec = [item_num] + vec
  # convert items in vec to strings, then join them with tabs
  line = "\t".join(map(str, new_vec)) + "\n"
  # write line to file
  rule_file_handle.write(line)
  # update item_num
  item_num = item_num + 1
#
# close file
#
rule_file_handle.close()
#