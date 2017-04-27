import unittest
from js9 import j


class AYSKey(unittest.TestCase):

    def setUp(self):
        self.test_table = [
            {
                'key': 'domain|name!instance@role',
                'expect': {
                    'domain': 'domain',
                    'name': 'name',
                    'instance': 'instance',
                    'role': 'role'
                }
            },
            {
                'key': 'domain|name',
                'expect': {
                    'domain': 'domain',
                    'name': 'name',
                    'instance': '',
                    'role': 'name'
                }
            },
            {
                'key': 'domain|role.name',
                'expect': {
                    'domain': 'domain',
                    'name': 'role.name',
                    'instance': '',
                    'role': 'role'
                }
            },
            {
                'key': 'role!instance',
                'expect': {
                    'domain': '',
                    'name': '',
                    'instance': 'instance',
                    'role': 'role'
                }
            },
            {
                'key': 'role.name',
                'expect': {
                    'domain': '',
                    'name': 'role.name',
                    'instance': '',
                    'role': 'role'
                }
            }
        ]

    def test_parse(self):
        for test in self.test_table:
            domain, name, instance, role = j.atyourservice._parseKey(test[
                                                                     'key'])
            self.assertEqual(domain, test['expect'][
                             'domain'], "domain should be %s, found %s" % (test['expect']['domain'], domain))
            self.assertEqual(name, test['expect']['name'], "name should be %s, found %s" % (
                test['expect']['name'], name))
            self.assertEqual(instance, test['expect'][
                             'instance'], "instance should be %s, found %s" % (test['expect']['instance'], instance))
            self.assertEqual(role, test['expect']['role'], "role should be %s, found %s" % (
                test['expect']['role'], role))

if __name__ == '__main__':
    unittest.main()
