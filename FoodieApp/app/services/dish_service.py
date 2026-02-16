class DishService:
    def __init__(self):
        self.dishes = {}
        self.current_id = 1

    def add_dish(self, data):
        data['id'] = self.current_id
        data['enabled'] = True
        self.dishes[self.current_id] = data
        self.current_id += 1
        return data

    def update_dish(self, did, data):
        if did in self.dishes:
            self.dishes[did].update(data)
            return self.dishes[did]
        return None

    def toggle_dish(self, did):
        if did in self.dishes:
            self.dishes[did]['enabled'] = not self.dishes[did]['enabled']
            return self.dishes[did]
        return None

    def delete_dish(self, did):
        return self.dishes.pop(did, None)

    def get_dish(self, did):
        return self.dishes.get(did)