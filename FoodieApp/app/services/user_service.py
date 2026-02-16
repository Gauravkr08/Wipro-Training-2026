class UserService:
    def __init__(self):
        self.users = {}
        self.current_id = 1

    def register_user(self, data):
        for u in self.users.values():
            if u['email'] == data.get('email'):
                return None
        data['id'] = self.current_id
        self.users[self.current_id] = data
        self.current_id += 1
        return data

    def search_restaurant(self, name=None):
        return [{"id":1,"name":"Food Hub"}]