# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'ContestEntry.birth_date'
        db.add_column('contests_contestentry', 'birth_date', self.gf('django.db.models.fields.DateField')(default=datetime.date(1983, 10, 13)), keep_default=False)

        # Adding field 'ContestEntry.phone_number'
        db.add_column('contests_contestentry', 'phone_number', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(default=-5555, max_length=20), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'ContestEntry.birth_date'
        db.delete_column('contests_contestentry', 'birth_date')

        # Deleting field 'ContestEntry.phone_number'
        db.delete_column('contests_contestentry', 'phone_number')


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
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'contest': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': "orm['contests.Contest']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'newsletter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'phone_number': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20'})
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
