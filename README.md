# TelegramTradeMsgBacktestML

## Table of Contents
1. [Introduction](#introduction)
2. [Test on HuggingFace](#test-on-huggingface)
3. [Repository Contents](#repository-contents)
4. [Custom Order](#custom-order)
5. [Contact Information](#contact-information)
6. [Related GitHub Repositories](#github-repositories)
7. [Other Products](#other-products)
8. [YouTube Videos](#youtube-videos)
9. [Blog and Apps](#blog-and-apps)
10. [Related GitLab Repositories](#gitlab-repositories)

---

## Introduction
Backtest telegram messages from a whole channel about trading (stocks or crypto) using Machine Learning (Named Entity Recognition or Token Classification).

---

## Test on HuggingFace
![Model Screenshot](https://user-images.githubusercontent.com/12392345/193395791-2a586c59-1ee2-433d-9f27-cc8e90b8e679.png)  
[Link to test this model](https://huggingface.co/hemangjoshi37a/autotrain-ratnakar_1000_sample_curated-1474454086?text=SUPER+DUPER+DELIVERY%0A%0ADELIVERY+%3A+BUY+BEPL+ABOVE+117+SL+103+TARGET+135+-+155+-+175)

---

## Repository Contents

1. **Label Data using LabelStudio**  
Convert:  
![LabelStudio](https://user-images.githubusercontent.com/12392345/193394190-3ad215d1-3205-4af3-949e-6d95cf866c6c.png)  
to:  
![Labeled Data](https://user-images.githubusercontent.com/12392345/193394213-9bb936e7-34ea-4cbc-9132-80c7e5a006d7.png)

2. **Data Conversion Script**  
Convert LabelStudio CSV or JSON to HuggingFace-autoTrain dataset:  
![Conversion Script](https://user-images.githubusercontent.com/12392345/193394227-32e293d4-6736-4e71-b687-b0c2fcad732c.png)

3. **Train NER Model**  
Train the NER model using HuggingFace-autoTrain:  
![Training](https://user-images.githubusercontent.com/12392345/193394247-bf51da86-45bb-41b4-b4da-3de86014e6a5.png)

4. **Predict Labels**  
Use the model to predict labels on new data in LabelStudio:  
![Predict Labels](https://user-images.githubusercontent.com/12392345/193394251-bfba07d4-c56b-4fe8-ba7f-08a1c69f0e2c.png)  
![Predictions](https://user-images.githubusercontent.com/12392345/193394261-df4bc8f8-9ffd-4819-ba26-04fddbba8e7b.png)  
![Prediction Labels](https://user-images.githubusercontent.com/12392345/193394267-c5a111c3-8d00-4d6f-b3c6-0ea82e4ac474.png)

5. **Python Prediction Function**  
Define a Python function to predict labels using the model:  
![Prediction Function](https://user-images.githubusercontent.com/12392345/193394278-81389606-f690-454a-bb2b-ef3f1db39571.png)  
![Function Code](https://user-images.githubusercontent.com/12392345/193394288-27a0c250-41af-48b1-9c57-c146dc51da1d.png)

6. **Label New Data**  
Only label new data from newly predicted-labels-dataset that has falsified labels:  
![Label New Data](https://user-images.githubusercontent.com/12392345/193394294-fdfaf40a-c9cd-4c2d-836e-1878b503a668.png)

7. **Backtest Data**  
Backtest truly labeled dataset against real historical data of the stock:  
![Backtest Data](https://user-images.githubusercontent.com/12392345/193394303-137c2a2a-3341-4be3-8ece-5191669ec53a.png)

8. **Evaluate Performance**  
Evaluate total gained percentage since inception summation-wise and compounded, then plot:  
![Evaluate Performance](https://user-images.githubusercontent.com/12392345/193394308-446eddd9-c5d1-47e3-a231-9edc620284bb.png)

9. **Live Telegram Channel Listening**  
Listen to the telegram channel for new live messages using the Telegram API for algo trading:  
![Live Listening](https://user-images.githubusercontent.com/12392345/193394319-8cc915b7-216e-4e05-a7bf-28360b17de99.png)

10. **Flask API**  
Serve the app as a Flask web API for web request and respond to it as labeled tokens:  
![Flask API](https://user-images.githubusercontent.com/12392345/193394323-822c2a59-ca72-45b1-abca-a6e5df3364b0.png)

11. **Performance Against Exchange Index**  
Outperforming or underperforming results of the telegram channel tips against the exchange index by percentage:  
![Performance](https://user-images.githubusercontent.com/12392345/193394685-53235198-04f8-4d3c-a341-535dd9093252.png)

---

## Custom Order
Place a custom order on [hjLabs.in](https://hjlabs.in/?product=custom-algotrading-software-for-zerodha-and-angel-w-source-code)

---


## 📫 How to reach me
[<img height="36" src="https://cdn.simpleicons.org/similarweb"/>](https://hjlabs.in/) &nbsp;
[<img height="36" src="https://cdn.simpleicons.org/WhatsApp"/>](https://wa.me/917016525813) &nbsp;
[<img height="36" src="https://cdn.simpleicons.org/telegram"/>](https://t.me/hjlabs) &nbsp;
[<img height="36" src="https://cdn.simpleicons.org/Gmail"/>](mailto:hemangjoshi37a@gmail.com) &nbsp;
[<img height="36" src="https://cdn.simpleicons.org/LinkedIn"/>](https://www.linkedin.com/in/hemang-joshi-046746aa) &nbsp;
[<img height="36" src="https://cdn.simpleicons.org/facebook"/>](https://www.facebook.com/hemangjoshi37) &nbsp;
[<img height="36" src="https://cdn.simpleicons.org/Twitter"/>](https://twitter.com/HemangJ81509525) &nbsp;
[<img height="36" src="https://cdn.simpleicons.org/tumblr"/>](https://www.tumblr.com/blog/hemangjoshi37a-blog) &nbsp;
[<img height="36" src="https://cdn.simpleicons.org/StackOverflow"/>](https://stackoverflow.com/users/8090050/hemang-joshi) &nbsp;
[<img height="36" src="https://cdn.simpleicons.org/Instagram"/>](https://www.instagram.com/hemangjoshi37) &nbsp;
[<img height="36" src="https://cdn.simpleicons.org/Pinterest"/>](https://in.pinterest.com/hemangjoshi37a) &nbsp;
[<img height="36" src="https://cdn.simpleicons.org/Blogger"/>](http://hemangjoshi.blogspot.com) &nbsp;
[<img height="36" src="https://cdn.simpleicons.org/gitlab"/>](https://gitlab.com/hemangjoshi37a) &nbsp;

 

---

## Related GitHub Repositories
- [pyPortMan](https://github.com/hemangjoshi37a/pyPortMan)
- [transformers_stock_prediction](https://github.com/hemangjoshi37a/transformers_stock_prediction)
- [TrendMaster](https://github.com/hemangjoshi37a/TrendMaster)
- [hjAlgos_notebooks](https://github.com/hemangjoshi37a/hjAlgos_notebooks)
- [AutoCut](https://github.com/hemangjoshi37a/AutoCut)
- [My_Projects](https://github.com/hemangjoshi37a/My_Projects)
- [Cool Arduino and ESP8266 or NodeMCU Projects](https://github.com/hemangjoshi37a/my_Arduino)
- [Telegram Trade Msg Backtest ML](https://github.com/hemangjoshi37a/TelegramTradeMsgBacktestML)

---

## Other Products
- [WiFi IoT LED Matrix Display](https://hjlabs.in/product/wifi-iot-led-display)
- [SWiBoard WiFi Switch Board IoT Device](https://hjlabs.in/product/swiboard-wifi-switch-board-iot-device)
- [Electric Bicycle](https://hjlabs.in/product/electric-bicycle)
- [Product 3D Design Service with SolidWorks](https://hjlabs.in/product/product-3d-design-with-solidworks/)
- [AutoCut : Automatic Wire Cutter Machine](https://hjlabs.in/product/automatic-wire-cutter-machine/)
- [Custom AlgoTrading Software Coding Services](https://hjlabs.in/product/custom-algotrading-software-for-zerodha-and-angel-w-source-code/)
- [SWiBoard : Tasmota MQTT Control](https://play.google.com/store/apps/details?id=in.hjlabs.swiboard)
- [Custom Token Classification or Named Entity Recognition (NER) model in NLP](https://hjlabs.in/product/custom-token-classification-or-named-entity-recognition-ner-model-as-in-natural-language-processing-nlp-machine-learning/)

---

## YouTube Videos
- [❤️ હદય અને હદયના ધબકારા 💙 दिल और दिल की धड़कन 💖 Heart and beating of heart by Priyanka madam. 💕](https://www.youtube.com/watch?v=9v3MK6oTOeA)
- [🩸 Blood Vessels And Their Functions 🩸 By Priyankama'am](https://www.youtube.com/watch?v=T7mMcEYNKyQ)
- [🩸 रक्त परिसंचरण तंत्र 🩸 Blood Circulation System in Humans 🩸 By Priyanka madam](https://www.youtube.com/watch?v=vxa6o_wrWnY)
- [AutoCut V2 - The World's Most Powerful Arduino Automatic Wire Cutting Machine](https://www.youtube.com/watch?v=oGr0mWmNhKY)
- [SWiBoard - A Killer Gadget to Boost Your Boring Switchboard](https://www.youtube.com/watch?v=ftza6WM4LiE)
- [🧪 Excretory System in Humans 🦠 By Priyanka madam](https://www.youtube.com/watch?v=UUGI-CFKsWI)
- [🌳 Transpiration in Plants 🌲](https://youtu.be/1da9p6iYlr4)
- [🌲 Transpiration in Trees 🎄](https://youtu.be/I9Sirc42Ktg)
- [🫁 Breathing in Organisms 👩🏻‍🔬](https://youtu.be/sIMl4t2OFmY)
- [🫁 Respiratory System 🦠](https://youtu.be/hua8ZD5Ge1w)
- [🫁 Respiration in Humans ⚛️](https://youtu.be/BI-CYgnkGCw)

---

## Blog and Apps
### Blog
- [Hemang Joshi](http://hemangjoshi.blogspot.com/)

### Apps
- [SWiBoard : Tasmota MQTT Control](https://play.google.com/store/apps/details?id=in.hjlabs.swiboard)

---

## Related GitLab Repositories
- [pyPortMan](https://gitlab.com/hemangjoshi37a/pyPortMan)
- [transformers_stock_prediction](https://gitlab.com/hemangjoshi37a/transformers_stock_prediction)
- [TrendMaster](https://gitlab.com/hemangjoshi37a/TrendMaster)
- [hjAlgos_notebooks](https://gitlab.com/hemangjoshi37a/hjAlgos_notebooks)
- [AutoCut](https://gitlab.com/hemangjoshi37a/AutoCut)
- [My_Projects](https://gitlab.com/hemangjoshi37a/My_Projects)
- [Cool Arduino and ESP8266 or NodeMCU Projects](https://gitlab.com/hemangjoshi37a/my_Arduino)
- [Telegram Trade Msg Backtest ML](https://gitlab.com/hemangjoshi37a/TelegramTradeMsgBacktestML)


## 📫 Try Our Algo Trading Platform hjAlgos

Ready to elevate your trading strategy? 

<a href="https://hjalgos.hjlabs.in" style="
    display: inline-block;
    padding: 12px 24px;
    background-color: #2563EB;
    color: #FFFFFF;
    text-decoration: none;
    border-radius: 8px;
    font-weight: bold;
    font-size: 16px;
    transition: background-color 0.3s, transform 0.3s;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
">
    Try Our AlgoTrading Platform
</a>
