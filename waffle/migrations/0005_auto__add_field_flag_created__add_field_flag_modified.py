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

# With the default User model these will be 'auth.User' and 'auth.user'
# so instead of using orm['auth.User'] we can use orm[user_orm_label]
from waffle.compat import get_user_model
User = get_user_model()
user_orm_label = '%s.%s' % (User._meta.app_label, User._meta.object_name)

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Flag.created'
        db.add_column('waffle_flag', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=default_datetime, db_index=True, blank=True), keep_default=False)

        # Adding field 'Flag.modified'
        db.add_column('waffle_flag', 'modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=default_datetime, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Flag.created'
        db.delete_column('waffle_flag', 'created')

        # Deleting field 'Flag.modified'
        db.delete_column('waffle_flag', 'modified')


    models = {
        'waffle.flag': {
            'Meta': {'object_name': 'Flag'},
            'authenticated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'everyone': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'rollout': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'superusers': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'testing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['%s']" % user_orm_label, 'symmetrical': 'False', 'blank': 'True'})
        },
    }

    complete_apps = ['waffle']
