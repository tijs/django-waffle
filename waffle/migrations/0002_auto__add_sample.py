# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):

        # Adding model 'Sample'
        db.create_table('waffle_sample', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('percent', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=1)),
        ))
        db.send_create_signal('waffle', ['Sample'])


    def backwards(self, orm):

        # Deleting model 'Sample'
        db.delete_table('waffle_sample')


    models = {
        'waffle.sample': {
            'Meta': {'object_name': 'Sample'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'percent': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '1'})
        }
    }

    complete_apps = ['waffle']
