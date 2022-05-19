from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
from keras.applications.vgg16 import preprocess_input


class ImagaeClassification:
    def __init__(self):
        self.model = load_model('image_classification')
        
    def predict(self, path):
        my_image = load_img(path, target_size=(224, 224))

        #preprocess the image
        my_image = img_to_array(my_image)
        my_image = my_image.reshape((1, my_image.shape[0], my_image.shape[1], my_image.shape[2]))
        my_image = preprocess_input(my_image)

        #make the prediction
        prediction = self.model.predict(my_image)

        return self.convertToString(prediction)

    def convertToString(self, modelOutput):
        pred_class = modelOutput.argmax(axis=-1) 

        if pred_class == 0:
            return "COVID"
        else:
            return "NORMAL"