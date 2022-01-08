# 微軟 FaceAPI 刷臉簽到實作
##### 高師大附中  高三信 31 黃崇傑
[github連結--jasper030](https://github.com/jasper030/FacePI)
---
### 前言
這是高師大附中110學年度高三多元選修課程。這學期我們學到了如何利用微軟提供的臉部辨識功能，運用**python**及其他套件實現一個刷臉簽到系統；此外，老師還教了**git**的基本使用，讓我們可以將程式碼上傳到github省去了不少存檔的麻煩。

*整支程式還在開發階段，有一些新增的功能還有問題，最新開發版本的 branch為testBranch*

### 程式碼說明
1. *main.py*：這是整支程式的運作核心，透過呼叫其他的function，實現我們所要的功能。
    1. `show_opencv`：這是提供給`SignIn`和`Train`呼叫並實現開啟攝像頭視窗的功能。
    2. `Identify`：這是讓`SignIn`和`Train`呼叫並將圖片資料回傳到微軟伺服器進行辨識再回傳結果的函式。
    3. `SignIn`：這是簽到的函式
    4. `Train`：這是訓練判斷新人的函式。將要新增的新人三連拍，並存檔以供以後辨識。
    5. `showConfig`：這是察看config.json資料的函式。
2. *classes*：這是所有函式存放的資料夾，所有的功能都放在這裡。
3. *config.json*：這是程式運作的基本資料，與微軟伺服器連線的**api_key**也放在這裡。

### 心得省思
雖然在上這堂課的過程，幾乎都是照著老師的程式碼打，但是透過追蹤程式碼的定義，我還是稍微有學到一個大專案是如何編織而成的。這學期比較可惜的是因為學測將近，比較沒時間自己寫程式，考完之後，我會自己重新審視程式碼，並試著將功能弄得完善一點，做成一個有圖形介面的軟體。
