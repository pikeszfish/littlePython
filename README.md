littlePython
============

还是决定将所有python的代码整合在一起...就不另外开小repo了

### GA_engine.py
Genetic Algorithm 遗传算法  
python实现的遗传算法(Genetic Algorithm)的图片合成引擎  
使用N个三角形来拟合成一张指定图片  


|参数|meaning|  
|:----  |------|    
|generation|[{"rate":0, "gene":[(x1,y1,x2,y2,x3,y3,r,g,b), ......]}, ......]|   
|generation_num|种群个体数目|  
|gene_num|每个个体所拥有的基因数目|  
|size|将图片resize的大小 (默认(100, 100))|  
|to_pic_rate|目标图片的RGB数据，为一个列表[(r,g,b), (r,g,b), (r,g,b)......]|  
|natural_selection_num|每一代从种群中筛选掉的个数|  
|gene_mutation_rate|基因变异的概率(默认0.02)|

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

```
create_one_pic(i, size, generation, generation_num, gene_num)
```
创建当前这一代种群，相似度最高的一个个体的拟合图片


TODO:目前收敛效果没达到预期。差异值在110W~160W。 初始差异是210W，算法的收敛度还需要改进

### args.py
解析python脚本参数 -a -o -h --help blabla

### pic_tochar.py
不是自己实现的，将图片生成为字符.html
好像效果不是那么好

### similar.py
使用PIL里面的直方图，来进行计算相似度，比较的一张图片中，某一颜色出现的次数。需要分割图片为更小的图片才可以比较。否则，对称的图片，相似度可以为100%

### TODO
1. python实现的自动签到
2. 输入网址，将现实的网页保存为pdf格式
3. blabla
