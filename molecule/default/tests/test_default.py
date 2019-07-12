import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def tests_sources_file(host):
    file = host.file('/etc/apt/sources.list.d/qbittorrent-stable.list')

    assert file.exists


def test_qbittorrent_nox_is_installed(host):
    qbittorrent_nox = host.package("qbittorrent-nox")

    assert qbittorrent_nox.is_installed


def test_service_file_exists(host):
    file = host.file("/etc/systemd/system/qbittorrent.service")

    assert file.exists
    assert file.user == "root"
    assert file.group == "root"
