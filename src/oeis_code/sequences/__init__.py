# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Enrique Pérez Herrero

import importlib
import pkgutil

for _loader, module_name, _is_pkg in pkgutil.walk_packages(__path__):
    importlib.import_module(f"{__name__}.{module_name}")
