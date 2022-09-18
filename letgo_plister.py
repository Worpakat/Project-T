from bs4 import BeautifulSoup
import requests

from product import Product 


class LetgoProductLister:  #url den html file isteyip return etmemize yarıyor
    
    __search_term__ = ""
    __input_searching_url__ = f"https://www.letgo.com/items/q-{__search_term__}?isSearchCall=true"
    __headers__ = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36' } 
    
    @classmethod
    def __get_input__(cls):
        space_plus_dict = {32 : 45}
        search_term = input("What product do you search for:")
        search_term = search_term.strip().translate(space_plus_dict) #strip() sağ soldaki boşlukları siliyor.
        #translate(): içinde verilen dictionaryde ki key lerin ascii sayı karşılığındaki karakterleri value ascii karşılığına çeviriyor
        #Biz burda boşlukları '+' ya çevirdik. url de o şekilde olduğu için
        # print(search_term)
        return search_term
    
    @classmethod
    def __modify_input__(cls, search_term):
        space_plus_dict = {32 : 45}
        search_term = search_term.strip().translate(space_plus_dict) #strip() sağ soldaki boşlukları siliyor.
        #translate(): içinde verilen dictionaryde ki key lerin ascii sayı karşılığındaki karakterleri value ascii karşılığına çeviriyor
        #Biz burda boşlukları '-' ye çevirdik. url de o şekilde olduğu için
        return search_term


    @classmethod
    def __get_searching_url__(cls, search_term):  #search_term in letgo urls halini return eder
        searching_url = f"https://www.letgo.com/items/q-{search_term}?isSearchCall=true"
        return searching_url

    @classmethod
    def __get_bsobj_from_url__(cls, url, headers = None):
        req = requests.get(url = url, headers = headers)
        bs_obj = BeautifulSoup(req.text,"html.parser")
        return bs_obj

    @classmethod
    def __list_page__(cls, page_bs):
        item_list = []

        product_list_tag = page_bs.find("ul", attrs={"data-aut-id":"itemsList"})
        # product_list_tag = page_bs.find("ul", class_="rl3f9 _3mXOU") #üsttekiyle aynı şeyi buluyor
    
        product_list = product_list_tag.find_all("li", attrs={"data-aut-id":"itemBox"}) 
        #item box olmayan kutuyu dahil etmemek için "contents" deilde bu şekilde liste aldım
        print("ITEM COUNT:",len(product_list))
        print() 

        for product in product_list:
            title_tag = product.find("span", attrs={"data-aut-id":"itemTitle"}) 
            price_tag = product.find("span", attrs={"data-aut-id":"itemPrice"})         
            location_tag = product.find("span", attrs={"data-aut-id":"item-location"})  
            link_tag = product.a #<a> tag inde href

            title = title_tag.get_text()       #product title
            price = price_tag.get_text()       #price
            location = location_tag.get_text() #location
            link = "https://www.letgo.com" + link_tag["href"]
            
            product = Product(title, price, location, link)

            item_list.append(product)
        
        return item_list

    @classmethod
    def __run_app__(cls, _searh_term_):
        # search_term = cls.__GetInput__()
        search_term = cls.__modify_input__(search_term = _searh_term_)
        search_url = cls.__get_searching_url__(search_term)
        search_result_bs = cls.__get_bsobj_from_url__(url = search_url, headers = cls.__headers__ ) #arama sonucu sayfasının bs objesini aldık
        
        # print(search_result_bs.prettify())
        print(f"{search_term}(link)={search_url}")

        current_page_bs = search_result_bs
        item_list = cls.__list_page__(current_page_bs)

        return item_list
    
    @classmethod
    def __run__(cls):
        search_term = cls.__get_input__()
        search_url = cls.__get_searching_url__(search_term)
        search_result_bs = cls.__get_bsobj_from_url__(url=search_url, headers=cls.__headers__ ) #arama sonucu sayfasının bs objesini aldık
        
        # print(search_result_bs.prettify())
        print(search_url)

        current_page_bs = search_result_bs
        item_list = cls.__list_page__(current_page_bs)

        for p in item_list:
            print(p[0])
            print(p[1])
            print(p[2])
            print()

        return item_list

    
    def run(self,search_term=""):
        # self.__run__()
        return self.__run_app__(search_term)
        