# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'PPPlayerStats'
        db.delete_table(u'dashboard_ppplayerstats')

        # Deleting field 'PPHockeyPlayerStats.ppplayerstats_ptr'
        db.delete_column(u'dashboard_pphockeyplayerstats', u'ppplayerstats_ptr_id')

        # Adding field 'PPHockeyPlayerStats.id'
        db.add_column(u'dashboard_pphockeyplayerstats', u'id',
                      self.gf('django.db.models.fields.AutoField')(primary_key=True),
                      keep_default=False)

        # Adding field 'PPHockeyPlayerStats.disabled'
        db.add_column(u'dashboard_pphockeyplayerstats', 'disabled',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'PPHockeyPlayerStats.time_created'
        db.add_column(u'dashboard_pphockeyplayerstats', 'time_created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'PPHockeyPlayerStats.time_modified'
        db.add_column(u'dashboard_pphockeyplayerstats', 'time_modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'PPHockeyPlayerStats.last_modified_by'
        db.add_column(u'dashboard_pphockeyplayerstats', 'last_modified_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='dashboard_pphockeyplayerstats_related', null=True, to=orm['accounts.PPUser']),
                      keep_default=False)

        # Adding field 'PPHockeyPlayerStats.height_feet'
        db.add_column(u'dashboard_pphockeyplayerstats', 'height_feet',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'PPHockeyPlayerStats.height_inches'
        db.add_column(u'dashboard_pphockeyplayerstats', 'height_inches',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'PPHockeyPlayerStats.shoots'
        db.add_column(u'dashboard_pphockeyplayerstats', 'shoots',
                      self.gf('django.db.models.fields.CharField')(default='shoots_unspecified', max_length=30),
                      keep_default=False)

        # Adding field 'PPHockeyPlayerStats.games_played'
        db.add_column(u'dashboard_pphockeyplayerstats', 'games_played',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PPHockeyPlayerStats.penalty_minutes'
        db.add_column(u'dashboard_pphockeyplayerstats', 'penalty_minutes',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PPHockeyPlayerStats.wins'
        db.add_column(u'dashboard_pphockeyplayerstats', 'wins',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PPHockeyPlayerStats.losses'
        db.add_column(u'dashboard_pphockeyplayerstats', 'losses',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PPHockeyPlayerStats.ties'
        db.add_column(u'dashboard_pphockeyplayerstats', 'ties',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PPHockeyPlayerStats.plus_minus'
        db.add_column(u'dashboard_pphockeyplayerstats', 'plus_minus',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PPHockeyPlayerStats.save_percentage'
        db.add_column(u'dashboard_pphockeyplayerstats', 'save_percentage',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PPHockeyPlayerStats.saves'
        db.add_column(u'dashboard_pphockeyplayerstats', 'saves',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PPHockeyPlayerStats.goals_against'
        db.add_column(u'dashboard_pphockeyplayerstats', 'goals_against',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PPHockeyPlayerStats.goals_against_avg'
        db.add_column(u'dashboard_pphockeyplayerstats', 'goals_against_avg',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PPHockeyPlayerStats.shots_on_goal'
        db.add_column(u'dashboard_pphockeyplayerstats', 'shots_on_goal',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PPHockeyPlayerStats.shutouts'
        db.add_column(u'dashboard_pphockeyplayerstats', 'shutouts',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PPHockeyPlayerStats.minutes'
        db.add_column(u'dashboard_pphockeyplayerstats', 'minutes',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'PPHockeyPlayerStats.games_started'
        db.add_column(u'dashboard_pphockeyplayerstats', 'games_started',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'PPPlayerStats'
        db.create_table(u'dashboard_ppplayerstats', (
            ('disabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('height_inches', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_modified_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='dashboard_ppplayerstats_related', null=True, to=orm['accounts.PPUser'], blank=True)),
            ('height_feet', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('dashboard', ['PPPlayerStats'])


        # User chose to not deal with backwards NULL issues for 'PPHockeyPlayerStats.ppplayerstats_ptr'
        raise RuntimeError("Cannot reverse this migration. 'PPHockeyPlayerStats.ppplayerstats_ptr' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'PPHockeyPlayerStats.ppplayerstats_ptr'
        db.add_column(u'dashboard_pphockeyplayerstats', u'ppplayerstats_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dashboard.PPPlayerStats'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'PPHockeyPlayerStats.id'
        db.delete_column(u'dashboard_pphockeyplayerstats', u'id')

        # Deleting field 'PPHockeyPlayerStats.disabled'
        db.delete_column(u'dashboard_pphockeyplayerstats', 'disabled')

        # Deleting field 'PPHockeyPlayerStats.time_created'
        db.delete_column(u'dashboard_pphockeyplayerstats', 'time_created')

        # Deleting field 'PPHockeyPlayerStats.time_modified'
        db.delete_column(u'dashboard_pphockeyplayerstats', 'time_modified')

        # Deleting field 'PPHockeyPlayerStats.last_modified_by'
        db.delete_column(u'dashboard_pphockeyplayerstats', 'last_modified_by_id')

        # Deleting field 'PPHockeyPlayerStats.height_feet'
        db.delete_column(u'dashboard_pphockeyplayerstats', 'height_feet')

        # Deleting field 'PPHockeyPlayerStats.height_inches'
        db.delete_column(u'dashboard_pphockeyplayerstats', 'height_inches')

        # Deleting field 'PPHockeyPlayerStats.shoots'
        db.delete_column(u'dashboard_pphockeyplayerstats', 'shoots')

        # Deleting field 'PPHockeyPlayerStats.games_played'
        db.delete_column(u'dashboard_pphockeyplayerstats', 'games_played')

        # Deleting field 'PPHockeyPlayerStats.penalty_minutes'
        db.delete_column(u'dashboard_pphockeyplayerstats', 'penalty_minutes')

        # Deleting field 'PPHockeyPlayerStats.wins'
        db.delete_column(u'dashboard_pphockeyplayerstats', 'wins')

        # Deleting field 'PPHockeyPlayerStats.losses'
        db.delete_column(u'dashboard_pphockeyplayerstats', 'losses')

        # Deleting field 'PPHockeyPlayerStats.ties'
        db.delete_column(u'dashboard_pphockeyplayerstats', 'ties')

        # Deleting field 'PPHockeyPlayerStats.plus_minus'
        db.delete_column(u'dashboard_pphockeyplayerstats', 'plus_minus')

        # Deleting field 'PPHockeyPlayerStats.save_percentage'
        db.delete_column(u'dashboard_pphockeyplayerstats', 'save_percentage')

        # Deleting field 'PPHockeyPlayerStats.saves'
        db.delete_column(u'dashboard_pphockeyplayerstats', 'saves')

        # Deleting field 'PPHockeyPlayerStats.goals_against'
        db.delete_column(u'dashboard_pphockeyplayerstats', 'goals_against')

        # Deleting field 'PPHockeyPlayerStats.goals_against_avg'
        db.delete_column(u'dashboard_pphockeyplayerstats', 'goals_against_avg')

        # Deleting field 'PPHockeyPlayerStats.shots_on_goal'
        db.delete_column(u'dashboard_pphockeyplayerstats', 'shots_on_goal')

        # Deleting field 'PPHockeyPlayerStats.shutouts'
        db.delete_column(u'dashboard_pphockeyplayerstats', 'shutouts')

        # Deleting field 'PPHockeyPlayerStats.minutes'
        db.delete_column(u'dashboard_pphockeyplayerstats', 'minutes')

        # Deleting field 'PPHockeyPlayerStats.games_started'
        db.delete_column(u'dashboard_pphockeyplayerstats', 'games_started')


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
            'goals_against_avg': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
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
            'save_percentage': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
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