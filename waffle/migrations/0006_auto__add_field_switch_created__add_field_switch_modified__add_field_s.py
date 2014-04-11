# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

try:
    from django.utils.timezone import now
except ImportError:
    now = datetime.datetime.now

default_datetime = now()


class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Switch.created'
        db.add_column('waffle_switch', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=default_datetime, db_index=True, blank=True), keep_default=False)

        # Adding field 'Switch.modified'
        db.add_column('waffle_switch', 'modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=default_datetime, blank=True), keep_default=False)

        # Adding field 'Sample.created'
        db.add_column('waffle_sample', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=default_datetime, db_index=True, blank=True), keep_default=False)

        # Adding field 'Sample.modified'
        db.add_column('waffle_sample', 'modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=default_datetime, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Switch.created'
        db.delete_column('waffle_switch', 'created')

        # Deleting field 'Switch.modified'
        db.delete_column('waffle_switch', 'modified')

        # Deleting field 'Sample.created'
        db.delete_column('waffle_sample', 'created')

        # Deleting field 'Sample.modified'
        db.delete_column('waffle_sample', 'modified')


    models = {
        'waffle.sample': {
            'Meta': {'object_name': 'Sample'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'percent': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '1'})
        },
        'waffle.switch': {
            'Meta': {'object_name': 'Switch'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['waffle']
