from ftplib import FTP

if __name__=='__main__' :
    HOST = "localhost"
    PORT = 2121

    ftp = FTP()
    ftp.connect(HOST, PORT)
    ftp.login(user='someUser', passwd='somePassword')
    ftp.retrlines('LIST')
    ftp.quit()

