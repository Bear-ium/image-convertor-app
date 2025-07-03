from PIL import Image

def generate_ico(input_path, output_path, sizes=[(16,16), (32,32), (48,48), (256,256)]):
    with Image.open(input_path) as img:
        img.save(output_path, format='ICO', sizes=sizes)
