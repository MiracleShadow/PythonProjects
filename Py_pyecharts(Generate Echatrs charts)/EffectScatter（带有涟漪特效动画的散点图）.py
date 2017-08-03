from pyecharts import EffectScatter

'''
v1 = [10,20,30,40,50,60]    #横坐标
v2 = [25,20,15,10,60,33]    #纵坐标

es = EffectScatter("动态散点图示例")
es.add("EffectScatter",v1,v2)
es.render(r"EffectScatter（带有涟漪特效动画的散点图）.html")
'''

es = EffectScatter("动态散点图各种图形示例")
es.add("", [10], [20], symbol_size=20, effect_scale=3.5, effect_period=3, symbol="pin")
es.add("", [20], [20], symbol_size=12, effect_scale=4.5, effect_period=4, symbol="rect")
es.add("", [30], [30], symbol_size=30, effect_scale=5.5, effect_period=5, symbol="roundRect")
es.add("", [40], [40], symbol_size=10, effect_scale=6.5, effect_brushtype='fill', symbol="diamond")
es.add("", [50], [50], symbol_size=16, effect_scale=5.5, effect_period=3, symbol="arrow")
es.add("", [60], [60], symbol_size=6, effect_scale=2.5, effect_period=3, symbol="triangle")
es.render(r"EffectScatter（带有涟漪特效动画的散点图）.html")
