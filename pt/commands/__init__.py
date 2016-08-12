
import sys
import pkgutil
import importlib

import click

def init_plugins(group):
    """Imports extra commands from modules to a provided click command group."""
    package = sys.modules[__name__]

    for (importer, module_name, ispkg) in pkgutil.iter_modules(package.__path__):
        if not ispkg:
            module = importlib.import_module(package.__name__ + '.' + module_name)

            if 'run' not in module.__dict__:
                print('Plugin command "%s" doesn\'t provide a "run" method. Aborting.' % (module_name))
                sys.exit(-1)

            try:
                params = module.run.__click_params__
                params.reverse()
                del module.run.__click_params__
            except AttributeError:
                params = []

            cmd = click.Command(name=module_name, help=module.__doc__, callback=module.run, params=params)

            group.add_command(cmd)
