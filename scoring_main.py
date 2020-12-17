#
# Scoring Main
#
# Peter Turney, December 4, 2020
#
# Find a way to score the 2**18 possible outer-totalistic 
# automata rules, such that the Game of Life (and hopefully
# other universal cellular automata) gets a high score.
#
# https://www.conwaylife.com/wiki/List_of_Life-like_cellular_automata
#
import golly as g
import random as rand
import scoring_functions as sfuncs
import scoring_parameters as sparams
#
# name of file with a list of rules and CPUs
#
rule_file_name = sparams.rule_file_name
#
# density range for initial random matrix
#
density_range = sparams.density_range
#
# width and height for initial random square matrix
#
initial_size = sparams.initial_size
#
# number of steps for given run of simulation
#
num_steps = sparams.num_steps
#
# number of samples to collect from each run
#
num_samples = sparams.num_samples
#
# number of random trials to evaluate
#
num_trials = sparams.num_trials
#
# prepare log file for recording statistics
#
# - use option 0 so that log file writes immediately (no buffer), 
#   in case of forced exit (crash)
#
log_path = sparams.log_path
log_handle = open(log_path, "w", 0)
#
# find the CPU id for the current run
#
current_cpu_id = sparams.current_cpu_id
#
# read the rule list and extract rules that match the current
# run's CPU id
#
rule_list = sfuncs.tsv_BS_rule_cpu(rule_file_name, current_cpu_id)
#
# Golly screen magnification
#
screen_mag = sparams.screen_mag
#
# initialize Golly
#
g.setalgo("QuickLife") # select the algorithm for Golly
g.autoupdate(False) # do not update the view unless requested
g.new("Signatures") # create an empty universe
g.setmag(screen_mag) # screen magnification
#
# show parameter settings in the log file
#
parameter_settings = sfuncs.show_parameters()
log_handle.write("\nParameter Settings\n\n")
for setting in parameter_settings:
  log_handle.write(setting + "\n")
log_handle.write("\n")
#
# -------------------------------------------------
# main loop: iterate through the list of rules
# -------------------------------------------------
#
for rule in rule_list:
  #
  # keep two lists, one for even time steps and one for odd 
  # time steps -- these will be merged later
  #
  # we separate these two lists because their sample sizes might
  # not be the same, because we skip over zero vectors, because
  # zero vectors might distort the statistics
  # 
  even_vec_list = []
  odd_vec_list = []
  #
  for trial in range(num_trials):
    # initialize Golly
    g.new("Signatures") # make a new, empty Golly universe
    g.setmag(screen_mag) # screen magnification
    g.setrule(rule) # set the rule that Golly will use
    g.show("running ...")
    offset = int(initial_size / 2) # this centers the matrix in the display
    # write initial matrix into the Golly universe
    density = rand.uniform(density_range[0], density_range[1]) 
    for x in range(initial_size):
      for y in range(initial_size):
        if (rand.uniform(0, 1) <= density):
          g.setcell(x - offset, y - offset, 1) # set cell to 1
    # run Golly for num_steps
    g.run(num_steps) 
    g.update() # update the Golly display
    # get a list of all live cells in generation num_steps (n0)
    boundary_n0 = g.getrect()
    cell_list_n0 = g.getcells(boundary_n0)
    # move forward one generation
    g.run(1)
    g.update()
    # get a list of all live cells in generation num_steps + 1 (n1)
    boundary_n1 = g.getrect()
    cell_list_n1 = g.getcells(boundary_n1)
    # calculate a semantic vector elements from the 
    # two lists of live cells
    even_vec = sfuncs.semantic_vector(boundary_n0, cell_list_n0, \
                                      boundary_n1, cell_list_n1, \
                                      num_samples)
    # add even_vec to even_vec_list
    even_vec_list.append(even_vec)
    # move forward one more generation
    g.run(1)
    g.update()
    # get a list of all live cells in generation num_steps + 2 (n2)
    boundary_n2 = g.getrect()
    cell_list_n2 = g.getcells(boundary_n2)
    # calculate another semantic vector elements from the 
    # two lists of live cells
    odd_vec = sfuncs.semantic_vector(boundary_n1, cell_list_n1, \
                                     boundary_n2, cell_list_n2, \
                                     num_samples)
    # add odd_vec to odd_vec_list
    odd_vec_list.append(odd_vec)
    #
    # end of trial loop
    #
  #
  # calculate averages for sem_vec_list
  #
  avg_even_vec = sfuncs.avg_sem_vec(even_vec_list)
  avg_odd_vec = sfuncs.avg_sem_vec(odd_vec_list)
  #
  # merge the two averages
  #
  avg_sem_vec = avg_even_vec + avg_odd_vec
  #
  # sanity check
  #
  assert len(avg_sem_vec) == sparams.double_vec_len
  #
  # report some statistics
  #
  row = [rule] + avg_sem_vec
  format_row = "\t".join(map(str, row)) + "\n"
  log_handle.write(format_row)
  #
  # end of rule loop
  #
#
# close log file
#
g.show("Done!")
log_handle.write("\nDone!\n")
log_handle.close()
# 
#