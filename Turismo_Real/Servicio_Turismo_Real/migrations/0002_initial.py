# Generated by Django 3.2.7 on 2021-12-05 23:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Servicio_Turismo_Real', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='f_use',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mantenimiento',
            name='f_dep',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Servicio_Turismo_Real.departamento'),
        ),
        migrations.AddField(
            model_name='imagendepartamento',
            name='f_dep',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Servicio_Turismo_Real.departamento'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='f_car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Servicio_Turismo_Real.cargo', verbose_name='Cargo'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='user_creation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='servicio_turismo_real_funcionario_creation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='user_updated',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='servicio_turismo_real_funcionario_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='detallecostodepartamento',
            name='pf_fun',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Servicio_Turismo_Real.funcionario'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='f_zona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Servicio_Turismo_Real.zona', verbose_name='Zona'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='user_creation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='servicio_turismo_real_departamento_creation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='departamento',
            name='user_updated',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='servicio_turismo_real_departamento_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='costodepartamento',
            name='dep',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Servicio_Turismo_Real.departamento'),
        ),
        migrations.AddField(
            model_name='costodepartamento',
            name='des_cos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Servicio_Turismo_Real.detallecostodepartamento'),
        ),
        migrations.AddField(
            model_name='checkout',
            name='f_fun',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Servicio_Turismo_Real.funcionario'),
        ),
        migrations.AddField(
            model_name='checkout',
            name='f_res',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Servicio_Turismo_Real.reserva'),
        ),
        migrations.AddField(
            model_name='checkin',
            name='f_fun',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Servicio_Turismo_Real.funcionario'),
        ),
        migrations.AddField(
            model_name='checkin',
            name='f_res',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Servicio_Turismo_Real.reserva'),
        ),
        migrations.AddField(
            model_name='articulodepartamento',
            name='f_cat_art',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Servicio_Turismo_Real.categoriaarticulo', verbose_name='Categoria'),
        ),
        migrations.AddField(
            model_name='articulodepartamento',
            name='user_creation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='servicio_turismo_real_articulodepartamento_creation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='articulodepartamento',
            name='user_updated',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='servicio_turismo_real_articulodepartamento_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inventariodepartamento',
            name='pf_art_dep',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Servicio_Turismo_Real.articulodepartamento'),
        ),
        migrations.AddField(
            model_name='detalleservicioadicional',
            name='pf_ser_adi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Servicio_Turismo_Real.servicioadicional'),
        ),
        migrations.AlterUniqueTogether(
            name='inventariodepartamento',
            unique_together={('pf_dep', 'pf_art_dep')},
        ),
        migrations.AlterUniqueTogether(
            name='detalleservicioadicional',
            unique_together={('pf_res', 'pf_ser_adi')},
        ),
    ]
