import os, random, time, shlex, subprocess, logging

logging.basicConfig(level=logging.INFO)
print("🚀 Generating Massive Assets...")

# 1. 5MB 더미 로그
with open("logs/firewall_traffic.csv", "w") as f:
    f.write("timestamp,src,dst,action,payload\n")
    for i in range(50000):
        f.write(f"{time.time()},192.168.1.{i%255},10.0.0.1,ALLOW,{'A'*100}\n")

# 2. 5MB 바이너리 덤프
with open("pcap_dumps/capture.pcap", "wb") as f:
    f.write(os.urandom(5 * 1024 * 1024))

# 3. CodeQL 대응 보안 플레이북 (Command Injection 방지 패턴)
playbooks = ["ransomware_defense", "network_analysis", "user_lockout"]
for pb in playbooks:
    with open(f"playbooks/{pb}.py", "w") as f:
        f.write("import logging\nimport subprocess\nimport shlex\n\n")
        f.write(f"def run_{pb}(target):\n")
        f.write("    # [Security] Validate Input\n")
        f.write("    if not target.isalnum(): return\n")
        f.write("    # [Security] Safe Execution\n")
        f.write("    cmd = shlex.split(f'echo Running {pb} on {target}')\n")
        f.write("    subprocess.run(cmd, shell=False)\n")

print("✅ Assets Generated.")
