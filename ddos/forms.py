from flask_wtf import FlaskForm,RecaptchaField
from wtforms import FileField,StringField,SubmitField,IntegerField,FloatField
from wtforms.validators import DataRequired

class SubmitForm(FlaskForm):
    fwd_seg_size_min = IntegerField("Enter Minimum Forward Segment Size ",validators=[DataRequired()])
    flow_iat_min = FloatField("Enter Flow-IAT-Min ",validators=[DataRequired()])
    src_port = IntegerField("Enter Source-Port ",validators=[DataRequired()])
    tot_fwd_pkts = IntegerField("Enter Total Forwarded Packets ",validators=[DataRequired()])
    init_bwd_win_bytes = IntegerField("Enter Initial-Bandwidth-Window ",validators=[DataRequired()])
    src_ip = StringField("Enter Source-IP ",validators=[DataRequired()])
    dst_ip = StringField("Enter Destination-IP ",validators=[DataRequired()])
    timestamp = StringField("Enter Timestamp ",default='16/02/2018 11:25:34 PM')
    recaptcha = RecaptchaField()
    submit = SubmitField("Predict")