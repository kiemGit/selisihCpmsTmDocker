from flask import Flask, render_template, request, redirect, session, url_for
from markupsafe import escape
from flask_mysqldb import MySQL
import yaml
from fpdf import FPDF, HTMLMixin
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.secret_key = 'hakimHafizBina212526'

db = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/selisih', methods = ['GET', 'POST'])
def kelasKendaraan():
    #if 'loginSession' in session:
    #    sessionLogin = session['loginSession']
        if request.method == 'POST':
            regVar = request.form
            timeout1 = regVar['tTimeout1']
            timeout2 = regVar['tTimeout2']
            timeout3 = regVar['tTimeout1']
            timeout4 = regVar['tTimeout2']
            cur = mysql.connection.cursor()
            sql = """SELECT 'dif id' as Stat,ID,RegNo,ClassID,Rate,rateTrstm(ID) FROM trs t
                     WHERE t.ID NOT IN (SELECT TrsID FROM trstm) AND
                     t.TimeOut >= %s AND 
                     t.TimeOut <= %s AND
                     IsCust = 0
                     UNION

                     select 'dif rate' as Stat,t2.ID,t2.RegNo,t2.ClassID,t2.Rate,rateTrstm(t2.ID) from trs t2
                     join trstm m on m.TrsID = t2.ID
                     where 
                     t2.TimeOut >= %s AND 
                     t2.TimeOut <= %s AND
                     t2.IsCust = 0 AND
                     t2.Rate != m.Amount"""
            sqlResult = cur.execute(sql, (timeout1,timeout2,timeout3,timeout4))
        if sqlResult > 0:
            aSelisih = cur.fetchall()
            return render_template('tblSelisih.html',aSelisih=aSelisih)
        else:
            return "data nill"
    #else:
    #    return redirect(url_for('fLogin'))

@app.route('/frm_selisih')
def frm_selisih():
     return render_template('frm_selisih.html')

@app.route('/editAkun/<akunId>')
def editAkun(akunId):
        cur = mysql.connection.cursor()
        qAkun = cur.execute("select * from trs where ID = "+akunId+"")
        if qAkun > 0:
            dataAkun = cur.fetchall()
            return render_template('fEditAkun.html',dataAkun=dataAkun)
        
@app.route('/trs/<trsId>')
def trs(trsId):
    #if 'loginSession' in session:
    #    sessionLogin = session['loginSession']
        cur = mysql.connection.cursor()
        resultValue = cur.execute("select * from trs where ID = "+trsId+"")
        if resultValue > 0:
            aTrs = cur.fetchall()
            return render_template('tblTrs.html',aTrs=aTrs)
        else:
            return "data nill"
    #else:
    #    return redirect(url_for('fLogin'))
        
