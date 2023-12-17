import numpy as np 


class MAB:
    def __init__(self, bandit_probs):
        self.bandit_probs = bandit_probs
    
    def draw(self, k): 
        """
        k : index of the bandit we want to draw from 
        """
        sample = np.random.binomial(1, self.bandit_probs[k])
        regret = np.max(self.bandit_probs) - self.bandit_probs[k] # QUESTION 
        return sample, regret