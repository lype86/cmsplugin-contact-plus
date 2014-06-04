# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ContactPlus.title'
        db.add_column(u'cmsplugin_contact_plus_contactplus', 'title',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=50),
                      keep_default=False)

        # Adding field 'ContactPlus.reset'
        db.add_column(u'cmsplugin_contact_plus_contactplus', 'reset',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ContactPlus.title'
        db.delete_column(u'cmsplugin_contact_plus_contactplus', 'title')

        # Deleting field 'ContactPlus.reset'
        db.delete_column(u'cmsplugin_contact_plus_contactplus', 'reset')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'cmsplugin_contact_plus.contactplus': {
            'Meta': {'object_name': 'ContactPlus', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'recipient_email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '75'}),
            'reset': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'submit': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'cmsplugin_contact_plus/contact.html'", 'max_length': '255'}),
            'thanks': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'cmsplugin_contact_plus.extrafield': {
            'Meta': {'ordering': "('inline_ordering_position',)", 'object_name': 'ExtraField'},
            'fieldType': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'form': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cmsplugin_contact_plus.ContactPlus']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'inline_ordering_position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'widget': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['cmsplugin_contact_plus']