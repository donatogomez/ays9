import importlib
import types
from js9 import j


class SourceLoader:
    """
    holds the logic of building the code of a service actions
    """

    def __init__(self, service):
        self._module = None
        self._source = None
        self.service = service

    def _load(self):
        """
        load all action module
        """
        path = self._source_path()
        loader = importlib.machinery.SourceFileLoader(self.service.model.key, path)
        self._module = types.ModuleType(loader.name)
        loader.exec_module(self._module)

    @property
    def source(self):
        """
        rebuild source code
        """
        if self._source is None:
            actions_model = []
            for model in self.service.model.actions.values():
                actions_model.append(j.core.jobcontroller.db.actions.get(model.actionKey))

            self._source = "from js9 import j\n"

            for model in actions_model:
                if model.imports == '':
                    continue
                source += '{}\n'.format('\n'.join(model.imports))

            tmpl = """
            def {name}({args}):
            {code}

            """
            for model in actions_model:
                tmpl = j.data.text.strip(tmpl)
                code = model.dbobj.code
                code = j.data.text.indent(code, 4)
                self._source += tmpl.format(
                    name=model.dbobj.name,
                    args=model.argsText,
                    code=code
                )
        return self._source

    def _source_path(self):
        """
        write code into a file
        """
        path = j.sal.fs.joinPaths(
            j.dirs.TMPDIR,
            "actions",
            self.service.model.dbobj.actorName,
            self.service.model.key + ".py"
        )
        j.sal.fs.createDir(j.sal.fs.getParent(path))
        j.sal.fs.writeFile(path, self.source)
        return path

    def get_method(self, name):
        """
        get a specific method from the action module
        """
        if self._module is None:
            self._load()
        return getattr(self._module, name)
