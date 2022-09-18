# Project-T
 A project for determine to bargain goods on exact 2nd hand good trading web sites.
 
 This is a very early personal project. Not just for exercise.
 I started this project on late August 2022 days and worked on 4-5 days.
 Then took a break because of an other project. But I want to continue on this soon.

# README BEFORE USE
For run program: Run "main.py"
Because of this is a verry early project. Can be a lot of problems and bugs.
One of them: If you make a search second or third time after running the program, any bug may occur and crash program. In this case shut down program and re-open it.
Some search terms may not work as intended.
Program using just one web site for now. "https://www.letgo.com/"
Because of this web site's language is Turkish. You have to use Turkish terms.
Examples for trying:(Eng:Tr)
"Shoes":"Ayakkabı"      "Shirt":"Gömlek"        "Eye Glass":"Gözlük"        "Bag/Satchel":"Çanta"       "Watch":"Saat"      "Carpet":"Halı"     "Phone":"Telefon"
"Seat":"Koltuk" etc. 
You can use translate to Turkish what you want to search for.     

# Used modules/libraries
"Kivy": For GUI     "Beatiful Soup and Selenium":Web scraping and browser automation.       
"requests":For returning HTML file via URL.

# What is this project going to do?
Basically, this program is going to find bargain goods on 2nd hand goods trading web sites. (As said above.)
1st It searches for typed search term. For example: Shoes, Car, Watch etc.
2nd It scrapes products from web sites search result page.
3rd It lists products and makes assesment for the actual value and that spesific 2nd hand goods' value.
4th Then it's choose bargain buy price goods. For We can buy that goods and sell for profit again in real life.

So how is this price and value assesment thing going to work?: Several methods will be used:
For example: What is a specific category's average "second hand price / unused price" rate.
If a second hand goods rate less than average rate, then it maybe a bargain goods. 
"Maybe" because of it maybe a worn goods and that is why this goods' "second hand price / unused price" rate less than average.
This is just one of them. It is going to be improved in time.
As you see this project not about just coding or software engineering. 
It's also about some skills and knowledge about trading and economics.
I research that topics as I need.

# Current Version of Program
*Have a basic GUI made with "Kivy". You can make a search for a product category.
*Program makes scraping for products from search result page.
*Search results page link is going to be printed at terminal. You can check products in order.
*And lists that results on GUI with buttons. Buttons' text: product's title, price and location.
*If you click a button, it is going to open product's web page on browser.
*Just made for one web site for now. "https://www.letgo.com/" (New web sites will be added later.) 

# !ATTENTION LAST NOTE!
Because of I started this as a personal project, most of comments in Turkish. I'm going to convert them English soon.
Annd I started use Git newly :D 
