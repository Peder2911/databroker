
import os
import pkg_resources
import tempfile
import shutil

import unittest
from databroker.databroker import app

class TestBasics(unittest.TestCase):
    def setUp(self):
        self.td = tempfile.TemporaryDirectory()
        self.tf = os.path.join(self.td.name,"dat.parquet") 
        shutil.copyfile(
                pkg_resources.resource_filename(__name__,"fixtures/tdat.parquet"),
                self.tf
                )
            
        app.config["TESTING"] = True
        app.config["SOURCES"] = {"testloa":{"testsource":f"file://{self.tf}"}}
        self.app = app.test_client()
    def tearDown(self):
        self.td.cleanup()

    def test_request(self):
        rsp = self.app.post("/",json={
            "variable":"x",
            "loa": "testloa",
            "transform": None
            })
        self.assertTrue(rsp.json["message"] == "ok")
