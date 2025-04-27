# cybershuttle-project

# Running the project locally
- Simply run resnetRunner.ipynb
- The notebook should handle downloading the model and any related dependencies

# Running the Model on HPC
### Step 1: Make the following changes in local2remote.ipynb, replacing gburdell3 with your own GT username:
```
username = "gburdell3"
remote_host = "login-ice.pace.gatech.edu"
remote_path = "/home/hice1/gburdell3/cybershuttle_project"
```
### Step 2: Add your SSH key (if you haven't done this already) to ICE to ensure passwordless login
- Run `ssh-keygen -t rsa` on your local machine to generate an SSH key
- Run `ssh-copy-id gburdell3@login-ice.pace.gatech.edu`, replacing gburdell3 with your own GT username
- Run local2remote.ipynb

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

Run "squeue -u gburdell3" to check your job (replace it with your GT username) -->