# scripts/validate_spl.py
import sys
import os
import re

def check_spl_safety(file_path):
    """
    SPL 쿼리에 위험한 명령어(delete)나 비효율적인 패턴(leading wildcard)이 있는지 검사
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    errors = []
    
    # 1. 데이터 삭제 명령어 사용 금지
    if re.search(r'\bdelete\b', content, re.IGNORECASE):
        errors.append("❌ Critical: 'delete' command found. Data deletion is prohibited.")

    # 2. 인덱스 지정 없이 전체 검색 금지 (성능 이슈)
    if not re.search(r'index\s*=', content, re.IGNORECASE):
        errors.append("⚠️ Warning: No 'index=' specified. This may cause performance issues.")

    # 3. 와일드카드로 시작하는 검색 지양 (*term)
    if re.search(r'\"\*\w+', content):
        errors.append("⚠️ Warning: Leading wildcard found. Avoid '*term' for better performance.")

    return errors

def main():
    target_dir = sys.argv[1]
    has_error = False

    print(f"🔍 Starting SPL Validation in {target_dir}...")
    
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".spl"):
                full_path = os.path.join(root, file)
                issues = check_spl_safety(full_path)
                
                if issues:
                    print(f"\n[FILE] {file}")
                    for issue in issues:
                        print(issue)
                        if "Critical" in issue:
                            has_error = True
                else:
                    print(f"✅ {file} is clean.")

    if has_error:
        sys.exit(1) # 워크플로우 실패 처리

if __name__ == "__main__":
    main()
