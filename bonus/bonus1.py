filenames = ["1.presentation.txt", "2.Report.txt"]

for filename in filenames:
    filename = filename.replace(".", "-", 1)
    print(filename)