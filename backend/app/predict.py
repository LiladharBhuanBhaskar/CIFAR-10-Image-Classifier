from fastapi import APIRouter, UploadFile, File
from PIL import Image
import numpy as np
from backend.app.model_loader import model

router = APIRouter()

class_names = [
    "airplane","automobile","bird","cat","deer",
    "dog","frog","horse","ship","truck"
]

@router.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    img = Image.open(file.file).convert("RGB")
    img = img.resize((32, 32))

    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    preds = model.predict(img_array)
    idx = int(np.argmax(preds))

    return {
        "class": class_names[idx],
        "confidence": float(preds[0][idx])
    }
