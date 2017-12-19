from keras.preprocessing import image
from keras.models import load_model
from imagenet_utils import preprocess_input
import numpy as np
from imagenet_utils import preprocess_input
import os
import h5py



def get_image(data_path):
	load_data = []
	images = os.listdir(os.getcwd() + "/" + data_path)
	if ".DS_Store" in images:
		images.remove(".DS_Store")
	for img in images:
		load_img = image.load_img(os.getcwd() + "/" + data_path + "/" + img , target_size=(224, 224))
		x = image.img_to_array(load_img)
		x = np.expand_dims(x, axis=0)
		x = preprocess_input(x)
		x = x.reshape(224,224,3)
		load_data.append(x)
	return load_data,images

def get_predictions(predicted_labels1, predicted_labels2):
	predicted_final=[]
	for i in range(len(images)):
		if predicted_labels2[i]==1:
			predicted_final.append(2)
		else:
			if predicted_labels1[i]==0:
				predicted_final.append(0)
			else:
				predicted_final.append(1)
	return predicted_final

def write_to_file(results,names):
	file = open("result.txt","w")
	print ("\nResults:\n")
	for i in range(len(results)):
		if(results[i] == 0):
			file.write(names[i] + " : " + "No Lens\n")
			print (names[i] + " : " + "No Lens")
		elif(results[i] == 1):
			file.write(names[i] + " : " + "Soft Lens\n")
			print (names[i] + " : " + "Soft Lens")
		else:
			file.write(names[i] + " : " + "Textured Lens\n")
			print (names[i] + " : " + "Textured Lens")
	file.close()

if __name__ == '__main__':

	# get all images in the folder 'images'
	images,names = get_image('images')

	# load the two models
	model_1 = load_model('model1.h5')
	model_2 = load_model('model2.h5')

	# predict labels from model_1 and model_2 for all the images
	predicted_labels1 = model_1.predict(np.array(images))
	predicted_labels1 = np.argmax(predicted_labels1, axis=1)
	predicted_labels2 = model_2.predict(np.array(images))
	predicted_labels2 = np.argmax(predicted_labels2, axis=1)

	# get final predictions for all the images
	results = get_predictions(predicted_labels1, predicted_labels2)

	# write the results to result.txt
	write_to_file(results,names)

