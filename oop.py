#create function -> define argument = population then create conditions if else
def count_living_per_year(population: list[tuple[int, int]]) -> dict[int, int]:
  living_per_year = {}
  for birth, death in population:
    if birth in living_per_year:
      living_per_year[birth] += 1
    else:
      living_per_year[birth] = 1
    if death in living_per_year:
      living_per_year[death] -= 1
    else:
      living_per_year[death] = -1
  for year in range(min(living_per_year), max(living_per_year)):
    living_per_year[year] += living_per_year.get(year - 1, 0)
  living_per_year.pop(max(living_per_year))
  return living_per_year

#create function -> define argument = population; then using concept collections defaultdict
#define max min 
def count_living_per_year(population: list[tuple[int, int]]) -> dict[int, int]:
  living_per_year = collections.defaultdict(int)
  for birth, death in population:
    living_per_year[birth] += 1
    living_per_year[death] -= 1
  min_ , max_ = min(living_per_year), max(living_per_year)
  for year in range(min_, max_):
    living_per_year[year] += living_per_year[year - 1]
  del living_per_year[min_ - 1], living_per_year[max_])
  return living_per_year

