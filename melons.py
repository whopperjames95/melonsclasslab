"""This file should have our melon-type classes in it."""
class AbstractMelonOrder:
    add_on = 0

    def __init__(self):
        raise NotImplementedError("Don't make instances of me")

    def get_base_prce(self):
        return 5.0

    def get_price(self, qty):
        each = self.get_base_price() + self.add_on
        total = each * qty

        if self.imported:
            total = total * 1.5

        if self.shape == "square":
            total = total * 2

        return total 

    def available_now(self):
        today = date.today()
        month = today.month

        if month == 1 and "Winter" in self.seasons:
            return True
        if month == 2 and "Winter" in self.seasons:
            return True
        if month == 3 and "Winter" in self.seasons:
            return True
        if month == 4 and "Spring" in self.seasons:
            return True
        if month == 5 and "Spring" in self.seasons:
            return True
        if month == 6 and "Spring" in self.seasons:
            return True
        if month == 7 and "Summer" in self.seasons:
            return True
        if month == 8 and "Summer" in self.seasons:
            return True
        if month == 9 and "Summer" in self.seasons:
            return True
        if month == 10 and "Fall" in self.seasons:
            return True
        if month == 11 and "Fall" in self.seasons:
            return True
        if month == 12 and "Fall" in self.seasons:
            return True

class WatermelonOrder(AbstractMelonOrder):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = "natural"
    seasons = ["Fall", "Summer"]

    def get_price(self, qty):
        total = super(WatermelonOrder, self).get_price(qty)
        if qty >= 5:
            total = total * 0.75
        return total

class OgenOrder(AbstractMelonOrder):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]

    add_on = 1



print(WatermelonOrder.seasons)