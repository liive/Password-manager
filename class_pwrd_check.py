import re

class PasswordCeck:
    
    def __init__(self, password):
        self.password = password

    def digits(self): 
        digits = any(i.isdigit() for i in self.password)
        return digits
     
    def alpha(self):
        alpha = any(i.isalpha() for i in self.password)
        return alpha

    def upper(self):
        upper = any(x.isupper() for x in self.password)
        return upper

    def lower(self):
        lower = any(x.islower() for x in self.password)
        return lower

    def special_ch(self):
        answer = re.search(r'[@_!#$%^&*()<>?/\|}{~:]', self.password)
        if answer: 
            return True
        return False

    def validate(self):
        digits = self.digits()
        alpha = self.alpha()
        upper = self.upper()
        lower = self.lower()
        special_ch = self.special_ch()

        length = len(self.password)
        report = special_ch and digits and alpha and upper and lower and length >= 8
        return report