# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

# With the default User model these will be 'auth.User' and 'auth.user'
# so instead of using orm['auth.User'] we can use orm[user_orm_label]
from waffle.compat import get_user_model
User = get_user_model()
user_orm_label = '%s.%s' % (User._meta.app_label, User._meta.object_name)

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Flag.note'
        db.add_column('waffle_flag', 'note', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'Switch.note'
        db.add_column('waffle_switch', 'note', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'Sample.note'
        db.add_column('waffle_sample', 'note', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Flag.note'
        db.delete_column('waffle_flag', 'note')

        # Deleting field 'Switch.note'
        db.delete_column('waffle_switch', 'note')

        # Deleting field 'Sample.note'
        db.delete_column('waffle_sample', 'note')


    models = {
        'waffle.flag': {
            'Meta': {'object_name': 'Flag'},
            'authenticated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'everyone': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'rollout': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'superusers': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['%s']" % user_orm_label, 'symmetrical': 'False', 'blank': 'True'})
        },
        'waffle.sample': {
            'Meta': {'object_name': 'Sample'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'percent': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '1'})
        },
        'waffle.switch': {
            'Meta': {'object_name': 'Switch'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['waffle']
