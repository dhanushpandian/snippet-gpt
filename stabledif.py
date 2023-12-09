from diffusers import AutoPipelineForImage2Image
from diffusers.utils import load_image
import torch


def main():
    # Load the pre-trained model and set it up for inference
    pipe = AutoPipelineForImage2Image.from_pretrained(
        "stabilityai/sdxl-turbo", torch_dtype=torch.float16, variant="fp16")
    # pipe.to("cuda")

    # Load the initial image
    init_image = load_image(
        "WhatsApp Image 2023-12-09 at 11.31.22 AM.jpeg").resize((512, 512))

    # Set the prompt
    prompt = "professional suite smiling"

    # Run the code
    image = pipe(prompt, image=init_image, num_inference_steps=2,
                 strength=0.5, guidance_scale=0.0).images[0]

    # Print information about the generated image
    print("Image type:", type(image))
    print("Image size:", image.size)

    # Optionally, you can save or display the generated image
    image.save("output_image.jpeg")
    image.show()


if __name__ == "__main__":
    main()
