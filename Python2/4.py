from multiprocessing import Pool
from collections import Counter
import glob


def histog(file):
    histArray = Counter()
    try:
        file1=open(file)
        for x in file1:
          histArray[x.strip()] += 1
    except IOError:
        raise "Error: File does not appear to exist."
    file1.close()
    return histArray



if __name__ == "__main__":

    file = glob.glob("examp*")

    pool = Pool(processes=3)
    histMap = pool.map(histog, file)

    pool.close()
    pool.join()

    merged_hist = histMap[0]
    for h in histMap[1:]:
        merged_hist.update(h)

    for word, count in merged_hist.items():
        print("%s:  %s" % (word, count))


