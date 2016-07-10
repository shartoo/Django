# -*- coding: utf-8 -*-

from django.http import HttpResponse

from models import Article

def testdb(request):
    test1 = Article(pos_id =1,author='xiatao',title='论个人主义',content='一个伟大的个人主义精神，一个')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")
