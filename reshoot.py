import os
from PIL import Image
import click
from datetime import datetime

@click.command("reshoot")
@click.option('--in_dir', required=True, help='directory to read pictures from.', type=click.Path(exists=True))
@click.option('--out_dir', required=True, help='directory to write resized pictures to.', type=click.Path(exists=True))
@click.option('--width', help='Width that you want to resize to. (default=400)', default=400, type=int)
@click.option('--height', help='Height that you want to resize to. (default=400)', default=400, type=int)
def reshoot_pictures(in_dir, out_dir, width=400, height=400):
    """Function to resize pictures from in_dir to out_dir, adds timestamp if filename is not unique."""
    counter = 0
    for file_path in os.listdir(in_dir):
        image = Image.open(os.path.join(in_dir, file_path))
        image.thumbnail((width, height))
        if os.path.exists(os.path.join(out_dir, file_path)):
            file_name_unique = datetime.now().strftime("%d%d%Y%H%M%S")
            file_path_split = file_path.split(".")
            file_path_unique = file_path_split[0] + f"-{file_name_unique}" + f".{file_path_split[1]}"
            image.save(os.path.join(out_dir, file_path_unique))
        else:
            image.save(os.path.join(out_dir, file_path))
        counter += 1
    print(f"Resized {counter} images in directory {in_dir}.")
    print(f"Stored to {out_dir}.")

if __name__ == '__main__':
    reshoot_pictures()