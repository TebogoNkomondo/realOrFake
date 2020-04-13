# import itertools
# import os
# import csv

# file_in = './train.csv'
# file_out = 'out.csv'
# file_temp = '_temp.csv'

# with open(file_in, "rt") as f_input, open(file_out, "ab") as f_output, open(file_temp, "wb") as f_temp:
#     csv_input = csv.reader(f_input)

#     # Append first 50 rows to file_out
#     csv.writer(f_output).writerows(itertools.islice(csv_input, 0, 10000))

#     # Write the remaining rows from file_in to file_temp
#     csv.writer(f_temp).writerows(csv_input)

# # Rename f_temp to file_in, first remove existing file_in then rename temp file
# os.remove(file_in)
# os.rename(file_temp, file_in)

val = ["hello", "world"]

for indexr, iterr1 in enumerate(val):
    print("%s is %s" % (indexr, iterr1))