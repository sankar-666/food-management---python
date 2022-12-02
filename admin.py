
from flask import *
from database import *


admin=Blueprint('admin',__name__)


@admin.route('/home')
def home():
    return render_template("admin/home.html")


@admin.route('/changepassword',methods=['get','post'])
def changepassword():
    if 'btn' in request.form:
        cpwd=request.form['cpwd']
        newpwd=request.form['newpwd']
        conformpwd=request.form['conformpwd']

        q="select * from login where usertype='admin' and password='%s'" %(cpwd)
        res=select(q)
        if res:
            if newpwd==conformpwd:
                q="update login set password='%s' where usertype='admin'"%(newpwd)
                update(q)
                return redirect(url_for("admin.home"))
            else:
                flash("New passwords Dosent Match ")
                return redirect(url_for("admin.changepassword"))
        else:
            flash("Current Password Entered is Wrong")
            return redirect(url_for("admin.changepassword"))
    return render_template("admin/changepassword.html")




@admin.route('/verifydonor')
def verifydonor():
    data={}
    q="select * from donor inner join login using (login_id)"
    res=select(q)
    data['res']=res

    if 'action' in request.args:
        action=request.args['action']
        lid=request.args['id']

        if action == 'update':
            q="update login set usertype='donor' where login_id='%s'"%(lid) 
            update(q)
            return redirect(url_for('admin.verifydonor'))
    return render_template('admin/verifydonor.html',data=data)

@admin.route('/verifyrecipient')
def verifyrecipient():
    data={}
    q="select * from recipient inner join login using (login_id)"
    res=select(q)
    data['res']=res

    if 'action' in request.args:
        action=request.args['action']
        lid=request.args['id']

        if action == 'update':
            q="update login set usertype='recipient' where login_id='%s'"%(lid) 
            update(q)
            return redirect(url_for('admin.verifyrecipient'))
    return render_template('admin/verifyrecipient.html',data=data)



@admin.route('/verifyvolunteer')
def verifyvolunteer():
    data={}
    q="select * from volunteer inner join login using (login_id)"
    res=select(q)
    data['res']=res

    if 'action' in request.args:
        action=request.args['action']
        lid=request.args['id']

        if action == 'update':
            q="update login set usertype='volunteer' where login_id='%s'"%(lid) 
            update(q)
            return redirect(url_for('admin.verifyvolunteer'))
    return render_template('admin/verifyvolunteer.html',data=data)



@admin.route('/viewfeedback',methods=['get','post'])
def viewfeedback():
    data={}
    q="""SELECT feedback_id,login_id,sender_id,feedback,reply,date,name,usertype FROM feedback INNER JOIN login ON login.login_id=feedback.sender_id INNER JOIN volunteer USING (login_id)
UNION
SELECT feedback_id,login_id,sender_id,feedback,reply,date,name,usertype FROM feedback INNER JOIN login ON login.login_id=feedback.sender_id INNER JOIN donor USING (login_id) 
UNION
SELECT feedback_id,login_id,sender_id,feedback,reply,date,name,usertype FROM feedback INNER JOIN login ON login.login_id=feedback.sender_id INNER JOIN recipient USING (login_id)"""
    

    res=select(q)
    data['res']=res

    if 'action' in request.args:
        action=request.args['action']
        lid=request.args['id']
    else:
        action=None
    
    if action=='update':
        data['action']=action
        if 'btn' in request.form:
            repley=request.form['rep']
            
            q="update feedback set reply='%s' where feedback_id='%s' "%(repley,lid)
            update(q)
            return redirect(url_for("admin.viewfeedback"))
    

    return render_template("admin/viewfeedback.html",data=data)


@admin.route('/viewreq')
def viewreq():
    data={}
    q="select *,requst.quantity as quantity  from requst inner join excess_food using (excessfood_id) inner join recipient using (recipient_id)"
    res=select(q)
    data['res']=res


    return render_template("admin/viewreq.html",data=data)


@admin.route('/vieworderdetails')
def vieworderdetails():
    data={}
    q="select *,requst.status as status  from requst inner join excess_food using (excessfood_id) inner join recipient using (recipient_id)"
    res=select(q)
    data['res']=res


    return render_template("admin/vieworderdetails.html",data=data)