littlePython
============

还是决定将所有python的代码整合在一起...就不另外开小repo了

### GA_engine.py
python实现的遗传算法(Genetic Algorithm)的图片合成引擎
使用N个三角形来合成一张指定图片
采用遗传算法实现用多个三角形拟合一张图片。

generation = [{"rate":0, "gene":[(x1,y1,x2,y2,x3,y3,r,g,b), ......]}, ......]


```
do_it(generation, generation_num, gene_num, size, to_pic_rate)
```
计算generation中的每个个体的与目标图片的相似度

```
natural_selection(generation, generation_num, natural_selection_num)
```
自然选择，除去匹配率最低的n个，然后从匹配率最高的n*m个中复制n。(优胜劣汰，牛逼的更可能遗传基因给后代)

```
crossover_generation(generation, size, generation_num, gene_num, gene_mutation_rate)
```
交叉，任选两个个体，进行交叉，任意基因都有二分之一的概率遗传给子女，并且有一定概率变异。当某一基因进行变异，则基因的x1，y1的坐标参数加上正态分布为(0, 0.5)的变异再乘以图片边长，而颜色数据进行正态分布为(0, 63)的变异

TODO:目前收敛效果没达到预期。差异值在110W~160W。 初始差异是210W

### pic_tochar.py
不是自己实现的，将图片生成为字符

### test.py
两图片相似度计算
