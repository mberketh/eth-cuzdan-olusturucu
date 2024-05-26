from eth_account import Account
import secrets

# Rastgele bir özel anahtar oluşturma
private_key = secrets.token_hex(32)
private_key_hex = "0x" + private_key

# Özel anahtardan bir hesap oluşturma
account = Account.from_key(private_key_hex)

# Genel anahtarı ve ETH adresini alma
public_key = account._key_obj.public_key
compressed_public_key = "0x" + public_key.to_compressed_bytes().hex()

# Bilgileri belirtilen formatta bir .txt dosyasına yazma
with open("ethereum_wallet.txt", "w") as file:
    file.write(f"Address: {account.address}\n")
    file.write(f"Public: {compressed_public_key}\n")
    file.write(f"Private: {private_key_hex}\n")

print("Ethereum cüzdan bilgileri ethereum_wallet.txt dosyasına kaydedildi")
