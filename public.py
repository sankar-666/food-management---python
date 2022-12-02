
from flask import *
from database import *
import uuid


public=Blueprint('public',__name__)



@public.route('/')
def home():
    return render_template("public/home.html")

@public.route("/donreg",methods=['get','post'])
def donreg():
    if 'btn' in request.form:
        fname=request.form['name']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        id=request.files['id']
        proof="static/images/"+ str(uuid.uuid4()) +id.filename
        id.save(proof)
        lat=request.form['lat']
        long=request.form['long'] 
        uname=request.form['uname']
        pswd=request.form['pswd']
        

        q="insert into `login` values(NULL,'%s','%s','pending')"%(uname,pswd)
        res=insert(q)

        w="insert into donor value(NULL,'%s','%s','%s','%s','%s','%s','%s','%s')"%(res,fname,place,phone,email,proof,lat,long)
        uidd=insert(w)
        return redirect(url_for("public.login"))
        # session['userid']=uidd

    return render_template("public/donreg.html")

@public.route('/volreg',methods=['get','post'])
def volreg():
    if 'btn' in request.form:
        fname=request.form['name']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        id=request.files['id']
        proof="static/images/"+ str(uuid.uuid4()) +id.filename
        id.save(proof)
        lat=request.form['lat']
        long=request.form['long'] 
        uname=request.form['uname']
        pswd=request.form['pswd']
        

        q="insert into `login` values(NULL,'%s','%s','pending')"%(uname,pswd)
        res=insert(q)

        w="insert into volunteer value(NULL,'%s','%s','%s','%s','%s','%s','%s','%s')"%(res,fname,place,phone,email,proof,lat,long)
        uidd=insert(w)
        return redirect(url_for("public.login"))
    return render_template("public/volreg.html")


@public.route('/recipreg',methods=['get','post'])
def recipreg():
    if 'btn' in request.form:
        fname=request.form['name']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
       
        lat=request.form['lat']
        long=request.form['long'] 
        uname=request.form['uname']
        pswd=request.form['pswd']
        

        q="insert into `login` values(NULL,'%s','%s','pending')"%(uname,pswd)
        res=insert(q)

        w="insert into recipient value(NULL,'%s','%s','%s','%s','%s','%s','%s')"%(res,fname,place,phone,email,lat,long)
        uidd=insert(w)
        return redirect(url_for("public.login"))
    return render_template("public/recipreg.html")


@public.route('/mainreg')
def mainreg():
    return render_template("public/mainreg.html")

@public.route('/login',methods=['post','get'])
def login():

    if 'btn' in request.form:
        uname=request.form['uname']
        pasw =request.form['pswd']

        q="select * from login where username='%s' and password='%s'"%(uname,pasw)
        res=select(q)
        session['loginid']=res[0]["login_id"]
        
        

        if res:
            utype=res[0]["usertype"]
            if utype == "admin":
                return redirect(url_for("admin.home"))
            elif utype == "donor":
                q="select * from donor where login_id='%s'"%(session['loginid'])
                res=select(q)
           
                if res:
                    session['donorid']=res[0]['donor_id']
                    return redirect(url_for('donor.home'))
                    
                       
            elif utype == "recipient":
                a="select * from recipient where login_id='%s'"%(session['loginid'])
                res2=select(a)
                if res2:
                    session['recipientid']=res2[0]['recipient_id']
                return redirect(url_for("recipient.home"))
            elif utype == "volunteer":
                a="select * from volunteer where login_id='%s'"%(session['loginid'])
                res3=select(a)
                if res3:
                    session['volunteerid']=res3[0]['volunteer_id']
                return redirect(url_for("volunteer.home"))
            else:
                return redirect(url_for("public.home"))


    return render_template("public/login.html")