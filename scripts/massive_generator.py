import os
import random
import string
import time

print("🚀 Starting MB-Scale Generation...")

# A. 대용량 방화벽 정책 및 로그 생성 (CSV - 약 5MB 목표)
print("  - Generating Massive Firewall Logs (CSV)...")
with open("logs/firewall_traffic_massive.csv", "w") as f:
    f.write("timestamp,src_ip,dst_ip,port,action,protocol,rule_id,payload_sample\n")
    for i in range(50000):  # 5만 라인 생성
        ts = time.time()
        src = f"192.168.{random.randint(0,255)}.{random.randint(0,255)}"
        dst = f"10.0.{random.randint(0,255)}.{random.randint(0,255)}"
        action = random.choice(["ALLOW", "DENY", "DROP", "ALERT"])
        payload = ''.join(random.choices(string.ascii_letters, k=50))
        f.write(f"{ts},{src},{dst},443,{action},TCP,RULE-{i},{payload}\n")

# B. 대용량 PCAP 더미 데이터 (Binary - 약 5MB 목표)
print("  - Generating Dummy PCAP Dumps (Binary)...")
with open("pcap_dumps/network_capture.pcap", "wb") as f:
    # 더미 바이너리 데이터 5MB 쓰기
    f.write(os.urandom(5 * 1024 * 1024))

# C. Playbooks (Python 코드 - CodeQL 분석 대상)
print("  - Generating Security Playbooks...")
playbooks = [
    "phishing_response", "ransomware_defense", "db_integrity_check", 
    "user_account_lockout", "network_traffic_analysis", "ddos_mitigation",
    "api_vulnerability_scan", "compliance_audit_log", "vpn_access_control",
    "ssh_session_monitor", "endpoint_isolation_procedure", "cloud_iam_audit"
]
for pb in playbooks:
    with open(f"playbooks/{pb}.py", "w") as f:
        f.write("import logging\nimport os\nimport subprocess\n")
        f.write("logging.basicConfig(level=logging.INFO)\n\n")
        f.write(f"def execute_{pb}():\n")
        f.write(f"    '''Auto-generated playbook for {pb}'''\n")
        f.write(f"    logging.info('🛡️ Running Security Protocol: {pb}')\n")
        f.write("    # Simulated logic\n")
        f.write("    if os.environ.get('DEBUG'):\n")
        f.write("        print('Debug mode')\n")
        f.write("    return 'SUCCESS'\n\n")
        f.write("if __name__ == '__main__':\n")
        f.write(f"    execute_{pb}()\n")

# D. SPL 탐지 룰 (대량 생성)
print("  - Generating Detection Rules (SPL)...")
for i in range(100):
    with open(f"detections/rule_{i}_generated.spl", "w") as f:
        f.write(f"index=security sourcetype=access_combined | search status=50{i%5} | stats count by src_ip")

print("✅ Massive Generation Complete.")
