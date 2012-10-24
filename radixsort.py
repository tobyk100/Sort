NUM_BUCKETS = 256

def sort(strings):
  """
  create list of 256 empty lists
  get number of passes by iterating through input list and taking max
  for i = 0 to i < pass
    for each url
      if url.length - i < 0 
        put into 0th bucket
      else
        hash each url into bucket based on length - ith char
      collect buckets into new list
  return collected buckets
  """
  buckets = list([] for i in range(0, NUM_BUCKETS));
  maxlength = max(map(len, strings))
  for i in range(1, maxlength):
    for url in strings:
      if (len(url) - i) < 0:
        buckets[0].append(url)
      else:
        char = ord(url[len(url) - i])
        buckets[char].append(url)
    strings = []
    for bucket in buckets:
      strings.extend(bucket)
    buckets = list([] for i in range(0, NUM_BUCKETS));
  return strings 
