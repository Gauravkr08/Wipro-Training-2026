class OrderService:
    def __init__(self):
        self.orders = {}
        self.current_id = 1

    def place_order(self, data):
        data['id'] = self.current_id
        self.orders[self.current_id] = data
        self.current_id += 1
        return data

    def view_orders_by_user(self, user_id):
        return [o for o in self.orders.values() if o.get('user_id')==user_id]

    def view_orders_by_restaurant(self, restaurant_id):
        return [o for o in self.orders.values() if o.get('restaurant_id')==restaurant_id]