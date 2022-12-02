

import re
from flask import *
from database import *


donor=Blueprint('donor',__name__)


@donor.route('/home')
def home():
    return render_template("donor/home.html")


@donor.route('/addfooddetails',methods=['get','post'])
def addfooddetails():
    did=session['donorid']
    if 'btn' in request.form:
        food=request.form['food']
        quant=request.form['quant']

        q="insert into excess_food values(null,'%s','%s','%s','available')"%(did,food,quant)
        insert(q)
        return redirect(url_for('donor.addfooddetails'))
    return render_template('donor/addfooddetails.html')

@donor.route('/viewreq')
def viewreq():
    data={}
    q="select *,requst.quantity as quantity  from requst inner join excess_food using (excessfood_id) inner join recipient using (recipient_id)"
    res=select(q)
    data['res']=res

    if 'action' in request.args:
        action=request.args['action']
        rid=request.args['rid']
        eid=request.args['eid']
        qty=request.args['qty']
        if action=="assign":
            q="update excess_food set quantity=quantity-'%s' where excessfood_id='%s'  "%(qty,eid)
            update(q)
            q="update requst set status='forwared to Volunteer' where requst_id='%s'"%(rid)
            update(q)
            q="insert into forward_volunteer values(null,'%s',0,'delivery pending')"%(rid)
            insert(q)
            return redirect(url_for('donor.home'))

        if action=="customer":
            q="update excess_food set quantity=quantity-'%s' where excessfood_id='%s'  "%(qty,eid)
            update(q)
            q="update requst set status='delevered sucessfull' where requst_id='%s'"%(rid)
            update(q)
            return redirect(url_for('donor.home'))

        if action=="direct":
            q="update excess_food set quantity=quantity-'%s' where excessfood_id='%s'  "%(qty,eid)
            update(q)
            q="update requst set status='delevered sucessfull' where requst_id='%s'"%(rid)
            update(q)
            return redirect(url_for('donor.home'))
    return render_template("donor/viewreq.html",data=data)

@donor.route("/addfeedback",methods=['get','post'])
def addfeedback():

    lid=session['loginid']

    if 'btn' in request.form:
        feed=request.form['feed']

        q="insert into `feedback` values(null,'%s','%s','pending',curdate())"%(lid,feed)
        insert(q)
        return redirect(url_for("donor.addfeedback")) 

    data={}
    q="select * from feedback inner join login on login.login_id=feedback.sender_id where usertype='donor'"
    ews=select(q)
    data['ews']=ews

    return render_template("donor/addfeedback.html",data=data)