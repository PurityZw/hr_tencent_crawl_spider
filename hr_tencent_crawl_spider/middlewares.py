# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
from .settings import USER_AGENT_LIST
import random

class UserAgentMiddleWare(object):
    """
    User-Agent List
    """
    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(USER_AGENT_LIST)


class ProxyAddrMiddleWare(object):
    """
    ProxyAddr List
    """
    def process_request(self, request, spider):
        request.meta['proxy'] = "maozhaojun:ntkn0npx@114.67.224.167:16819"