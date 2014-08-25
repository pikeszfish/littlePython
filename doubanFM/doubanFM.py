#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import logging
import time
import requests
import json

from douban import Douban

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%Y-%b-%d, %H:%M:%S',
                filename='myapp.log',
                filemode='a')


class doubanFM():
    def __init__(self):
        self.douban_username = None
        self.douban_password = None
        # self.douban_cookie = None
        # self.expire = None
        # self.token = None
        self.douban_enable = False
        try:
            arg = sys.argv[1]
            arg = sys.argv[2]
            self._do_config()
        except getopt.GetoptError as e:
            logging.error("parse error" + e)
        except IndexError:
            self._load_config()


        self.douban = douban(self.douban_username, self.douban_password)
        


    def _do_config(self):
        opts,args = getopt.getopt(sys.argv[1:], "u:p:h", ["username=", "password=", "help"]);
        print("============ opts ==================");
        print(opts);
        print("============ args ==================");
        print(args);
        #check all param
        for opt,arg in opts:
            if opt in ("-h", "--help"):
                usage();
                sys.exit(1);
            elif opt in ("-u", "--username="):
                self.douban_username = arg
            elif opt in ("-p", "--password="):
                self.douban_password = arg
        if self.douban_username is not None and self.douban_password is not None:
            self.douban_enable = True

    def _load_config(self):
        try:
            f = open("cache.json", "r")
            cache = json.load(f)
        except FileNotFoundError:
            logger.debug("Cache file not found.")
        try:
            self.douban_username = cache["douban_username"]
            self.douban_password = cache["douban_password"]
            self.douban_enable = True
        except (KeyError, ValueError):
            self.douban_account = False
            logger.error("Cache title is not true")










