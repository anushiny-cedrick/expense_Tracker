class CategoryManager:
    def __init__(self):
        self.categories = set()

    def add_category(self, name: str):
        if not name:
            raise ValueError("Category name cannot be empty")
        self.categories.add(name.lower())

    def remove_category(self, name: str):
        self.categories.discard(name.lower())

    def list_categories(self):
        return sorted(list(self.categories))
