from facenet_pytorch import MTCNN, InceptionResnetV1
import numpy as np
from PIL import Image
import pandas as pd
import FaceBoxRecognition_mtcnn

mtcnn = MTCNN()
resnet = InceptionResnetV1(pretrained='vggface2').eval()

def distance(emb1, emb2):
    diff = np.subtract(emb1.detach().numpy(), emb2.detach().numpy())
    return np.sum(np.square(diff))


def isSame(filename_1, filename_2):
    img_1 = Image.open(filename_1)
    img_2 = Image.open(filename_2)
    res_1 = FaceBoxRecognition_mtcnn.get_boxes(filename_1)
    res_2 = FaceBoxRecognition_mtcnn.get_boxes(filename_2)
    if (res_1 == []) or (res_2 == []):
        return False
    crop_1 = mtcnn(img_1, 'crop_1.jpg')
    crop_2 = mtcnn(img_2, 'crop_2.jpg')
    embedding_1 = resnet(crop_1.unsqueeze(0))
    embedding_2 = resnet(crop_2.unsqueeze(0))

    if distance(embedding_1, embedding_2) <= 0.8:
        return True
    else:
        return False