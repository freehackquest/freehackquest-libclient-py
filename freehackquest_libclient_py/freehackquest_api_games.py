#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 FreeHackQuest Team <freehackquest@gmail.com>
"""This file was automatically generated by fhq-server
Version: v0.2.47
Date: 2022-01-01 07:15:35
"""

class FreeHackQuestApiGames:
    """ API Group games"""
    __client = None
    def __init__(self, client):
        self.__client = client

    def info(self, req):
        """Return info about game by uuid
            Activated From Version: 0.2.39
            Permissins:
                Allowed access for unauthorized users
                Allowed access for users
                Allowed access for admins
            Args:
                uuid (string,required):
                    Global Identificator of the Game
        """
        if not self.__client.has_connection():
            return None
        request_json = self.__client.generate_base_command('games.info')
        allowed_params = [
            'uuid',
        ]
        self.__client.check_on_excess_params(req, 'games.info', allowed_params)
        required_params = [
            'uuid',
        ]
        self.__client.check_on_required_params(req, 'games.info', required_params)
        for param_name in required_params:
            if param_name not in req:
                raise Exception('Parameter "' + param_name + '" expected (lib)')
        if 'uuid' in req:
            request_json['uuid'] = req['uuid']
        return self.__client.send_command(request_json)

