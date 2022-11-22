class Storage:

    def __init__(self, world):
        self.world = world
       
    def save_game(self, filename):
       self.saving_menu(filename)

    def restore_world(self, filename):
        f = open(filename, "w")
        lines = f.readlines()
        print(lines)

    def saving_menu(self, filename):
        f = open("model/storage/" + filename, "w+")
        f.write(str(self.world))
        f.close()