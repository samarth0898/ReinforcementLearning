import matplotlib.pyplot as plt 
import numpy as np

# Custom class
from mab import MAB


class bandit_viz:
    def __init__(self, bandit_probs, mab : MAB): 
        self.num_draws, self.bandit_probs = 500, bandit_probs 
        self.num_badits = len(self.bandit_probs)
        self.mab = mab

    def __bandit__(self):

        k_array = np.zeros((self.num_badits, self.num_draws))
        reward_array = np.zeros((self.num_badits, self.num_draws))

        fig, self.axs = plt.subplot(9,3,1)
        self.axs.set(xlim=(-1, self.num_draws), ylim=(-0.5, self.num_badits-0.5))

        # colors for each bandit    
        bandit_colors = ['red', 'green', 'blue', 'purple']

        self.k_list, self.reward_list = [],[]
        for draw_number in range(self.num_draws):
            # choosing arm and drawing
            k = np.random.choice(range(self.num_badits),1)[0]
            reward, regret = self.mab.draw(k)
            
            # record information about this draw
            self.k_list.append(k)
            self.reward_list.append(reward)
            k_array[k, draw_number] = 1
            reward_array[k, draw_number] = reward
      
        # getting list of colors that tells us the bandit
        self.color_list = [bandit_colors[k] for k in self.k_list]
        
        # getting list of facecolors that tells us the reward
        self.facecolor_list = [['none', bandit_colors[self.k_list[i]]][r] for i, r in enumerate(self.reward_list)]   

        # initializing with first data
        self.scatter = self.axs.scatter(y=[self.k_list[0]], x=[list(range(self.num_draws))[0]], color=[self.color_list[0]], linestyle='-', marker='o', s=30, facecolor=[facecolor_list[0]])

        # titles
        plt.title('Random draws from the row of slot machines (MAB)', fontsize=10)
        plt.xlabel('Round', fontsize=10); plt.ylabel('Bandit', fontsize=10);
        self.axs.set_yticks([0,1,2,3])
        self.axs.set_yticklabels(['{}\n($\\theta = {}$)'.format(i, self.bandit_probs[i]) for i in range(4)])
        self.axs.tick_params(labelsize=10)
        fig.tight_layout()

        # function for updating
    def animate(self,i):
        x = list(range(self.num_draws))[:i]
        y = self.k_list[:i]
        self.scatter.set_offsets(np.c_[x, y])
        self.scatter.set_color(self.color_list[:i])
        self.scatter.set_facecolor(self.facecolor_list[:i])
        self.axs.set_yticks([0,1,2,3])
        self.axs.set_yticklabels(['{}\n($\\theta = {}$)'.format(i, self.bandit_probs[i]) for i in range(4)])
        self.axs.tick_params(labelsize=10)
        return (self.scatter,)
    
    