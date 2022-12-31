import os
import pandas as pd



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

            movie_path = path.abspath(path.join(movie_data_path))
            logging.info("Fetching movies data done")
            logging.info("{} data points are fetched".format((end_index-start_index)))
            return new_df.to_csv(movie_path,mode='a', index=False, header=False)


