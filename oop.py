#create function -> define argument = population
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
