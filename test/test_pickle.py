import pickle

def pickle_load(pickle_file):
    with open(pickle_file, "rb") as f:
        return pickle.load(f)

def pickle_save(pickle_file, pickle_data):
	with open(pickle_file, "wb") as f:
		pickle.dump(pickle_data, f)

if __name__ == '__main__':
	pickle_data_path = r"E:\Dataset\sketches\sdgraph\folders\SketchX_Shoe_ChairV2\ShoeV2\ShoeV2_Coordinate"
	pickle_data = pickle_load(pickle_data_path)
	print(pickle_data)