###from charms.reactive import when, when_not, set_flag
from charmhelpers.core.hookenv import (
    open_port,
    status_set,
)
from charmhelpers.core.hookenv import application_version_set
from charms.reactive import (
    when,when_not,
    set_flag,clear_flag
)
from charms.layer import snap

###@when_not('rocketchat.installed')
###def install_rocketchat():
    ###set_flag('rocketchat.installed')

@when('snap.installed.rocketchat-server')
def set_rocketchat_snapped_available():
    """
    When snap is installed, just keep on updating.
    """
    version = snap.get_installed_version('rocketchat-server')
    channel = snap.get_installed_channel('rocketchat-server')
    application_version_set(version)
    status_set('active', "Ready rocketchat-{} ({})".format(version,channel))
    set_flag('my.rocketchat.application.available')

@when_not('snap.installed.rocketchat-server')
def rocketchat_not_installed():
    """
    Whenever the snap is not installed, clear statuses and flags.
    """
    application_version_set("")
    clear_flag('my.rocketchat.application.available')
    status_set('waiting', "rocketchat snap not installed.")

