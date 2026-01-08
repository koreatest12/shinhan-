# [Upgrade] Using latest stable Debian Bookworm slim image
FROM python:3.12-slim-bookworm

WORKDIR /secure_vault

# Install dependencies for decryption tools
RUN pip install cryptography --no-cache-dir &&     apt-get update && apt-get install -y --no-install-recommends openssl &&     rm -rf /var/lib/apt/lists/*

# Copy ONLY Encrypted Assets
COPY encrypted_vault/ /secure_vault/

# Set permission to read-only for security
RUN chmod -R 400 /secure_vault

LABEL description="Secure Ops Vault - Encrypted Storage"
LABEL version="v2026.01.08.1057"

CMD ["python", "-c", "print('🔒 This container holds encrypted assets. Use the master key to decrypt.')"]
