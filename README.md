## Project Overview

- **Milestone 2.1**: Simplified the AI model workflow for non-expert users
- **Milestone 2**: Connected local execution to ICE HPC using SSH and SLURM
- **Milestone 3**: Packaged the model into a deployable app via Cybershuttle Sandbox

## Repository Structure

```
CYBERSHUTTLE-PROJECT/
├── .gitignore                # Git ignore file
├── cybershuttle.yml           # Deployment config for Cybershuttle
├── job_script.sh              # SLURM batch job script
├── local2remote.ipynb         # Automated local-to-remote execution notebook
├── README.md                  # Project guide (this file)
├── resnetRunner.ipynb         # Final packaged Jupyter app for Cybershuttle
└── run_model.py               # Model script for running on ICE HPC
```
This project extends an AI model to be **user-friendly, scalable, and remotely executable** on Georgia Tech ICE HPC via the Cybershuttle platform.

## Running the project locally
- Simply run resnetRunner.ipynb
- The notebook should handle downloading the model and any related dependencies


<!-- This is manual way -->
<!-- Log in into Georgia tech ICE by running "ssh gburdell3@login-ice.pace.gatech.edu" then provide your password

Then make a new directory by "mkdir cybershuttle_project" in the root directory of your ICE(You should call this command inside ICE)

RUN "scp run_model.py input.png job_script.sh gburdell3@login-ice.pace.gatech.edu:/home/hice1/gburdell3/cybershuttle_project/" to upload your script and data to ICE using scp

SSH into ICE again: by running "ssh gburdell3@login-ice.pace.gatech.edu"

Cd into your folder by "cd cybershuttle_project"


Before submit the job, make sure you create a venv with all the python package needed for the project
"module load python/3.10
python -m venv myenv
source myenv/bin/activate
pip install --upgrade pip
pip install torch torchvision transformers pillow
"

Submit your job by "sbatch job_script.sh" then you should be seeing something like Submitted batch job 2539899
 -->

## Running the Model on HPC

### 1. Using Airavata (Recommended for online images)
Run airavataRunner.ipynb one cell at a time. Make sure to follow all prompts as needed and input the link to the image you want classified at the bottom of the final cell.

### 2. Automated Pipeline (Recommended for local images)

**Step 1**: Edit `local2remote.ipynb`
```python
username = "your_GTID"
remote_host = "login-ice.pace.gatech.edu"
remote_path = "/home/hice1/your_GTID/cybershuttle_project"
```

**Step 2**: Setup SSH Key for passwordless login
```bash
ssh-keygen -t rsa
ssh-copy-id [your_GTID]@login-ice.pace.gatech.edu
```

**Step 3**: Run all cells in `local2remote.ipynb` to automate file transfer, environment setup, and job submission.

### 3. Manual Remote Execution

**Step 1**: SSH into ICE
```bash
ssh [your_GTID]@login-ice.pace.gatech.edu
```

**Step 2**: Create a project directory
```bash
mkdir cybershuttle_project
```

**Step 3**: Upload scripts and inputs
```bash
scp run_model.py job_script.sh [your_GTID]@login-ice.pace.gatech.edu:/home/hice1/[your_GTID]/cybershuttle_project/
```

**Step 4**: Set up the environment on ICE
```bash
module load python/3.10
python -m venv myenv
source myenv/bin/activate
pip install --upgrade pip
pip install torch torchvision transformers pillow
```

**Step 5**: Submit the SLURM job
```bash
sbatch job_script.sh
```

Check job status:
```bash
squeue -u [your_GTID]
```


<!-- For Part 2:

make sure you change username to your GTID in local2remote.ipynb
username = "zyan319"
remote_host = "login-ice.pace.gatech.edu"
remote_path = "/home/hice1/zyan319/cybershuttle_project"

Using this to use the local to remote pipline:

SSH key setup by running "ssh-keygen -t rsa" to generate SSH key this avoid needing a password to login in ICE
then run "ssh-copy-id zyan319@login-ice.pace.gatech.edu"

after you have done, this simply run local2remote.ipynb -->

---


## Credits

- Developed for Georgia Tech CS /VIP PACE Cybershuttle Project 2.

# 🚀 Let's Launch It!
