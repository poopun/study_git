import re

from urllib import request

# 断点调试 F5 单步F10 进入某个函数或对象得内部
class Spider():
    # 类变量
    url = 'https://www.huya.com/g/lol'
    root_pattern = '<span class="txt">([\s\S]*?)<span class="num">([\s\S]*?)</span>'
    number_pattern = '<i class="js-num">([\s\S]*?)</i>'
    name_pattern1 = '<i class="nick" title=([\s\S]*?)</i>'
    name_pattern = '"([\s\S]*?)"'

    # __私有方法、实例方法、需要加self
    def __fetch_content(self):
        # 在实例方法里面读取类变量用 Spider.url
        r = request.urlopen(Spider.url)
        # html 是字节码byte 需要转换为字符串
        htmls = r.read()
        # 将html字节码转换为字符串 encoding = 'utf-8' 是用utf-8编码
        htmls = str(htmls, encoding='utf-8')
        return htmls

    # 私有实例方法
    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        anchors = []
        for html in root_html:
            name1 = re.findall(Spider.name_pattern1, str(html))
            # print(name1)
            name = re.findall(Spider.name_pattern, str(name1))
            # print(name)
            number = re.findall(Spider.number_pattern, str(html))
            # print(name)
            # print(number)
            anchor = {'name':name, 'number':number}
            anchors.append(anchor)
        # print(anchors)
        # print(anchors)
        # print(root_html[0])
        return anchors

    # 精炼数据 函数
    def __refine(self, anchors):
        l = lambda anchor: {
            'name':anchor['name'][0].strip(),
            'number':anchor['number'][0]
        }
        return map(l, anchors)

    # 排序函数
    def __sort(self, anchors):s
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return anchors


    # 为sort函数编写比较关键子key
    def __sort_seed(self, anchor):
        # r = re.findall('\d*', anchor['number'])
        # number = float(r[0])
        # if '万' in anchor['number']:
        #     number *= 10000
        return anchor['number']
    # 展现数据函数
    def __show(self, anchors):
        # for rank in range(0, len(anchors)):
        #     print('rank' + str(rank + 1 )
        #     + ':' + anchors[rank]['name']
            # + '  ' + str(anchors[rank]['number']))
            for anchor in anchors:
                print(anchor['name'] + anchor['number'])
    # 公有方法、入口方法、总控方法

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchots = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)
        # print(anchors)


spider = Spider()
spider.go()