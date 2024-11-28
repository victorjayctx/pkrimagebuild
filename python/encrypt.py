import base64
from nacl import encoding, public

# GitHub public key (32 bytes)
github_public_key = "KlI10j7sf4CV6Pw8zc8dKt1RJh9muMHqdf7iTksW1Ck="
decoded_key = base64.b64decode(github_public_key)

# The secret you want to encrypt
secret_value = "my_secret_value"

# Encrypt the secret
sealed_box = public.SealedBox(public.PublicKey(decoded_key))
encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))

# Base64 encode the encrypted secret
encrypted_value = base64.b64encode(encrypted).decode("utf-8")

print("Encrypted value:", encrypted_value)
