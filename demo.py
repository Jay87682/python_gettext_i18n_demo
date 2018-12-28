#!/usr/bin/python3
import gettext

zh = gettext.translation("hello", "locale", languages=["zh_CN"])
zh.install()
print(_('Hello'))


