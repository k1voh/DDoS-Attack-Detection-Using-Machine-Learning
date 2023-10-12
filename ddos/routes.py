from flask import render_template,request,flash
from ddos import app
from ddos.forms import * 
from Model.Detect import detectDdos
import pandas as pd
import json

@app.route('/',methods=['GET','POST'])
def home():
    form=SubmitForm()
    
    if request.method=='POST':
        rendered_object = {}
        rendered_object['Fwd Seg Size Min']=[form.fwd_seg_size_min.data]
        rendered_object['Flow IAT Min']=[form.flow_iat_min.data]
        rendered_object['Src Port']=[form.src_port.data]
        rendered_object['Tot Fwd Pkts']=[form.tot_fwd_pkts.data]
        rendered_object['Init Bwd Win Byts']=[form.init_bwd_win_bytes.data]
        rendered_object['Src IP']=[form.src_ip.data]
        rendered_object['Dst IP']=[form.dst_ip.data]
        rendered_object['Timestamp']=[form.timestamp.data]
        form.fwd_seg_size_min.data,form.flow_iat_min.data="",""
        form.src_port.data,form.tot_fwd_pkts.data="",""
        form.init_bwd_win_bytes.data,form.src_ip.data="",""
        form.dst_ip.data,form.timestamp.data="",""
        result = detectDdos(json.dumps(rendered_object))
        value=result[0]
        if value=='Benign':
            flash("The system is safe for the given parameters!")
        else:
            flash("BEWARE! The system prone to DDoS attack for the given parameters!")
        print("Result:",value)
    return render_template('home.html',form=form)