from mab import MAB
from viz import bandit_viz


from matplotlib.animation import FuncAnimation
from IPython.display import HTML

if __name__ == "__main__":
    bandit_probs = [0.35, 0.40, 0.30, 0.25]
    bandit = MAB(bandit_probs)

    # Visualizatiom 

    # viz_component = bandit_viz(bandit_probs, bandit)
    # fig = viz_component.__bandit__()
    # anim = FuncAnimation(fig, viz_component.animate, frames=viz_component.num_draws, interval=25, blit=True)
    # HTML(anim.to_html5_video())


