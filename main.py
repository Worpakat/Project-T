from itertools import product
from bs4 import BeautifulSoup
import requests #url den html file isteyip return etmemize yarıyor
from letgo_plister import LetgoProductLister

def get_bsobj_from_url(_url_, _headers_ = None):
    req = requests.get(url = _url_, headers = _headers_)
    bs_obj = BeautifulSoup(req.text, "html.parser")
    return bs_obj

# headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36' } 
# # "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
# letgo_url = "https://www.letgo.com/"
# letgo_bs = Get_BSobj_From_URL(letgo_url,headers)

##Şimdiii.: Şu "HEADER" olayından bahsedelim. Bazı sitelerde biliyosun bot detection mevzusu mevcut ve request etmeni engelliyor.
#Biz ama requestmizi header kullanarak yaparsak bunu program değilde bilgisayrdan elle yapmış gibi gösteriyoruz. 
#"HTTP headers let the client and the server pass additional information with an HTTP request or response."
#Biz header da ek bilgileri yazarak(bunlarda bizim browser ve işletim sistemi bilgilerimiz gibi gözüküyor.) request'i
#browserdan yapmış gibi gösteriyoruz. Bu header ı nası bulduğumuza gelirsek 
# https://mkyong.com/computer-tips/how-to-view-http-headers-in-google-chrome/
#Direk bu sorunu nasıl çözdük dersek: https://www.quora.com/Why-doesnt-Pythons-requests-get-work-for-websites-like-Adidas-com
#BTW sorun şuydu: Letgo dan request alamıyodu, hatada vermiyodu, öle kod orda takılıp kalıyodu. Header ekleyince çözüldü.

# print(letgo_bs)
# print("OVER")

#Search=telefon : https://www.letgo.com/items/q-telefon?isSearchCall=true
#Search=telefon : https://www.letgo.com/items/q-saat?isSearchCall=true
#Search=gözlük : https://www.letgo.com/items/q-g%C3%B6zl%C3%BCk?isSearchCall=true    
# https://www.letgo.com/items/q-kad%C4%B1n-ayakkab%C4%B1?isSearchCall=true   ___birden fazla kelime arasına '-' koyuyor
#Gördüğün gibi belirli bir arama urlsinin belli yerinde arama kelimemiz var. 
import webbrowser

webbrowser.register('chrome', None,	webbrowser.GenericBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
#manuel url açmak için kullanılacak browaser: bilgi için: https://pythonexamples.org/python-open-url-in-chrome-browser/
letgo_pl = LetgoProductLister()

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

from functools import partial 

class RootWidget(Widget):
    products_gl = ObjectProperty(None)
    search_text_input = ObjectProperty(None)
    letgo_pl = LetgoProductLister()

    product_buttons = [];

    def __on_release_product__(self, url, instance):
        """product button method: product'ın web page ini açar browserda"""
        webbrowser.get('chrome').open(url)
        

    def on_release_search(self):
        search_items_list = self.letgo_pl.run(self.search_text_input.text) 

        for product_button in self.product_buttons:
            self.products_gl.remove_widget(product_button)
            self.product_buttons.remove(product_button)

        for product in search_items_list:
            product_btn = Button(text = product.title + product.price + product.location + "\n" + product.link)
            self.product_buttons.append(product_btn)
            product_btn.bind(on_press = partial(self.__on_release_product__, product.link))
            self.products_gl.add_widget(product_btn)



class LetgoProductListerApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    letgo_pl_app = LetgoProductListerApp()
    letgo_pl_app.run()