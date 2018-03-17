#!/usr/bin/env python

"""
Unit test for classes in fpy program
"""

from f5.bigip import ManagementRoot
import fpy
import pytest

# Connect to the test unit. Credential will be sanitized after test.
mgmt = ManagementRoot("1.1.1.1", "admin", "password")

def test_LTM_init():
    """ LTM object initialization test """
    l = fpy.LTM(mgmt)
    assert l.mgmt.tmos_version == '12.1.1'

def test_get_pool_state():
    """ Test get_pool_state function """
    p = fpy.Pool(mgmt)
    assert p.get_pool_state('sipp') == 'unknown'
    assert p.get_pool_state('p1p1', 'p1') == 'offline'

def test_get_pool(capfd):
    """ Test get_pool function """
    p = fpy.Pool(mgmt)
    p.get_pool()
    out, err = capfd.readouterr()
    assert 'Pool Status' in out

def test_get_virtual_state():
    """ Test get_virtual_state function """
    v = fpy.Virtual(mgmt)
    assert v.get_virtual_state('main_test') == 'unknown'

def test_get_virtual(capfd):
    """ Test get_virtual function """
    v = fpy.Virtual(mgmt)
    v.get_virtual()
    out, err = capfd.readouterr()
    assert 'Virtual Status' in out

def test_apply_rule(capfd):
    """ Test apply rule function """
    v = fpy.Virtual(mgmt)
    v.apply_rule('test_rule')
    out, err = capfd.readouterr()
    assert 'HTTP profile required' in out

def test_remove_rule(capfd):
    """ Test remove rule function """
    v = fpy.Virtual(mgmt)
    v.remove_rule('test_rule')
    out, err = capfd.readouterr()
    assert 'removed' in out

def test_get_rule(capfd):
    """ Test get rule function """
    r = fpy.Rule(mgmt)
    r.get_rule()
    out, err = capfd.readouterr()
    assert 'iRule List' in out

def test_create_rule():
    """ Test create rule function """
    r = fpy.Rule(mgmt)
    r.create_rule('test_rule_2')
    assert mgmt.tm.ltm.rules.rule.exists(name='test_rule_2', partition='Common')

def test_creat_rule2(capfd):
    """ Test create rule output function """
    r = fpy.Rule(mgmt)
    r.create_rule('test_rule_3')
    out, err = capfd.readouterr()
    assert 'created' in out

def test_check_rule():
    """ Test check rule function """
    r = fpy.Rule(mgmt)
    assert r.check_rule('test_rule')
