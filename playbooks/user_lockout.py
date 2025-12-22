import logging
import subprocess
import shlex

def run_user_lockout(target):
    # [Security] Validate Input
    if not target.isalnum(): return
    # [Security] Safe Execution
    cmd = shlex.split(f'echo Running {pb} on {target}')
    subprocess.run(cmd, shell=False)
