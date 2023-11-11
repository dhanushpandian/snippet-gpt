import streamlit as st
import io
from PIL import Image, ImageDraw


def take_screenshot():
    """Takes a screenshot of the current Streamlit app."""

    # Get the current app state
    app_state = st.session_state

    # Create a PIL image to store the screenshot
    image = Image.new("RGB", (app_state["width"], app_state["height"]))
    draw = ImageDraw.Draw(image)

    # Render the app to the PIL image
    st.write(image)

    # Save the screenshot to a file
    image.save("screenshot.png")


# Initialize the screenshot key
st.session_state["screenshot"] = None

# Create a button to trigger the screenshot function
st.button("Take Screenshot", on_click=take_screenshot)

# Display the screenshot when it is available
if st.session_state["screenshot"] is not None:
    st.image("screenshot.png")


