# TelegramTradeMsgBacktestML

#### Backtest telegram mesaage from whole channel about trading(as in stocks or crypto) using Mahcine Learnig (Named Entity Recognition or Token Classification).

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

------------------------------------------------------------------------------

### Contact us

Mobile : [+917016525813](tel:+917016525813)
Whatsapp & Telegram : [+919409077371](tel:+919409077371)

Email : [hemangjoshi37a@gmail.com](mailto:hemangjoshi37a@gmail.com)

Place a custom order on hjLabs.in : [https://hjLabs.in](https://hjlabs.in/)

Please contribute your suggestions and corections to support our efforts.

Thank you.

Buy us a coffee for $5 ?

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=5JXC8VRCSUZWJ)

----------------------------------------------------------------------------------------

## Checkout Our Other Repositories

- [pyPortMan](https://github.com/hemangjoshi37a/pyPortMan)
- [transformers_stock_prediction](https://github.com/hemangjoshi37a/transformers_stock_prediction)
- [TrendMaster](https://github.com/hemangjoshi37a/TrendMaster)
- [hjAlgos_notebooks](https://github.com/hemangjoshi37a/hjAlgos_notebooks)
- [AutoCut](https://github.com/hemangjoshi37a/AutoCut)
- [My_Projects](https://github.com/hemangjoshi37a/My_Projects)
- [Cool Arduino and ESP8266 or NodeMCU Projects](https://github.com/hemangjoshi37a/my_Arduino)
- [Telegram Trade Msg Backtest ML](https://github.com/hemangjoshi37a/TelegramTradeMsgBacktestML)

## Checkout Our Other Products

- [WiFi IoT LED Matrix Display](https://hjlabs.in/product/wifi-iot-led-display)
- [SWiBoard WiFi Switch Board IoT Device](https://hjlabs.in/product/swiboard-wifi-switch-board-iot-device)
- [Electric Bicycle](https://hjlabs.in/product/electric-bicycle)
- [Product 3D Design Service with Solidworks](https://hjlabs.in/product/product-3d-design-with-solidworks/)
- [AutoCut : Automatic Wire Cutter Machine](https://hjlabs.in/product/automatic-wire-cutter-machine/)
- [Custom AlgoTrading Software Coding Services](https://hjlabs.in/product/custom-algotrading-software-for-zerodha-and-angel-w-source-code//)
- [SWiBoard :Tasmota MQTT Control](https://play.google.com/store/apps/details?id=in.hjlabs.swiboard)

## Some Cool Arduino and ESP8266 (or NodeMCU) IoT projects

- [IoT_LED_over_ESP8266_NodeMCU : Turn LED on and off using web server hosted on a nodemcu or esp8266](https://github.com/hemangjoshi37a/my_Arduino/tree/master/IoT_LED_over_ESP8266_NodeMCU)
- [ESP8266_NodeMCU_BasicOTA : Simple OTA (Over The Air) upload code from Arduino IDE using WiFi to NodeMCU or ESP8266](https://github.com/hemangjoshi37a/my_Arduino/tree/master/ESP8266_NodeMCU_BasicOTA)  
- [IoT_CSV_SD : Read analog value of Voltage and Current and write it to SD Card in CSV format for Arduino, ESP8266, NodeMCU etc](https://github.com/hemangjoshi37a/my_Arduino/tree/master/IoT_CSV_SD)  
- [Honeywell_I2C_Datalogger : Log data in A SD Card from a Honeywell I2C HIH8000 or HIH6000 series sensor having external I2C RTC clock](https://github.com/hemangjoshi37a/my_Arduino/tree/master/Honeywell_I2C_Datalogger)
- [IoT_Load_Cell_using_ESP8266_NodeMC : Read ADC value from High Precision 12bit ADS1015 ADC Sensor and Display on SSD1306 SPI Display as progress bar for Arduino or ESP8266 or NodeMCU](https://github.com/hemangjoshi37a/my_Arduino/tree/master/IoT_Load_Cell_using_ESP8266_NodeMC)
- [IoT_SSD1306_ESP8266_NodeMCU : Read from High Precision 12bit ADC seonsor ADS1015 and display to SSD1306 SPI as progress bar in ESP8266 or NodeMCU or Arduino](https://github.com/hemangjoshi37a/my_Arduino/tree/master/IoT_SSD1306_ESP8266_NodeMCU)  

## Checkout Our Awesome 3D GrabCAD Models

- [AutoCut : Automatic Wire Cutter Machine](https://grabcad.com/library/automatic-wire-cutter-machine-1)
- [ESP Matrix Display 5mm Acrylic Box](https://grabcad.com/library/esp-matrix-display-5mm-acrylic-box-1)
- [Arcylic Bending Machine w/ Hot Air Gun](https://grabcad.com/library/arcylic-bending-machine-w-hot-air-gun-1)
- [Automatic Wire Cutter/Stripper](https://grabcad.com/library/automatic-wire-cutter-stripper-1)

## Our HuggingFace Models

- [Stock tip message NER(Named Entity Recognition or Token Classification) using HUggingFace-AutoTrain and LabelStudio and Ratnakar Securities Pvt. Ltd.](https://huggingface.co/hemangjoshi37a/autotrain-ratnakar_1000_sample_curated-1474454086)
