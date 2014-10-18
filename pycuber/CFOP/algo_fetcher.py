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
            entry.append(str(info[2].b.get_text().replace("(", "", 10).replace(")", "", 10)))
            result.append(tuple(entry))
    result.sort()
    return result

def get_img(url):
    pic = requests.get(prefix + url)
    image = Image.open(BytesIO(pic.content))
    image = image.convert("RGB")
    print(image)
    return image

def get_case_identifier(image):
    result = ""
    for point in [(0, 13), (0, 38), (0, 63), (13, 75), (38, 75), (63, 75), (75, 63), (75, 38), (75, 13), (63, 0), (38, 0), (13, 0)]:
        result += str(int(image.getpixel(point) == (255, 255, 0)))
    return result

def write_to_file(algoset, filename):
    with open(filename, "w") as f:
        writer = csv.writer(f, delimiter=",")
        for a in algoset:
            #print([bytes("O{0:02d}".format(a[0]), "UTF-8")] + list(map(lambda x:bytes(x, "UTF-8"), a[1:])))
            #writer.writerow([bytes("O{0:02d}".format(a[0]), "UTF-8")] + list(map(lambda x:bytes(x, "UTF-8"), a[1:])))
            writer.writerow(["O{0:02d}".format(a[0])] + list(a[1:]))
    return True

if __name__ == "__main__":
    page = requests.get(prefix + "oll.php")
    soup = BeautifulSoup(page.text)
    algoset = get_all_algos(soup)
    for alg in algoset:
        print(alg)
    write_to_file(algoset, "oll_algos.csv")
