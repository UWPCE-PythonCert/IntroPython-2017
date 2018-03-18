from node_db import Node, NodeStorage
import pytest




@pytest.fixture
def sample_data():

    ds = NodeStorage()
    n1 = Node(node_id='TRNSOY30', site_id='SYO', management_ip='1.2.3.4.5', console_id='CACSYO123',
              vendor_id='Cisco', platform_id='IOS', os_id='5.2')
    n2 = Node(node_id='TRCAUS30', site_id='AUS', management_ip='1.2.3.4.5', console_id='CACSYO123',
              vendor_id='Cisco', platform_id='IOS', os_id='5.3')
    n3 = Node(node_id='TRADAL30', site_id='DAL', management_ip='1.2.3.4.5', console_id='CACSYO123',
              vendor_id='Cisco', platform_id='IOS', os_id='5.4')
    # print(donor1)
    ds.add_node(n1)
    ds.add_node(n2)
    ds.add_node(n3)
    return ds


def test_find_node(sample_data):
    device = sample_data.find_node('TRNSOY30')
    assert device.node_id == 'TRNSOY30'


def test_find_node_notthere(sample_data):
    device = sample_data.find_node('TGRIRV30')
    assert device is None


def test_remove_node(sample_data):
    device = sample_data.remove_node('TRNSOY30')
    device2 = sample_data.find_node('TRNSOY30')
    assert device2 is None

