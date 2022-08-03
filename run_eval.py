import os 

for _ in range(10):
    os.system("python3.7 train.py --algo sac --env AntBulletEnv-v0 -f control")
