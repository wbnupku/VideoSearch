# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright All Rights Reserved
#
###############################################################################
"""
 This module provides.

Authors: wangxiao05(wbnupku@gmail.com)
Date:    2018/08/19 19:29:30
"""
import requests
import pyperclip
from lxml import etree
from data_models import VideoData


import Tkinter as tk


def run_search():
    window = tk.Tk()
    window.title(u'搜索')
    window.geometry('400x400')
    e = tk.Entry(window)
    # Entry的第一个参数是父窗口，即这里的window
    # *表示输入的文本变为星号，在Entry不可见内容，若为None则表示为输入文本以原形式可见
    e.pack()

    def insert_point():
        var = e.get()
        t.insert('insert', var)

    def click_and_process():
        var = e.get()
        e.delete(0, tk.END)
        text = u'搜索词: ' + var + u'\n'
        t.insert('end', text + '\n')
        t.pack()
        ret = search_by_keyword(var)

        text += u'搜索结果: %d\n' % len(ret)
        for i, vd in enumerate(ret):
            if i == 0:
                pyperclip.copy(vd.rid)
                pyperclip.paste()
            text += unicode(i) + u'. ' + vd.title + u'\n\t' + vd.rid.decode('utf-8') + u'\n'
        t.delete(1.0, tk.END)
        t.insert('end', text + '\n')

    # 这里的end表示插入在结尾，可以换为1.2，则插入在第一行第二位后面
    # b1 = tk.Button(window, text='insert point', width=15, height=2, command=insert_point)
    # b1.pack()
    b2 = tk.Button(window, text=u'搜索', width=15, height=2, command=click_and_process)
    window.bind('<Return>', lambda event: click_and_process())
    b2.pack()
    t = tk.Text(window)  # 这里设置文本框高，可以容纳两行
    t.pack()
    e.focus_set()
    window.mainloop()


def search_by_keyword(keyword):
    if isinstance(keyword, unicode):
        keyword = keyword.encode('utf-8')
    url_pat = 'https://zhongzishenqi.cc/shenqi/{}/1-4-0/'.format(keyword)
    html = requests.get(url_pat).content
    page = etree.HTML(html.lower().decode('utf-8'))
    resource_urls = page.xpath(u"//dl/dt/a/@href[1]")
    resource_ids = map(lambda x: x.split('/')[-1].split('.')[0], resource_urls)
    popularity = [int(e) for e in page.xpath("//dl/dd[1]/span[5]/b/text()")]
    titles = page.xpath("//dl/dt/a")
    rsc_size_content = page.xpath("//dl/dd[1]/span[2]/b/text()")
    rsc_sizes = []
    for s in rsc_size_content:
        s_mb = float(s.split()[0])
        if s[-2:] in ['gb', 'GB']:
            s_mb *= 1024
        elif s[-2:] in ['kb', 'KB']:
            s_mb /= 1024
        rsc_sizes.append(s_mb)

    ret = []
    for i in range(len(resource_urls)):
        ret.append(VideoData(rid=resource_ids[i],
                             popularity=popularity[i],
                             title=titles[i].xpath('string()'),
                             rsc_size=rsc_sizes[i]))

    return ret




if __name__ == '__main__':
    run_search()
