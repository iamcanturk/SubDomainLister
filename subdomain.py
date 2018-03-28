import urllib.request
text = input("Web Sitesini Giriniz: ")
path = "https://dnsdumpster.com/static/map/"+text+".png"
urllib.request.urlretrieve(path,text+".png")
print("Resim Uygulamanın Olduğu Klasöre İndirilmiştir.")