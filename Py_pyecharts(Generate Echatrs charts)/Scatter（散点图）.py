from pyecharts import Scatter

# v1 = [10, 20, 30, 40, 50, 60]
# v2 = [10, 20, 30, 40, 50, 60]
# scatter = Scatter("散点图示例")
# scatter.add("A", v1, v2)
# scatter.add("B", v1[::-1], v2)
# scatter.show_config()
# scatter.render(r"Scatter（散点图）.html")

scatter = Scatter("散点图示例", width=1000, height=480)
v1, v2 = scatter.draw("cup.png")
scatter.add("Cup", v1, v2, label_color='#000')
scatter.render(r"Scatter（散点图）.html")
