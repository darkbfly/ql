import json
import pickle

if __name__ == '__main__':
    # pkl文件转JSON
    with open('huazhu.pkl', 'rb') as f:
        data = pickle.load(f)
        for i in data:
            print(f"{i['name']}={i['value']};")

    pass