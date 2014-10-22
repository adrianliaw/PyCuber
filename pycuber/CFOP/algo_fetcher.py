from io import BytesIO
from PIL import Image
from bs4 import BeautifulSoup
import requests
import csv

prefix = "http://cubewhiz.com/"

def get_oll_algos(soup):
    tbodies = soup.find_all("tbody")
    result = []
    for tbody in tbodies:
        algos = tbody.find_all("tr")[1:]
        for a in algos:
            print("Algorithm found: O{0:02d}".format(int(a.td.get_text())))
            info = a.find_all("td")
            entry = []
            entry.append(int(info[0].get_text()))
            entry.append(oll_case_identifier(oll_img(str(info[1].img["src"]))))
            print(info[2].get_text())
            if entry[0] == 19:
                entry.append(str(info[2].b.get_text().replace("(", "", 10).replace(")", "", 10)) + " x'")
            else:
                entry.append(str(info[2].b.get_text().replace("(", "", 10).replace(")", "", 10)))
            result.append(tuple(entry))
    result.sort()
    return result

def oll_img(url):
    pic = requests.get(prefix + url)
    while pic.status_code >= 500:
        pic = requests.get(prefix + url)
    while True:
        try:
            image = Image.open(BytesIO(pic.content))
            image = image.convert("RGB")
            print("Image loaded: {0}".format(url))
            return image
        except IOError:
            continue

def oll_case_identifier(image):
    result = ""
    for point in [(0, 13), (0, 38), (0, 63), (13, 75), (38, 75), (63, 75), (75, 63), (75, 38), (75, 13), (63, 0), (38, 0), (13, 0)]:
        result += str(int(image.getpixel(point) == (255, 255, 0)))
    print("Result case identifier: {0}".format(result))
    return result

def write_oll_file(algoset, filename):
    with open(filename, "w") as f:
        writer = csv.writer(f, delimiter=",")
        print("Writing into {0}...".format(filename))
        for a in algoset:
            writer.writerow(["O{0:02d}".format(a[0])] + list(a[1:]))
        print("Successfully wrote into file.")
    return True

def oll_algos():
    print("Starting...")
    page = requests.get(prefix + "oll.php")
    print("Page loaded.")
    soup = BeautifulSoup(page.text)
    print("Page parsed.")
    algoset = get_oll_algos(soup)
    print("Algorithm set:")
    for alg in algoset:
        print(alg)
    write_oll_file(algoset, "oll_algos.csv")
    print("Ended.")

def get_pll_algos(soup1, soup2):
    tbodies1 = soup1.find_all("tbody")
    tbodies2 = soup2.find_all("tbody")
    result = []
    for i in range(len(tbodies1)):
        tbody1 = tbodies1[i]
        tbody2 = tbodies2[i]
        algos = tbody1.find_all("tr")[1:]
        views = tbody2.find_all("tr")[1:]
        for j in range(len(algos)):
            a = algos[j]
            v = views[j]
            print("Algorithm found: {0}-perm".format(a.td.get_text()))
            info = a.find_all("td")
            entry = []
            entry.append(info[0].get_text())
            entry.append(pll_case_identifier(info[0].get_text()))
            print(info[2].get_text())
            entry.append(str(info[2].b.get_text().replace("(", "", 10).replace(")", "", 10).split("\r\n")[0]))
            result.append(tuple(entry))
    result.sort()
    return result

def pll_case_identifier(case_name):
    views = []
    for i in range(1, 5):
        if len(views) < i:
            img = requests.get(prefix + "images/pllrec/{0}view{1}.gif".format(case_name, (i if case_name not in "AaAbE" else i%4+1)))
            while img.status_code >= 500:
                img = requests.get(prefix + "images/pllrec/{0}view{1}.gif".format(case_name, (i if case_name not in "AaAbE" else i%4+1)))
            while True:
                try:
                    views.append(Image.open(BytesIO(img.content)).convert("RGB"))
                    print("Image loaded: {0}".format("images/pllrec/{0}view{1}.gif".format(case_name, (i if case_name not in "AaAbE" else i%4+1))))
                except IOError:
                    continue
                else:
                    break
    result = ""
    for img in views:
        for point in [(20, 50), (35, 60), (55, 70)]:
            colour = img.getpixel(point)
            if colour == (237, 0, 0): result += "F" if case_name not in "AaAbE" else "L"
            elif colour == (0, 216, 0): result += "R" if case_name not in "AaAbE" else "F"
            elif colour == (254, 160, 0): result += "B" if case_name not in "AaAbE" else "R"
            elif colour == (0, 0, 241): result += "L" if case_name not in "AaAbE" else "B"
    result = result[-3:] + result[:-3]
    print("Result case identifier: {0}".format(result))
    return result

def write_pll_file(algoset, filename):
    with open(filename, "w") as f:
        writer = csv.writer(f, delimiter=",")
        print("Writing into {0}...".format(filename))
        for a in algoset:
            writer.writerow(["{0}-perm".format(a[0])] + list(a[1:]))
        print("Successfully wrote into file.")
    return True

def pll_algos():
    print("Starting...")
    page = requests.get(prefix + "pll.php")
    print("Page1 loaded")
    rec_page = requests.get(prefix + "pllrecognition.php")
    print("Page2 loaded")
    soup1 = BeautifulSoup(page.content)
    print("Page1 parsed")
    soup2 = BeautifulSoup(rec_page.content)
    print("Page2 parsed")
    algoset = get_pll_algos(soup1, soup2)
    print("Algorithm set:")
    for algo in algoset:
        print(algo)
    write_pll_file(algoset, "pll_algos.csv")
    print("Ended.")



