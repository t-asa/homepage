remotes::install_github("ykunisato/delphiR")

library(delphiR)

set_round1(inst='<br><font size="6">\u30c7\u30eb\u30d5\u30a1\u30a4\u6cd5\u30e9\u30a6\u30f3\u30c9\uff11\u8abf\u67fb</font><br><br>\u4ee5\u4e0b\u306e\u8cea\u554f\u3078\u306e\u56de\u7b54\u3092\u304a\u9858\u3044\u3044\u305f\u3057\u307e\u3059\u3002\u3067\u304d\u308b\u3060\u3051\u591a\u304f\u306e\u56de\u7b54\u3092\u304a\u9858\u3044\u3044\u305f\u3057\u307e\u3059\u3002\u307e\u305f\uff0c\u56de\u7b54\u306f\u601d\u3044\u3064\u3044\u305f\u9806\u756a\u3067\u56de\u7b54\u3044\u305f\u3060\u3044\u3066\u304b\u307e\u3044\u307e\u305b\u3093\u3002\u306a\u304a\uff0c\u56de\u7b54\u306f\u5c11\u306a\u304f\u3068\u3082\uff15\u500b\u4ee5\u4e0a\uff0c\uff11\uff10\u500b\u672a\u6e80\u3067\u304a\u9858\u3044\u3044\u305f\u3057\u307e\u3059\u3002',
           question='\u5c02\u9580\u9818\u57df\u306b\u304a\u3051\u308b\u73fe\u5728\u306e\u512a\u5148\u3057\u3066\u884c\u3046\u3079\u304d\u7814\u7a76\u306f\u4f55\u3067\u3059\u304b\uff1f',
           max_response = 10,
           min_response = 5)

set_round1(inst='<br><font size=“6”>これkore',
           question='テストtest',
           max_response = 10,
           min_response = 5)

set_round1(inst='<br><font size="6">デルファイ法ラウンド１調査</font><br><br>以下の質問への回答をお願いいたします。できるだけ多くの回答をお願いいたします。また，回答は思いついた順番で回答いただいてかまいません。なお，回答は少なくとも５個以上，１０個未満でお願いいたします。',
           question='専門領域における現在の優先して行うべき研究は何ですか？',
           max_response = 10,
           min_response = 5)
