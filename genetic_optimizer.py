"""Reproducible rack-placement genetic optimizer with configured power limits."""

from __future__ import annotations

import logging
import math
import random
from typing import Any

logger = logging.getLogger("Planner.Genetic")


class RackOptimizer:
    """Optimize rack-to-slot assignments under a shared power-capacity limit."""

    def __init__(
        self,
        racks: list[dict[str, Any]],
        max_slots: int,
        population_size: int = 50,
        generations: int = 20,
        power_capacity_kw: float = 80.0,
        seed: int = 42,
    ) -> None:
        if not isinstance(racks, list) or not racks:
            raise ValueError("racks must be a non-empty list")
        if isinstance(max_slots, bool) or not isinstance(max_slots, int) or max_slots < 1:
            raise ValueError("max_slots must be a positive integer")
        if (
            isinstance(population_size, bool)
            or not isinstance(population_size, int)
            or population_size < 2
        ):
            raise ValueError("population_size must be at least 2")
        if isinstance(generations, bool) or not isinstance(generations, int) or generations < 1:
            raise ValueError("generations must be a positive integer")
        if (
            isinstance(power_capacity_kw, bool)
            or not isinstance(power_capacity_kw, (int, float))
            or not math.isfinite(power_capacity_kw)
            or power_capacity_kw <= 0
        ):
            raise ValueError("power_capacity_kw must be a positive finite number")
        if isinstance(seed, bool) or not isinstance(seed, int):
            raise ValueError("seed must be an integer")

        normalized = []
        for index, rack in enumerate(racks):
            if not isinstance(rack, dict):
                raise ValueError(f"rack {index} must be an object")
            power = rack.get("power_draw_kw")
            if (
                isinstance(power, bool)
                or not isinstance(power, (int, float))
                or not math.isfinite(power)
                or power < 0
            ):
                raise ValueError(f"rack {index} power_draw_kw must be finite and non-negative")
            normalized.append(dict(rack))

        self.racks = normalized
        self.max_slots = max_slots
        self.pop_size = population_size
        self.generations = generations
        self.power_capacity_kw = float(power_capacity_kw)
        self.rng = random.Random(seed)

    def _generate_chromosome(self) -> list[int]:
        """Return one slot index per rack."""
        return [self.rng.randrange(self.max_slots) for _ in self.racks]

    def _fitness(self, chromosome: list[int]) -> float:
        """Penalize overloads and prefer balanced utilization across slots."""
        if len(chromosome) != len(self.racks):
            raise ValueError("chromosome length must match rack count")
        if any(
            isinstance(slot, bool) or not isinstance(slot, int) or not 0 <= slot < self.max_slots
            for slot in chromosome
        ):
            raise ValueError("chromosome contains an invalid slot index")

        slot_power = [0.0] * self.max_slots
        for rack, slot in zip(self.racks, chromosome):
            slot_power[slot] += float(rack["power_draw_kw"])

        utilization_penalty = sum(
            (power / self.power_capacity_kw) ** 2 for power in slot_power
        )
        overload_penalty = sum(
            1000.0 + 100.0 * (power - self.power_capacity_kw) / self.power_capacity_kw
            for power in slot_power
            if power > self.power_capacity_kw
        )
        return -(utilization_penalty + overload_penalty)

    def run(self) -> list[int]:
        """Return the best assignment; repeated instances with the same seed reproduce it."""
        logger.info("Running genetic optimizer for rack placement...")
        population = [self._generate_chromosome() for _ in range(self.pop_size)]
        survivor_count = max(2, int(self.pop_size * 0.2))

        for _ in range(self.generations):
            population.sort(key=self._fitness, reverse=True)
            survivors = population[:survivor_count]
            next_generation = list(survivors)
            while len(next_generation) < self.pop_size:
                parent = self.rng.choice(survivors)
                child = parent.copy()
                mutation_index = self.rng.randrange(len(child))
                child[mutation_index] = self.rng.randrange(self.max_slots)
                next_generation.append(child)
            population = next_generation

        population.sort(key=self._fitness, reverse=True)
        best = population[0]
        logger.info("Optimization complete. Best fitness: %.4f", self._fitness(best))
        return best
