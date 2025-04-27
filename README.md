# cybershuttle-project





<!-- This is manual way -->
<!-- Log in into Georgia tech ICE by running "ssh gburdell3@login-ice.pace.gatech.edu" then provide your password

Then make a new directory by "mkdir cybershuttle_project" in the root directory of your ICE(You should call this command inside ICE)

RUN "scp run_model.py input.png job_script.sh zyan319@login-ice.pace.gatech.edu:/home/hice1/zyan319/cybershuttle_project/" to upload your script and data to ICE using scp

SSH into ICE again: by running "ssh zyan319@login-ice.pace.gatech.edu"

Cd into your folder by "cd cybershuttle_project"


Before submit the job, make sure you create a venv with all the python package needed for the project
"module load python/3.10
python -m venv myenv
source myenv/bin/activate
pip install --upgrade pip
pip install torch torchvision transformers pillow
"

Submit your job by "sbatch job_script.sh" then you should be seeing something like Submitted batch job 2539899

Run "squeue -u zyan319" to check your job(replace it with your GTID) -->

For Part 2:

make sure you change username to your GTID in local2remote.ipynb
username = "zyan319"
remote_host = "login-ice.pace.gatech.edu"
remote_path = "/home/hice1/zyan319/cybershuttle_project"

Using this to use the local to remote pipline:

SSH key setup by running "ssh-keygen -t rsa" to generate SSH key this avoid needing a password to login in ICE
then run "ssh-copy-id zyan319@login-ice.pace.gatech.edu"

after you have done, this simply run local2remote.ipynb