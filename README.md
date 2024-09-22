# TelegramTradeMsgBacktestML

#### Backtest telegram mesaage from whole channel about trading(as in stocks or crypto) using Mahcine Learnig (Named Entity Recognition or Token Classification).

## Test now on HuggingFace : ![Screenshot from 2022-10-01 11-50-07](https://user-images.githubusercontent.com/12392345/193395791-2a586c59-1ee2-433d-9f27-cc8e90b8e679.png)
[:: Link to test this model ::](https://huggingface.co/hemangjoshi37a/autotrain-ratnakar_1000_sample_curated-1474454086?text=SUPER+DUPER+DELIVERY%0A%0ADELIVERY+%3A+BUY+BEPL+ABOVE+117+SL+103+TARGET+135+-+155+-+175)


## What this repository contains? :

1. Label data using LabelStudio NER(Named Entity Recognition or Token Classification) tool.
 ![Screenshot from 2022-09-30 12-28-50](https://user-images.githubusercontent.com/12392345/193394190-3ad215d1-3205-4af3-949e-6d95cf866c6c.png) convert to  ![Screenshot from 2022-09-30 18-59-14](https://user-images.githubusercontent.com/12392345/193394213-9bb936e7-34ea-4cbc-9132-80c7e5a006d7.png)

2. Convert LabelStudio CSV or JSON to HuggingFace-autoTrain dataset conversion script
![Screenshot from 2022-10-01 10-36-03](https://user-images.githubusercontent.com/12392345/193394227-32e293d4-6736-4e71-b687-b0c2fcad732c.png)

3. Train NER model on Hugginface-autoTrain.
 ![Screenshot from 2022-10-01 10-38-24](https://user-images.githubusercontent.com/12392345/193394247-bf51da86-45bb-41b4-b4da-3de86014e6a5.png)

4. Use Hugginface-autoTrain model to predict labels on new data in LabelStudio using LabelStudio-ML-Backend.
 ![Screenshot from 2022-10-01 10-41-07](https://user-images.githubusercontent.com/12392345/193394251-bfba07d4-c56b-4fe8-ba7f-08a1c69f0e2c.png)
 ![Screenshot from 2022-10-01 10-42-36](https://user-images.githubusercontent.com/12392345/193394261-df4bc8f8-9ffd-4819-ba26-04fddbba8e7b.png)
 ![Screenshot from 2022-10-01 10-44-56](https://user-images.githubusercontent.com/12392345/193394267-c5a111c3-8d00-4d6f-b3c6-0ea82e4ac474.png)

5. Define python function to predict labels using Hugginface-autoTrain model.
 ![Screenshot from 2022-10-01 10-47-08](https://user-images.githubusercontent.com/12392345/193394278-81389606-f690-454a-bb2b-ef3f1db39571.png)
![Screenshot from 2022-10-01 10-47-25](https://user-images.githubusercontent.com/12392345/193394288-27a0c250-41af-48b1-9c57-c146dc51da1d.png)

6. Only label new data from newly predicted-labels-dataset that has falsified labels.
 ![Screenshot from 2022-09-30 22-47-23](https://user-images.githubusercontent.com/12392345/193394294-fdfaf40a-c9cd-4c2d-836e-1878b503a668.png)

7. Backtest Truely labelled dataset against real historical data of the stock using zerodha kiteconnect and jugaad_trader.
 ![Screenshot from 2022-10-01 00-05-55](https://user-images.githubusercontent.com/12392345/193394303-137c2a2a-3341-4be3-8ece-5191669ec53a.png)

8. Evaluate total gained percentage since inception summation-wise and compounded and plot.
 ![Screenshot from 2022-10-01 00-06-59](https://user-images.githubusercontent.com/12392345/193394308-446eddd9-c5d1-47e3-a231-9edc620284bb.png)

9. Listen to telegram channel for new LIVE messages using telegram API for algotrading.
 ![Screenshot from 2022-10-01 00-09-29](https://user-images.githubusercontent.com/12392345/193394319-8cc915b7-216e-4e05-a7bf-28360b17de99.png)

10. Serve the app as flask web API for web request and respond to it as labelled tokens.
 ![Screenshot from 2022-10-01 00-12-12](https://user-images.githubusercontent.com/12392345/193394323-822c2a59-ca72-45b1-abca-a6e5df3364b0.png)

11. Outperforming or underperforming results of the telegram channel tips against exchange index by percentage.
 ![Screenshot from 2022-10-01 11-16-27](https://user-images.githubusercontent.com/12392345/193394685-53235198-04f8-4d3c-a341-535dd9093252.png)



Place a custom order on hjLabs.in : [https://hjLabs.in](https://hjlabs.in/?product=custom-algotrading-software-for-zerodha-and-angel-w-source-code)


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

 
## Checkout Cool GitHub Other Repositories:
- [pyPortMan](https://github.com/hemangjoshi37a/pyPortMan)
- [transformers_stock_prediction](https://github.com/hemangjoshi37a/transformers_stock_prediction)
- [TrendMaster](https://github.com/hemangjoshi37a/TrendMaster)
- [hjAlgos_notebooks](https://github.com/hemangjoshi37a/hjAlgos_notebooks)
- [AutoCut](https://github.com/hemangjoshi37a/AutoCut)
- [My_Projects](https://github.com/hemangjoshi37a/My_Projects)
- [Cool Arduino and ESP8266 or NodeMCU Projects](https://github.com/hemangjoshi37a/my_Arduino)
- [Telegram Trade Msg Backtest ML](https://github.com/hemangjoshi37a/TelegramTradeMsgBacktestML)

## Checkout Our Other Products:
- [WiFi IoT LED Matrix Display](https://hjlabs.in/product/wifi-iot-led-display)
- [SWiBoard WiFi Switch Board IoT Device](https://hjlabs.in/product/swiboard-wifi-switch-board-iot-device)
- [Electric Bicycle](https://hjlabs.in/product/electric-bicycle)
- [Product 3D Design Service with Solidworks](https://hjlabs.in/product/product-3d-design-with-solidworks/)
- [AutoCut : Automatic Wire Cutter Machine](https://hjlabs.in/product/automatic-wire-cutter-machine/)
- [Custom AlgoTrading Software Coding Services](https://hjlabs.in/product/custom-algotrading-software-for-zerodha-and-angel-w-source-code//)
- [SWiBoard :Tasmota MQTT Control](https://play.google.com/store/apps/details?id=in.hjlabs.swiboard)
- [Custom Token Classification or Named Entity Recognition (NER) model as in Natural Language Processing (NLP) Machine Learning](https://hjlabs.in/product/custom-token-classification-or-named-entity-recognition-ner-model-as-in-natural-language-processing-nlp-machine-learning/)

## Some Cool Arduino and ESP8266 (or NodeMCU) IoT projects:
- [IoT_LED_over_ESP8266_NodeMCU : Turn LED on and off using web server hosted on a nodemcu or esp8266](https://github.com/hemangjoshi37a/my_Arduino/tree/master/IoT_LED_over_ESP8266_NodeMCU)
- [ESP8266_NodeMCU_BasicOTA : Simple OTA (Over The Air) upload code from Arduino IDE using WiFi to NodeMCU or ESP8266](https://github.com/hemangjoshi37a/my_Arduino/tree/master/ESP8266_NodeMCU_BasicOTA)  
- [IoT_CSV_SD : Read analog value of Voltage and Current and write it to SD Card in CSV format for Arduino, ESP8266, NodeMCU etc](https://github.com/hemangjoshi37a/my_Arduino/tree/master/IoT_CSV_SD)  
- [Honeywell_I2C_Datalogger : Log data in A SD Card from a Honeywell I2C HIH8000 or HIH6000 series sensor having external I2C RTC clock](https://github.com/hemangjoshi37a/my_Arduino/tree/master/Honeywell_I2C_Datalogger)
- [IoT_Load_Cell_using_ESP8266_NodeMC : Read ADC value from High Precision 12bit ADS1015 ADC Sensor and Display on SSD1306 SPI Display as progress bar for Arduino or ESP8266 or NodeMCU](https://github.com/hemangjoshi37a/my_Arduino/tree/master/IoT_Load_Cell_using_ESP8266_NodeMC)
- [IoT_SSD1306_ESP8266_NodeMCU : Read from High Precision 12bit ADC seonsor ADS1015 and display to SSD1306 SPI as progress bar in ESP8266 or NodeMCU or Arduino](https://github.com/hemangjoshi37a/my_Arduino/tree/master/IoT_SSD1306_ESP8266_NodeMCU)  

## Our HuggingFace Models :
- [hemangjoshi37a/autotrain-ratnakar_1000_sample_curated-1474454086 : Stock tip message NER(Named Entity Recognition or Token Classification) using HUggingFace-AutoTrain and LabelStudio and Ratnakar Securities Pvt. Ltd.](https://huggingface.co/hemangjoshi37a/autotrain-ratnakar_1000_sample_curated-1474454086)

## Our HuggingFace Datasets :
- [hemangjoshi37a/autotrain-data-ratnakar_1000_sample_curated : Stock tip message NER(Named Entity Recognition or Token Classification) using HUggingFace-AutoTrain and LabelStudio and Ratnakar Securities Pvt. Ltd.](https://huggingface.co/datasets/hemangjoshi37a/autotrain-data-ratnakar_1000_sample_curated)

## Awesome Youtube Videos :
- [❤️ હદય અને હદયના ધબકારા 💙 दिल और दिल की धड़कन 💖 Heart and beating of heart by Priyanka madam. 💕](https://www.youtube.com/watch?v=9v3MK6oTOeA)
- [🩸 રુધિર વહીનીઓ અને એના કર્યો. 🩸 Blood Vessels And Working of Blood Vessels 🩸 By Priyankama'am](https://www.youtube.com/watch?v=T7mMcEYNKyQ)
- [🩸 મનુષ્યમાં પરિવહન તંત્ર 🩸 परिसंचरण तंत्र 🩸 Blood Circulation System in Humans🩸 By Priyanka madam](https://www.youtube.com/watch?v=vxa6o_wrWnY)
- [AutoCut V2 - The World's Most Powerful Arduino Automatic Wire Cutting Machine](https://www.youtube.com/watch?v=oGr0mWmNhKY)
- [SWiBoard - A Killer Gadget to Boost Your Boring Switchboard](https://www.youtube.com/watch?v=ftza6WM4LiE)
- [🧪 મનુષ્યમાં ઉત્સર્જન-તંત્ર 🦠 मानव उत्सर्जन तंत्र ⚗️ excretory system 🩺](https://www.youtube.com/watch?v=UUGI-CFKsWI)
- [🌳વનસ્પતિમાં પાણી અને ખનીજ તત્વોનું વહન 🌲](https://youtu.be/1da9p6iYlr4)
- [🌲 વનસ્પતિમાં બાષ્પોત્સર્જન 🌳 पेड़ में वाष्पोत्सर्जन 🎄Transpiration in Trees](https://youtu.be/I9Sirc42Ktg)
- [🫁 સજીવોમાં શ્વસન 🧬 जीवों में श्वास 🫀 Breathing in organisms 👩🏻‍🔬](https://youtu.be/sIMl4t2OFmY)
- [🫁 શ્વસનની પ્રક્રિયા 🫀Respiratory System 🦠](https://youtu.be/hua8ZD5Ge1w)
- [🫁 મનુષ્યમાં શ્વાસ અને ઉચ્છશ્વાસ ⚛️ ](https://youtu.be/BI-CYgnkGCw)

## My Quirky Blog :
- [Hemang Joshi](http://hemangjoshi.blogspot.com/)

## Awesome Android Apps :
- [SWiBoard :Tasmota MQTT Control](https://play.google.com/store/apps/details?id=in.hjlabs.swiboard)
 
## Checkout Cool GitLab Other Repositories:
- [pyPortMan](https://gitlab.com/hemangjoshi37a/pyPortMan)
- [transformers_stock_prediction](https://gitlab.com/hemangjoshi37a/transformers_stock_prediction)
- [TrendMaster](https://gitlab.com/hemangjoshi37a/TrendMaster)
- [hjAlgos_notebooks](https://gitlab.com/hemangjoshi37a/hjAlgos_notebooks)
- [AutoCut](https://gitlab.com/hemangjoshi37a/AutoCut)
- [My_Projects](https://gitlab.com/hemangjoshi37a/My_Projects)
- [Cool Arduino and ESP8266 or NodeMCU Projects](https://gitlab.com/hemangjoshi37a/my_Arduino)
- [Telegram Trade Msg Backtest ML](https://gitlab.com/hemangjoshi37a/TelegramTradeMsgBacktestML)
