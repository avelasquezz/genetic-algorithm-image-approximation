import random
import copy

def mate_one_point(ind1, ind2):
  size = min(len(ind1), len(ind2))
  cxpoint = random.randint(1, size - 1)

  child1 = copy.deepcopy(ind1[:cxpoint] + ind2[cxpoint:])
  child2 = copy.deepcopy(ind2[:cxpoint] + ind1[cxpoint:])
  return child1, child2

def mate_uniform(ind1, ind2, prob=0.5):
  size = min(len(ind1), len(ind2))
  child1, child2 = [], []

  for i in range(size):
    if random.random() < prob:
      child1.append(copy.deepcopy(ind2[i]))
      child2.append(copy.deepcopy(ind1[i]))
    else:
      child1.append(copy.deepcopy(ind1[i]))
      child2.append(copy.deepcopy(ind2[i]))

  return child1, child2

def mate_partial(ind1, ind2):
  size = len(ind1)
  start = random.randint(0, size // 2)
  end = random.randint(size // 2, size - 1)

  child1 = copy.deepcopy(ind1)
  child2 = copy.deepcopy(ind2)

  child1[start:end], child2[start:end] = (
    copy.deepcopy(ind2[start:end]),
    copy.deepcopy(ind1[start:end]),
  )

  return child1, child2

def mate_mixed(ind1, ind2):
  r = random.random()
  if r < 0.5:
      return mate_one_point(ind1, ind2)
  elif r < 0.8:
      return mate_uniform(ind1, ind2, prob=0.3)
  else:
      return mate_partial(ind1, ind2)
