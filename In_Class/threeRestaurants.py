class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a restaurant that cooks {self.cuisine_type}.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant2 = Restaurant("Pinsa Romani", "Italian Food")
restaurant3 = Restaurant("Asian Fusion", "Indian Food")
restaurant4 = Restaurant("KFC", "Fast Food")

restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3.describe_restaurant()
restaurant3.open_restaurant()

restaurant4.describe_restaurant()
restaurant4.open_restaurant()