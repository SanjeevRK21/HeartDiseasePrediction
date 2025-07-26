from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired

class HeartDiseaseForm(FlaskForm):
    age = IntegerField("Age", validators=[DataRequired()])
    sex = SelectField("Sex", choices=[("1", "Male"), ("2", "Female")], validators=[DataRequired()])
    chestpaintype = SelectField("Chest Pain Type", choices=[("1", "ATA"), ("2", "NAP"), ("3", "ASY"), ("4", "TA")], validators=[DataRequired()])
    restingbp = IntegerField("Resting Blood Pressure", validators=[DataRequired()])
    cholesterol = IntegerField("Cholesterol", validators=[DataRequired()])
    fastingbs = SelectField("Fasting Blood Sugar", choices=[("0", "No"), ("1", "Yes")], validators=[DataRequired()])
    restingecg = SelectField("Resting ECG", choices=[("1", "Normal"), ("2", "ST"), ("3", "LVH")], validators=[DataRequired()])
    maxhr = IntegerField("Maximum Heart Rate", validators=[DataRequired()])
    exerciseangina = SelectField("Exercise Induced Angina", choices=[("0", "No"), ("1", "Yes")], validators=[DataRequired()])
    oldpeak = IntegerField("Oldpeak", validators=[DataRequired()])
    st_slope = SelectField("ST Slope", choices=[("0", "Down"), ("1", "Flat"), ("2", "Up")], validators=[DataRequired()])
    submit = SubmitField("Predict")
