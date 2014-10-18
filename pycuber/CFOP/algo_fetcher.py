from io import BytesIO
from PIL import Image
from bs4 import BeautifulSoup
import requests
import csv

prefix = "http://cubewhiz.com/"

def get_all_algos(soup):
    tbodies = soup.find_all("tbody")
    result = []
    for tbody in tbodies:
        algos = tbody.find_all("tr")[1:]
        for a in algos:
            print("Algorithm found: O{0:02d}".format(int(a.td.get_text())))
            info = a.find_all("td")
            entry = []
            entry.append(int(info[0].get_text()))
            while True:
                try:
                    entry.append(get_case_identifier(get_img(str(info[1].img["src"]))))
                except IOError:
                    continue
                else:
                    break
            print(info[2].get_text())
            if entry[0] == 19:
                entry.append(str(info[2].b.get_text().replace("(", "", 10).replace(")", "", 10)) + " x'")
            else:
                entry.append(str(info[2].b.get_text().replace("(", "", 10).replace(")", "", 10)))
            result.append(tuple(entry))
    result.sort()
    return result

def get_img(url):
    pic = requests.get(prefix + url)
    image = Image.open(BytesIO(pic.content))
    image = image.convert("RGB")
    print("Image loaded: {0}".format(url))
    return image

def get_case_identifier(image):
    result = ""
    for point in [(0, 13), (0, 38), (0, 63), (13, 75), (38, 75), (63, 75), (75, 63), (75, 38), (75, 13), (63, 0), (38, 0), (13, 0)]:
        result += str(int(image.getpixel(point) == (255, 255, 0)))
    print("Result case identifier: {0}".format(result))
    return result

def write_to_file(algoset, filename):
    with open(filename, "w") as f:
        writer = csv.writer(f, delimiter=",")
        print("Writing into {0}...".format(filename))
        for a in algoset:
            writer.writerow(["O{0:02d}".format(a[0])] + list(a[1:]))
        print("Writed.")
    return True

if __name__ == "__main__":
    print("Starting...")
    page = requests.get(prefix + "oll.php")
    print("Page loaded.")
    soup = BeautifulSoup(page.text)
    print("Page parsed.")
    algoset = get_all_algos(soup)
    print("Algorithm set:")
    for alg in algoset:
        print(alg)
    write_to_file(algoset, "oll_algos.csv")
    print("Ended.")
