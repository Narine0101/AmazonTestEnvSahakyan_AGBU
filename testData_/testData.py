class User:
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password


# User Data
validUser = User("narine.narine.1962@mail.ru", "Sahakyan1963!")
userWithInvalidPassword = User("narine.narine.1962@mail.ru", "WrongPassword")
userWithInvalidUserName = User("InvalidUserName@mail.ru", "WrongPassword")

# URL_s

signInPageUrl = "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
mainPageUrl = "https://www.amazon.com/"


