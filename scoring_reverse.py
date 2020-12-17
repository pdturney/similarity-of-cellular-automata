#
# Scoring Reverse
#
# Peter Turney, December 7, 2020
#
# For each rule, find its reversal.
#
import scoring_functions as sfuncs
#
# open a file for storing the unpacked rules
#
rule_file_name = "reverse_rules.txt"
rule_file_handle = open(rule_file_name, "w")
#
# make a list of B/S rules (born/survive -- outer-totalistic)
#
rules_list = sfuncs.all_BS_rules()
#
# write expanded_list to the file
#
item_num = 1
#
for rule in rules_list:
  # find the reverse rule
  reverse_rule = sfuncs.reverse(rule)
  # list of things we want to print
  print_list = [item_num, rule, reverse_rule]
  # convert items in tuple to strings, then join them with tabs
  line = "\t".join(map(str, print_list)) + "\n"
  # write line to file
  rule_file_handle.write(line)
  # update item_num
  item_num = item_num + 1
#
# close file
#
rule_file_handle.close()
#