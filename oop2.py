class utensils:
    def __init__(self,material):
        self.material = material
    def use(self):
        print("used in the kitchen and is made of " + self.material)
class plate(utensils):
    def __init__(self,material):
        utensils.__init__(self,material)
p=plate('paper')
p.use()