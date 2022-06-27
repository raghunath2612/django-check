from urllib import request
from django.shortcuts import render
import pymysql


def printHello(request):
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password = "hello@123",
        db='students',
        )
    curr = conn.cursor()
    curr.execute("select * from student")
    output = curr.fetchall()
    for i in output:
        print(i)
    return render(request,'hello.html',{"studentData":output[0]})