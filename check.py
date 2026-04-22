import gymnasium as gym
import mujoco
import numpy as np

# 1. CREATE THE ENVIRONMENT
# 'Ant-v5' is a classic MuJoCo robot that learns to walk
env = gym.make('Ant-v5', render_mode="human")

# 2. THE BRAIN (The Policy)
# In high-level RL, this is usually a Neural Network.
# For now, let's imagine a 'magic' function that takes state and gives actions.
def policy(observation):
    # This is where the AI "decides" what to do.
    # Someday, a trained model will replace this random action.
    return env.action_space.sample() 

# 3. THE TRAINING LOOP
epochs = 10
for episode in range(epochs):
    observation, info = env.reset()
    score = 0
    terminated = False
    truncated = False

    while not (terminated or truncated):
        # A: Agent looks at the robot's position/velocity
        action = policy(observation)

        # B: Agent performs action in MuJoCo
        observation, reward, terminated, truncated, info = env.step(action)
        
        # C: Keep track of how well the robot is doing
        score += reward

    print(f"Episode {episode+1} finished with Score: {score:.2f}")

env.close()