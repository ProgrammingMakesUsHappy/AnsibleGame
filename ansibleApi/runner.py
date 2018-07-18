# -*- coding:utf-8 -*-
from ansible.executor.playbook_executor import PlaybookExecutor


from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.utils.display import logger
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from tempfile import NamedTemporaryFile
from ansible.plugins.callback import CallbackBase
import os


class ansibleRunner(object):
    """
    This is a General object for parallel execute modules.
    """

    def __init__(self, resource, *args, **kwargs):
        self.resource = resource
        self.inventory = None
        self.variable_manager = None
        self.loader = None
        self.options = None
        self.passwords = None
        self.callback = None
        self.__initializeData()
        self.results_raw = {}

    def __initializeData(self):
        """
        初始化ansible
        """

        Options = namedtuple('Options',
                             ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check',
                              'diff'])

        self.loader = DataLoader()

        self.options = Options(connection='ssh', module_path='/path/to/mymodules', forks=100, become=None,
                               become_method=None, become_user=None, check=False,
                               diff=False)

        self.passwords = dict(vault_pass='secret')
        self.inventory = InventoryManager(loader=self.loader, sources=self.resource)
        self.variable_manager = VariableManager(loader=self.loader, inventory=self.inventory)

    def run(self, host_list, module_name, module_args, ):
        """
        run module from andible ad-hoc.
        module_name: ansible module_name
        module_args: ansible module args
        """
        # create play with tasks
        play_source = dict(
            name="Ansible Play",
            hosts=host_list,
            gather_facts='no',
            tasks=[dict(action=dict(module=module_name, args=module_args))]
        )
        play = Play().load(play_source, variable_manager=self.variable_manager, loader=self.loader)

        # actually run it
        tqm = None
        self.callback = ResultsCollector()
        try:
            tqm = TaskQueueManager(
                inventory=self.inventory,
                variable_manager=self.variable_manager,
                loader=self.loader,
                options=self.options,
                passwords=self.passwords,
                stdout_callback='default',
            )
            tqm._stdout_callback = self.callback
            result = tqm.run(play)
            # print result
        # print self.callback
        finally:
            if tqm is not None:
                tqm.cleanup()

    def run_playbook(self, host_list, role_name, role_uuid, temp_param):
        """
        run ansible palybook
        """
        try:
            self.callback = ResultsCollector()
            filenames = [BASE_DIR + '/handlers/ansible/v1_0/sudoers.yml']  # playbook的路径
            logger.info('ymal file path:%s' % filenames)
            template_file = TEMPLATE_DIR  # 模板文件的路径
            if not os.path.exists(template_file):
                logger.error('%s 路径不存在 ' % template_file)
                sys.exit()

            extra_vars = {}  # 额外的参数 sudoers.yml以及模板中的参数，它对应ansible-playbook test.yml --extra-vars "host='aa' name='cc' "
            host_list_str = ','.join([item for item in host_list])
            extra_vars['host_list'] = host_list_str
            extra_vars['username'] = role_name
            extra_vars['template_dir'] = template_file
            extra_vars['command_list'] = temp_param.get('cmdList')
            extra_vars['role_uuid'] = 'role-%s' % role_uuid
            self.variable_manager.extra_vars = extra_vars
            ##logger.info('playbook 额外参数:%s'%self.variable_manager.extra_vars)
            # actually run it
            executor = PlaybookExecutor(
                playbooks=filenames, inventory=self.inventory, variable_manager=self.variable_manager,
                loader=self.loader,
                options=self.options, passwords=self.passwords,
            )
            executor._tqm._stdout_callback = self.callback
            executor.run()
        except Exception as e:
            ##logger.error("run_playbook:%s"%e)
            pass

    def get_result(self):
        self.results_raw = {'success': {}, 'failed': {}, 'unreachable': {}}
        for host, result in self.callback.host_ok.items():
            self.results_raw['success'][host] = result._result

        for host, result in self.callback.host_failed.items():
            self.results_raw['failed'][host] = result._result

        for host, result in self.callback.host_unreachable.items():
            self.results_raw['unreachable'][host] = result._result['msg']

            # print "Ansible执行结果集:%s"%self.results_raw
        return self.results_raw


class ResultsCollector(CallbackBase):

    def __init__(self, *args, **kwargs):
        super(ResultsCollector, self).__init__(*args, **kwargs)
        self.host_ok = {}
        self.host_unreachable = {}
        self.host_failed = {}

    def v2_runner_on_unreachable(self, result):
        self.host_unreachable[result._host.get_name()] = result

    def v2_runner_on_ok(self, result, *args, **kwargs):
        self.host_ok[result._host.get_name()] = result

    def v2_runner_on_failed(self, result, *args, **kwargs):
        self.host_failed[result._host.get_name()] = result

