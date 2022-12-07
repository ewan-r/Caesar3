import pickle

class Storage:
    def __init__(self, world):
        self.world = world
       
    def save_game(self, filename):
       self.saving_menu(filename)

    def restore_world(self, filename):
        with open('model/storage/' + filename, 'rb') as f:
            world = pickle.load(f)
            return world

    def saving_menu(self, filename):
        with open('model/storage/' + filename + ".bin", 'wb') as f:
            pickle.dump(self.world, f, pickle.HIGHEST_PROTOCOL)
        