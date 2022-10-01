# TelegramTradeMsgBacktestML

Backtest telegram mesaage from whole channel about trading(as in stocks or crypto) using Mahcine Learnig (Named Entity Recognition or Token Classification)

1. Label data using LabelStudio NER(Named Entity Recognition or Token Classification) tool.
2. Convert LabelStudio CSV or JSON to HuggingFace-autoTrain dataset conversion script
3. Train NER model on Hugginface-autoTrain.
4. Use Hugginface-autoTrain model to predict labels on new data in LabelStudio using LabelStudio-ML-Backend.
5. Define python function to predict labels using Hugginface-autoTrain model.
6. Only label new data from newly predicted-labels-dataset that has falsified labels.
7. Backtest Truely labelled dataset against real historical data of the stock using zerodha kiteconnect and jugaad_trader.
8. Evaluate total gained percentage since inception summation-wise and compounded and plot.
9. Listen to telegram channel for new LIVE messages using telegram API for algotrading.
10. Serve the app as flask web API for web request and respond to it as labelled tokens.
