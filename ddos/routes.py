from flask import render_template,request,flash,jsonify
from ddos import app
from ddos.forms import * 
from Model.Detect import detectDdos
import json

@app.route('/',methods=['GEt','POST'])
def home():
    form=SubmitForm()
    if request.method=='POST':
        rendered_object = {}
        rendered_object['Fwd Seg Size Min']=form.fwd_seg_size_min.data
        rendered_object['Flow IAT Min']=form.flow_iat_min.data
        rendered_object['Src Port']=form.src_port.data
        rendered_object['Tot Fwd Pkts']=form.tot_fwd_pkts.data
        rendered_object['Init Bwd Win Byts']=form.init_bwd_win_bytes.data
        rendered_object['Src IP']=form.src_ip.data
        rendered_object['Dst IP']=form.dst_ip.data
        rendered_object['Timestamp']=form.timestamp.data
        print(rendered_object)
        # form.fwd_seg_size_min.data=""
        # form.flow_iat_min.data=""
        # form.src_port.data=""
        # form.tot_fwd_pkts.data=""
        # form.init_bwd_win_bytes.data=""
        # form.src_ip.data=""
        # form.dst_ip.data=""
        # form.timestamp.data=""
        flash('Answer returned!')
        # print(detectDdos(jsonify(rendered_object)))
        return jsonify(rendered_object)
    return render_template('home.html',form=form)