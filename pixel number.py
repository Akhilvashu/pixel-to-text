from PIL import Image,ImageDraw, ImageFont
import matplotlib.pyplot as plt


img = Image.open('images.jpeg', 'r')
print(img.size)

resized_image = img.resize((7, 50))
#print(resized_image.size)
new_pixels = list(resized_image.getdata())
#print(len(new_pixels))

pixels_size = (505, 605)
image= Image.new("RGB",pixels_size,color="black")
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf",size=14)



def format_pixel(value):
    str_value = str(value)
    if len(str_value) < 3:
        return f"{str_value:0>3}"  
    return str_value

p = 1
i = 1
for pixels in new_pixels:
                
                pixel_1 = format_pixel(pixels[0])
                pixel_2 = format_pixel(pixels[1])
                pixel_3 = format_pixel(pixels[2])

                draw.text((p,i),pixel_1,fill=(255,0,0),font=font)
                draw.text((p+24,i),pixel_2,fill=(0,255,0),font=font)
                draw.text((p+48,i),pixel_3,fill=(0,0,255),font=font)
                p+=72
                if p > 481:
                    p=1
                    i+=12
              
image.save("pixel.jpeg")


fig,axs = plt.subplots(1,2,figsize=(10,5))
fig.patch.set_facecolor("black")
axs[0].imshow(img)
axs[0].axis('off')
axs[1].imshow(image)
axs[1].axis('off')
plt.show()