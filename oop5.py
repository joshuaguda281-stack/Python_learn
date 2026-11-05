class Microwave:
    def __init__(self, brand: str, power_rating: str):
        self.brand = brand
        self.power_rating = power_rating

    def cook(self, food: str):
        print(f"Cooking {food} at {self.power_rating} watts in the {self.brand} microwave.")

    def display_info(self):
        print(f"Microwave Brand: {self.brand}, Power Rating: {self.power_rating} watts")

    def set_power_rating(self,  new_power_rating: str):
        self.power_rating = new_power_rating


    def turned_on(self):
        print(f"The {self.brand} microwave is now turned on.")

    def turned_off(self):
        print(f"The {self.brand} microwave is now turned off.")

smeg = Microwave("Smeg", "1000")
smeg.display_info()
smeg.turned_on()
smeg.turned_off()
smeg.set_power_rating("1200")
smeg.display_info()
smeg.cook("popcorn")