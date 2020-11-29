from facenet_pytorch import InceptionResnetV1
import matplotlib.pyplot as plt
import numpy as np
import torch
from mtcnn import MTCNN

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print('Running on device: {}'.format(device))

mtcnn = MTCNN()

def crop(filename, x0, y0, width, height):
    data = plt.imread(filename)
    return data[y0:y0 + height , x0:x0 + width, :]


def draw_facebox(filename, result_list):
    data = plt.imread(filename)
    plt.imshow(data)
    ax = plt.gca()

    for result in result_list:
        x, y, width, height = result
        rect = plt.Rectangle((x, y), width, height, fill=False, color='green')
        ax.add_patch(rect)
    plt.show()


detector = MTCNN()

def get_boxes(filename):
    data = plt.imread(filename)
    faces = detector.detect_faces(data)
    res = []
    for result in faces:
        x0, y0, width, height = result['box']
        res.append(crop(filename, x0, y0, width, height))
    return res