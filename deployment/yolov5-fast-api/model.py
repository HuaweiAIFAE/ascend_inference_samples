import time
import cv2
from PIL import Image, ImageDraw
import random as rnd
import sys
from main import app_variables

# Define acllite library path
sys.path.append(app_variables["acllite_path"])

# Import modules of acllite library
from acllite_model import AclLiteModel
from acllite_resource import AclLiteResource
from src.model import preprocessing, postprocessing

# Define npu device ip (check id with "npu-smi info" command)
device_id = app_variables["device_id"]
model_path = app_variables["model_path"]

# Initialize acllite library
acl_resource = AclLiteResource()
acl_resource.init()

# Load *.om model
model = AclLiteModel(model_path, device_id)

# Define Coco labels
with open(app_variables["coco_names_path"]) as fd:
    coco_labels = fd.readlines()
coco_labels = [i[:-1] for i in coco_labels][0:]


def inference():
    img_path = "./static/image.jpg"
    img_org_bgr = cv2.imread(img_path)
    data = preprocessing(img_org_bgr,model._model_desc)

    # Measuring inference time
    start = time.time()
    # Inference
    result_list = model.execute([data,]) 
    end = time.time()
    total_time = end - start

    bboxes = postprocessing(result_list, img_org_bgr, model._model_desc)
    
    img = Image.open(img_path)
    img1 = ImageDraw.Draw(img)

    for bbox in bboxes:
        label = coco_labels[int(bbox[5])] + ' ' + str(round(bbox[4],2))
        # print(bbox[:4], bbox[4], bbox[5], label)

        color ="#FF"+''.join([rnd.choice('0123456789ABCDEF') for j in range(4)]) # random color for bounding boxes

        img1.rectangle(list(bbox[:4]), outline =color, width=3) # draw bounding boxes
        img1.rectangle((bbox[0], bbox[1], bbox[0] + len(label)*8, bbox[1] + 15), 
                    outline = (255,255,255), width=10) # draw box for lable

        img1.text((bbox[0]+5, bbox[1]), label, (0,0,0), thickness=10)

    img.convert('RGB').save(img_path)
    return total_time