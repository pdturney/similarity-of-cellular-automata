#
# Scoring Parmeters
#
# Peter Turney, December 13, 2020
#
# Set various parameters for running experiments
#
#
# file generated by scoring_initialize.py
#                   ---------------------
# - rows have the form <rule> <tab> <CPU>
# - each rule is randomly assigned to a CPU for 
#   parallel processing
#
rule_file_prefix = "trial-C"
#
rule_file_name = rule_file_prefix + ".txt"
#
# files generated by scoring_main.py
#                    ---------------
# - multiple files are generated, one for each CPU
# - each row is a vector corresponding to a rule
# - current_cpu_id is the ID number of the CPU to 
#   use for the current run
# - current_cpu_id ranges from 1 to num_cpus
# - num_cpus is the total number of CPUs to be used
#
current_cpu_id = 6
num_cpus = 6
#
log_path = rule_file_prefix + "-CPU" + \
           str(current_cpu_id) + ".txt"
#
# file generated by scoring_merge.py
#                   ----------------
# - one file is generated
# - the files from scoring_main.py are merged together
#   and the lines are sorted by their scores
# - scores depend on the target rule
#
target_rule = "B3/S23"
#
sorted_file_name = rule_file_prefix + "-sorted-" \
                 + target_rule.replace("/", "-") \
                 + ".txt"
#
# semantic vector lengths
#
single_vec_len = 36 # 4 groups of 9
double_vec_len = 72 # 2 groups of 4 groups of 9
#
# density range for initial random matrix
#
density_range = [0.0, 1.0]
#
# width and height for initial random square matrix
# of boolean values
#
initial_size = 16
#
# number of steps for given run of simulation
#
num_steps = 50 # this should be an even number
#
# number of samples to collect from each run
#
num_samples = 50
#
# number of trials to evaluate for each rule
#
num_trials = 1000
#
# screen magnification for Golly
#
screen_mag = 2 # mag 3 = ratio 1:8
#
#