# TelegramTradeMsgBacktestML

#### Backtest telegram mesaage from whole channel about trading(as in stocks or crypto) using Mahcine Learnig (Named Entity Recognition or Token Classification).

## What this repository contains? :

1. Label data using LabelStudio NER(Named Entity Recognition or Token Classification) tool.
 ![img1](file:///home/hemang/Pictures/Screenshots/Screenshot%20from%202022-09-30%2012-28-50.png) convert to  file:///home/hemang/Pictures/Screenshots/Screenshot%20from%202022-09-30%2018-59-14.png

2. Convert LabelStudio CSV or JSON to HuggingFace-autoTrain dataset conversion script
 file:///home/hemang/Pictures/Screenshots/Screenshot%20from%202022-10-01%2010-36-03.png

3. Train NER model on Hugginface-autoTrain.
 file:///home/hemang/Pictures/Screenshots/Screenshot%20from%202022-10-01%2010-38-24.png

4. Use Hugginface-autoTrain model to predict labels on new data in LabelStudio using LabelStudio-ML-Backend.
 file:///home/hemang/Pictures/Screenshots/Screenshot%20from%202022-10-01%2010-41-07.png
 file:///home/hemang/Pictures/Screenshots/Screenshot%20from%202022-10-01%2010-42-36.png
 file:///home/hemang/Pictures/Screenshots/Screenshot%20from%202022-10-01%2010-44-56.png

5. Define python function to predict labels using Hugginface-autoTrain model.
 file:///home/hemang/Pictures/Screenshots/Screenshot%20from%202022-10-01%2010-47-08.png
-167:11:70:16
 file:///home/hemang/Pictures/Screenshots/Screenshot%20from%202022-10-01%2010-47-25.png
-43:-10:70:37

6. Only label new data from newly predicted-labels-dataset that has falsified labels.
 file:///home/hemang/Pictures/Screenshots/Screenshot%20from%202022-09-30%2022-47-23.png

7. Backtest Truely labelled dataset against real historical data of the stock using zerodha kiteconnect and jugaad_trader.
 file:///home/hemang/Pictures/Screenshots/Screenshot%20from%202022-10-01%2000-05-55.png
8. Evaluate total gained percentage since inception summation-wise and compounded and plot.
 file:///home/hemang/Pictures/Screenshots/Screenshot%20from%202022-10-01%2000-06-59.png

9. Listen to telegram channel for new LIVE messages using telegram API for algotrading.
 file:///home/hemang/Pictures/Screenshots/Screenshot%20from%202022-10-01%2000-09-29.png
 
10. Serve the app as flask web API for web request and respond to it as labelled tokens.
 file:///home/hemang/Pictures/Screenshots/Screenshot%20from%202022-10-01%2000-12-12.png

Place a custom order on hjLabs.in : [https://hjLabs.in](https://hjlabs.in/?product=custom-algotrading-software-for-zerodha-and-angel-w-source-code)

------------------------------------------------------------------------------

### Contact us

Mobile : [+917016525813](tel:+917016525813)
Whatsapp & Telegram : [+919409077371](tel:+919409077371)

Email : [hemangjoshi37a@gmail.com](mailto:hemangjoshi37a@gmail.com)

Place a custom order on hjLabs.in : [https://hjLabs.in](https://hjlabs.in/)

Please contribute your suggestions and corections to support our efforts.

Thank you.

Buy us a coffee for $5 on PayPal ?

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
