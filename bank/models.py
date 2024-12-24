from django.db import models


# Create your models here.

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    job_place = models.CharField(max_length=100)
    salary = models.IntegerField()
    banks = models.JSONField(default={})
    credit_accounts = models.JSONField(default={})
    payment_accounts = models.JSONField(default={})
    score = models.IntegerField(default=0)





class Bank(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    office_count = models.IntegerField(default=0, )
    atm_count = models.IntegerField(default=0, )
    employee_count = models.IntegerField(default=0, )
    client_count = models.IntegerField(default=0, )
    score = models.IntegerField(default=0, )
    balance = models.IntegerField(default=0, )
    interest = models.IntegerField(default=0, )


class BankAtm(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    service_employee = models.CharField(max_length=50)
    is_withdrawal = models.BooleanField(default=False)
    is_deposit = models.BooleanField(default=False)
    balance = models.IntegerField(default=0, )
    maintenance_cost = models.IntegerField(default=0, )


class BankOffice(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    state = models.BooleanField(max_length=50)
    is_atm_able = models.BooleanField(default=False)
    atm_count = models.IntegerField(default=0, )
    is_loan_able = models.BooleanField(default=False)
    is_withdrawal = models.BooleanField(default=False)
    is_deposit = models.BooleanField(default=False)
    balance = models.IntegerField(default=0, )
    maintenance_cost = models.IntegerField(default=0, )


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    position = models.CharField(max_length=50)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    is_remote = models.BooleanField(default=False)
    bank_office = models.ForeignKey(BankOffice, on_delete=models.CASCADE)
    is_loan_able = models.BooleanField(default=False)
    salary = models.IntegerField(default=0, )


class CreditAccount(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=50)
    begin_date = models.DateField()
    end_date = models.DateField()
    months_count = models.IntegerField(default=0, )
    credit_amount = models.IntegerField(default=0, )
    monthly_payment = models.IntegerField(default=0, )
    interest = models.IntegerField(default=0, )
    parent_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    payment_account = models.CharField()


class PaymentAccount(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bank_name = models.ForeignKey(Bank, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0, )