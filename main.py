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
    print 'Usage: python main.py input-file output-file'
  else:
    inputfile = open(sys.argv[1])
    strings = get_strings(inputfile)

    # set up sort function names and functions
    sort_fns_keys = ['bubblesort', 'mergesort', 'quicksort', 'radixsort']
    
    sort_fns = {
      'bubblesort': bubblesort, 
      'mergesort': mergesort, 
      'quicksort': quicksort, 
      'radixsort': radixsort
    }

    for n in algorithms.sort_fns.keys():
      name = n
      if sort_fns.has_key(n):
        name = n + '2'
      sort_fns[name] = algorithms.sort_fns[n]
      sort_fns_keys.append(name)

    # output format:
    # 1) sort_function1  2) sort_function2  3) sort_function3  4) sort_function4
    print 'Which sorting algorithm would you like?'
    s = ''
    for i in range(0, len(sort_fns_keys)):
      s += '%d) %s\n' % (i + 1, sort_fns_keys[i])
    print s

    option = None
    while option is None or (option > len(sort_fns_keys) or option < 1):
      sorting_method = raw_input('Enter an option number: ')
      try:
        option = int(sorting_method)
        if option < 1 or option > len(sort_fns_keys):
          raise ValueError('Option out of range')
      except ValueError:
        print 'Invalid input %s. Please enter the integer before each option.' % sorting_method
 
    key = sort_fns_keys[option - 1]
    module = sort_fns[key]

    # Fullhouse's sort functions do not return sorted result, instead they manipulate the input list
    if option > 4:
      results = strings
      module(results)
    else:
      results = module.sort(strings)

    outputfile = open(sys.argv[2], 'w+')
    for item in results:
      outputfile.write('%s\n' % item)

    print 'Sorting with \'%s\' successfully.\n' % key
    inputfile.close()
    outputfile.close()
