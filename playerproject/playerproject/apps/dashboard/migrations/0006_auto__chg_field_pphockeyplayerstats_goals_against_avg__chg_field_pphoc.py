# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'PPHockeyPlayerStats.goals_against_avg'
        db.alter_column(u'dashboard_pphockeyplayerstats', 'goals_against_avg', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3))

        # Changing field 'PPHockeyPlayerStats.save_percentage'
        db.alter_column(u'dashboard_pphockeyplayerstats', 'save_percentage', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=4))

    def backwards(self, orm):

        # Changing field 'PPHockeyPlayerStats.goals_against_avg'
        db.alter_column(u'dashboard_pphockeyplayerstats', 'goals_against_avg', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'PPHockeyPlayerStats.save_percentage'
        db.alter_column(u'dashboard_pphockeyplayerstats', 'save_percentage', self.gf('django.db.models.fields.PositiveIntegerField')())

    models = {
        'accounts.ppuser': {
            'Meta': {'object_name': 'PPUser'},
            'contact_info': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['accounts.PPUserContactInfo']"}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_activity': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'accounts_ppuser_related'", 'null': 'True', 'to': "orm['accounts.PPUser']"}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'role': ('django.db.models.fields.CharField', [], {'default': "'standard'", 'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        },
        'accounts.ppusercontactinfo': {
            'Meta': {'object_name': 'PPUserContactInfo'},
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'accounts_ppusercontactinfo_related'", 'null': 'True', 'to': "orm['accounts.PPUser']"}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
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
        'dashboard.pphockeyplayerstats': {
            'Meta': {'object_name': 'PPHockeyPlayerStats'},
            'assists': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'games_played': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'games_started': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'goals': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'goals_against': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'goals_against_avg': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'height_feet': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'height_inches': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'dashboard_pphockeyplayerstats_related'", 'null': 'True', 'to': "orm['accounts.PPUser']"}),
            'losses': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'minutes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'penalty_minutes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'plus_minus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'points': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'position': ('django.db.models.fields.CharField', [], {'default': "'not_specified'", 'max_length': '30'}),
            'save_percentage': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '4'}),
            'saves': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'shoots': ('django.db.models.fields.CharField', [], {'default': "'shoots_unspecified'", 'max_length': '30'}),
            'shots_on_goal': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'shutouts': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ties': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'wins': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'dashboard.ppuserrecord': {
            'Meta': {'object_name': 'PPUserRecord'},
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'contact_info': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['accounts.PPUserContactInfo']"}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'dashboard_ppuserrecord_related'", 'null': 'True', 'to': "orm['accounts.PPUser']"}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'recorded_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['accounts.PPUser']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['dashboard']