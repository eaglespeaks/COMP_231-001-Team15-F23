from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_industry_state_job_job_type_job_industry_job_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='location',
            new_name='city',
        ),
    ]
