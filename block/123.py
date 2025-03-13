import os

def test(name):
    print (name)

def test2 (name):
    return(name)

test("A")
test2("B")

def load_image( image_name: str, size: tuple[int, int]):
    image_path = os.path.join(os.path.dirname(__file__), "images")
    full_path = os.path.join(image_path, image_name)
    return full_path

print(load_image('kydio', [1, 1]))

print(os.path.join(os.path.dirname(__file__), "sdf"))