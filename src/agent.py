# -*- coding: utf-8 -*-
#
# This file is part of Zoe Assistant
# Licensed under MIT license - see LICENSE file
#

from zoe import *
import random

@Agent('Insult')
class InsultAgent:

    def __init__(self):
        
        #load insults
        self.loadInsults(('en', 'es'))

    def loadInsults(self, locales):
        self.insults = {}
        for locale in locales:
            path = 'res/insults_{}.txt'.format(locale)
            file = open(path, 'r')
            self.insults[locale] = file.readlines()

            print('Loaded ' + path + ' insult file.')

    @Intent('insult.get')
    def receive(self, intent):
        user = intent['username']
        locale = intent['locale']
        insult = random.choice(self.insults[locale])

        return {
            'data': 'insult',
            'from': 'insultagent',
            'text': insult
        }
