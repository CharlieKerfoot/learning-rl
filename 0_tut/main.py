import gymnasium as gym

def main():
    env = gym.make('CartPole-v1', render_mode="human")
    #environment objective is to balance a pole on a moving cart

    observation, info = env.reset()
    #observation - what the agent is seeing
    #info - debugging info

    episode_over = False
    total_reward = 0

    #agent-environment loop
    while not episode_over:
        action = env.action_space.sample() #basic agent -> random action
        #action: 0 = push cart left, 1 = push cart right

        observation, reward, terminated, truncated, info = env.step(action)
        #reward: +1 if pole stays upright
        #terminated: True if pole falls (agent failed)
        #truncated: True if we hit time limit

        total_reward += float(reward)
        episode_over = terminated or truncated

    print(f"Episode over. Total reward: {total_reward}")
    env.close()

if __name__ == "__main__":
    main()
