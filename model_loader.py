import pickle
import numpy as np


class ModelLoader:

    def __init__(self, path, data):
        self.path = path
        with open(self.path, 'rb') as pkl_file:
            self.model = pickle.load(pkl_file)
            X = np.array([1, 1, 1, 0.661212487096872])
            self.res = self.model.predict(X.reshape(1, -1))
            # self.res = self.model.predict(data))

    def get_res(self):
        return self.res

