from base64 import b64decode, b64encode
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicNumbers
from cryptography.hazmat.primitives import serialization

# GitHub's raw base64-encoded public key
github_public_key = "KlI10j7sf4CV6Pw8zc8dKt1RJh9muMHqdf7iTksW1Ck="

try:
    # Decode the raw base64 key
    decoded_key = b64decode(github_public_key)

    # Print the key size for debugging
    print(f"Key size: {len(decoded_key)} bytes")

    # Ensure the key length is valid for RSA
    if len(decoded_key) < 128:
        raise ValueError("Invalid public key size. The key may be incomplete or incorrectly formatted.")

    # Create an RSA public key object
    public_key = RSAPublicNumbers(
        e=65537,  # GitHub always uses this public exponent
        n=int.from_bytes(decoded_key, byteorder="big")  # Convert the raw key to an integer
    ).public_key()

    # The secret you want to encrypt
    secret_value = "my_secret_value"

    # Encrypt the secret
    encrypted = public_key.encrypt(
        secret_value.encode("utf-8"),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=SHA256()),
            algorithm=SHA256(),
            label=None
        )
    )

    # Base64 encode the encrypted value
    encrypted_value = b64encode(encrypted).decode("utf-8")
    print("Encrypted value:", encrypted_value)

except ValueError as ve:
    print(f"ValueError: {ve}")
except Exception as e:
    print(f"Error: {e}")
