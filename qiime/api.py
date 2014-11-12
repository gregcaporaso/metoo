from qiime.core.registry import plugin_registry

_api_methods = {}

def api_method(function):
    _api_methods[function.__name__] = function
    return function

def get_api_methods():
    return _api_methods

@api_method
def list_methods(plugins=None):
    return {'methods': [m.uri for m in plugin_registry.get_methods(plugins=plugins)]}

@api_method
def list_plugins():
    return {'plugins': list(plugin_registry.get_plugin_uris())}

@api_method
def method_info(method_uri):
    method = plugin_registry.get_method(method_uri)
    return {
        'uri': method.uri,
        'name': method.name,
        'help': method.docstring,
        'annotations': {
            'artifacts': [],  # (parameterized) artifacts (defined in org.qiime.plugins.[plugin-name].artifacts)
            'parameters': {}, # (parameterized) primitives (defined in org.qiime.types.primitives|parameterized)
            'return': []      # (parameterized) artifacts
        }
    }
