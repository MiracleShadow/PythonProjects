from pyecharts import Graph

nodes = [{"name":"淮南师范学院","symboSize":10},
         {"name": "安徽师范大学", "symbolSize": 20},
         {"name": "安徽财经大学", "symbolSize": 30},
         {"name": "宿州学院", "symbolSize": 40},
         {"name": "安徽大学", "symbolSize": 50},
         {"name": "铜陵学院", "symbolSize": 40},
         {"name": "中国科技大学", "symbolSize": 30},
         {"name": "安徽理工大学", "symbolSize": 20}]
links = []
for i in nodes:
    links.extend({"source":i.get('name'),"target":j.get('name')} for j in nodes)
graph = Graph("关系图-环形布局示例")
graph.add("",nodes,links,is_label_show=True,repulsion=8000,layout='circular',label_text_color='#000',line_curve=0.05)
graph.show_config()
graph.render(r"Graph（关系图）.html")