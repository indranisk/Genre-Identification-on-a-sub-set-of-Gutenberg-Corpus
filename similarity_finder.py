import pandas as pd
import csv
from sklearn.metrics.pairwise import cosine_similarity

FILE_NAME = "feature_lables_Bknames.csv"
TOP_K_RESULTS = 5


def read_csv(file_name):
    csv_data = pd.read_csv(file_name, sep=',', engine='python')
    return csv_data


if __name__ == "__main__":

    data = read_csv(FILE_NAME)
    # print(data)

    data_values = data.drop("BOOK_ID", axis=1).drop("Book_Name", axis=1).drop("guten_genre", axis=1)
    data_ids = data["BOOK_ID"].tolist()
    book_names = data["Book_Name"].tolist()
    guten_genre = data["guten_genre"].tolist()
    name_genre_dict = dict(zip(data_ids, zip(book_names, guten_genre)))
    print(data_ids)
    similarities = cosine_similarity(data_values)
    # print(similarities)

    while 1:
        book_id = input("Enter Book ID :")
        try:
            index = data.index[data["BOOK_ID"] == book_id].tolist()[0]
            # print(index)
            # print(similarities[index])
            zipped_vals = zip(data_ids, similarities[index])
            sorted_vals = sorted(zipped_vals, key=lambda t: t[1])[-TOP_K_RESULTS - 1:]
            # print(sorted_vals[-TOP_K_RESULTS - 1:])
            sorted_vals.reverse()
            # print(sorted_vals)
            # print(book_id)
            for x in sorted_vals:
                # if x[0] != book_id:
                # print(x[0])
                print(x[0], name_genre_dict[x[0]])
        except:
            print("BOOK NOT FOUND !!")
