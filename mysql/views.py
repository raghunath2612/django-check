from urllib import request
from django.shortcuts import render
import pymysql


def printHello(request):
    conn = pymysql.connect(
        host='bpojo8ld2swtxhtak50q-mysql.services.clever-cloud.com',
        user='ui80hikunzugjqkz', 
        password = "6l4RtFGqcoaumQoaGrtF",
        db='bpojo8ld2swtxhtak50q',
        )
    curr = conn.cursor()
    curr.execute("select * from student")
    output = curr.fetchall()
    for i in output:
        print(i)
    return render(request,'hello.html',{"studentData":output})