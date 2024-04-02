import matplotlib.pyplot as plt
import japanize_matplotlib

left = [1, 2, 3, 4,5]
height = [8.8,8.8,8.8,8.8,8.8]  # 点数
labels = ['外遊び',"ボードゲーム","TVゲーム","昔あそび","その他",]

plt.bar(left, height, width=0.5, linewidth=2, tick_label=labels)
plt.show()
