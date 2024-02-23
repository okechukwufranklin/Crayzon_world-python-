class Gun:

    def __init__(self, Bullet=0):
        self.Bullet = Bullet



    def is_empty(self):
        return self.Bullet == 0

    def Shoot_Gun(self,):
        self.Bullet -= 1

    def reload_Gun(self):
        self.Bullet += 5

    def Checkammo(self):
        return self.Bullet

    def Clip(self):
        if self.Bullet > 5:
            return "Magazine full"
