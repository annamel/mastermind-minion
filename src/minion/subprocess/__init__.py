from minion.subprocess.rsync import RsyncSubprocess
from minion.subprocess.dnet_ioclient import DnetIoclientSubprocess
from minion.subprocess.dnet_client import DnetClientSubprocess
from minion.subprocess.dnet_recovery import DnetRecoverySubprocess
from minion.subprocess.ubic import UbicSubprocess
from minion.subprocess.executor import GroupCreator, GroupRemover
from minion.subprocess.base import BaseSubprocess


def subprocess_factory(cmd):
    if cmd[0] == 'rsync':
        Subprocess = RsyncSubprocess
    elif cmd[0] == 'dnet_recovery':
        Subprocess = DnetRecoverySubprocess
    elif cmd[0] == 'dnet_ioclient':
        Subprocess = DnetIoclientSubprocess
    elif cmd[0] == 'dnet_client':
        Subprocess = DnetClientSubprocess
    elif cmd[0] == 'ubic':
        Subprocess = UbicSubprocess
    elif cmd[0] == 'create_group':
        Subprocess = GroupCreator
    elif cmd[0] == 'remove_group':
        Subprocess = GroupRemover
    elif cmd[0] == 'lrc_convert':
        Subprocess = UbicSubprocess
    elif cmd[0] == 'lrc_validate':
        Subprocess = UbicSubprocess
    elif cmd[0] == 'mds_cleanup':
        Subprocess = BaseSubprocess
    else:
        raise ValueError('Unsupported command: {0}'.format(cmd[0]))
    return Subprocess
