# DSAI_HW1_F74062052
## data analysis:
  綜觀2020/01/01 ~ 2021/01/31，看不出來太大的趨勢:
  ![image](https://github.com/shaohey0930/DSAI_HW1_F74062052/blob/main/20200101_20210131.png)
  將 2019 ~ 2021 三年 1~3月的資料放到一起看，可以看出每年有其趨勢，但對於預測並不有效:
  ![image](https://github.com/shaohey0930/DSAI_HW1_F74062052/blob/main/1_3.png)

## model selecting:
  這邊使用 auto arima 來train model。
  
## processing:使用兩種方法來train:
  * 1.原本使用 前40天-前10天(共30天)來train，最後10天來逐點tune Model。
  * 2.直接使用最後30天train。
  * 使用訓練完的model去預測3/22~3/29，共8天的MW值。雖然第1種方法比較合理，但在與台電的未來一周預測結果比較後，發現第2種比較好於是選擇第2種當作training方式。
