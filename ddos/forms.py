from flask_wtf import FlaskForm,RecaptchaField
from wtforms import FileField,StringField,SubmitField,IntegerField
from wtforms.validators import DataRequired

class SubmitForm(FlaskForm):
    fwd_seg_size_min = IntegerField("Enter Fwd-Seg-Size-Min ",validators=[DataRequired()])
    flow_iat_min = IntegerField("Enter Flow-IAT-Min ",validators=[DataRequired()])
    src_port = IntegerField("Enter Src-Port ",validators=[DataRequired()])
    tot_fwd_pkts = IntegerField("Enter Tot-Fwd-Pkts ",validators=[DataRequired()])
    init_bwd_win_bytes = IntegerField("Enter Init-Bwd-Win-Byts ",validators=[DataRequired()])
    new_src_ip = StringField("Enter Source-IP ",validators=[DataRequired()])
    new_dst_ip = StringField("Enter Destination-IP ",validators=[DataRequired()])
    new_timestamp = StringField("Enter Timestamp ",validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField("Send Mail")