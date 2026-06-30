import os
import pickle

print("Current directory:", os.getcwd())
print("Model exists:", os.path.exists("model.pkl"))
print("Model path:", os.path.abspath("model.pkl"))
model = pickle.load(open("model.pkl", "rb"))
print(type(model))
print(model)
print(hasattr(model, "classes_"))