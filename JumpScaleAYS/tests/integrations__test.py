import unittest
from JumpScale import j

descr = """
AtYourService Tests
"""

organization = "jumpscale"
author = "christophe dCPM"
license = "bsd"
version = "1.0"
category = "app.ays.integration"
enable = True
priority = 1
send2osis = False


class AYSTestBase(unittest.TestCase):
    """Base class for AYS Test"""

    @classmethod
    def setUpClass(self):
        """
        creates a directory where we can run the test in isolation
        """
        self.tmp_dir = j.sal.fs.getTmpDirPath()
        self.services_dir = j.sal.fs.joinPaths(self.tmp_dir, 'services')
        self.templates_dir = j.sal.fs.joinPaths(self.tmp_dir, 'actorTemplates')
        self.domain = j.sal.fs.getBaseName(self.tmp_dir)
        # create ays directories
        j.sal.fs.createDir(self.tmp_dir)
        j.sal.fs.createDir(self.services_dir)
        j.sal.fs.createDir(self.templates_dir)

        # copy templates fixtures in place
        parent = j.sal.fs.getParent(__file__)
        src = j.sal.fs.joinPaths(parent, 'fixtures')
        j.sal.fs.copyDirTree(src, self.templates_dir)
        j.sal.fs.changeDir(self.tmp_dir)

    @classmethod
    def tearDownClass(self):
        if j.sal.fs.exists(path=self.tmp_dir):
            j.sal.fs.removeDirTree(self.tmp_dir)
            # need to move in an existing folder otherwise unittest gives
            # errors
            j.sal.fs.changeDir("/opt")

        # reset ays status
        j.atyourservice.services = []
        j.atyourservice.templates = []
        j.atyourservice._init = False
        j.atyourservice._domains = []


class AYSInit(AYSTestBase):

    def setUp(self):
        """
        executed before each test method.
        """
        j.sal.fs.changeDir(self.tmp_dir)

    def tearDown(self):
        """
        executed after each test method.
        """

    def test_init(self):
        """
        """
    pass
