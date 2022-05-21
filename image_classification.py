from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
from keras.applications.vgg16 import preprocess_input


class ImagaeClassification:
    def __init__(self):
        self.model = load_model('image_classification.h5')
        
    def predict(self, path):
        my_image = load_img(path, target_size=(224, 224), grayscale=True)

        #preprocess the image
        my_image = img_to_array(my_image)
        my_image = my_image.reshape(1, my_image.shape[0], my_image.shape[1], my_image.shape[2])
        # my_image = preprocess_input(my_image)

        #make the prediction
        prediction = self.model.predict(my_image)

        return self.convertToString(prediction[0][0])

    def convertToString(self, modelOutput):

        if modelOutput == 0:
            return "Result: COVID"
        else:
            return "Result: NORMAL"