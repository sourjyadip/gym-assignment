import gym 
import matplotlib.pyplot as plt  

env2 = gym.make('FrozenLake8x8-v1')
'''
action_size = env2.action_space.n
state_size = env2.observation_space.n
print(f"Action Space : {action_size} | State Space: {state_size}")

env2.reset()
print("_____OBSERVATION SPACE_____ \n")
print("Observation Space", env2.observation_space)
print("Sample observation", env2.observation_space.sample()) # Get a random observation

print("\n _____ACTION SPACE_____ \n")
print("Action Space Shape", env2.action_space.n)
print("Action Space Sample", env2.action_space.sample()) # Take a random action

MAX_ITERATIONS = 10
env2.reset()
env2.render()
for i in range(MAX_ITERATIONS):
    random_action = env2.action_space.sample()
    new_state, reward, done, info = env2.step(random_action)
    env2.render()
    if done:
        break
'''
env2.reset()
env_screen = env2.render()
print(env_screen)
#env2.close()
