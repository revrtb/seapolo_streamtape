
ulist = {
        "admin": [1, "SBB@admin1985"]
        }

class User():
 
    def __init__(self, email, password, id):
        self.id = 1
        self.authenticated = False
        self.password = password
        self.email = email

    @staticmethod
    def get(uid):
        for k in ulist.keys():
            if ulist[k][0] == uid:
                return User(k, ulist[k][1], uid)

    @staticmethod
    def get_user(email):
        if email in ulist.keys():
            return User(email, ulist[email][1], ulist[email][0])

    def check_user(self, pswd):
        return self.password == pswd

    def auth_user(self):
        self.authenticated = True

    def is_authenticated(self):
        return self.authenticated
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return str(self.id)
 
    def __repr__(self):
        return '<User %r>' % (self.email)

