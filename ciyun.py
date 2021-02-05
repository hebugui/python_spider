import jieba
import jieba.analyse
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 我们以刘德华的《今天》歌词为例
text = """走过岁月我才发现世界多不完美
成功或失败都有一些错觉
沧海有多广 江湖有多深
局中人才了解
生命开始情不情愿总要过完一生
交出一片心不怕被你误解
谁没受过伤 谁没流过泪
何必要躲在黑暗里 自苦又自怜
我不断失望 不断希望
苦自己尝 笑与你分享
如今站在台上也难免心慌
如果要飞得高 就该把地平线忘掉
等了好久终于等到今天
梦了好久终于把梦实现
前途漫漫任我闯
幸亏还有你在身旁
盼了好久终于盼到今天
忍了好久终于把梦实现
那些不变的风霜早就无所谓
累也不说累"""

# jieba分词（精确模式）
text_after_split = jieba.cut(str(text), cut_all=False)
words = ' '.join(text_after_split)

# 词云参数设置
wc = WordCloud(
               background_color='white', # 词云图背景颜色，默认为白色
               font_path='simhei.ttf',  # 词云图 字体（中文需要设定为本机有的中文字体）
			  )
wc.generate(words)

# matplotlib用于显示 词云图
plt.imshow(wc)
plt.axis("off")
plt.show()
