# This is what your GUI will use to call the server

import subprocess

def analyze_image(file_path):
    remote_path = "/u/cna8eg/hoohacks/HooHacks2025/input.jpg"

    # Step 1: Upload image to the server
    subprocess.run([
        "scp", file_path, f"cna8eg@portal.cs.virginia.edu:{remote_path}"
    ])


    # Step 2: Run emotion detection remotely
    result = subprocess.run([
        "ssh", "cna8eg@portal.cs.virginia.edu",
        f"/sw/ubuntu2204/ebu082024/software/common/compiler/gcccore/13.2.0/python/3.11.5/bin/python3 /u/cna8eg/hoohacks/HooHacks2025/src/main/run_analysis.py {remote_path}"
        #f"ssh cna8eg@gpusrv01.cs.virginia.edu 'python3 /u/cna8eg/hoohacks/HooHacks2025/src/main/SSHConnector.py {remote_path}'"
    ], capture_output=True, text=True)

    print(result.stderr)

    # Step 3: Get the emotion result
    emotion = result.stdout.strip()
    print("Detected emotion:", emotion)
    return emotion
