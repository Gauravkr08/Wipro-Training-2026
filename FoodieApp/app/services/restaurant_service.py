class RestaurantService:
    def __init__(self):
        self.restaurants = {}
        self.current_id = 1

    def add_restaurant(self, data):
        data['id'] = self.current_id
        data['enabled'] = True
        self.restaurants[self.current_id] = data
        self.current_id += 1
        return data

    def update_restaurant(self, rid, data):
        if rid in self.restaurants:
            self.restaurants[rid].update(data)
            return self.restaurants[rid]
        return None

    def disable_restaurant(self, rid):
        if rid in self.restaurants:
            self.restaurants[rid]['enabled'] = False
            return True
        return False

    def get_restaurant(self, rid):
        return self.restaurants.get(rid)
