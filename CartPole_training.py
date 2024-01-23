from ray.rllib.algorithms.ppo import PPOConfig
from ray.tune.logger import pretty_print
from log_creator import custom_log_creator
from log_checkpoint import custom_log_checkpoint

env_name = "CartPole-v1"
custom_path = "C:/Users/is12f/Documents/programming/pythonProject/trained_agent"
algo = (
    PPOConfig()
    .rollouts(num_rollout_workers=1)
    .resources(num_gpus=0)
    .environment(env=env_name)
    .framework("torch")
    .evaluation(evaluation_num_workers=1)
    .build()
    # .build(logger_creator=custom_log_creator(custom_path, env_name))
)

for i in range(1):
    result = algo.train()
    print(pretty_print(result))


'''
need to make a function or use custom_log_creator function
to select a folder for the checkpoint result

# checkpoint_dir = custom_log_checkpoint(custom_path, env_name)
checkpoint_dir = custom_path + "/" + env_name
checkpoint_dir = algo.save(checkpoint_dir)
'''
checkpoint_dir = algo.save().checkpoint.path
print(f"Checkpoint saved in directory {checkpoint_dir}")
algo.evaluate()

