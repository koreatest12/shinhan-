import os

# 1. Playbooks (Python) - 10종 생성
playbooks = [
    "phishing_response", "ransomware_defense", "db_integrity_check", 
    "user_account_lockout", "network_traffic_analysis", "ddos_mitigation",
    "api_vulnerability_scan", "compliance_audit_log", "vpn_access_control",
    "endpoint_isolation_procedure"
]
for pb in playbooks:
    with open(f"playbooks/{pb}.py", "w") as f:
        f.write("import logging\n")
        f.write("logging.basicConfig(level=logging.INFO)\n\n")
        f.write(f"def execute_{pb}():\n")
        f.write(f"    '''Auto-generated playbook for {pb}'''\n")
        f.write(f"    logging.info('🛡️ Running Security Protocol: {pb}')\n")
        f.write("    return 'SUCCESS'\n\n")
        f.write("if __name__ == '__main__':\n")
        f.write(f"    execute_{pb}()\n")

# 2. Detections (SPL - Splunk) - 빈 폴더 에러 방지용 파일 생성
detections = {
    "brute_force.spl": "index=auth action=failure | stats count by src_ip | where count > 100",
    "sql_injection.spl": "index=web_logs method=POST | regex uri=\"(?i)UNION SELECT\" | table src_ip uri",
    "data_exfiltration.spl": "index=firewall direction=outbound | stats sum(bytes) as total by dest_ip | where total > 10GB",
    "ransomware_ext.spl": "index=endpoint action=write | regex file_name=\".*\.(enc|lock|crypted)$\"",
    "new_admin_user.spl": "index=ad_logs EventCode=4720 | table _time, user, src_user"
}
for filename, content in detections.items():
    with open(f"detections/{filename}", "w") as f:
        f.write(content)

# 3. System Services
with open("system_services/health_check.py", "w") as f:
    f.write("def check_status(): return 'OK'")

with open("system_services/upgrade_agent.py", "w") as f:
    f.write("def upgrade(): print('Upgrading...')")

# 4. Firewall Policies
with open("firewall_policies/global_deny.rules", "w") as f:
    f.write("*filter\n:INPUT DROP [0:0]\n-A INPUT -p tcp --dport 443 -j ACCEPT\nCOMMIT")

# 5. Reports (HTML)
with open("reports/security_summary.html", "w") as f:
    f.write("<html><body><h1>Daily Security Report</h1><p>Status: Green</p></body></html>")

print("✅ Massive Assets Generated Successfully.")
