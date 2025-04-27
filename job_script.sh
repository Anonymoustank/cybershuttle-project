#!/bin/bash
#SBATCH --job-name=run_inference
#SBATCH --output=output.log
#SBATCH --error=error.log
#SBATCH --time=00:10:00
#SBATCH --mem=4G
#SBATCH --cpus-per-task=2
#SBATCH --gres=gpu:1

module load python/3.10

# Activate the virtual environment INSIDE cybershuttle_project
source ./myenv/bin/activate

# Run the model
python run_model.py --input input.png --output output.txt
