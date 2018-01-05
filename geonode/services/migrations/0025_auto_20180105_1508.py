# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '24_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceprofilerole',
            name='role',
            field=models.CharField(help_text='function performed by the responsible party', max_length=255, choices=[(b'author', 'Person welche die Quelle verfasst hat'), (b'processor', 'Person, welche die Daten in einer Weise ver\xe4ndert hat, sodass auch die Quelle ge\xe4ndert wurde'), (b'publisher', 'Person welche die Quelle ver\xf6ffentlicht hat'), (b'custodian', 'Partei, die Rechenschaftspflicht und Verantwortung \xfcbernimmt f\xfcr die Daten und sorgt f\xfcr angemessene Pflege und Wartung der Ressource'), (b'pointOfContact', 'Person welche f\xfcr den Erwerb von Wissen \xfcber oder Erwerb der Quelle selbst kontaktiert werden kann'), (b'distributor', 'Person welche die Quelle verbreitet'), (b'user', 'Person welche die Quelle benutzt'), (b'resourceProvider', 'Person welche die Quelle liefert'), (b'originator', 'Person welche die Quelle erstellt hat'), (b'owner', 'Person welche die Quelle besitzt'), (b'principalInvestigator', 'Person oder Stelle, die verantwortlich f\xfcr die Erhebung der Daten und die Untersuchung ist')]),
        ),
    ]
