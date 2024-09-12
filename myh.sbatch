#!/bin/bash
#SBATCH --job-name=Test #任务名 
#SBATCH --partition=cnGPUtest #partition 名 
#SBATCH -o myh%j.out #正确输出 
#SBATCH -e myh%j.err #异常输出 
#SBATCH --gres=gpu:1 #GPU 卡数 
#SBATCH --cpus-per-gpu=3 #每个 GPU 卡分配的 cpu 数目 
srun env | grep CUDA #在 Test%j.out 中看到分配到的 GPU 卡的编号 
srun python train.py
