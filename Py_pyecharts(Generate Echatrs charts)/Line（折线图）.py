from pyecharts import Line

attr = ["{}年{}月".format(i, j) for i in range(2016, 2018) for j in range(1, 13)]
v1 = [5, 9, 1, 6, 4, 7, 6, 6, 4, 2, 3, 4, 5, 9, 1, 6, 4, 7, 6, 6, 4, 2, 3, 4]
v2 = [15, 12, 17, 12, 10, 7, 15, 12, 17, 12, 10, 7, 16, 7, 15, 21, 16, 15, 16, 7, 15, 21, 16, 15]
v3 = [12, 14, 16, 13, 12, 14, 16, 13, 14, 19, 16, 14, 12, 18, 12, 14, 14, 19, 16, 14, 12, 18, 12, 14]
line = Line(title="淮南师范学院折线图示例")
# line.add("商家A", attr, v1, mark_point=["average"])
# line.add("商家B", attr, v2, is_smooth=True, mark_line=["max", "min", "average"])      #is_smooth=True平滑曲线
# line.add("商家A", attr, v1, is_step=True, is_label_show=True)     #阶梯图
line.add("校园建设", attr, v1, is_fill=True, line_opacity=1, area_opacity=0,
         is_smooth=True, is_label_show=True,
         line_type="solid", is_datazoom_show=True,
         datazoom_range=[50, 100])
line.add("教学通知", attr, v2, is_fill=True, line_opacity=1, area_opacity=0, is_smooth=True, is_label_show=True,
         line_type="dashed", is_datazoom_show=True,
         datazoom_range=[50, 100])
line.add("工作安排", attr, v3, xaxis_name="时间", xaxis_name_pos="end", yaxis_name="新闻数量", yaxis_name_pos="middle",
         namegap=40, is_fill=True, line_opacity=1,
         area_opacity=0, is_smooth=True, is_label_show=True,
         line_type="dotted", is_datazoom_show=True,
         datazoom_range=[50, 100])
# 面积图，symbol=None无标点信息
# line.add("", attr, v2, is_fill=True, area_color='#000', area_opacity=0.3, is_smooth=True)
# 面积图，area_color='#000'区域背景为黑色，area_opacity(0～1.0)越高颜色越深
line.show_config()
line.render(r"Line（折线图）.html")
