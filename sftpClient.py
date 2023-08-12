'''
Use sftpserver/main.py from https://github.com/rspivak/sftpserver to run the server to test this client

How to create keys:
openssl req -out CSR.csr -new -newkey rsa:2048 -nodes -keyout test_rsa.key
openssl genrsa -out keypair_new.pem 2048
openssl genrsa -aes256 -out key_with_pass.key 2048
ssh-keygen -f /home/cho-uc/ecdsa_key.pem -t ecdsa -b 521

'''

import paramiko


pkey = paramiko.RSAKey.from_private_key_file('/home/cho_uc/keypair.pem')

transport = paramiko.Transport(('localhost', 3373))

# publickey checking has more priority compared to password
# transport.connect(username='abc', password='1234') # check_auth_password() will be called
transport.connect(username='abc', password='1234', pkey=pkey) # check_auth_publickey will be called


sftp = paramiko.SFTPClient.from_transport(transport)
print(sftp.listdir('.'))  # not recursively

