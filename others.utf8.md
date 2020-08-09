---
title: "Others"
---

# Inquisitについて

私はオンライン実験をする際には，行動課題用に [Inquisit](https://www.millisecond.com/products/inquisit6/laboverview.aspx) と 質問紙調査用に [Qualtrics](https://www.qualtrics.com/jp/)を使っています。  
ここでは**Milliseconds社のInquisit** というソフトウェアについて簡単に紹介します。（2020/8/10現在）  
  
<span style="color:#BB0000;">Inquisit は有料ですが，下記のようなメリットがあります。</span>

- 比較的安く**永久ライセンスも購入できる**ので，一度購入してしまえば後はお金がかからない。
(短期間使用用の価格もあります。また，お金がない学生は交渉次第で少し安くしてくれます。)
- **サーバーも提供してくれる**ので，Inquisit Webのライセンスの購入費用以外にお金はかからない。（自分のサーバーを指定することも可能）
- **心理学実験のコードが充実**していて参考になる。([Test library](https://www.millisecond.com/download/library/))
- 課題を作りながら，一部だけ実行する，というのが可能。課題実行中にブロックをスキップするショートカットもあります。
- スマホなどにも対応しており，オンライン実験向けの更新が積極的にされている。

    
<span style="color:#BB0000;">Inquisitの使用に関する留意点や特徴もいくつか挙げておきます。</span>

- スクリプトは**Inquisit独自の言語**を使って書きます。最近のバージョンでは，**コードを書きながら，入力の候補が表示される**ので便利になってきました。あとは，やはりTest Libraryなどを利用して書き方を学ぶと早いと思います。
- Inquisitを動かすには Inquisit Labのライセンスを購入しますが，ウェブ実験を行う際には，さらに Inquisit Webのライセンスを購入する必要があります。
（ [Webライセンスの金額](https://www.millisecond.com/products/inquisit6/academicweb.aspx)， [Labライセンスの金額](https://www.millisecond.com/products/inquisit6/academiclab.aspx）)）
- オンライン実験をする場合は，**Webライセンス１つにつき，１つの実験**をアップできます。古いのを消せば，また新しいものをアップできます。
- パソコンが変わったときのライセンス移行は可能です。
- Inquisit Labは，最初に**無料のお試し**ができます。ライセンスがきれると実行はできてもランダムな結果が記録されるだけなので注意。
- 出力としては，サマリーとローデータと両方出してくれます。カスタマイズできます。
- リッカートスケール，ラジオボタン，プルダウンメニューなどもあり，**質問紙調査にももちろん使えます**。ただビジュアル的な好みもあり，私は質問紙関係は有料のQualtricsを使っています。（無料であればgoogle formなどもあります。）
- PsychPyのように，刺激提示に関する**エクセルを読み込む機能はありません。**
- チュートリアル（Documentation）はちょっと内容が古めです。アップされているTest libraryのコードを参考にするとよいと思います。

----

# Resources 

#### オンライン実験 

* [オンライン実験備忘録](オンライン実験備忘録.pdf)![](PDF_24.png){.pull-left width=2.5%} : こちらの備忘録は，**Qualtrics**で質問紙調査，**Inquisit**で行動課題，**クラウドワークス社**のシステムを利用してWEB実験を行う際の情報を載せています。それぞれの基本的な使い方については省略し，これらをWEB実験で組み合わせる際の方法に焦点を当てています。2020.6.9時点

* [Inquisit uninstall page (Japanese)](https://sites.google.com/view/inquisit-player-uninstall/%e3%83%9b%e3%83%bc%e3%83%a0?subjectid=1  )：
InquistのWeb実験で使う __Inquisit 5 Player__ のアンインストール方法を書いたサイトです。内容ご確認の上，ご自由にリンクしてお使いください。

#### R関係

* [R, Rstudio による統計解析](RAnalysis.pdf)![](PDF_24.png){.pull-left width=2.5%}  : 学部生用にツールとしての使い方を簡潔にまとめたものです。

* [個人的なQ & A](QA_20200609.pdf)![](PDF_24.png){.pull-left width=2.5%}:
2019年からつけ始めた**R**や**Inquisit**のメモです。特に私がよく使う事項や，解決策を見つけるのに苦労した内容を載せています。お役に立つ情報があれば幸いです。 2020.6.9時点


#### PsychoPy

* ![](new.png){.pull-left width=2.5%}[PsychoPyで簡単な課題作成①](PsychoPy_ref1.pdf)![](PDF_24.png){.pull-left width=2.5%}:選択課題で選択肢によってあたりの確率が違う課題例 Step① 2019.11時点

* ![](new.png){.pull-left width=2.5%}[PsychoPyで簡単な課題作成②](PsychoPy_ref2.pdf)![](PDF_24.png){.pull-left width=2.5%}:選択課題で選択肢によってあたりの確率が違う課題例 Step② 2019.11時点

* ![](new.png){.pull-left width=2.5%}[PsychoPy例1](demo.zip)![](zip.jpg){.pull-left width=2.5%}
__３つの刺激から１つをマウスで選択 & 選ばなかった刺激は半透明グレー__: 
簡単なデモと説明のパワーポイントファイルがあります。必ずzipファイルを展開してからお試しください。PsychoPy3(v3.2.4)で作成，2020.07.29

    
**内容に誤りを見つけられた方は，遠山までご連絡頂けますと幸いです。

***
        
# Link

#### Senshu University
* [専修大学のHP](https://www.senshu-u.ac.jp/)
* [国里愛彦先生のHP: Computational Clinical Psychology Lab](https://kunisatolab.github.io/main/index.html)  

#### Nagoya University 

* [情報学研究科：School of Informatics, Graduate School of Informatics](https://www.i.nagoya-u.ac.jp/en/)
* [片平健太郎先生のHP: Computational Behavioral Science Laboratory](https://sites.google.com/site/nagoyacbslab/home)
* [齋藤菜月さんのHP： (psychologist of empathy)](https://n-saito.amebaownd.com/)  

#### Useful sites
* [日本心理学会第83回大会 チュートリアル・ワークショップ004 機械学習と心理学の接点の補足資料(片平先生)](https://kkatahira.github.io/personality/index.html)
    
  
