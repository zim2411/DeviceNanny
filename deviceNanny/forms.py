from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, FileField, SelectField, TextAreaField
from wtforms.validators import DataRequired


class SingleUserForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Add')


class SingleDeviceForm(FlaskForm):
    device_name = StringField('Device Name', validators=[DataRequired()])
    serial_udid = StringField('Serial UDID', validators=[DataRequired()])
    manufacturer = StringField('Manufacturer', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    device_type = StringField('Device Type', validators=[DataRequired()])
    os_version = StringField('OS Version', validators=[DataRequired()])
    submit = SubmitField('Add')


class SettingsForm(FlaskForm):
    slack_channel = StringField('Slack Channel')
    slack_team_channel = StringField('Slack Team Channel')
    reminder_interval = StringField('Reminder Interval (hours)')
    checkout_expires = StringField('Checkout Expires (hours)')
    office_location = StringField('Office Location')
    update_submit = SubmitField('Update')


class UploadFileForm(FlaskForm):
    file = FileField('Choose csv file')
    upload_submit = SubmitField("Upload")
