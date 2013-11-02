# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DZTemplateSource'
        db.create_table(u'dashboard_dztemplatesource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('disabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('last_modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='dashboard_dztemplatesource_related', null=True, to=orm['accounts.DZUser'])),
            ('source_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('link', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal('dashboard', ['DZTemplateSource'])

        # Adding model 'DZTemplate'
        db.create_table(u'dashboard_dztemplate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('disabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('last_modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='dashboard_dztemplate_related', null=True, to=orm['accounts.DZUser'])),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['dashboard.DZTemplateSource'])),
        ))
        db.send_create_signal('dashboard', ['DZTemplate'])

        # Adding model 'DZSiteSettings'
        db.create_table(u'dashboard_dzsitesettings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('disabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('last_modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='dashboard_dzsitesettings_related', null=True, to=orm['accounts.DZUser'])),
        ))
        db.send_create_signal('dashboard', ['DZSiteSettings'])

        # Adding model 'DZSite'
        db.create_table(u'dashboard_dzsite', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('disabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('last_modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='dashboard_dzsite_related', null=True, to=orm['accounts.DZUser'])),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['accounts.DZUser'])),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('settings', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.DZSiteSettings'])),
        ))
        db.send_create_signal('dashboard', ['DZSite'])

        # Adding model 'DZSiteCommit'
        db.create_table(u'dashboard_dzsitecommit', (
            (u'dztemplate_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dashboard.DZTemplate'], unique=True, primary_key=True)),
            ('commited_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='commits', null=True, to=orm['accounts.DZUser'])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='commits', null=True, to=orm['dashboard.DZSite'])),
        ))
        db.send_create_signal('dashboard', ['DZSiteCommit'])

        # Adding model 'DZSiteOwnership'
        db.create_table(u'dashboard_dzsiteownership', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('disabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('last_modified_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='dashboard_dzsiteownership_related', null=True, to=orm['accounts.DZUser'])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='owners', null=True, to=orm['dashboard.DZSite'])),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='sites', null=True, to=orm['accounts.DZUser'])),
            ('ownership_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('dashboard', ['DZSiteOwnership'])

        # Adding unique constraint on 'DZSiteOwnership', fields ['site', 'owner']
        db.create_unique(u'dashboard_dzsiteownership', ['site_id', 'owner_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'DZSiteOwnership', fields ['site', 'owner']
        db.delete_unique(u'dashboard_dzsiteownership', ['site_id', 'owner_id'])

        # Deleting model 'DZTemplateSource'
        db.delete_table(u'dashboard_dztemplatesource')

        # Deleting model 'DZTemplate'
        db.delete_table(u'dashboard_dztemplate')

        # Deleting model 'DZSiteSettings'
        db.delete_table(u'dashboard_dzsitesettings')

        # Deleting model 'DZSite'
        db.delete_table(u'dashboard_dzsite')

        # Deleting model 'DZSiteCommit'
        db.delete_table(u'dashboard_dzsitecommit')

        # Deleting model 'DZSiteOwnership'
        db.delete_table(u'dashboard_dzsiteownership')


    models = {
        'accounts.dzuser': {
            'Meta': {'object_name': 'DZUser'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_activity': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'accounts_dzuser_related'", 'null': 'True', 'to': "orm['accounts.DZUser']"}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'dashboard.dzsite': {
            'Meta': {'object_name': 'DZSite'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['accounts.DZUser']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'dashboard_dzsite_related'", 'null': 'True', 'to': "orm['accounts.DZUser']"}),
            'settings': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dashboard.DZSiteSettings']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        'dashboard.dzsitecommit': {
            'Meta': {'object_name': 'DZSiteCommit', '_ormbases': ['dashboard.DZTemplate']},
            'commited_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'commits'", 'null': 'True', 'to': "orm['accounts.DZUser']"}),
            u'dztemplate_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dashboard.DZTemplate']", 'unique': 'True', 'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'commits'", 'null': 'True', 'to': "orm['dashboard.DZSite']"})
        },
        'dashboard.dzsiteownership': {
            'Meta': {'unique_together': "(('site', 'owner'),)", 'object_name': 'DZSiteOwnership'},
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'dashboard_dzsiteownership_related'", 'null': 'True', 'to': "orm['accounts.DZUser']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'sites'", 'null': 'True', 'to': "orm['accounts.DZUser']"}),
            'ownership_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owners'", 'null': 'True', 'to': "orm['dashboard.DZSite']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        'dashboard.dzsitesettings': {
            'Meta': {'object_name': 'DZSiteSettings'},
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'dashboard_dzsitesettings_related'", 'null': 'True', 'to': "orm['accounts.DZUser']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        'dashboard.dztemplate': {
            'Meta': {'object_name': 'DZTemplate'},
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'dashboard_dztemplate_related'", 'null': 'True', 'to': "orm['accounts.DZUser']"}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['dashboard.DZTemplateSource']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        'dashboard.dztemplatesource': {
            'Meta': {'object_name': 'DZTemplateSource'},
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'dashboard_dztemplatesource_related'", 'null': 'True', 'to': "orm['accounts.DZUser']"}),
            'link': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'source_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'model.modelattribute': {
            'Meta': {'unique_together': "(('name', 'content_type', 'object_id'),)", 'object_name': 'ModelAttribute'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'value': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'})
        }
    }

    complete_apps = ['dashboard']