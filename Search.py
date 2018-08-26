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
from lxml import etree
from data_models import VideoData

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


def main():
    """Main."""
    # print search_by_keyword(u'神探狄仁杰'.encode('utf-8'))
    html = """<dl class='item'>
                    <dt><sup>Hot</sup>&nbsp;<a href='//zhongzishenqi.cc/show/4f00e8a3ef6e6f03ee30cdbac4fbb99b8077fa4c.html' target='_blank'>[下载库www.xzk.cc]<b>神</b><b>探</b><b>狄</b><b>仁</b><b>杰</b>4.720p</a></dt>
                    
                    <dd class='attr'><span>收录时间:<b>2011-03-14</b></span><span>文件大小:<b>19.61 GB</b></span><span>文件数:<b>91</b></span><span>下载速度:<b>极快</b></span><span>人气:<b>348342</b></span><span><a style='color:#777;' href='//zhongzishenqi.cc/show/4f00e8a3ef6e6f03ee30cdbac4fbb99b8077fa4c.html#magnetlink' target='_blank'>磁力链接</a></span><span><a style='color:#777;' href='//zhongzishenqi.cc/show/4f00e8a3ef6e6f03ee30cdbac4fbb99b8077fa4c.html#download' target='_blank'>下载BT种子</a></span></dd>
                    
                    <dd class='flist'><p><img src='//zhongzishenqi.cc/images/ext/video.png' /><span class='name'><b>神</b><b>探</b><b>狄</b><b>仁</b><b>杰</b>4.12.mkv</span><span class='size'>528.3 MB</span></p><p><img src='//zhongzishenqi.cc/images/ext/video.png' /><span class='name'><b>神</b><b>探</b><b>狄</b><b>仁</b><b>杰</b>4.05.mkv</span><span class='size'>528.16 MB</span></p></dd>
                    <dd class='related'><img src='//zhongzishenqi.cc/images/favorite.png' /><span>喜欢：</span><a  class='show' href='//zhongzishenqi.cc/shenqi/%E4%B8%8B%E8%BD%BD%E5%BA%93www/1-1-0/' target='_blank'>下载库www</a><a  class='show' href='//zhongzishenqi.cc/shenqi/%E7%A5%9E%E6%8E%A2%E7%8B%84%E4%BB%81%E6%9D%B04/1-1-0/' target='_blank'>神探狄仁杰4</a></dd>
                    </dl>
<dl class='item'>
                    <dt><sup>Hot</sup>&nbsp;<a href='//zhongzishenqi.cc/show/3fb8cdec6baa993d9b96d6743f7ad974ff118fc8.html' target='_blank'>[下载库www.xzk.cc]<b>神</b><b>探</b><b>狄</b><b>仁</b><b>杰</b>2.480P</a></dt>
                    
                    <dd class='attr'><span>收录时间:<b>2011-03-10</b></span><span>文件大小:<b>13.74 GB</b></span><span>文件数:<b>93</b></span><span>下载速度:<b>极快</b></span><span>人气:<b>221052</b></span><span><a style='color:#777;' href='//zhongzishenqi.cc/show/3fb8cdec6baa993d9b96d6743f7ad974ff118fc8.html#magnetlink' target='_blank'>磁力链接</a></span><span><a style='color:#777;' href='//zhongzishenqi.cc/show/3fb8cdec6baa993d9b96d6743f7ad974ff118fc8.html#download' target='_blank'>下载BT种子</a></span></dd>
                    
                    <dd class='flist'><p><img src='//zhongzishenqi.cc/images/ext/video.png' /><span class='name'>[下载库www.xzk.cc]<b>神</b><b>探</b><b>狄</b><b>仁</b><b>杰</b>2.CCTV.Shen.Tan.Di.Ren.Jie.II.EP14.HDTV.480p.x264.AAC.xzk.mkv</span><span class='size'>355.87 MB</span></p><p><img src='//zhongzishenqi.cc/images/ext/video.png' /><span class='name'>[下载库www.xzk.cc]<b>神</b><b>探</b><b>狄</b><b>仁</b><b>杰</b>2.CCTV.Shen.Tan.Di.Ren.Jie.II.EP22.HDTV.480p.x264.AAC.xzk.mkv</span><span class='size'>355.62 MB</span></p></dd>
                    <dd class='related'><img src='//zhongzishenqi.cc/images/favorite.png' /><span>喜欢：</span><a  class='show' href='//zhongzishenqi.cc/shenqi/%E7%A5%9E%E6%8E%A2%E7%8B%84%E4%BB%81%E6%9D%B02/1-1-0/' target='_blank'>神探狄仁杰2</a><a  class='show' href='//zhongzishenqi.cc/shenqi/%E4%B8%8B%E8%BD%BD%E5%BA%93www/1-1-0/' target='_blank'>下载库www</a></dd>
                    </dl>
            """

    page = etree.HTML(html.lower().decode('utf-8'))
    print page.xpath("string(//dl/dt/a)")
    print page.xpath(u"//dl/dd[1]/span[5]/b/text()")
    ret = search_by_keyword(u'legs and ass')
    for vd in ret:
        print vd.title
        print '\t', vd.get_url()
        print ''


def search():
    import sys
    ret = search_by_keyword(sys.argv[1].decode('utf-8'))
    for vd in ret:
        print vd.title
        print '\t', vd.get_url()
        print ''



if __name__ == '__main__':
    search()
