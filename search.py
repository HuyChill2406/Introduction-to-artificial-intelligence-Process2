import random

class LocalSearchStrategy:
    """Implements various local search strategies including hill climbing and simulated annealing."""
    def random_restart_hill_climbing(self,problem, num_trial):
        if not isinstance(num_trial, int) or num_trial <= 0:
            raise ValueError("num_trial must be a positive integer")
        """Performs random restart hill climbing and returns the best path found."""
        best_path = []
        best_evaluation = float('-inf')

        for _ in range(num_trial):
            x, y = problem.random_state()
            current_state = (x, y, int(problem.Z[y, x]))
            current_path = [current_state]
            path_evaluation = problem.Z[y, x]

            while True:
                neighbors = problem.get_neighbors(current_state)
                next_state = max(neighbors, key=lambda s: s[2], default=None)

                if not next_state or next_state[2] <= current_state[2]:
                    break

                current_state = next_state
                current_path.append(current_state)
                path_evaluation = current_state[2]

            if path_evaluation > best_evaluation:
                best_path = current_path
                best_evaluation = path_evaluation

        return best_path

    def simulated_annealing_search(self,problem, schedule):
        """Performs simulated annealing search and returns the path traversed."""
        x, y = problem.random_state()
        current = (x, y, int(problem.Z[y, x]))
        path = [current]
        time = 0
        max_iterations=1000
        for _ in range(max_iterations):
            T = schedule(time)
            if T <= 0:
                break

            neighbors = problem.get_neighbors(current)
            if not neighbors:
                break
            
            next_state = random.choice(neighbors)
            delta_e = next_state[2] - current[2]
            
            if delta_e > 0 or random.uniform(0, 1) < problem.safe_exp(delta_e / T):
                current = next_state
                path.append(current)   
                  
            time += 1
            
        return path
            
    def local_beam_search(self, problem, k):
        """Performs local beam search with full path tracking."""
        if not isinstance(k, int) or k <= 0:
            raise ValueError("k must be a positive integer")
        # Initialize 1 random state
        x, y = problem.random_state()
        initial_state = (x, y, int(problem.Z[y, x]))
        
        current_states = [initial_state]
        best_state = initial_state
        full_path = [initial_state]  # Start with the initial state
        
        while True:
            all_candidates = []
            for state in current_states:
                neighbors = problem.get_neighbors(state)
                all_candidates.extend(neighbors)
            # Select the top k unique candidates based on their Z value
            new_states = sorted(set(all_candidates), key=lambda x: x[2], reverse=True)[:k]
            
            if not new_states:
                break  # No new states to consider

            current_best = max(new_states, key=lambda x: x[2])
            if current_best[2] > best_state[2]:
                best_state = current_best
                current_states = new_states
                full_path.append(best_state)  # Update path with better state only
            else:
                break  # Break the loop if no improvement

        return full_path
