from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client

auth = v3.Password(auth_url='https://ctrl-node.mycloud.example.org:35357/v3',
                   username='myservice',
                   password='myservicesecretpassword',
                   project_name='services',
                   user_domain_id='default',
                   project_domain_id='default')
sess = session.Session(auth=auth)
keystone = client.Client(session=sess)

class Validator:
    def __init__(self, token):
        self.validate = keystone.tokens.validate(token)
        
    def is_admin(self):
        for role in self.validate['roles']:
            if role['name'] == 'admin':
                return True
        return False

    def is_member(self):
        for role in self.validate['roles']:
            if role['name'] == '_member_':
                return True
        return False

    def get_project(self):
        return self.validate['project']
