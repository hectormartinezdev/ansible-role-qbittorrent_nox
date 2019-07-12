# hectormartinezdev.qbittorrent-nox

This role installs the "No X Server" qBittorrent version as a service
with systemd. It automatically accepts the license, so be sure to check
qBittorrent first before using this role.

## Role Variables

```yaml
---
# PPA style, 'stable' or 'unstable'
qbittorrent_ppa: stable

# User that should be running qbittorrent
qbittorrent_user: "{{ ansible_user_id }}"

# If the service should be enabled
qbittorrent_service_enabled: true

# State of the service
qbittorrent_service_state: started
```

## Example Playbook

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

```yaml
- hosts: servers
  vars:
    qbittorrent_ppa: unstable
    qbittorrent_user: qbtuser

  roles:
    - hectormartinezdev.qbittorrent-nox
```

## License

MIT
