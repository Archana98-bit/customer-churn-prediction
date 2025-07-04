from django import forms

class ChurnForm(forms.Form):
    gender = forms.ChoiceField(choices=[('Female', 'Female'), ('Male', 'Male')])
    SeniorCitizen = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')])
    Partner = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')])
    tenure = forms.IntegerField()
    MonthlyCharges = forms.FloatField()
    TotalCharges = forms.FloatField()
    InternetService = forms.ChoiceField(choices=[('DSL', 'DSL'), ('Fiber optic', 'Fiber optic'), ('No', 'No')])
    Contract = forms.ChoiceField(choices=[('Month-to-month', 'Month-to-month'), ('One year', 'One year'), ('Two year', 'Two year')])

    # ✅ Add human-readable labels
    def __init__(self, *args, **kwargs):
        super(ChurnForm, self).__init__(*args, **kwargs)
        self.fields['SeniorCitizen'].label = "Senior Citizen"
        self.fields['MonthlyCharges'].label = "Monthly Charges"
        self.fields['TotalCharges'].label = "Total Charges"
        self.fields['InternetService'].label = "Internet Service"
        self.fields['tenure'].label = "Tenure"
        self.fields['Partner'].label = "Partner"