from random import choice
import string


class Cred(object):
    
    def __init__(self, usr_range=16,pwd_range=32):
        self.ascii = string.ascii_lowercase
        self.digits = string.digits
        self.usr_range =  usr_range
        self.pwd_range = pwd_range
        self.case = [str.upper, str.lower]
        self.p = None
        self.u = None
    
        
    
    def alpha(self):
        return self.digits + self.ascii

    def randomify(self, size):
        seed = ''.join(choice(self.case)(i) for i in self.alpha())
        return ''.join(choice(seed) for i in range(size))


    @property
    def password(self):
        if not self.p:
            self.p = self.randomify(self.pwd_range)
        return ('password', self.p)
       

    @property
    def user(self):
        if not self.u:
            self.u = self.randomify(self.usr_range)
        return ('user',self.u)

    @property
    def credentials(self):
        return dict((self.user,self.password))


if __name__ == "__main__":
    cred = Cred()
    print(cred, cred.credentials)


