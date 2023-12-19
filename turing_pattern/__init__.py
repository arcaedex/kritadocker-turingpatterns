from krita import DockWidgetFactory, DockWidgetFactoryBase
from .turing_pattern import TuringPattern

DOCKER_ID = 'turing_pattern'
instance = Krita.instance()
dock_widget_factory = DockWidgetFactory(DOCKER_ID,
                                        DockWidgetFactoryBase.DockRight,
                                        TuringPattern)

instance.addDockWidgetFactory(dock_widget_factory)