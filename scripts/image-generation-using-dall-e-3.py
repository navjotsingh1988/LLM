# accessing operating system resources
import os
# accessing the OpenAI API
from openai import OpenAI
# downloading files
import requests
# Pillow is the most popular image processing library in Python
# pip install pillow
from PIL import Image

# Import OpenAI client and initialize with your API key.
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# AI Image Generator Agent
# ------------------------
'''
Generate an image using the client.images.generate() method.
This will require the following parameters:
    model: This is the model that you want to use.
    prompt: This is a description of the image that you want to generate.
    size: This is the size of the image to generate and should be either of the following:
            1792x1024
            1024x1792
            1024x1024
    quality: This is set to either standard, or hd.
    n: This needs to be set to 1.
'''
# ------------------------

# Number of images to be Generated : 1
for i in range(1):
    response = client.images.generate(
        model = "dall-e-3",
        prompt = "technical drawing of human teeth",
        size = "1024x1024",
        quality = "hd",
        n=1
    )

    # prompt given above will be reworded using the GPT-4 model.
    reworded_prompt = response.data[0].revised_prompt
    print(reworded_prompt)

    # extract the image url
    image_url = response.data[0].url

    # saving the image locally
    local_path = '/tmp/usercode/images'
    os.makedirs(local_path, exist_ok=True)

    image_name = local_path + '/' + 'abc.jpg'
    image_data = requests.get(image_url).content

    with open(image_name, 'wb') as f:
       f.write(image_data)

    # open and show the image
    # img.show() will launch the image in the default viewer for your OS.
    img = Image.open(image_name)
    img.show()
