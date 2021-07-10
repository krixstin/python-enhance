class Product(object):
    pass

#__items : private type
class Inventroy(object):
    def __init__(self):
        self.__items = []

    def add_new_item(self, product):
        if type(product) == Product:
            self.__items.append(product)
            print("New item added")
        else:
            print("Invalid item")

    def get_number_of_items(self):
        return len(self.__itmes)