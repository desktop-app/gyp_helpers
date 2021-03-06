# This file is part of Desktop App Toolkit,
# a set of libraries for developing nice desktop applications.
#
# For license and copyright information please follow this link:
# https://github.com/desktop-app/legal/blob/master/LEGAL

{
  'conditions': [
    [ 'build_linux', {
      'variables': {
        'linux_common_flags': [
          '-pipe',
          '-Wall',
          '-Werror',
          '-W',
          '-fPIC',
          '-Wno-unused-variable',
          '-Wno-unused-parameter',
          '-Wno-unused-function',
          '-Wno-switch',
          '-Wno-comment',
          '-Wno-unused-but-set-variable',
          '-Wno-missing-field-initializers',
          '-Wno-sign-compare',
          '-Wno-attributes',
          '-Wno-parentheses', # happens in foreign headers
          '-Wno-stringop-overflow', # false positives
          '-Wno-error=class-memaccess',
        ],
        'linux_path_ffmpeg%': '/usr/local',
        'linux_path_openal%': '/usr/local',
        'linux_path_va%': '/usr/local',
        'linux_path_vdpau%': '/usr/local',
        'linux_path_breakpad%': '/usr/local',
        'linux_path_range%': '/usr/local',
      },
      'include_dirs': [
        '/usr/local/include',
        '<(linux_path_ffmpeg)/include',
        '<(linux_path_openal)/include',
        '<(linux_path_breakpad)/include/breakpad',
        '<(linux_path_range)/include',
      ],
      'library_dirs': [
        '/usr/local/lib',
        '<(linux_path_ffmpeg)/lib',
        '<(linux_path_openal)/lib',
        '<(linux_path_va)/lib',
        '<(linux_path_vdpau)/lib',
        '<(linux_path_breakpad)/lib',
      ],
      'conditions': [
        [ '"<!(uname -m)" == "x86_64" or "<!(uname -m)" == "aarch64"', {
          'defines': [
            'Q_OS_LINUX64',
          ],
          'conditions': [
            [ '"<(special_build_target)" != "" and "<(special_build_target)" != "linux"', {
              'sources': [ '__Wrong_Special_Build_Target_<(special_build_target)_' ],
            }],
          ],
        }, {
          'defines': [
            'Q_OS_LINUX32',
          ],
          'conditions': [
            [ '"<(special_build_target)" != "" and "<(special_build_target)" != "linux32"', {
              'sources': [ '__Wrong_Special_Build_Target_<(special_build_target)_' ],
            }],
          ],
        }], [ '"<!(uname -m)" == "x86_64"', {
          # 32 bit version can't be linked with debug info or LTO,
          # virtual memory exhausted :(
          'cflags_c': [ '-g' ],
          'cflags_cc': [ '-g' ],
          'ldflags': [ '-g' ],
          'configurations': {
            'Release': {
              'cflags_c': [ '-flto' ],
              'cflags_cc': [ '-flto' ],
              'ldflags': [ '-flto', '-fuse-linker-plugin' ],
            },
          },
        }]
      ],
      'defines': [
        '_REENTRANT',
        'QT_STATICPLUGIN',
        'QT_PLUGIN',
      ],
      'cflags_c': [
        '<@(linux_common_flags)',
        '-std=gnu11',
      ],
      'cflags_cc': [
        '<@(linux_common_flags)',
        '-std=c++1z',
        '-Wno-register',
      ],
      'make_global_settings': [
        ['AR', '/usr/bin/gcc-ar'],
        ['RANLIB', '/usr/bin/gcc-ranlib'],
        ['NM', '/usr/bin/gcc-nm'],
      ],
      'configurations': {
        'Debug': {
        },
      },
    }],
  ],
}
