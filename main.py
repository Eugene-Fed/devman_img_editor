from PIL import Image

CROP_SIZE = 50

monro = Image.open("monro.jpg")
red, green, blue = monro.split()

red_left = red.crop((CROP_SIZE, 0, red.width, red.height))
red_center = red.crop((CROP_SIZE//2, 0, red.width-CROP_SIZE//2, red.height))
red_blended = Image.blend(red_left, red_center, 0.5)

blue_right = blue.crop((0, 0, blue.width-CROP_SIZE, blue.height))
blue_center = blue.crop((CROP_SIZE//2, 0, blue.width-CROP_SIZE//2, blue.height))
blue_blended = Image.blend(blue_right, blue_center, 0.5)

green_center = green.crop((CROP_SIZE//2, 0, green.width-CROP_SIZE//2, green.height))

merged = Image.merge("RGB", (red_blended, green_center, blue_blended))
merged.thumbnail((80, 80))
merged.save("monro_thumb.jpg")
