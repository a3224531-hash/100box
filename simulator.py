import random

class PrisonersSimulator:
    def __init__(self, num_prisoners=100):
        self.num_prisoners = num_prisoners
        self.max_attempts = num_prisoners // 2

    def generate_boxes(self):
        """Generates a list of boxes containing randomly shuffled prisoner numbers."""
        boxes = list(range(1, self.num_prisoners + 1))
        random.shuffle(boxes)
        # To match prisoner 1 to index 1, we can prepend a dummy value, 
        # but using 0-indexed logic is simpler here, so boxes[0] is box 1.
        return boxes

    def play_random_strategy(self, boxes) -> bool:
        """
        Simulates one run using the Random strategy.
        Each prisoner selects up to self.max_attempts boxes uniformly at random.
        Returns True if ALL prisoners find their number, False otherwise.
        """
        for prisoner in range(1, self.num_prisoners + 1):
            success_for_prisoner = False
            
            # Prisoner picks max_attempts random, unique boxes
            chosen_boxes = random.sample(range(self.num_prisoners), self.max_attempts)
            
            for box_index in chosen_boxes:
                if boxes[box_index] == prisoner:
                    success_for_prisoner = True
                    break
            
            # If any prisoner fails, the entire game is lost
            if not success_for_prisoner:
                return False
                
        # All prisoners survived!
        return True

    def play_cycle_strategy(self, boxes) -> bool:
        """
        Simulates one run using the Cycle strategy.
        Prisoner N starts at box N-1 (0-indexed). If the number inside is not N,
        they go to the box indicated by the number inside.
        Returns True if ALL prisoners find their number, False otherwise.
        """
        for prisoner in range(1, self.num_prisoners + 1):
            success_for_prisoner = False
            current_box_index = prisoner - 1
            
            for _ in range(self.max_attempts):
                found_number = boxes[current_box_index]
                if found_number == prisoner:
                    success_for_prisoner = True
                    break
                else:
                    # The number inside dictates the next box index (0-indexed)
                    current_box_index = found_number - 1
                    
            if not success_for_prisoner:
                return False
                
        return True

    def run_simulations(self, strategy: str, num_runs: int):
        """
        Runs the simulation `num_runs` times.
        Strategy can be 'random' or 'cycles'.
        Returns a dict with statistics.
        """
        success_count = 0
        
        for _ in range(num_runs):
            boxes = self.generate_boxes()
            if strategy == 'random':
                if self.play_random_strategy(boxes):
                    success_count += 1
            elif strategy == 'cycles':
                if self.play_cycle_strategy(boxes):
                    success_count += 1
            else:
                raise ValueError("Unknown strategy")
                
        failure_count = num_runs - success_count
        success_percentage = (success_count / num_runs) * 100 if num_runs > 0 else 0
        
        return {
            "total_games": num_runs,
            "success_percentage": round(success_percentage, 2),
            "successes": success_count,
            "failures": failure_count
        }
