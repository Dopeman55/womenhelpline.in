# Generated by Django 3.2.8 on 2021-11-05 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_helplines_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='verify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isvalid', models.BooleanField(default=True)),
                ('OrganizationName', models.CharField(default='TBD', max_length=100)),
                ('OrganizationAddress', models.TextField(default='TBD', null=True)),
                ('PhoneNumber', models.TextField(default='TBD')),
                ('City', models.CharField(default='TBD', max_length=100)),
                ('State', models.CharField(default='TBD', max_length=100)),
                ('Issues', models.CharField(default='TBD', max_length=500)),
                ('OrganizationDescription', models.TextField(default='TBD', null=True)),
                ('OrganizationType', models.CharField(default='TBD', max_length=30)),
                ('Charges', models.CharField(default='TBD', max_length=200)),
                ('Email', models.EmailField(default='TBD', max_length=254)),
                ('Website', models.URLField(default='TBD')),
                ('OperationalHours', models.CharField(default='TBD', max_length=200)),
                ('Status', models.CharField(default='Not Verified', max_length=20)),
            ],
        ),
    ]
