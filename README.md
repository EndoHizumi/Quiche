# Quiche

赤外線モジュール『ADRSIR』を使用して、Raspberry Piで家電を操作するWebシステム

[![Github issues](https://img.shields.io/github/issues/EndoHizumi/Quiche)](https://github.com/EndoHizumi/Quiche/issues)
[![Github forks](https://img.shields.io/github/forks/EndoHizumi/Quiche)](https://github.com/EndoHizumi/Quiche/network/members)
[![Github stars](https://img.shields.io/github/stars/EndoHizumi/Quiche)](https://github.com/EndoHizumi/Quiche/stargazers)
[![Github license](https://img.shields.io/github/license/EndoHizumi/Quiche)](https://github.com/EndoHizumi/Quiche/)

# Tags
`RaspberryPi` `Python` `Flask` `adrsir`

# Advantages
登録した家電をREST APIで操作ができます。

# Installation
dependence.sh を実行する。  
※パッケージのインストールのため、パスワードの入力があります。  
 
```bash
$ sh dependence.sh
```

# Usage
- 家電の登録
```bash
 curl -X PUT http://localhost:8080/signals/A940JB -H "Content-Type: application/json" --data '{"type":"ir", "button_no_list":"[0]", "action_names":"['cooling-20-auto-swing']"}'
```

- 家電の操作
```bash
curl -X POST http://localhost:8080/signals/A940JB/cooling-20-auto-swing
```

- 登録されている操作一覧の取得
```bash
curl http://localhost:8080/signals/A940JB/appliances
```

- 登録されている家電一覧の取得
```bash
curl http://localhost:8080/signals/appliances

```

## Deployment

### 利用ライブラリ・フレームワーク

API部分: Flask
ADRSIR操作: [you0708/adrsir](https://github.com/you0708/adrsir)

## モジュール構成

 [app.py] -> [Quiche/home_appliance_controller.py] -> [adrsir/adrsir.py] 

- app.py : QuicheのAPIルーター
- home_appliance_controller.py : Quicheの家電操作コントローラー
- adrsir.py : Raspberry Piの赤外線モジュール"ADRDIR"のPythonライブラリ

# Contributors
- [EndoHizumi](https://github.com/EndoHizumi)
