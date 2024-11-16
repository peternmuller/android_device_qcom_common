#!/usr/bin/env -S PYTHONPATH=../../:../../../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-FileCopyrightText: 2024 Paranoid Android
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import ExtractUtils

from extract_utils_qti.module import ExtractUtilsQTIModule, QTIComponentType

namespace_imports = [
    'hardware/qcom/display',
    'vendor/qcom/common/vendor/dsprpcd',
]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'libc2dcolorconvert',
        'libmmosal',
        'libOmxCore',
        'libplatformconfig',
        'libwfdcommonutils_proprietary',
        'libwfdmmservice_proprietary',
        'libwfdutils_proprietary',
    ): lib_fixup_remove,
}

module = ExtractUtilsQTIModule(
    'media-legacy',
    QTIComponentType.VENDOR,
    namespace_imports=namespace_imports,
    lib_fixups=lib_fixups,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
