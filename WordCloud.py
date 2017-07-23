from wordcloud import WordCloud
import matplotlib.pyplot as plt

# -*- coding: utf-8 -*-
f = open('text.txt', encoding='utf-8')
text = f.read()

# the font from github: https://github.com/adobe-fonts
font = r'C:\Windows\Fonts\simfang.ttf'
wc = WordCloud(collocations=False, font_path=font, width=1400, height=1400, margin=2).generate(text.lower())

plt.imshow(wc)
plt.axis("off")
plt.show()

wc.to_file('关键字.png')  # 把词云保存下来

