"""Regression tests for reproducible rack placement optimization."""

from __future__ import annotations

import unittest

from genetic_optimizer import RackOptimizer


class RackOptimizerTests(unittest.TestCase):
    def setUp(self):
        self.racks = [
            {"id": "A", "power_draw_kw": 35.0},
            {"id": "B", "power_draw_kw": 30.0},
            {"id": "C", "power_draw_kw": 25.0},
            {"id": "D", "power_draw_kw": 20.0},
        ]

    def test_same_seed_reproduces_same_plan(self):
        first = RackOptimizer(self.racks, 3, seed=19).run()
        second = RackOptimizer(self.racks, 3, seed=19).run()
        self.assertEqual(first, second)

    def test_different_power_capacity_changes_fitness_baseline(self):
        plan = [0, 0, 1, 1]
        low_capacity = RackOptimizer(self.racks, 2, power_capacity_kw=40.0)
        high_capacity = RackOptimizer(self.racks, 2, power_capacity_kw=100.0)
        self.assertLess(low_capacity._fitness(plan), high_capacity._fitness(plan))

    def test_plan_has_one_valid_slot_per_rack(self):
        optimizer = RackOptimizer(self.racks, 2, seed=7)
        plan = optimizer.run()
        self.assertEqual(len(plan), len(self.racks))
        self.assertTrue(all(0 <= slot < 2 for slot in plan))

    def test_rejects_empty_racks_and_invalid_slots(self):
        with self.assertRaises(ValueError):
            RackOptimizer([], 2)
        with self.assertRaises(ValueError):
            RackOptimizer(self.racks, 0)

    def test_rejects_invalid_power_value(self):
        with self.assertRaises(ValueError):
            RackOptimizer([{"power_draw_kw": float("nan")}], 2)


if __name__ == "__main__":
    unittest.main()
