def readd_large_file(filename):
    with open(filename,"r") as f:
        for line in f:
            yield line.strip()

        for line in readd_large_file("hosiptal_logs.txt"):
            print(Line)