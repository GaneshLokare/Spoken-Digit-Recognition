import os
import sys
import pandas as pd
import os.path as path 
from src.constants.file_paths import labels_path




#Creating a dataframe(name=df_audio) with two columns(path, label).   
#Eg: 0_jackson_0 --> 0 (label)
#0_jackson_43 --> 0 (label)
all_files = os.listdir('src/recordings')
df_audio = pd.DataFrame()
df_audio['path'] = ['src/recordings/' + ele for ele in all_files]
df_audio['label'] = [ele.split('_')[0] for ele in all_files]

label_path = path.abspath(path.join(labels_path))
           
df_audio.to_csv(label_path,index=False)