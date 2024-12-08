filenames = ["1.doc", "1.report", "1.presentation"]
#
# for filename in filenames:
#     file = filename.replace(".", "-") + ".txt"
#     print(file)

new_filenames = [f"{filename.replace('.', '-')}.txt" for filename in filenames]
print(new_filenames)