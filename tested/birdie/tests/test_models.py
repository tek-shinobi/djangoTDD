import pytest

from mixer.backend.django import mixer

class TestPost:
    def test_model(self):
        '''no instance of Post exists yet. first pk is 1'''
        obj = mixer.blend('birdie.Post')
        assert obj.pk == 1, 'Should create a Post instance'