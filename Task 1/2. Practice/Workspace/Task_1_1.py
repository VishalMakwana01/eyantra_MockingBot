
# Mocking Bot - Task 1.1: Note Detection

#  Instructions
#  ------------
#
#  This file contains Main function and note_detect function. Main Function helps you to check your output
#  for practice audio files provided. Do not make any changes in the Main Function.
#  You have to complete only the note_detect function. You can add helper functions but make sure
#  that these functions are called from note_detect function. The final output should be returned
#  from the note_detect function.
#
#  Note: While evaluation we will use only the note_detect function. Hence the format of input, output
#  or returned arguments should be as per the given format.
#
#  Recommended Python version is 2.7.
#  The submitted Python file must be 2.7 compatible as the evaluation will be done on Python 2.7.
#
#  Warning: The error due to compatibility will not be entertained.
#  -------------


# Library initialisation

# Import Modules
# DO NOT import any library/module
# related to Audio Processing here
import numpy as np
from scipy.stats import mode
import math
import struct
import wave
import os

# Teams can add helper functions
# Add all helper functions here

############################### Your Code Here ##############################################
######################Read File######################

def note_detect(audio_file):

    #   Instructions
    #   ------------
    #   Input   :   audio_file -- a single test audio_file as input argument
    #   Output  :   Detected_Note -- String corresponding to the Detected Note
    #   Example :   For Audio_1.wav file, Detected_Note = "A4"

	Detected_Note = ""
    # Add your code here
	sound_file = audio_file
	window_size = 2205    # Size of window to be used for detecting silence

	sampling_freq = 44100	# Sampling frequency of audio signal

	threshold = 600

	array = [130.81, 146.83, 164.81, 174.61, 196.00, 220.0, 246.94,
			 261.63, 293.66, 329.63, 349.23, 392.0, 440.0, 493.88,
			 1046.50, 1174.66, 1318.51, 1396.91, 1567.98, 1760.00, 1975.53,
    	     2093.00, 2349.32, 2637.02, 2793.83, 3135.96, 3520.00, 3951.07,
        	 4186.01, 4698.63, 5274.04, 5587.65, 6271.93, 7040.00, 7902.13]

	notes = ['C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3',
			 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4',
			 'C6', 'D6', 'E6', 'F6', 'G6', 'A6', 'B6',
	         'C7', 'D7', 'E7', 'F7', 'G7', 'A7', 'B7',
    	     'C8', 'D8', 'E8', 'F8', 'G8', 'A8', 'B8']
	
	file_length = sound_file.getnframes()
	sound = np.zeros(file_length)

	for i in range(file_length):
		data = sound_file.readframes(1)
		data = struct.unpack("<h", data)
		sound[i] = int(data[0])	
	sound = np.divide(sound, float(2**15))  # Normalize data in range -1 to 1
	soundSquare = np.zeros(file_length)
	soundSquare = np.square(sound)
	frequencyArray = []
	frequency = 0;
	dft = []

	i = 0
	j = 0
	k = 0    
	# traversing array with a fixed window_size
	while(i<=len(soundSquare)-window_size):
		s = 0.0
		j = 0
		while(j<=window_size):
			s = s + soundSquare[i+j]
			j = j + 1	
	# detecting the silence waves
		if s < threshold:
			if(i-k>window_size*4):
				dft = np.array(dft) # applying fourier transform function
				dft = np.fft.fft(sound[k:i])
				dft=np.argsort(dft)

				if(dft[0]>dft[-1] and dft[1]>dft[-1]):
					iMax = dft[-1]
				elif(dft[1]>dft[0] and dft[-1]>dft[0]):
					iMax = dft[0]
				else :	
					iMax = dft[1]
					# claculating frequency				
				frequencyArray.append((iMax*sampling_freq)/(i-k))
				dft = []
				k = i+1
		i = i + window_size

	print(frequencyArray)
	frequency = frequencyArray[-1]
	print("Frequency: " + str(frequency))
	#Detected_Note = notes[array.index(frequency)]
	#print(notes[array.index(frequency)])
	return Detected_Note

############################### Main Function ##############################################

if __name__ == "__main__":

    #   Instructions
    #   ------------
    #   Do not edit this function.

    # code for checking output for single audio file
    path = os.getcwd()

    file_name = path + "\Task_1.1_Audio_files\Audio_1.wav"
    audio_file = wave.open(file_name)

    Detected_Note = note_detect(audio_file)

    print("\n\tDetected Note = " + str(Detected_Note))

    # code for checking output for all audio files
    x = raw_input("\n\tWant to check output for all Audio Files - Y/N: ")

    if x == 'Y':

        Detected_Note_list = []

        file_count = len(os.listdir(path + "\Task_1.1_Audio_files"))

        for file_number in range(1, file_count):

            file_name = path + "\Task_1.1_Audio_files\Audio_" + str(file_number)+".wav"
            audio_file = wave.open(file_name)

            Detected_Note = note_detect(audio_file)

            Detected_Note_list.append(Detected_Note)

        print("\n\tDetected Notes = " + str(Detected_Note_list))
