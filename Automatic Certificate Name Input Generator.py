from PIL import Image, ImageDraw, ImageFont
import csv
import os

TEMPLATE_PATH = ""
FONTH_PATH = ""
FONTH_SIZE = 80
CSV_PATH = ""
OUTPUT_DIR = ""

if not os.path.exist(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def generate_certificate(name):
    img = Image.open(TEMPLATE_PATH)
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(FONTH_PATH, FONTH_SIZE)

    img_width, img_height = img.size
    text_bbox = draw.textbbox((0,0), name, font=font)
    test_width = text_bbox (2) - text_bbox (0)
    text_height = text_bbox (3) - text_bbox (1)

    x = (img_width - img_height) / 2
    y = (img_height * 0.465) - (text_height/2)

    draw.text((x,y), name, font=font, fill="#d35400")

    safe_name=name.replace("","_")
    output_path = os.path.join(OUTPUT_DIR, f"{safe_name}_cerfiticate.png")
    img.convert ('RGB').save(output_path, quality=95)
    print(f"Generate:{output_path}")

    with open(CSV_PATH, mode='r', encoding='uft-8') as file:
        reader = csv.reader(file)
        next(reader)

    for row in reader:
        if row:
            participant_name = row(0)
            generate_certificate(participant_name)

    print("completed")