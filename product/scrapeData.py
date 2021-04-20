import requests
from bs4 import BeautifulSoup

def amazon_scrape(colors,tag):  
   
    # colors = colors[:2]
    baseurl = "https://www.amazon.in/"
    base = "https://www.amazon.in/"
    gender = "women"

    #if more than one color:
    # color = 'red+blue+green'
    color=[]
    urls=[]
   

    for i in colors:
        color.append(i)

    

    for element in tag:
        category =element 
        for col in color:
            url = baseurl + 's?k=' + gender + '+' + col + '+' + category + '&ref=nb_sb_noss_2'
            url = url.replace('++', '+')
            print(url)
            urls.append(url)
    
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
    ls=[]
    for url in urls:
        
        r = requests.get(url, headers = headers)
        soup = BeautifulSoup(r.content, 'html.parser')

        productlist = soup.find_all('div', class_ = "s-asin")

    # productlist
    # print(productlist)

        for item in productlist:
            
            l = []
            for link, title, des, price, image in zip(item.find_all('a', href = True), item.find_all('h5', class_ = 's-line-clamp-1'), item.find_all('span', class_ = "a-size-base-plus a-color-base a-text-normal"), item.find_all('span', class_ = 'a-offscreen'), item.find_all('img', src = True)):
                l.append(base + link['href'])
                l.append(title.get_text() + des.get_text())
                l.append(price.get_text())
                l.append(image['src'])
                ls.append(l)
                
    return ls
    





def koovs_scrape(colors,tag):      

    baseurl = "https://www.koovs.com/"
    base = "https://www.koovs.com"
    gender = "women"

    #if more than one color:
    # color = 'red+blue+green'
    color=[]
    urls=[]
  

    for i in colors:        
        color.append(i.replace('+', '-'))

    

    for element in tag:
        category =element 
        for col in color:            
            url = baseurl + gender + '-' + col + '-' + category 
            url = url.replace('--', '-')
            print(url)
            urls.append(url)
            
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
    ls=[]
    for url in urls:
        r = requests.get(url, headers = headers)
        soup = BeautifulSoup(r.content, 'html.parser')

        productlist = soup.find_all('li', class_ = "imageView")

  

    for item in productlist:
        
        l = []
        for link, title, des, price, image in zip(item.find_all('a', href = True), item.find_all('span', class_ = "product_title clip-text brandName"), item.find_all('span', class_ = "product_title clip-text productName"), item.find_all('span', class_ = 'hide'), item.find_all('img', src = True)):
            l.append(base + link['href'])
            l.append(title.get_text()+ " " + des.get_text())
            l.append(price.get_text())
            l.append(image['src'])
            ls.append(l)
              
    return ls



    



