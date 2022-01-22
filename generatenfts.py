# use pillow to make 64 images
# each image is a 500x500 pixel image
# each image has random squares in it (1-4 random squares)
# each square is a random size (1-10)
# each square is a random color ("red", "green", "blue", "yellow", "purple", "orange")
#  after each square is drawn, the image is saved to a folder
#  the image is saved as a png
#  make a json file with the following info:
#     -date made
#     -mint cost

#     -color
#     -num squares
#     -tags {"cool", "funny", "cute", "scary"}
import os
import json
import random
import datetime
from PIL import Image, ImageDraw, ImageFont
IMAGE_WIDTH = 250
IMAGE_HEIGHT = 250
raritys = ['COMMON', 'UNCOMMON', 'RARE', 'LIMITED']
raritys_rgb = {'COMMON' : ( 134, 134, 134 ), 'UNCOMMON' : ( 94, 174, 3 ), 'RARE' : ( 3, 161, 229 ), 'LIMITED' : ( 218, 224, 0 )}
def make_nft(name):
    mint_cost = random.random() * 100
    # random date between 1/1/2019 and 1/1/2020
    date = random.randint(
        int(datetime.datetime(2019, 1, 1).timestamp()), 
        int(datetime.datetime(2020, 1, 1).timestamp()))
    rarity_pass = 1
    rarity = raritys[0]
    for x in range(4):
        rarity_pass *= random.randint(0,1)
        if rarity_pass == 0:
            rarity = raritys[x]
            break
    rarity_rgb = raritys_rgb[rarity]
    tags = random.sample(["Cool", "Funny", "Cute", "Scary", "Retarded", "Incredible"], k=random.randint(1, 4))
    img = Image.new('RGB', (random.randint(200, 400), random.randint(200, 400)), rarity_rgb)
    draw = ImageDraw.Draw(img)
    num_squares = random.randint(1, 4)

    colors = set()
    for _ in range(num_squares):
        color = random.choice(["red", "green", "blue", "yellow", "purple", "orange"])
        if color not in colors:
            colors.add(color)
        size = random.randint(IMAGE_WIDTH // 10, IMAGE_WIDTH // 2)
        x = random.randint(0, IMAGE_WIDTH - size)
        y = random.randint(0, IMAGE_HEIGHT - size)
        draw.rectangle([x, y, x + size, y + size], fill=color)
    img.save(f"public/assets/{name}.png")

    if os.path.exists("src/asset_data.json"):
        with open (f'src/asset_data.json') as f:
            old_data = json.load(f)
    else:
        old_data = {"assets" : []}

    with open(f"src/asset_data.json", "w") as f:
        info = {
            "id" : name,
            "data" : {
                "rarity" : rarity,
                "mint_cost": mint_cost,
                "date": date,
                "tags": tags,
                "num_squares": num_squares,
                "colors": list(colors)
            }
        }
        old_data["assets"].append(info)
        json.dump(old_data, f, indent=4)

if __name__ == "__main__":
    #  make asset folder if not exists
    if not os.path.exists("public/assets"):
        os.makedirs("public/assets")
    for i in range(50):
        make_nft(f"nft{i}")