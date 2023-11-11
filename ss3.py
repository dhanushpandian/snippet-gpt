import pyautogui
from PIL import Image, ImageDraw
import time

def draw_area():
    # Get the screen resolution
    screen_width, screen_height = pyautogui.size()

    # Create a transparent full-screen image
    image = Image.new("RGBA", (screen_width, screen_height), (0, 0, 0, 0))

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Draw a rectangle while capturing mouse events
    try:
        while True:
            x1, y1, _, _ = pyautogui.dragTo(image.width, image.height, button="left")
            _, _, x2, y2 = pyautogui.dragTo(x1, y1, button="left")

            # Draw the rectangle on the image
            draw.rectangle([(x1, y1), (x2, y2)], outline="red", width=2)

    except pyautogui.FailSafeException:
        pass

    # Close the image
    image.close()

    # Crop the captured area from the screenshot
    captured_area = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))

    # Save the captured area to a file
    captured_area.save("captured_area.png")

    # Display the captured area for a short time
    captured_area.show()
    time.sleep(3)  # Adjust as needed

    # Close the captured area display
    captured_area.close()

if __name__ == "__main__":
    draw_area()

