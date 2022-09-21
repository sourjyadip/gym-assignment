import gym 
import matplotlib.pyplot as plt  
from frozen_lake import FrozenLakeEnv

env2 = FrozenLakeEnv()

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

def random_policy():
    return env2.action_space.sample()

V = {}
for s in range(env2.observation_space.n):
    V[s] = 0.0

alpha = 0.85
gamma = 0.90
num_episodes = 5000
num_timesteps = 1000

#for each episode
for i in range(num_episodes):
    
    #initialize the state by resetting the environment
    s = env2.reset()
    
    #for every step in the episode
    for t in range(num_timesteps):
        
        #select an action according to random policy
        a = random_policy()
        
        #perform the selected action and store the next state information
        s_, r, done, _ = env2.step(a)
        
        #compute the value of the state
        V[s] += alpha * (r + gamma * V[s_]-V[s])
        
        #update next state to the current state
        s = s_
        
        #if the current state is the terminal state then break
        if done:
            break

values = []
values =  list(V.items())
#print(values)

for i in range(len(values)):
    print(i)
    print(values[i])

#env2.close()
