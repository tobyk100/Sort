"""

  The main function. Assume all characters are in ASCII.

"""

import sys, random
import quicksort, bubblesort, mergesort, radixsort

from full_house import algorithms

def get_strings(f):
  strings = []
  line = f.readline()
  while len(line) > 0:
    # do not add empty line
    if len(line) > 1:
      strings.append(line[:len(line) - 1])
    line = f.readline()
  return strings

if __name__ == "__main__":

  filename = None
  if len(sys.argv) < 3:
    print 'Usage: python main.py input-file output-file [--fullhouse]'
  else:
    inputfile = open(sys.argv[1])
    strings = get_strings(inputfile)

    use_module_sort_function = (len(sys.argv) == 4 and sys.argv[3] == '--fullhouse')
    sort_fns = {
      'bubblesort': bubblesort, 
      'mergesort': mergesort, 
      'quicksort': quicksort, 
      'radixsort': radixsort
    }
    if use_module_sort_function:
      sort_fns = algorithms.sort_fns
    sort_fns_keys = list(sort_fns.keys())

    # output format:
    # 1) sort_function1  2) sort_function2  3) sort_function3  4) sort_function4
    print 'Which sorting algorithm would you like?'
    s = ''
    for i in range(1, 5):
      s += '%d) %s  ' % (i, sort_fns_keys[i - 1])
    print s

    option = None
    while option is None or (option > 4 or option < 1):
      sorting_method = raw_input('Enter an option number: ')
      try:
        option = int(sorting_method[:1])
        if option <= 0 or option > 4: raise ValueError('Option out of range')
      except ValueError:
        print 'Invalid input %d. Please enter the integer before each option.' % option
 
    key = sort_fns_keys[option - 1]
    module = sort_fns[key]
    if use_module_sort_function:
      results = strings
      module(results)
    else:
      results = module.sort(strings)

    outputfile = open(sys.argv[2], 'w+')
    for item in results:
      outputfile.write('%s\n' % item)

    print 'Sorting with \'%s\' successfully.' % key
    inputfile.close()
    outputfile.close()
