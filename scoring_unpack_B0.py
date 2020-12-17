#
# Scoring Unpack B0
#
# Peter Turney, December 4, 2020
#
# Unpack B0 rules into their two parts. Each B0 rule
# can be decomposed into two parts, an odd rule and
# an even rule. These parts are necessary (1) to avoid
# infinities and (2) to avoid annoying strobe effects.
#
# See Emulating B0 rules: 
#
# http://golly.sourceforge.net/Help/Algorithms/QuickLife.html#b0emulation
#
import scoring_functions as sfuncs
#
# open a file for storing the unpacked rules
#
rule_file_name = "unpacked_B0_rules.txt"
rule_file_handle = open(rule_file_name, "w")
#
# make a list of B/S rules (born/survive -- outer-totalistic)
#
rules_list = sfuncs.all_BS_rules()
#
# iterate through the list of B0 rules
#
expanded_list = []
#
for rule in rules_list:
  if (rule[1] == "0"):
    new_rules = sfuncs.unpack_B0(rule)
    expanded_list.append(new_rules)
#
# write expanded_list to the file
#
item_num = 1
#
for tuple in expanded_list:
  # add item_num to the beginning of tuple
  new_tuple = [item_num] + tuple
  # convert items in tuple to strings, then join them with tabs
  line = "\t".join(map(str, new_tuple)) + "\n"
  # write line to file
  rule_file_handle.write(line)
  # update item_num
  item_num = item_num + 1
#
# close file
#
rule_file_handle.close()
#