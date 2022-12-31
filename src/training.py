import pandas as pd
import numpy as np
from sklearn.utils import shuffle
from constants.file_paths import labels_path

df_audio = pd.read_csv(labels_path)

# shuffle the data

df_audio = shuffle(df_audio, random_state=33)
# create dependant and independant vriable
X = df_audio['path']
y = df_audio['label']
# train test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, stratify=y, random_state = 45)

