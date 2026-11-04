import random
import logging
from typing import List, Dict

logger = logging.getLogger("Planner.Genetic")

class RackOptimizer:
    """Uses a Genetic Algorithm to optimize rack placement."""
    
    def __init__(self, racks: List[Dict], max_slots: int, population_size: int = 50):
        self.racks = racks
        self.max_slots = max_slots
        self.pop_size = population_size
        self.generations = 20
        
    def _generate_chromosome(self):
        """Represents a slot assignment for each rack."""
        return [random.randint(0, self.max_slots - 1) for _ in range(len(self.racks))]
        
    def _fitness(self, chromosome: List[int]) -> float:
        """Score is based on maximizing power efficiency and avoiding overloaded slots."""
        score = 0.0
        slot_power = {i: 0.0 for i in range(self.max_slots)}
        
        for rack_idx, slot in enumerate(chromosome):
            slot_power[slot] += self.racks[rack_idx]["power_draw_kw"]
            
        for slot, power in slot_power.items():
            if power > 80.0: # Overload penalty
                score -= 1000
            else:
                score += (80.0 - power) # Reward for balancing power
                
        return score

    def run(self) -> List[int]:
        logger.info("Running Genetic Algorithm for rack placement...")
        population = [self._generate_chromosome() for _ in range(self.pop_size)]
        
        for gen in range(self.generations):
            population.sort(key=self._fitness, reverse=True)
            # Keep top 20%, mutate the rest to create new generations
            survivors = population[:int(self.pop_size * 0.2)]
            next_gen = survivors.copy()
            
            while len(next_gen) < self.pop_size:
                parent = random.choice(survivors)
                child = parent.copy()
                # Mutate
                child[random.randint(0, len(child)-1)] = random.randint(0, self.max_slots - 1)
                next_gen.append(child)
                
            population = next_gen
            
        best_plan = population[0]
        logger.info(f"Optimization complete. Best plan score: {self._fitness(best_plan):.2f}")
        return best_plan
