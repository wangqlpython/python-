# -*- coding: utf-8 -*-
import scrapy
import json
import re

from copy import deepcopy

class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['tencent.com']
    # start_urls = ['https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1580111339825&countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn']
    start_urls=['https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1580117823073&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn']

    def parse(self, response):
        i = int(re.findall("pageIndex=(\d+)", response.request.url)[0])
        print("开始爬取%s" %i)
        item = {}
        ret=json.loads(response.body.decode())
        info =ret["Data"]["Posts"]
        data_count=ret["Data"]["Count"]
        # print(data_count)
        page=int((data_count/10))+1
        # print("总页数",page)
        for id in info:
            item["titel"]=id["RecruitPostName"]
            # item["Responsibility"]=id["Responsibility"]
            # item["LastUpdateTime"] = id["LastUpdateTime"]
            # item["PostURL"]=id["PostURL"]
            # item["PostId"]=id["PostId"]
            item_url="https://careers.tencent.com/tencentcareer/api/post/ByPostId?postId={}&language=zh-cn"
            # print(item_url.format(item["PostId"]))
            yield scrapy.Request(
                item_url.format(id["PostId"]),
                callback=self.parse_item,
                meta={"item":deepcopy(item)},
            )
            # yield item
        # print(response.request.url)
        # print("当前网页",response.url)
        # i = int(re.findall("pageIndex=(\d+)",response.request.url)[0])
        url = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1580117823073&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn"
        print("第%s页爬取结束" % i)
        if i<(page-417):
            next_url=url.format(i+1)
            yield scrapy.Request(
                next_url,
                callback=self.parse,
                )

    def parse_item(self,response):
        item=response.meta["item"]
        info= response.body.decode()
        info=json.loads(info)
        # print(info)
        item["position"]=info["Data"]["LocationName"]
        yield item








