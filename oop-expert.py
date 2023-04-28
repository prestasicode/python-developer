def count_living_per_year(population: list[tuple[int, int]] -> dict[int, int]:
                          births = collections.Counter(birth for birth, _ in population)
                          deaths = collections.Counter(death for _, death in population)
                          living_per_year = births
                          for year in range(min(births), max(deaths)):
                              living_per_year[year] += living_per_year[year - 1] - deaths[year]
                          return living_per_year
