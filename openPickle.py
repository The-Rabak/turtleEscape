import pickle

with open("data_rand", "rb") as f:
    print(pickle.load(f))