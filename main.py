from PIL import Image
import os
import numpy as np
import pillow_heif
import pillow_avif

# image_name = "JPG" #画像のフォルダ名
# extension = "jpg" #画像の拡張子

# original_images = [" ",
#               "PGM/camera.pgm", "PGM/couple.pgm", "PGM/noisesquare.pgm",
#               "PGM/airplane.pgm", "PGM/baboon.pgm", "PGM/lena.pgm", "PGM/lennagrey.pgm", "PGM/peppers.pgm", "PGM/shapes.pgm",
#               "PGM/balloon.pgm", "PGM/barb.pgm", "PGM/barb2.pgm", "PGM/goldhill.pgm"]

# images = [" ",
#               "{0}/quality10/camera_10.{1}".format(image_name, extension), "{0}/quality25/camera_25.{1}".format(image_name, extension), "{0}/quality50/camera_50.{1}".format(image_name, extension), "{0}/quality75/camera_75.{1}".format(image_name, extension),
#               "{0}/quality10/couple_10.{1}".format(image_name, extension), "{0}/quality25/couple_25.{1}".format(image_name, extension), "{0}/quality50/couple_50.{1}".format(image_name, extension), "{0}/quality75/couple_75.{1}".format(image_name, extension),
#               "{0}/quality10/noisesquare_10.{1}".format(image_name, extension), "{0}/quality25/noisesquare_25.{1}".format(image_name, extension), "{0}/quality50/noisesquare_50.{1}".format(image_name, extension), "{0}/quality75/noisesquare_75.{1}".format(image_name, extension),
#               "{0}/quality10/airplane_10.{1}".format(image_name, extension), "{0}/quality25/airplane_25.{1}".format(image_name, extension), "{0}/quality50/airplane_50.{1}".format(image_name, extension), "{0}/quality75/airplane_75.{1}".format(image_name, extension),
#               "{0}/quality10/baboon_10.{1}".format(image_name, extension), "{0}/quality25/baboon_25.{1}".format(image_name, extension), "{0}/quality50/baboon_50.{1}".format(image_name, extension), "{0}/quality75/baboon_75.{1}".format(image_name, extension),
#               "{0}/quality10/lena_10.{1}".format(image_name, extension), "{0}/quality25/lena_25.{1}".format(image_name, extension), "{0}/quality50/lena_50.{1}".format(image_name, extension), "{0}/quality75/lena_75.{1}".format(image_name, extension),
#               "{0}/quality10/lennagrey_10.{1}".format(image_name, extension), "{0}/quality25/lennagrey_25.{1}".format(image_name, extension), "{0}/quality50/lennagrey_50.{1}".format(image_name, extension), "{0}/quality75/lennagrey_75.{1}".format(image_name, extension),
#               "{0}/quality10/peppers_10.{1}".format(image_name, extension), "{0}/quality25/peppers_25.{1}".format(image_name, extension), "{0}/quality50/peppers_50.{1}".format(image_name, extension), "{0}/quality75/peppers_75.{1}".format(image_name, extension),
#               "{0}/quality10/shapes_10.{1}".format(image_name, extension), "{0}/quality25/shapes_25.{1}".format(image_name, extension), "{0}/quality50/shapes_50.{1}".format(image_name, extension), "{0}/quality75/shapes_75.{1}".format(image_name, extension),
#               "{0}/quality10/balloon_10.{1}".format(image_name, extension), "{0}/quality25/balloon_25.{1}".format(image_name, extension), "{0}/quality50/balloon_50.{1}".format(image_name, extension), "{0}/quality75/balloon_75.{1}".format(image_name, extension),
#               "{0}/quality10/barb_10.{1}".format(image_name, extension), "{0}/quality25/barb_25.{1}".format(image_name, extension), "{0}/quality50/barb_50.{1}".format(image_name, extension), "{0}/quality75/barb_75.{1}".format(image_name, extension),
#               "{0}/quality10/barb2_10.{1}".format(image_name, extension), "{0}/quality25/barb2_25.{1}".format(image_name, extension), "{0}/quality50/barb2_50.{1}".format(image_name, extension), "{0}/quality75/barb2_75.{1}".format(image_name, extension),
#               "{0}/quality10/goldhill_10.{1}".format(image_name, extension), "{0}/quality25/goldhill_25.{1}".format(image_name, extension), "{0}/quality50/goldhill_50.{1}".format(image_name, extension), "{0}/quality75/goldhill_75.{1}".format(image_name, extension)]


# tmp = 1
# cnt = 0
# prev = float("inf")
# for i in range(1, len(original_images)):
#     rate = 1
#     original_image = Image.open(original_images[i])
#     Image_name_tmp = original_images[i].split("/")
#     Image_name_tmp = Image_name_tmp[1].split(".")
#     Image_name = Image_name_tmp[0]
#     original_image.save(Image_name + ".avif", "avif")
#     for j in range(tmp, len(images)):
#         while(rate < 101):
#             Image_name_tmp2 = images[j].split("/")
#             Image_name_tmp2 = Image_name_tmp2[2].split(".")
#             Image_name2 = Image_name_tmp2[0]
#             webp_image = Image.open(Image_name + ".avif")
#             webp_image = webp_image.convert("L")
#             quality_name = ""
#             if(cnt % 4 == 0):
#                 quality_name = "_10"
#             elif(cnt % 4 == 1):
#                 quality_name = "_25"
#             elif(cnt % 4 == 2):
#                 quality_name = "_50"
#             elif(cnt % 4 == 3):
#                 quality_name = "_75"
            
#             webp_image.save(Image_name + quality_name + ".avif", "avif", quality = rate)
#             webp_bits = os.path.getsize(Image_name + quality_name + ".avif") * 8
#             jpg_bits = os.path.getsize(images[j]) * 8
#             diff = abs(webp_bits - jpg_bits)
#             if(prev > diff):
#                 prev = diff
#                 quality_val = rate
#             rate = rate + 1
            
#         cnt = cnt + 1
#         webp_image.save("AVIF/quality" + quality_name[1] + quality_name[2] + "/" + Image_name + quality_name + ".avif", "avif", quality = quality_val)
#         prev = float("inf")
#         rate = 1
#         os.remove(Image_name + quality_name + ".avif")
#         if(cnt % 4 == 0):
#             tmp = cnt + 1
#             os.remove(Image_name + ".avif")
#             break

# quality = "75"
# Image_name = "goldhill"
# name = "{0}_{1}.heif".format(Image_name, quality)


# heif_bits = os.path.getsize(name) * 8
# print("HEIF bits = ",heif_bits)
# jpg_bits = os.path.getsize("JPG/quality{1}/{0}_{1}.jpg".format(Image_name, quality)) * 8
# print("JPG bits = ", jpg_bits)

image = Image.open("airplane_50.webp")
image.convert("L")
if(image.mode == "RGB"):
    print("Y")
image = np.array(image)
r = image[ :, :, 0]
g = image[ :, :, 1]
b = image[ :, :, 2]

if(np.array_equal(r, g)):
    print("Y")
