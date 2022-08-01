import base64

password = "mudar123"
print("Initial password: " + password)

def base64_Encryption(message):      
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message
    
def base64_Decryption(message):    
    base64_message = message
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes.decode('ascii')

print("Encrypted password: " + base64_Encryption(password))
print("Decrypted password: " + base64_Decryption(base64_Encryption(password)))