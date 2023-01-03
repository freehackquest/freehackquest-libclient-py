#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 FreeHackQuest Team <freehackquest@gmail.com>
"""This file was automatically generated by fhq-server
Version: v0.2.51
Date: 2023-01-03 17:03:28
"""

class FreeHackQuestApiLeaks:
    """ API Group leaks"""
    __client = None
    def __init__(self, client):
        self.__client = client

    def add(self, req):
        """Method adds a leak
            Permissins:
                Denied access for unauthorized users
                Denied access for users
                Denied access for admins
            Args:
                uuid (string,required):
                    UUID of the leak
                game_uuid (string,required):
                    UUID of the game
                name (string,required):
                    Visible part of the content
                content (string,required):
                    Content of the leak
                score (integer,required):
                    Price of the leak
        """
        if not self.__client.has_connection():
            return None
        request_json = self.__client.generate_base_command('leaks.add')
        allowed_params = [
            'uuid',
            'game_uuid',
            'name',
            'content',
            'score',
        ]
        self.__client.check_on_excess_params(req, 'leaks.add', allowed_params)
        required_params = [
            'uuid',
            'game_uuid',
            'name',
            'content',
            'score',
        ]
        self.__client.check_on_required_params(req, 'leaks.add', required_params)
        for param_name in required_params:
            if param_name not in req:
                raise Exception('Parameter "' + param_name + '" expected (lib)')
        if 'uuid' in req:
            request_json['uuid'] = req['uuid']
        if 'game_uuid' in req:
            request_json['game_uuid'] = req['game_uuid']
        if 'name' in req:
            request_json['name'] = req['name']
        if 'content' in req:
            request_json['content'] = req['content']
        if 'score' in req:
            request_json['score'] = req['score']
        return self.__client.send_command(request_json)

    def buy(self, req):
        """Method buys a leak
            Permissins:
                Denied access for unauthorized users
                Allowed access for users
                Allowed access for admins
            Args:
                id (integer,required):
                    Leak id
        """
        if not self.__client.has_connection():
            return None
        request_json = self.__client.generate_base_command('leaks.buy')
        allowed_params = [
            'id',
        ]
        self.__client.check_on_excess_params(req, 'leaks.buy', allowed_params)
        required_params = [
            'id',
        ]
        self.__client.check_on_required_params(req, 'leaks.buy', required_params)
        for param_name in required_params:
            if param_name not in req:
                raise Exception('Parameter "' + param_name + '" expected (lib)')
        if 'id' in req:
            request_json['id'] = req['id']
        return self.__client.send_command(request_json)

    def delete(self, req):
        """Method deletes a leak
            Permissins:
                Denied access for unauthorized users
                Denied access for users
                Denied access for admins
            Args:
                id (integer,required):
                    Leak id
        """
        if not self.__client.has_connection():
            return None
        request_json = self.__client.generate_base_command('leaks.delete')
        allowed_params = [
            'id',
        ]
        self.__client.check_on_excess_params(req, 'leaks.delete', allowed_params)
        required_params = [
            'id',
        ]
        self.__client.check_on_required_params(req, 'leaks.delete', required_params)
        for param_name in required_params:
            if param_name not in req:
                raise Exception('Parameter "' + param_name + '" expected (lib)')
        if 'id' in req:
            request_json['id'] = req['id']
        return self.__client.send_command(request_json)

    def list(self, req):
        """Method returns list of leaks
            Permissins:
                Allowed access for unauthorized users
                Allowed access for users
                Allowed access for admins
            Args:
                page (integer,required):
                    Number of page
                onpage (integer,required):
                    How much rows in one page
        """
        if not self.__client.has_connection():
            return None
        request_json = self.__client.generate_base_command('leaks.list')
        allowed_params = [
            'page',
            'onpage',
        ]
        self.__client.check_on_excess_params(req, 'leaks.list', allowed_params)
        required_params = [
            'page',
            'onpage',
        ]
        self.__client.check_on_required_params(req, 'leaks.list', required_params)
        for param_name in required_params:
            if param_name not in req:
                raise Exception('Parameter "' + param_name + '" expected (lib)')
        if 'page' in req:
            request_json['page'] = req['page']
        if 'onpage' in req:
            request_json['onpage'] = req['onpage']
        return self.__client.send_command(request_json)

    def update(self, req):
        """Method updates a leak
            Permissins:
                Denied access for unauthorized users
                Denied access for users
                Denied access for admins
            Args:
                id (integer,required):
                    Leak id
                name (string,optional):
                    Visible part of the content
                content (string,optional):
                    Content of the leak
                score (integer,optional):
                    Price of the leak
        """
        if not self.__client.has_connection():
            return None
        request_json = self.__client.generate_base_command('leaks.update')
        allowed_params = [
            'id',
            'name',
            'content',
            'score',
        ]
        self.__client.check_on_excess_params(req, 'leaks.update', allowed_params)
        required_params = [
            'id',
        ]
        self.__client.check_on_required_params(req, 'leaks.update', required_params)
        for param_name in required_params:
            if param_name not in req:
                raise Exception('Parameter "' + param_name + '" expected (lib)')
        if 'id' in req:
            request_json['id'] = req['id']
        if 'name' in req:
            request_json['name'] = req['name']
        if 'content' in req:
            request_json['content'] = req['content']
        if 'score' in req:
            request_json['score'] = req['score']
        return self.__client.send_command(request_json)

