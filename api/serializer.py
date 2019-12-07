from rest_framework import serializers
from .models import Marriage,Baptism,  Annoucement, Reading

class MarriageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marriage
        fields = [
            'url',
            'id',
            'no',
            'name_of_groom',
            'name_of_bride',
            'groom_Town',
            'bride_Town',
            'groom_parent',
            'bride_parent',
            'assisting_priest',
            'groom_witnesses',
            'bride_witnesses',
            'date_of_marriage',
            'remark'
        ]


class BaptismSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Baptism
        fields = [
            'url',
            'id',
            'name',
            'date_of_baptism',
            'place_of_baptism',
            'baptismal_name',
            'other_names',
            'surname',
            'date_of_birth',
            'place_of_birth',
            'hometown',
            'name_of_parents',
            'solenm_or_private',
            'name_of_God_parents',
            'name_of_minister'
        ]

class ReadingsSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Reading
       fields = [

           'url',
           'id',
           'date',
           'title',
           'entrace_antiphon',
           'opening_prayers',
           'first_reading_title',
           'first_reading_subtitle',
           'first_reading_body',
           'responsorial_psalm_title',
           'responsorial_psalm_subtitle',
           'responsorial_psalm_body',
           'second_reading_title',
           'second_reading_subtitle',
           'second_reading_body',
           'gospel_acclamation_title',
           'gospel_acclamation_body',
           'gospel_title',
           'gospel_subtitle',
           'gospel',
           'prayer_over_the_offerings',
           'communion_antiphon',
           'prayer_after_communion'
       ]

class AnnouncementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Annoucement
        fields = [
            'url',
            'id',
            'date',
            'body'
        ]
