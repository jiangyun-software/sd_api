# import requests
# from PIL import Image
# from io import BytesIO
# import base64
# import json

# def txt2img():
#     url_txt2img = "http://127.0.0.1:1338/sdapi/v1/txt2img"
#     json_dict = {
#             "enable_hr": False,
#             "denoising_strength": 0,
#             "firstphase_width": 0,
#             "firstphase_height": 0,
#             "prompt": "(Highest picture quality) Pencil texture, bare shoulder, bone feeling, wearing clothes with exposed belly, transparent yarn texture, exposed umbilicus, exposed legs, lovely, children, girls, imperial sisters, Laurie, group photo, many people, clear eyes, warm eyes, dyed eyes, star eyes, big eyes, almond eyes, baby fat, sensual, beautiful, Cute (masterpiece) (masterpiece of a master) (detailed description) (detailed description of hair) (detailed description of eyes) (detailed description of face) (detailed description of human body) (detailed description of the whole body) (anime) dynamics, exquisite CG, exquisite illustration, (the best quality), {masterpiece}}, {high resolution}, (delicate facial features), (delicate facial description) thin. Big eyes, double eyelids, light eyelashes, handsome and clear face. Smile, atmosphere, sense of light and shadow, film lighting, perfect composition, messy and gorgeous, beautiful clothes, gorgeous decoration, full of details, and detailed cloth",
#             "styles": [],
#             "seed": -1,
#             "subseed": -1,
#             "subseed_strength": 0,
#             "seed_resize_from_h": -1,
#             "seed_resize_from_w": -1,
#             "batch_size": 1,
#             "n_iter": 1,
#             "steps": 50,
#             "cfg_scale": 7,
#             "width": 512,
#             "height": 512,
#             "restore_faces": False,
#             "tiling": False,
#             "negative_prompt": "",
#             "eta": 0,
#             "s_churn": 0,
#             "s_tmax": 0,
#             "s_tmin": 0,
#             "s_noise": 1,
#             "sampler_index": "Euler a"
#     }
#     response = json.loads(requests.post(url_txt2img, json=json_dict).text)
#     bs64img = response['images'][0]
#     img = Image.open(BytesIO(base64.b64decode(bs64img)))
#     img.save('novalai.png')

# if __name__ == "__main__":
#     txt2img()

import requests
import io
import base64
from PIL import Image, PngImagePlugin

url = "https://artfy.cc/serve/"

payload = {
    "prompt": "(Highest picture quality) Pencil texture, bare shoulder, bone feeling, wearing clothes with exposed belly, transparent yarn texture, exposed umbilicus, exposed legs, lovely, children, girls, imperial sisters, Laurie, group photo, many people, clear eyes, warm eyes, dyed eyes, star eyes, big eyes, almond eyes, baby fat, sensual, beautiful, Cute (masterpiece) (masterpiece of a master) (detailed description) (detailed description of hair) (detailed description of eyes) (detailed description of face) (detailed description of human body) (detailed description of the whole body) (anime) dynamics, exquisite CG, exquisite illustration, (the best quality), {masterpiece}}, {high resolution}, (delicate facial features), (delicate facial description) thin. Big eyes, double eyelids, light eyelashes, handsome and clear face. Smile, atmosphere, sense of light and shadow, film lighting, perfect composition, messy and gorgeous, beautiful clothes, gorgeous decoration, full of details, and detailed cloth",
    "steps": 50
}

response = requests.get(url=f'{url}/v2/progress', json=payload)

r = response.json()
print(r)
# for i in r['images']:
#     image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))

#     png_payload = {
#         "image": "data:image/png;base64," + i
#     }
#     response2 = requests.post(url=f'{url}/v2/png-info', json=png_payload)

#     pnginfo = PngImagePlugin.PngInfo()
#     pnginfo.add_text("parameters", response2.json().get("info"))
#     image.save('output.png', pnginfo=pnginfo)