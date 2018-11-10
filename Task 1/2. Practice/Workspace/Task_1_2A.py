
## Mocking Bot - Task 1.2 A: Notes and Onset Detection

#  Instructions
#  ------------
#
#  This file contains Main function and onset_detect function. Main Function helps you to check your output
#  for practice audio files provided. Do not make any changes in the Main Function.
#  You have to complete only the onset_detect function. You can add helper functions but make sure
#  that these functions are called from onset_detect function. The final output should be returned
#  from the onset_detect function.
#
#  Note: While evaluation we will use only the onset_detect function. Hence the format of input, output
#  or returned arguments should be as per the given format.
#  
#  Recommended Python version is 2.7.
#  The submitted Python file must be 2.7 compatible as the evaluation will be done on Python 2.7.
#  
#  Warning: The error due to compatibility will not be entertained.
#  -------------


## Library initialisation

# Import Modules
# DO NOT import any library/module
# related to Audio Processing here
import numpy as np
import math
import wave
import os

# Teams can add helper functions
# Add all helper functions here

############################### Your Code Here #############################################

def onset_detect(audio_file):
	
	#   Instructions
	#   ------------
	#   Input 	:	audio_file -- a single test audio_file as input argument
	#   Output	:	1. Onsets -- List of Float numbers corresponding
	#							 to the Note Onsets (up to Two decimal places)
	#				2. Detected_Notes -- List of string corresponding
	#									 to the Detected Notes
	#	Example	:	For Audio_1.wav file,
	# 				Onsets = [0.00, 2.15, 4.30, 7.55]
	#				Detected_Notes = ["F4", "B3", "C6", "A4"]

	Onsets = []
	Detected_Notes = []

	# Add your code here

	return Onsets, Detected_Notes


############################### Main Function #############################################

if __name__ == "__main__":

	#   Instructions
	#   ------------
	#   Do not edit this function.

	# code for checking output for single audio file
	path = os.getcwd()
	
	file_name = path + "\Task_1.2A_Audio_files\Audio_1.wav"
	audio_file = wave.open(file_name)
	
	Onsets, Detected_Notes = onset_detect(audio_file)

	print("\n\tOnsets = " + str(Onsets))
	print("\n\tDetected Notes = " + str(Detected_Notes))

	# code for checking output for all audio files
	x = raw_input("\n\tWant to check output for all Audio Files - Y/N: ")
		
	if x == 'Y':

		Onsets_list = []
		Detected_Notes_list = []

		file_count = len(os.listdir(path + "\Task_1.2A_Audio_files"))

		for file_number in range(1, file_count):

			file_name = path + "\Task_1.2A_Audio_files\Audio_"+str(file_number)+".wav"
			audio_file = wave.open(file_name)

			Onsets, Detected_Notes = onset_detect(audio_file)
			
			Onsets_list.append(Onsets)
			Detected_Notes_list.append(Detected_Notes)

		print("\n\tOnsets = " + str(Onsets_list))
		print("\n\tDetected Notes = " + str(Detected_Notes_list))


