from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime
import pymysql


def hello(request):
    return HttpResponse("Hello World")


def current_datetime(request):
    now = datetime.datetime.now()
    # html = "<html><body>It is now {}.</body></html>".format(now)
    # t = Template("<html><body>It is now {{ current_date }}.</body></html>")
    # t = get_template("current_datetime.html")
    # html = t.render(Context({'current_date': now}))
    # return HttpResponse(html)
    return render_to_response('current_datetime.html', {'current_date': now})


def hours_head(request, offset):
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In {} hour(s), it will be {}</body></html>".format(offset, dt)
    return HttpResponse(html)


def book_list(request):
    db = pymysql.connect("localhost", "root", "123456", "helloworld")
    cursor = db.cursor()
    cursor.execute("SELECT name FROM books ORDER BY name")
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response("book_list.html", {'names': names})