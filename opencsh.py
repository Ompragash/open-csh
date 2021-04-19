#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import webbrowser
import argparse

class OpenCSH:
    def __init__(self):
        
        #CLI args
        self.cli_parse()

        if self.args.caseid:
            self.open_case_links()

        if self.args.caseidfile:
            self.open_multiple_case_links()

    def cli_parse(self):
        parser = argparse.ArgumentParser(description='OpenCSH is a CLI tool written in Python3 to open one or more CSH case links in the defaultly used Webbrowser.')
        parser.add_argument('--case-id', metavar="", dest='caseid', help="Opens the given Case ID in a new webbrowser tab. Eg: '--case-id 123456'")
        parser.add_argument('--case-id-file', metavar="", dest='caseidfile', help="Opens the list of Case ID's from case-id.txt file in a new browser tab. Eg: '--case-id-file case-id.txt'")
        self.args = parser.parse_args()

    def open_multiple_case_links(self):
        j = []
        with open(self.args.caseidfile, 'r') as idlist:
            for i in idlist:
                case = i[:-1]
                j.append(case)
                for k in j:
                    webbrowser.open("https://csh.cloudera.com/ccs/index.html#/case/" + k + "/case-details")

    def open_case_links(self):
        webbrowser.open("https://csh.cloudera.com/ccs/index.html#/case/" + self.args.caseid + "/case-details")

OpenCSH()
