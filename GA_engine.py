#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import os
import sys
import time
import random
import timeit

from PIL import Image, ImageDraw

def create_pic(generation, size, generation_num, gene_num):
    '''
        (x1,y1,x2,y2,x3,y3,g,b,a,r)
        draw.polygon([(x1, y1), (x2, y2), (x3, y3)], fill = (g, b, a, r))
    '''
    for i in xrange(0, generation_num):
        single = generation[i]
        gene = single['gene']
        base_img = Image.new('RGBA', size)
        base_draw = ImageDraw.Draw(base_img)
        base_draw.polygon([(0, 0), (0, size[1] - 1), (size[0] - 1, size[1] - 1), (size[0] - 1, 0)], fill = (0, 0, 0, 0))
        for j in xrange(0, gene_num):
            img = Image.new('RGBA', size)
            draw = ImageDraw.Draw(img)
            single_gene = gene[j]
            draw.polygon([(single_gene[0], single_gene[1]), (single_gene[2], single_gene[3]), (single_gene[4],single_gene[5])], \
                        fill = (single_gene[6], single_gene[7], single_gene[8], 120))
            base_img = Image.alpha_composite(base_img, img)
        print "/Users/Pike/CODES/pic/generation_%d.png" % i
        base_img.save("/Users/Pike/CODES/pic/generation_%d.png" % i)

def create_one_pic(a, size, generation, generation_num, gene_num):
    '''
        (x1,y1,x2,y2,x3,y3,g,b,a,r)
        draw.polygon([(x1, y1), (x2, y2), (x3, y3)], fill = (g, b, a))
    '''
    single = generation[1]
    gene = single['gene']
    base_img = Image.new('RGBA', size)
    base_draw = ImageDraw.Draw(base_img)
    base_draw.polygon([(0, 0), (0, size[1] - 1), (size[0] - 1, size[1] - 1), (size[0] - 1, 0)], fill = (0, 0, 0, 0))
    for j in xrange(0, gene_num):
        img = Image.new('RGBA', size)
        draw = ImageDraw.Draw(img)
        single_gene = gene[j]
        draw.polygon([(single_gene[0], single_gene[1]), (single_gene[2], single_gene[3]), (single_gene[4],single_gene[5])], \
                        fill = (single_gene[6], single_gene[7], single_gene[8], 128))
        base_img = Image.alpha_composite(base_img, img)
    print "/Users/Pike/CODES/pic/middle_%d.png"%a
    base_img.save("/Users/Pike/CODES/pic/middle_%d.png"%a)

def mutate_or_not(rate):
    if rate > random.random():
        return True
    else:
        return False

def f_or_m():
    '''
        alike father or mother ?
    '''
    return random.randint(0, 1)

def crossover_generation(generation, size, generation_num, gene_num, gene_mutation_rate):
    index = 0
    generation_num = generation_num - 1
    while generation_num > 0:
        f_single = generation.pop(0)
        f_genes = f_single["gene"]
        generation_num = generation_num - 1
        m_single = generation.pop(random.randint(0, generation_num))
        m_genes = m_single["gene"]
        generation_num = generation_num - 1
        f = []
        m = []
        for i in xrange(0, gene_num):
            f_gene = f_genes[i]
            m_gene = m_genes[i]
            a = []
            b = []
            if mutate_or_not(gene_mutation_rate):
                for j in xrange(0, 6):
                    a.append(f_gene[j] + int(random.normalvariate(0, 0.5) * size[0]))
                    if a[j] > size[0]:
                        a[j] = random.randint(0, size[0] - 1)
                    if a[j] < 0:
                        a[j] = random.randint(0, size[0] - 1)
                for j in xrange(6, 9):
                    a.append(f_gene[j] + int(random.normalvariate(0, 0.5) * 255))
                    if a[j] > 255:
                        a[j] = random.randint(0, 255)
                    if a[j] < 0:
                        a[j] = random.randint(0, 255)
            else:
                a = [g for g in f_gene]
            if mutate_or_not(gene_mutation_rate):
                for k in xrange(0, 6):
                    # b.append(m_gene[k] + int(random.random() * 2 * size[0] - size[0]))
                    b.append(m_gene[k] + int(random.normalvariate(0, 0.5) * size[0]))
                    if b[k] > size[0]:
                        b[k] = random.randint(0, size[0] - 1)
                    if b[k] < 0:
                       b[k] = random.randint(0, size[0] - 1) 
                for k in xrange(6, 9):
                    b.append(m_gene[k] + int(random.normalvariate(0, 0.5) * 255))
                    if b[k] > 255:
                        b[k] = random.randint(0, 255)
                    if b[k] < 0:
                        b[k] = random.randint(0, 255) 
            else:
                b = [g for g in m_gene]
            if f_or_m():
                f.append(tuple(a))
                m.append(tuple(b))
            else:
                f.append(tuple(b))
                m.append(tuple(a))
        generation.append({'rate':0, 'gene':f})
        generation.append({'rate':0, 'gene':m})

