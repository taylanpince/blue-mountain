# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Contest'
        db.create_table('contests_contest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('contests', ['Contest'])

        # Adding model 'ContestEntry'
        db.create_table('contests_contestentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contest', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entries', to=orm['contests.Contest'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('entry_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('newsletter', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('contests', ['ContestEntry'])

        # Adding unique constraint on 'ContestEntry', fields ['contest', 'email']
        db.create_unique('contests_contestentry', ['contest_id', 'email'])

        # Adding model 'ContestWinner'
        db.create_table('contests_contestwinner', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('contest', self.gf('django.db.models.fields.related.ForeignKey')(related_name='winners', to=orm['contests.Contest'])),
        ))
        db.send_create_signal('contests', ['ContestWinner'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'ContestEntry', fields ['contest', 'email']
        db.delete_unique('contests_contestentry', ['contest_id', 'email'])

        # Deleting model 'Contest'
        db.delete_table('contests_contest')

        # Deleting model 'ContestEntry'
        db.delete_table('contests_contestentry')

        # Deleting model 'ContestWinner'
        db.delete_table('contests_contestwinner')


    models = {
        'contests.contest': {
            'Meta': {'object_name': 'Contest'},
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'contests.contestentry': {
            'Meta': {'unique_together': "(('contest', 'email'),)", 'object_name': 'ContestEntry'},
            'contest': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': "orm['contests.Contest']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'newsletter': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'contests.contestwinner': {
            'Meta': {'object_name': 'ContestWinner'},
            'contest': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'winners'", 'to': "orm['contests.Contest']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['contests']
