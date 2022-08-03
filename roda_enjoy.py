import os 

exp = "HopperBulletEnv-v0"
folder = "incremental"

log_folder = os.path.join(folder,exp+"_")
timesteps = 1000_000

for id in range(14,20):
    os.system(f"python3.7 enjoy.py -f {folder} --algo sac --env {exp} --exp-id {id} --reward-log {log_folder+ str(id)} -n {timesteps} --no-render")