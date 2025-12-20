register_module_line('AlgoSec Rest', 'start', __line__())

import json 
from typing import Any, LiteralString


class Client(BaseClient):

    ALGOSEC_TIMEOUT = 180
    ALGOSEC_QUERY_TIMEOUT = 600

    def __init__(self, base_url:str, use_ssl: bool, use_proxy:bool, sid: Optional[str] = None, **kwargs):
        super().__init__(base_url, verify=use_ssl, proxy=use_proxy, timeout=self.ALGOSEC_TIMEOUT, **kwargs)
        self.sid = sid if sid and sid != "None" else None
        self.is_logged_in = self.sid is not None 

    def __param_to_list__(self, param):
        return param if type(param) == list else [param]
    
    @property
    def headers(self):
        if self.sid is None:  # for loggin in, before self.sid is set 
            return {'Accept': 'application/json'}
        return {'Content-type': 'application/json', 'Accept': 'application/json', 'Cookie': 'PHPSESSID={}'.format(self.sid)}
    

    def login(self, username: str, password: str):
        payload = {'username': username, 'password':password}
        response = self._http_request(method='POST', url_suffix='/fa/server/connection/login', data=payload)
        sid = response.get('SessionID', '')
        if sid : 
            self.sid = sid 
            self.is_logged_in = True
        else:
            demisto.debug("Login: failed")

        return response            


    def logout(self) -> str:
        payload = {'session': self.sid}
        response = self._http_request(method='POST', url_suffix='/fa/server/connection/logout', data=payload)
        
        logout_status = response.get('status', False)
        message = response.get('message', '')
        
        if logout_status: 
            self.sid = None
            self.is_logged_in = False
            message = 'LogOut OK'

        return message  
    
    def test_connection(self, username:str, password:str) -> str:
        response = self.login(username, password)
        
        if response.get('status') and self.sid: 
            logout_result = self.logout()
            if logout_result == 'LogOut OK':
                return 'ok'
            else:
                return 'Wrong logout'
                
        else:
            return 'Error: {}'.format(response.get('message'))
        
    def query(self, source, destination, service, user, application, queryTarget='ALL_FIREWALLS'):
        body = {
            'queryInput':[
                {
                    'source': self.__param_to_list__(source), 
                    'destination': self.__param_to_list__(destination),
                    'service': self.__param_to_list__(service),
                    'user': self.__param_to_list__(user),
                    'application': self.__param_to_list__(application)
                }
            ],
            'queryTarget': queryTarget,
            'includeRulesZones': True
        }
        
        payload = json.dumps(body)
        return self._http_request(method='POST', url_suffix='/afa/api/v1/query', headers=self.headers, data=payload, timeout=self.ALGOSEC_QUERY_TIMEOUT)
    
    def device_details(self, name):
        return self._http_request(method='GET', url_suffix='/afa/api/v1/device/{}'.format(name), headers=self.headers)
    
    def device_details_zones(self, name):
        params = {"device": name}
        return self._http_request(method='GET', url_suffix='/afa/api/v1/deviceZones', params=params, headers=self.headers)
    