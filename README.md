# MeituanCostCalc
本代码旨在帮助商铺计算如何让美团拿到最低的外卖抽成，po主自己也是个体户，随手写了一个，代码虽烂能用就行Orz

Usage：python3 main.py

输入参数：
1、原价 - 指商品的价格，如果有打折请输入折后价，没打折直接输原价；
2、配送距离 - 美团配送距离分为3km内与3km外，起底四舍五入为3块，超过3km每1km多收1.1元配送费；
3、打包费 - 就是打包费；

美团抽成计算方式为：服务费（每单流水总额6.4%，底价1.04元）+ 配送费（商品价格抽成 + 配送距离抽成 + 配送时间段抽成），具体可参考本代码计算方式；

注：po主自己在特殊时间段是不营业的，所以本代码中未包含对特殊时段的抽成计算（即 21:00 p.m - 06:00 a.m），该功能随po主需要后续添加；

祝各位同僚早日脱离苦海，不再为别人卖命，能为自己拼搏。
