from pyecharts import Bar

bar = Bar("my first echart", "subtitle")

bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
# 主要方法，用于添加图表的数据和设置各种配置项

bar.show_config()
# 打印输出图标的所有配置项

bar.render(r"D:\visual studio 2015\Projects\PythonProjects\Py_pyecharts(Generate Echatrs charts)\First Echarts.html")
# 默认将会在根目录下生成一个render.html的文件，支持path参数，设置文件保存位置，如render(r"e:\myfirst_chart.html")，文件用浏览器打开
