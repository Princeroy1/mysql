from django.shortcuts import render
import mysql.connector as sql
# Create your views here.
fn=''
ln=''
un=''
em=''
p=''

def sin(request):
    global fn,ln,un,em,p
    if request.method=="POST":
        m=sql.connect(host="localhot",user="root",password="",database="student")
        cursor=m.cursor()
        d=request.Post
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="username":
                un=value
            if key=="email":
                em=value
            if key=="password":
                p=value
        c="insert into student Values('{},{},{},{},{}')".format(fn,ln,un,em,p)
        cursor.execute(c)
        m.commit()
    return render(request,'signup.html')