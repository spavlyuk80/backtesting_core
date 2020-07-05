#!/usr/bin/env python
# -*- coding:utf-8 -*-


class IG(object):
    username = u"spavlyuk80"
    password = "Sergunya_1904"
    api_key = "82c49849528a2d1b251cb137b064bb34c19765a2"
    acc_type = "DEMO"  # LIVE / DEMO
    acc_number = "Z350S2"

    proxies = {'https': u''}
    epic = 'IX.D.FTSE.IFM.IP'

    def is_demo(self):
        if self.acc_type == "DEMO":
            return True
        else:
            return False


if __name__ == "__main__":
    personal = IG()
    print (personal.username)

