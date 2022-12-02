from flask import *
from database import *


volunteer=Blueprint('volunteer',__name__)

@volunteer.route('/home')
def home():
    return render_template('volunteer/home.html')

@volunteer.route('/viewfoodreq')
def viewfoodreq():
    data={}
    vid=session['volunteerid']
    q="select *,requst.quantity as quantity from forward_volunteer inner join requst on requst.requst_id=forward_volunteer.request_id inner join excess_food using (excessfood_id) inner join donor using (donor_id)"
    res=select(q)
    data['res']=res

    if 'action' in request.args:
        action=request.args['action']
        if action== 'assign':
            q="update forward_volunteer set volunteer_id='%s'"%(vid)
            update(q)
            return redirect(url_for('volunteer.home'))    
    
    return render_template('volunteer/viewfoodreq.html',data=data)

@volunteer.route('/order')
def order():
    data={}
    vid=session['volunteerid']
    q="select *,requst.quantity as quantity from forward_volunteer inner join requst on requst.requst_id=forward_volunteer.request_id inner join excess_food using (excessfood_id) inner join donor using (donor_id) where volunteer_id > 0 "
    res=select(q)
    data['res']=res

    if 'action' in request.args:
        action=request.args['action']
        rid=request.args['rid']
        if action=='assign':
            q="update forward_volunteer set status='delevered sucessfull' where volunteer_id='%s'"%(vid)
            update(q)
            q="update requst set status='delevered sucessfull' where requst_id='%s'"%(rid)
            update(q)
            return redirect(url_for('volunteer.home'))


    return render_template('volunteer/order.html',data=data)



@volunteer.route("/addfeedback",methods=['get','post'])
def addfeedback():

    lid=session['loginid']

    if 'btn' in request.form:
        feed=request.form['feed']

        q="insert into `feedback` values(null,'%s','%s','pending',curdate())"%(lid,feed)
        insert(q)
        return redirect(url_for("volunteer.addfeedback"))

    data={}
    q="select * from feedback inner join login on login.login_id=feedback.sender_id where usertype='volunteer'"
    ews=select(q)
    data['ews']=ews 

    return render_template("volunteer/addfeedback.html",data=data)