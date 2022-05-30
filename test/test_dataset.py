from torch.utils.data import Dataset, DataLoader

# 构建自己的数据集
class MyDataset(Dataset):
	def __init__(self, data):
		# 对数据集进行初始化
		super(MyDataset, self).__init__()
		# 直接传输数据作为数据集的数据
		self.data = data

	def __len__(self):
		# 这是获取数据集总长度的方法
		return len(self.data)

	def __getitem__(self, index):
		# 这是对数据集进行迭代的方法
		return self.data[index]

# 这是数据集中的数据
data = [1, 2, 3, 4, 5, 6, 7]
# 实例化一个数据集对象
dataset = MyDataset(data)
# 通过数据集实例化一个dataloader对象
dataloader = DataLoader(dataset, batch_size=3, shuffle=True, drop_last=True)

# 对dataloader对象进行迭代看效果
for data in dataloader:
	print(data)



