
from flask import *
from database import *


recipient=Blueprint('recipient',__name__)


@recipient.route('/home')
def home():
    return render_template("recipient/home.html")

@recipient.route('/viewfoods',methods=['get','post'])
def viewfoods():
    data={}
    rid=session['recipientid']
    q='select * from excess_food inner join donor using (donor_id)'
    res=select(q)
    data['res']=res


    for i in range(1, len(res)+1):
        if 'btn'+str(i) in request.form:
            eid=request.form['eid'+str(i)]
            types=request.form['types'+str(i)]
            quant=request.form['quant'+str(i)]

            q="insert into requst values(null,'%s','%s','%s','%s','waiting for Conformation')"%(eid,quant,rid,types)
            insert(q)
            return redirect(url_for('recipient.home'))


    # if 'action' in request.args:
    #     action=request.args['action']
    #     id=request.args['id']

    #     if  action == 'update':
    #         q="insert into requst values(null,'%s','%s','booked by recipient')"%(id,rid)
    #         insert(q)
    #         q="update excess_food set status='booked by recipetent' where excessfood_id='%s'"%(id)
    #         update(q)
    #         return redirect(url_for('recipient.home'))
    return render_template("recipient/viewfoods.html",data=data)

@recipient.route('/viewstatus')
def viewstatus():
    data={}
    q="select *,requst.status as rstatus from requst inner join excess_food using(excessfood_id)"
    res=select(q)
    data['res']=res
    return render_template('recipient/viewstatus.html',data=data)


@recipient.route("/addfeedback",methods=['get','post'])
def addfeedback():

    lid=session['loginid']

    if 'btn' in request.form:
        feed=request.form['feed']

        q="insert into `feedback` values(null,'%s','%s','pending',curdate())"%(lid,feed)
        insert(q)
        return redirect(url_for("recipient.addfeedback")) 

    data={}
    q="select * from feedback inner join login on login.login_id=feedback.sender_id where usertype='recipient'"
    ews=select(q)
    data['ews']=ews

    return render_template("recipient/addfeedback.html",data=data)