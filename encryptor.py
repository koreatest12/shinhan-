import os
from cryptography.fernet import Fernet
import base64

# Key Generation (In real ops, use Secrets)
# derive key from fixed seed for demo or generate random
key = Fernet.generate_key()
cipher = Fernet(key)

# Save Key (Simulated Secure Storage)
with open("encrypted_vault/master_key.key", "wb") as f:
    f.write(key)

src_dir = "raw_assets"
dst_dir = "encrypted_vault"

for root, dirs, files in os.walk(src_dir):
    for file in files:
        file_path = os.path.join(root, file)
        with open(file_path, "rb") as f:
            data = f.read()
        
        encrypted_data = cipher.encrypt(data)
        
        # Create path structure
        rel_path = os.path.relpath(root, src_dir)
        dest_folder = os.path.join(dst_dir, rel_path)
        os.makedirs(dest_folder, exist_ok=True)
        
        # Save as .enc file
        dest_path = os.path.join(dest_folder, file + ".enc")
        with open(dest_path, "wb") as f:
            f.write(encrypted_data)
        print(f"🔒 Encrypted: {file} -> {file}.enc")
