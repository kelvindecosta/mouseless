from django.shortcuts import render,Httpresponse,redirect
from event.models import *

# Create your views here.

def register_team(req):
    if req.method == "POST":
        team = req.POST['team']
        team_type = req.POST['team_type']
        pwd = req.POST['pwd']
        cpwd = req.POST['cpwd']
        if pwd != cpwd:
            raise ("password and confirm_password does not match")
        t= Team(team=team,team_type=team_type,pwd=pwd)
        t.save()
        return Httpresponse("You are registered")
    else:
        return render(req,"register.html")

def login_team(req):
    if req.method == "POST":
        team = req.POST["team"]
        pwd= req.POST['pwd']
        result=Team.objects.filter(tname=team,pwd=pwd)
        if len(result)>0:
            team=result[0]
            req.session['tname'] = team.tname
            return redirect('/details')
        else:
            req.session['msg']= 'Invalid Team name or Password'
            return redirect('login')
    else:
        if 'msg' in req.session:
            msg=req.session['msg']
        else:
            msg = ""
            return render(req,'login.html',locals())

def home_page(req):
    if req.method=='POST':
        if 'add' in req.POST:
            return redirect('/details')
        else:
            return redirect('/task')
    else:
        return render(req,'home.html')

def details(req):
    if req.method=="POST":
        pname1=req.POST['pname1']
        email1=req.POST['email1']
        cont1=req.POST['cont1']
        pname2=req.POST['pname2']
        email2=req.POST['email2']
        cont2=req.POST['cont2']
        i = Information(pname1=pname1,email1=email1,cont1=cont1,pname2=pname2,email2=email2,cont2=cont2)
        i.save()
        return render(req,'details.html')
