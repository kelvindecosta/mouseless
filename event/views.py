from django.shortcuts import render,Httpresponse,redirecct
from event.models import *

# Create your views here.

def register_team(req):
    if req.method == "POST":
        team = req.POST['team']
        players = req.POST['players']
        pwd = req.POST['pwd']
        t= Team(team,players,pwd)
        t.save()
        return redirect("#")
    else:
        return render(req,"users.html")

def login_team(req):
    if req.method == "POST":
        Team = req.POST["team"]
        pwd= req.POST['pwd']
        result=Team.objects.filter(tname=team,pwd=pwd)
        if len(result)>0:
            team=result[0]
            req.session['tname'] = team.tname
            return redirect(#)
        else:
            req.session['msg']= 'Invalid Team name or Password'
            return redirect('login')
    else:
        if 'msg' in req.session:
            msg=req.session['msg']
        else:
            msg = ""
            return render(req.'login.html',locals())

def details(req):
    if req.method=="POST":
        pname1=req.POST['pname1']
        email1=req.POST['email1']
        cont1=req.POST['cont1']
        pname2=req.POST['pname2']
        email2=req.POST['email2']
        cont2=req.POST['cont2']
        
