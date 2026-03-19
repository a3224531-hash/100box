import unittest
from simulator import PrisonersSimulator

class TestPrisonersSimulator(unittest.TestCase):
    def test_random_strategy(self):
        sim = PrisonersSimulator(num_prisoners=10)
        
        # Test success case
        boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # Random strategy might fail even with sorted boxes since it picks randomly.
        # So we can't easily force a success without mocking random.
        
        # Let's just run 1000 simulations and ensure success % is around the expected mathematical value
        # For random strategy, probability is exactly (1/2)^100 which is ~0.
        # For N=10, it's (1/2)^10 = 1/1024 ~ 0.1%
        res = sim.run_simulations('random', 1000)
        self.assertTrue(res['successes'] < 50) # Very unlikely to exceed 50
        
    def test_cycles_strategy(self):
        sim = PrisonersSimulator(num_prisoners=100)
        
        # Test 1000 simulations, cycles should hold ~31.18% success rate
        res = sim.run_simulations('cycles', 2000)
        
        # 31.18% of 2000 is ~623. We allow a comfortable margin 500-750.
        self.assertTrue(500 < res['successes'] < 750, f"Expected successes around 623, got {res['successes']}")
        
    def test_cycle_exact(self):
        sim = PrisonersSimulator(num_prisoners=4)
        # max_attempts = 2
        
        # All cycles <= 2 length
        boxes1 = [2, 1, 4, 3] 
        self.assertTrue(sim.play_cycle_strategy(boxes1))
        
        # A cycle of length 3: 1->2->3->1, 4->4
        # Prisoner 1, 2, 3 will fail because max_attempts is 2.
        boxes2 = [2, 3, 1, 4]
        self.assertFalse(sim.play_cycle_strategy(boxes2))

if __name__ == '__main__':
    unittest.main()
