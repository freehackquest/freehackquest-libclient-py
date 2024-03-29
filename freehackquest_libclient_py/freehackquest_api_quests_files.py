#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 FreeHackQuest Team <freehackquest@gmail.com>
"""This file was automatically generated by fhq-server
Version: v0.2.51
Date: 2023-01-03 17:03:28
"""

class FreeHackQuestApiQuestsfiles:
    """ API Group quests_files"""
    __client = None
    def __init__(self, client):
        self.__client = client

    def delete(self, req):
        """Delete file from quest
            Permissins:
                Denied access for unauthorized users
                Denied access for users
                Denied access for admins
            Args:
                quest_uuid (string,required):
                    Quest UUID
                file_id (integer,required):
                    File ID
        """
        if not self.__client.has_connection():
            return None
        request_json = self.__client.generate_base_command('quests_files.delete')
        allowed_params = [
            'quest_uuid',
            'file_id',
        ]
        self.__client.check_on_excess_params(req, 'quests_files.delete', allowed_params)
        required_params = [
            'quest_uuid',
            'file_id',
        ]
        self.__client.check_on_required_params(req, 'quests_files.delete', required_params)
        for param_name in required_params:
            if param_name not in req:
                raise Exception('Parameter "' + param_name + '" expected (lib)')
        if 'quest_uuid' in req:
            request_json['quest_uuid'] = req['quest_uuid']
        if 'file_id' in req:
            request_json['file_id'] = req['file_id']
        return self.__client.send_command(request_json)

    def upload(self, req):
        """Update the quest
            Permissins:
                Denied access for unauthorized users
                Denied access for users
                Denied access for admins
            Args:
                quest_uuid (string,required):
                    Quest UUID
                file_base64 (string,required):
                    Byte-array encoded in base64
                file_name (string,required):
                    File name
        """
        if not self.__client.has_connection():
            return None
        request_json = self.__client.generate_base_command('quests_files.upload')
        allowed_params = [
            'quest_uuid',
            'file_base64',
            'file_name',
        ]
        self.__client.check_on_excess_params(req, 'quests_files.upload', allowed_params)
        required_params = [
            'quest_uuid',
            'file_base64',
            'file_name',
        ]
        self.__client.check_on_required_params(req, 'quests_files.upload', required_params)
        for param_name in required_params:
            if param_name not in req:
                raise Exception('Parameter "' + param_name + '" expected (lib)')
        if 'quest_uuid' in req:
            request_json['quest_uuid'] = req['quest_uuid']
        if 'file_base64' in req:
            request_json['file_base64'] = req['file_base64']
        if 'file_name' in req:
            request_json['file_name'] = req['file_name']
        return self.__client.send_command(request_json)

