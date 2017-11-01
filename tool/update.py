#! /usr/bin/python3

import os
import sys
import config

if len(sys.argv) >= 2:
    for page in sys.argv[1:]:
        if page in config.PAGES:
            os.system("python3 tool/merge.py %s %s" % config.PAGES[page])
        elif page == "all":
            for p in config.PAGES:
                print("### updating " + p)
                os.system("python3 tool/merge.py %s %s" % config.PAGES[p])
        else:
            print("no such page %s(fix config.py!!!)" % page)
else:
    print("wrong argument")
    print("usage: " + sys.argv[0] + " <name_of_the_page(can be found in config.py) or 'all' to update all pages>")
