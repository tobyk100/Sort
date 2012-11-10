from url_normalize import url_normalize

class URL:
  def __init__(self, url):
    self.url = url
    self.normalized = url_normalize(url)

  def isValid(self):
    return self.url == self.normalized

  def getNormalized(self):
    return self.normalized

  def __len__(self):
    return len(self.url)

  def __getitem__(self, index):
    return self.url[index]

  # Comparison using normalized url
  def __lt__(self, other):
    return self.normalized < other.normalized

  def __gt__(self, other):
    return self.normalized > other.normalized

  def __eq__(self, other):
    return self.normalized == other.normalized
