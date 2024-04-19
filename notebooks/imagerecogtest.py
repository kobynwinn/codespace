from PIL import Image, ImageDraw
import cv2 
 
# Create a new image with a white background 
width, height = 200, 200 
background_color = (255, 255, 255)  # White 
image = Image.new("RGB", (width, height), background_color) 
 
# Create a mask using ImageDraw 
mask = Image.new("L", (width, height), 0)  # Initialize a mask image with all black pixels 
draw = ImageDraw.Draw(mask) 
 
# Draw a shape on the mask (e.g., a rectangle) 
draw.rectangle([(50, 50), (150, 150)], fill=255)  # Fill the rectangle with white 
 
# Apply the mask to the original image 
image.putalpha(mask) 
 
# Save the resulting image 
image.save("masked_image.png") 