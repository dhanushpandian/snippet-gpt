import pyautogui
from PIL import Image, ImageDraw
import time

# Capture screenshot of the entire screen
screenshot = pyautogui.screenshot()

# Define the region you want to draw on
region_left = 100
region_top = 100
region_width = 300
region_height = 200

# Crop the screenshot to the desired region
region = screenshot.crop((region_left, region_top, region_left + region_width, region_top + region_height))

# Create an ImageDraw object
draw = ImageDraw.Draw(region)

# Draw a rectangle on the region
draw.rectangle([(50, 50), (150, 150)], outline="red", width=3)

# Save the modified region
region.save("output.png")

# Display the modified region for a short time
region.show()
time.sleep(3)  # Adjust as needed

# Close the modified region display
region.close()

