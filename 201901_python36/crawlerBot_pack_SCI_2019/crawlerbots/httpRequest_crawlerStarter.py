#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import logging
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
from crawlerBot_pack_SCI_2019.crawlerbots.kakaostoryCrawlerBot import kakao_story_crawler_start
from crawlerBot_pack_SCI_2019.crawlerbots.facebookCrawlerBot import facebook_crawler_start
from crawlerBot_pack_SCI_2019.crawlerbots.instagramCrawlerBot import instagram_crawler_start


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def _set_response(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Headers', 'origin, x-requested-with, content-type, accept')
        self.send_header('Pragma', 'No-Cache')
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('Expires', 'Sun, 01 Jan 2014 00:00:00 GMT')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Cache-Control', 'post-check=0, pre-check=0, FALSE')
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.end_headers()


    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n", str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.parsed_POST_data(post_data)

    def parsed_POST_data(self, post_data):
        #getParam = urllib.parse.unquote(post_data.decode('utf-8'))
        getParam = urllib.parse.unquote(post_data.decode())

        print('입력한 데이터: ', getParam)
        #http://172.30.1.33:8000/kakao_story=https%3A%2F%2Fstory.kakao.com%2F_9W0DZ3&naver_blog=https%3A%2F%2Fblog.naver.com%2Ftramper2&facebook=https%3A%2F%2Fwww.facebook.com%2Fdanny.woo.33&instagram=XXXX&username=%EA%B9%80%ED%83%9C%ED%98%B8
        # kakao_story=https%3A%2F%2Fstory.kakao.com%2F_9W0DZ3&
        # naver_blog=https%3A%2F%2Fblog.naver.com%2Ftramper2&
        # facebook=https%3A%2F%2Fwww.facebook.com%2Fdanny.woo.33&
        # instagram=&
        # username=%EA%B9%80%ED%83%9C%ED%98%B8

        userData = {}



httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()