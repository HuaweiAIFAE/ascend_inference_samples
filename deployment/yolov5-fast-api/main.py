import os
import shutil
import uvicorn
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import model

#---------------------------------------------------------------
# CHANGE VALUES IF NECCESSARY
app_variables = {
    "host_ip":"10.1.6.13",
    "host_port":"6565",
    "inference_port":505,
    "device_id":0,
    "acllite_path":"../pyacl_samples/Common/acllite",
    "model_path":"./model/yolov5s.om",
    "coco_names_path":"../pyacl_samples/Common/data/coco.names"
}
#---------------------------------------------------------------

# Create a FastAPI instance
app = FastAPI()

# Define the location for static files(html,css etc.) to look for
templates = Jinja2Templates(directory="./static/")

# Define GET operation at path "/" that uses function below to handle requests
@app.get("/", response_class=HTMLResponse)
async def upload(request: Request):
   inference_time = model.inference()
   return templates.TemplateResponse("upload_image.html", 
                                     {
                                         "request": request, 
                                         "inference_time":inference_time, 
                                         "app_variables":app_variables,
                                         "image_path":os.path.relpath("static/image.jpg", "/workspace")
                                     })

# Define POST operation at path "/" that uses function below to handle requests
@app.post("/")
async def create_upload_file(request: Request, file: UploadFile = File(...)):
   
   # Write posted image to "image.jpg" file
   with open("./static/image.jpg", "wb") as buffer:
      shutil.copyfileobj(file.file, buffer)
   
   # Call inference on the image
   inference_time = model.inference()
   return templates.TemplateResponse("upload_image.html", 
                                     {
                                         "request": request, 
                                         "inference_time":inference_time, 
                                         "app_variables":app_variables,
                                         "image_path":os.path.relpath("static/image.jpg", "/workspace")
                                     })


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=app_variables["inference_port"], log_level="info")