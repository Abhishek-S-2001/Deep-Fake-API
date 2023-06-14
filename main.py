from imports import *
from Model.video_model import check_video
from AWSCloud.s3_file import load_video, save_video

class image_base64(BaseModel):
    img_base64: str


class video_code(BaseModel):
    video_code: str


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#
# def basetoimage(base):
#     try:
#         im_bytes = base64.b64decode(base)  # im_bytes is a binary image
#         im_file = BytesIO(im_bytes)  # convert image to file-like object
#         img = Image.open(im_file)
#         return img, 1
#     except:
#         return None, 0

def get_video(vcode):
    return 0


# @app.post("/get_data")
# async def read_image(file: image_base64):
#     # download image_model.py file
#     if os.path.exists('Model/model.h5') == False:
#         url = 'https://drive.google.com/u/1/uc?id=14RV5bQTw1r9HSYF_zkab4PlzwLJaP4kk&export=download'
#         filename = 'Model/model.h5'
#         urlretrieve(url, filename)
#     model = torch.jit.load("Model/model.h5")
#
#     base64 = file.img_base64
#     image, flag = basetoimage(base64)
#     ## result = {"Result": "1"}
#     if flag == 1:
#         result0 = predict(model, image)
#         result = {"Result": result0}
#     else:
#         result = {"Result": "Please Provide Correct Input"}
#     print(result)
#     return result

@app.post("/check_video")
async def read_vcode(file: video_code):
    vcode = file.video_code
    load_video(vcode)
    check_video()
    save_video(vcode)
    return 'Video Checked'


@app.get("/")
def index():
    return "API Started..."


if __name__ == '__main__':
    app.run()
