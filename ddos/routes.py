from flask import render_template,request,flash,jsonify
from ddos import app
from ddos.forms import * 
from Model.Detect import detectDdos
import pandas as pd
import json

@app.route('/',methods=['GEt','POST'])
def home():
    form=SubmitForm()
    value=0
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
        inputSet = pd.DataFrame(rendered_object)
        form.fwd_seg_size_min.data,form.flow_iat_min.data="",""
        form.src_port.data,form.tot_fwd_pkts.data="",""
        form.init_bwd_win_bytes.data,form.src_ip.data="",""
        form.dst_ip.data,form.timestamp.data="",""
        flash('Answer returned!')
        ro = json.dumps(rendered_object)
        result = detectDdos(json.dumps(rendered_object))
        print("Result:",result[0])
        return jsonify(rendered_object)
    return render_template('home.html',form=form,value=value)