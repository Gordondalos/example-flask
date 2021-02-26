class Car:
    def __init__(self, color, door):
        """

        :type door: object
        """
        self.color = color
        self.door = door

    def set_color(self, color):
        self.color=color

    def get_color(self):
        return self.color

    def get_count_letters(self, word):
        return len(word)

    def get_door(self):
        return self.door

    def change_door(self, door):
        self.door = door



