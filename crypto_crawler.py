import requests
import bs4
def getData(infor):
    request = requests.get(infor[0])
    data = bs4.BeautifulSoup(request.text, "html.parser")
    titles = data.find_all("h3", class_="jeg_post_title")
    infor = [""]
    i=1
    for title in titles:
        if title.a != None:
            infor.insert(i,title.a.text+" "+title.a["href"]+ "\n")
            i=i+1
            if i >= 11:
                break
    prePage = data.find("a", class_ = "page_nav next")
    newUrl =  prePage["href"]
    infor[0]= newUrl
    return infor
infor= ["https://www.blocktempo.com/2022"]
print("-------------------------")
files_num = input("請輸入產生檔案數")
print("設定檔案數為 ",files_num," 份")
pages_num = input("請輸入每份檔案所需的網站資料頁數")
print("設定每份檔案資料頁數為 ",pages_num," 份")
for x in range(1,int(files_num)+1,1):
    file = open("crypto"+str(x)+".txt","w",encoding = "utf-8")
    for i in range(1,int(pages_num)+1,1):
        file.write("---------------第"+str(i)+"頁---------------\n")
        file.write(infor[0]+"\n")
        infor= getData(infor)
        for inf in infor[1:]:
            file.write(inf)
    file.close()
print("爬蟲完畢")
