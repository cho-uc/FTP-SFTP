'''
Use sftpserver/main.py from https://github.com/rspivak/sftpserver to run the server to test this client

'''

import paramiko


pkey = paramiko.RSAKey.from_private_key_file('/home/cho_uc/keypair.pem')

transport = paramiko.Transport(('localhost', 3373))

# publickey checking has more priority compared to password
# transport.connect(username='abc', password='1234') # check_auth_password() will be called
transport.connect(username='abc', password='1234', pkey=pkey) # check_auth_publickey will be called


sftp = paramiko.SFTPClient.from_transport(transport)
print(sftp.listdir('.'))  # not recursively

