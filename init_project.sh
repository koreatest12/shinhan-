#!/bin/bash

# 1. 디렉토리 구조 생성
mkdir -p .github/workflows
mkdir -p playbooks
mkdir -p detections
mkdir -p templates
mkdir -p tests
mkdir -p scripts

# 2. 예시 SOAR 플레이북 생성 (Python) - Flake8 및 Bandit 통과용
cat <<EOF > playbooks/phishing_response.py
"""
Phishing Response Playbook
"""
import logging

logging.basicConfig(level=logging.INFO)

def block_sender(sender_email):
    """
    Simulates blocking a sender email address.
    """
    if "@malicious.com" in sender_email:
        logging.info(f"Blocking malicious sender: {sender_email}")
        return True
    logging.info(f"Sender {sender_email} is safe.")
    return False

if __name__ == "__main__":
    block_sender("attacker@malicious.com")
EOF

# 3. 예시 Splunk 탐지 룰 생성 (SPL) - 검증 통과용
cat <<EOF > detections/brute_force.spl
index=security sourcetype=access_combined action=failure
| stats count by src_ip
| where count > 100
EOF

# 4. 예시 Jinja2 템플릿 생성
cat <<EOF > templates/report.j2
Incident Report: {{ incident_id }}
Severity: {{ severity }}
EOF

# 5. SPL 검증 스크립트 생성 (scripts/validate_spl.py)
cat <<EOF > scripts/validate_spl.py
import sys
import os
import re

def check_spl_safety(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    errors = []
    if re.search(r'\bdelete\b', content, re.IGNORECASE):
        errors.append("CRITICAL: 'delete' command found.")
    if not re.search(r'index\s*=', content, re.IGNORECASE):
        errors.append("WARNING: No 'index=' specified.")
    return errors

def main():
    target_dir = sys.argv[1]
    has_error = False
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".spl"):
                issues = check_spl_safety(os.path.join(root, file))
                if any("CRITICAL" in i for i in issues):
                    has_error = True
    if has_error:
        sys.exit(1)

if __name__ == "__main__":
    main()
EOF

# 6. 모의해킹 테스트 스크립트 생성 (tests/simulation_attack.py)
cat <<EOF > tests/simulation_attack.py
import pytest
from playbooks.phishing_response import block_sender

def test_phishing_block():
    # 시나리오: 악성 메일 주소 입력 시 차단 기능 동작 확인
    result = block_sender("hacker@malicious.com")
    assert result is True

def test_safe_sender():
    # 시나리오: 정상 메일 주소 입력 시 차단하지 않음
    result = block_sender("user@company.com")
    assert result is False
EOF

echo "✅ 프로젝트 파일 및 구조 생성 완료!"
