# niku.py
* ローストビーフの1次元熱伝導を解いてアニメーション表示するお遊びプログラムです。

## 実行に必要なもの
* Unix系シェル
* Python (3.5.2で動作確認）
* numpy
* matplotlib
* imagemagick（アニメーションgif作成に使用）

## 実行結果サンプル


## 良いローストビーフを作るために
* ほぼすべての調理法で、基本的に境界条件（肉表面の温度）は100度を超えません。
** 水分を失うと100度を超えることもあります（焦げます）。
* 境界条件を70-80度でキープするのが良さそうです。
** オーブン調理の場合、庫内温度を120度くらいにしてホイルを被せると肉表面はこれくらいの温度で落ち着くようです。
* よく「冷蔵庫から出してすぐ調理するな」と言いますが、初期条件が10度変わっても出来上がりに大した差はでません。適切な境界条件管理をしましょう。

## そのうちやりたいこと
* 非平面肉への対応（形状ファクターの考慮）
* 肉より外側（オーブンの庫内）の熱伝導・対流のモデル化