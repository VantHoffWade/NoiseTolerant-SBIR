from torchvision.transforms import v2 as transforms
import matplotlib.pyplot as plt
from PIL import Image

# 用pillow读取一张图片
def get_img(img_path):
	img = Image.open(img_path).convert('RGB')
	img = transforms.ToTensor()(img)
	print(img.size())


if __name__ == '__main__':
	img_path = r"E:\Dataset\images\Tiny ImageNet\tiny-imagenet-200\tiny-imagenet-200\test\images\test_0.JPEG"
	get_img(img_path)