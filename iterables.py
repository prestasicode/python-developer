#Iterable classes define an __iter__ and a __next__ method
class MyIterable:
  def __iter__(self):
    return self
  def __next__(self):

    
class MySequence:
  def __getitem__(self, index):
    if (condition):
      raise IndexError
     return (item)
