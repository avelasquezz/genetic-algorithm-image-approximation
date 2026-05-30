import random

from core.individual import random_individual 
from core.crossover  import *
from core.mutation   import *
from core.fitness    import evaluate, draw_individual 
from utils.image     import load_image, save_image
from config          import config
from deap            import base, creator, tools
from PIL             import Image

def main():
  toolbox = base.Toolbox()

  toolbox.register("individual", random_individual)
  toolbox.register("population", tools.initRepeat, list, toolbox.individual)

  toolbox.register("evaluate", evaluate)
  toolbox.register("select", tools.selTournament, tournsize=3)

  toolbox.register("mate", mate_mixed)

  toolbox.register("mutate", mutate_individual)

  population = toolbox.population(n=config["population_size"])
  NGEN = config["max_generations"]
  CXPB = config["crossover_prob"]
  MUTPB = config["mutation_prob"]

  for gen in range(NGEN + 1):
    for ind in population:
      if not ind.fitness.valid:
        ind.fitness.values = toolbox.evaluate(ind)

    offspring = toolbox.select(population, len(population))
    offspring = list(map(toolbox.clone, offspring))

    # Crossover
    for child1, child2 in zip(offspring[::2], offspring[1::2]):
      if random.random() < CXPB:
        child1[:], child2[:] = toolbox.mate(child1, child2)
        del child1.fitness.values
        del child2.fitness.values

    # Mutation 
    for mutant in offspring:
      if random.random() < MUTPB:
        mutant[:] = toolbox.mutate(mutant)[0]
        del mutant.fitness.values

    # Re-evaluate
    invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
    for ind in invalid_ind:
      ind.fitness.values = toolbox.evaluate(ind)

    # Replacement 
    population[:] = offspring

    # Progess log 
    best = tools.selBest(population, 1)[0]
    rendered = draw_individual(best)
    print(f"Gen {gen}: Best fitness = {best.fitness.values[0]:.2f}")

    if gen % 100 == 0:
      save_path = f"./output/best_gen{gen}.png"
      save_image(rendered, save_path)

  print("Evolution completed.")
  return population

if __name__ == "__main__":
  main()