def natural_selection(generation, generation_num, natural_selection_num):
    '''
        除掉匹配率最低的natural_selection_num个，然后将匹配率最高的natural_selection_num * 2随机复制
        适者生存
        优秀的parents有更高概率遗传基因给后代
        like 28定律
    '''
    for i in xrange(0, natural_selection_num - 1):
        generation.pop()
    for i in xrange(0, natural_selection_num - 1):
        generation.append(generation[random.randint(0, natural_selection_num * 3 - 1)])

def do_it(generation, generation_num, gene_num, size, to_pic_rate):
    '''
        计算种群各个个体的匹配率，写入generation[i]["rate"]
    '''
    for i in xrange(0, generation_num):
        single = generation[i]
        gene = single['gene']
        base_img = Image.new('RGBA', size)
        base_draw = ImageDraw.Draw(base_img)
        base_draw.polygon([(0, 0), (0, size[1] - 1), (size[0] - 1, size[1] - 1), (size[0] - 1, 0)], fill = (0, 0, 0, 0))
        t1 = time.time()
        for j in xrange(0, gene_num):
            img = Image.new('RGBA', size)
            draw = ImageDraw.Draw(img)
            single_gene = gene[j]
            draw.polygon([(single_gene[0], single_gene[1]), (single_gene[2], single_gene[3]), (single_gene[4],single_gene[5])],\
                            fill = (single_gene[6], single_gene[7], single_gene[8], 120))
            base_img = Image.alpha_composite(base_img, img)
        t2 = time.time()
        single_rate = [base_img.getpixel((x, y)) for x in xrange(0, size[0] - 1) for y in xrange(0, size[1] - 1)]
        generation[i]['rate'] = sum([abs(single_rate[a][0] - to_pic_rate[a][0]) + \
                                    abs(single_rate[a][1] - to_pic_rate[a][1]) + \
                                    abs(single_rate[a][2] - to_pic_rate[a][2]) \
                                    for a in xrange(0, len(single_rate))])
    generation.sort(lambda x,y : cmp(x['rate'], y['rate']))

def GA_engine_init(generation, generation_num, gene_num, size_1):
    '''
        种群generation初始化
        generation = [{"rate":0.123, "gene":[(x1,y1,x2,y2,x3,y3,g,b,a,r), (x1,y1,x2,y2,x3,y3,g,b,a,r), ……]},
                      {"rate":0.123, "gene":[(x1,y1,x2,y2,x3,y3,g,b,a,r), (x1,y1,x2,y2,x3,y3,g,b,a,r), ……]},
                      ……
                     ]
        rate是相似度，gene是generation_num个基因，里面存了三个点的坐标，和rgba的参数，最后一个参数是透明度
        这里参数设置颜色好像有问题。尤其是透明度。 
        透明度过低，合成的图片覆盖太严重。
    '''
    for i in xrange(0, generation_num):
        single = {}
        single['rate'] = 0
        total_gene = []
        for j in xrange(0, gene_num):
            gene = (random.randint(0, size_1[0]), random.randint(0, size_1[0]), random.randint(0, size_1[0]), \
                    random.randint(0, size_1[0]), random.randint(0, size_1[0]), random.randint(0, size_1[0]), \
                    random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            total_gene.append(gene)
        single['gene'] = total_gene
        generation.append(single)

def to_pic_init(size, path="/Users/Pike/CODES/pic/ttt.png"):
    img = Image.open(path).resize(size).convert('RGBA')
    return [img.getpixel((x, y)) for x in xrange(0, size[0] - 1) for y in xrange(0, size[0] - 1)]

def main():
    '''
        最近看到pep8 感觉好捉急。。。
        函数定义空两行。。。。。。
    '''
    # 遗传多少代
    select_num = 200000
    # 个体数量 ||每一代的个体数量
    generation_num = 80
    # 基因数量
    gene_num = 120
    # 种群列表
    generation = []
    # 自然选择率 未启用
    natural_selection_rate = 0.1
    # 自然选择数量
    natural_selection_num = 4
    # 个体变异概率 与上面是两种变异方式
    single_mutation_rate = 0.1
    # 基因变异概率 
    gene_mutation_rate = 0.02
    
    size = (100, 100)

    size_1 = (size[0] - 1, size[1] - 1)

    to_pic_rate = []

    GA_engine_init(generation, generation_num, gene_num, size_1)
    
    to_pic_rate = to_pic_init(size, "/Users/Pike/CODES/pic/ttt.png")
    a = 0
    for i in xrange(0, select_num):
        a = a + 1
        
        print len(generation[0]["gene"])
        time0 = time.time()
        do_it(generation, generation_num, gene_num, size, to_pic_rate)
        if a > 9:
            print generation
            for j in xrange(0, len(generation)):
                print generation[j]["rate"]
            create_one_pic(i, size, generation, generation_num, gene_num)
            a = 0
        natural_selection(generation, generation_num, natural_selection_num)
        crossover_generation(generation, size, generation_num, gene_num, gene_mutation_rate)
        time3 = time.time()
        print "This is NO:" + str(i) + "selection"
        print time3 - time0
    create_pic(generation, generation_num, gene_num)

    generation.sort(lambda x,y : cmp(x['rate'], y['rate']))
    print generation[0]["rate"]


if __name__ == '__main__':
    main()
