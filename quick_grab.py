import pyscreenshot as ImageGrab

def screenGrab():
	im = ImageGrab.grab()
	im.show()

def main():
	screenGrab()

if __name__ == '__main__':
	main()