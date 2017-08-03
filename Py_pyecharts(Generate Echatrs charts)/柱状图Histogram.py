from pyecharts import Bar

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]

bar = Bar("柱状图数据堆叠示例")

bar.add("商家A", attr, v1, is_stack=True, mark_point=["average"])  # 标记点["average"]标记平均值

bar.add("商家B", attr, v2, is_stack=True, mark_line=["min", "max"])  # 标记线["min", "max"]标记最大值和最小值

bar.add("商家C", attr, v1, is_stack=False, is_convert=True)  # is_stack=False：数据条柱分开显示；is_conver=Ture：x轴和y轴交换

bar.render(r"D:\visual studio 2015\Projects\PythonProjects\Py_pyecharts(Generate Echatrs charts)\柱状图数据堆叠示例.html")
