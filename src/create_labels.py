import os
import sys
import pandas as pd
import os.path as path 
from logger import logging
from exception import Spoken_Digit_Exception
from constants.file_paths import labels_path



class labels:
    def __init__():
        pass

    def get_labels():
        try:
            # get file names and store it in list
            all_files = []
            for i in os.walk("src/recordings"):
                all_files.append(i)
            all_files = all_files[0][2] 


            # generate labels from file name
            labels = []
            for i in all_files:
                labels.append(i[0])

            # create dataframe
            df_audio = pd.DataFrame(list(zip(all_files, labels)),columns =['path', 'label'])

            label_path = path.abspath(path.join(labels_path))
            logging.info("Labeling completed")
            
            return df_audio.to_csv(label_path,index=False)

        except  Exception as e:
                raise  Spoken_Digit_Exception(e,sys)

labels.get_labels()


