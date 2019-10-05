from PIL import ImageFont, ImageDraw, Image
import argparse
# https://blog.gtwang.org/programming/opencv-drawing-functions-tutorial/

def paste(name, output):
    image = Image.open("./base.png")
    drawer = ImageDraw.Draw(image)
    font_ttf = "./MicrosoftJhengHei.ttf"
    name_len = len(name)
    if name_len == 4:
        font = ImageFont.truetype("./標楷體.ttf", 68)
        drawer.text((922, 853), name, font=font, fill=(0, 0, 0))
    elif name_len == 5:
        font = ImageFont.truetype("./標楷體.ttf", 55)
        drawer.text((918, 858), name, font=font, fill=(0, 0, 0))
    elif name_len == 6:
        font = ImageFont.truetype("./標楷體.ttf", 50)
        drawer.text((912, 862), name, font=font, fill=(0, 0, 0))
    else:
        raise NotImplementedError
    image.save(output)

def paste_10_names(names, output):
    assert(len(names) <= 10)
    image = Image.open("./base.png")
    drawer = ImageDraw.Draw(image)
    font_ttf = "./Microsoft-JhengHei-Bold.ttf"

    card_w, card_h = 500, 324

    for idx, name in enumerate(names):
        row, col = idx // 2, idx % 2

        if len(name) == 2:
            # insert a space between two characters
            x, y = 100 + col * card_w, 90 + row * card_h

            name = name[:1] + "  " + name[1:]
            font = ImageFont.truetype(font_ttf, 120)
            drawer.text((x, y), name, font=font, fill=(0, 0, 0))
        elif len(name) == 3:
            x, y = 70 + col * card_w, 90 + row * card_h
            
            font = ImageFont.truetype(font_ttf, 120)
            drawer.text((x, y), name, font=font, fill=(0, 0, 0))
        elif len(name) == 4:
            x, y = 32 + col * card_w, 100 + row * card_h

            font = ImageFont.truetype(font_ttf, 110)
            drawer.text((x, y), name, font=font, fill=(0, 0, 0))
        else:
            raise NotImplementedError
        
    image.save(output)


def load_names(names_file):
    names = []
    with open(names_file, "r") as f:
        for line in f:
            line = line.strip()
            if len(line) != 0:
                names.append(line)
    return names

def main(args):
    names = load_names(args.names_file)
    num_names = len(names)
    num_images = num_names // 10 + (1 if num_names % 10 != 0 else 0)
    for i in range(num_images):
        paste_10_names(names[i*10:(i+1)*10], args.output_prefix + str(i) + ".png")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("names_file", type=str)
    parser.add_argument("output_prefix", type=str)
    args = parser.parse_args()
    
    main(args)
