import sources
from .interface_source import *
from .proxyscrape import *
from .sslproxies import *
from .didsoft import *


def get_sources(auth=None):
    # Get all classes from sources module
    source_classes = [cls for name, cls in sources.__dict__.items() if isinstance(cls, type)]
    source_classes = [cls for cls in source_classes
                      if issubclass(cls, sources.SourceInterface) and cls != sources.SourceInterface]
    classes = []
    for source_class in source_classes:
        source_instance = source_class()
        if isinstance(auth, bool):
            if source_instance.auth is auth:
                classes.append(source_class)
                pass
        else:
            classes.append(source_class)
    return classes


__all__ = ['get_sources']
