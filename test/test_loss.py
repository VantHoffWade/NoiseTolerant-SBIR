import torch
from torch import nn

if __name__ == '__main__':
	triplet_loss = nn.TripletMarginLoss(margin=0.1, reduction='sum', p=2.0)
	x1 = torch.tensor([[1, 2, 3]])
	x2 = torch.tensor([[4, 5, 6]])
	x3 = torch.tensor([[7, 8, 9]])
	loss = triplet_loss(x1, x3, x2)
	print(loss)

