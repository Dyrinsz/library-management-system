class AboutManager():
    def __init__(self):
        self.db = AboutDAO()
        self.db.table = "about"

    def get_about_info(self):
        return self.db.get_all()

    def update_about_info(self, data):
        return self.db.update(data)