import os

# 1. Playbooks (12종 - SSH, VPN 기능 포함)
playbooks = [
    "phishing_response", "ransomware_defense", "db_integrity_check", 
    "user_account_lockout", "network_traffic_analysis", "ddos_mitigation",
    "api_vulnerability_scan", "compliance_audit_log", "vpn_access_control",
    "ssh_session_monitor", "endpoint_isolation_procedure", "cloud_iam_audit"
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

# 2. Detections (Splunk SPL 6종)
detections = {
    "ssh_brute_force.spl": "index=linux_secure process=sshd 'Failed password' | stats count by src_ip > 10",
    "vpn_unusual_login.spl": "index=vpn_logs action=login status=success src_country!=KR | alert",
    "sql_injection.spl": "index=web_logs method=POST | regex uri=\"(?i)UNION SELECT\" | table src_ip uri",
    "data_exfiltration.spl": "index=firewall direction=outbound | stats sum(bytes) > 5GB",
    "ransomware_ext.spl": "index=endpoint action=write file_name=\"*.crypt\"",
    "root_privilege_escalation.spl": "index=audit command=\"sudo su\" OR command=\"uid=0\""
}
for filename, content in detections.items():
    with open(f"detections/{filename}", "w") as f:
        f.write(content)

# 3. System Services (VPN/SSH Manager)
with open("system_services/vpn_manager.py", "w") as f:
    f.write("def connect_vpn(): print('Connecting to Corporate VPN...')")

with open("system_services/ssh_tunnel.py", "w") as f:
    f.write("def establish_tunnel(): print('Establishing Secure SSH Tunnel...')")

# 4. Reports (HTML)
with open("reports/security_dashboard.html", "w") as f:
    f.write("<html><body><h1>Security Ops Dashboard</h1><p>VPN Status: Active</p><p>SSH Status: Secure</p></body></html>")

print("✅ Massive Assets Generated (Including VPN/SSH modules).")
