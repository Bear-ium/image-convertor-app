from PIL import Image

def convert_image(input_path, output_path, format, width=None, height=None, quality=85):
    with Image.open(input_path) as img:
        if width and height:
            img = img.resize((width, height), Image.Resampling.LANCZOS)
        img.save(output_path, format=format.upper(), quality=quality)
