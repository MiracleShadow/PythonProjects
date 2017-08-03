from pyecharts import Pie

# attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# v1 = [11, 12, 13, 10, 10, 10]
# pie = Pie("饼图示例")
# pie.add("", attr, v1, is_label_show=True)       #is_label_show=True显示标签信息
# pie.show_config()
# pie.render(r"Pie（饼图）.html")

attr = ["校园建设", "教学通知", "工作安排", "召开会议", "高校交流", "党政要务"]
v1 = [11, 12, 13, 10, 10, 10]
v2 = [19, 21, 32, 20, 20, 33]
pie = Pie("新闻类别比例示例", width=1000, height=500)  # title_pos='center'标题居中显示
pie.add("淮南师范学院", attr, v1, center=[25, 50], is_random=True, radius=[0, 45], rosetype='area', is_legend_show=True,
        is_label_show=True)
pie.add("安徽师范大学", attr, v2, center=[75, 50], is_random=True, radius=[0, 45], is_legend_show=True,
         is_label_show=True)
# is_legend_show=False：标签不显示  legend_orient='vertical', legend_pos='right'
pie.show_config()
pie.render(r"Pie（饼图）.html")
