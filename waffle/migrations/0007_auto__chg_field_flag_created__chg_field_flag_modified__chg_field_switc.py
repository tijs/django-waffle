# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

# With the default User model these will be 'auth.User' and 'auth.user'
# so instead of using orm['auth.User'] we can use orm[user_orm_label]
from waffle.compat import get_user_model
User = get_user_model()
user_orm_label = '%s.%s' % (User._meta.app_label, User._meta.object_name)
user_model_label = '%s.%s' % (User._meta.app_label, User._meta.module_name)

class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Flag.created'
        db.alter_column('waffle_flag', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Flag.modified'
        db.alter_column('waffle_flag', 'modified', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Switch.created'
        db.alter_column('waffle_switch', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Switch.modified'
        db.alter_column('waffle_switch', 'modified', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Sample.created'
        db.alter_column('waffle_sample', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Sample.modified'
        db.alter_column('waffle_sample', 'modified', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):

        # Changing field 'Flag.created'
        db.alter_column('waffle_flag', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'Flag.modified'
        db.alter_column('waffle_flag', 'modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'Switch.created'
        db.alter_column('waffle_switch', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'Switch.modified'
        db.alter_column('waffle_switch', 'modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'Sample.created'
        db.alter_column('waffle_sample', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'Sample.modified'
        db.alter_column('waffle_sample', 'modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

    models = {
        user_model_label: {
            'Meta': {
                'object_name': User.__name__,
                'db_table': "'%s'" % User._meta.db_table
            },
            User._meta.pk.attname: (
                'django.db.models.fields.AutoField', [],
                {'primary_key': 'True',
                'db_column': "'%s'" % User._meta.pk.column}
            ),
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'waffle.flag': {
            'Meta': {'object_name': 'Flag'},
            'authenticated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'everyone': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'rollout': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'superusers': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'testing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['%s']" % user_orm_label, 'symmetrical': 'False', 'blank': 'True'})
        },
        'waffle.sample': {
            'Meta': {'object_name': 'Sample'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'percent': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '1'})
        },
        'waffle.switch': {
            'Meta': {'object_name': 'Switch'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['waffle']