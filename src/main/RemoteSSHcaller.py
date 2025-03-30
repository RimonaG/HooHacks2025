# This is what your GUI will use to call the server

import subprocess

def analyze_image(file_path):
    remote_path = "/u/cna8eg/hoohacks/HooHacks2025/images/input.jpg"

    # Step 1: Upload image to the server
    subprocess.run([
        "scp", file_path, f"cna8eg@gpusrv01.cs.virginia.edu:{remote_path}"
    ])

    # Step 2: Run emotion detection remotely
    result = subprocess.run([
        "ssh", "cna8eg@gpusrv01.cs.virginia.edu",
        f"python3 /u/cna8eg/hoohacks/HooHacks2025/src/main/run_analysis.py {remote_path}"
    ], capture_output=True, text=True)

    # Step 3: Get the emotion result
    emotion = result.stdout.strip()
    print("Detected emotion:", emotion)
    return emotion
