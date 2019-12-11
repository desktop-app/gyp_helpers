# This file is part of Desktop App Toolkit,
# a set of libraries for developing nice desktop applications.
#
# For license and copyright information please follow this link:
# https://github.com/desktop-app/legal/blob/master/LEGAL

{
  'includes': [
    'win.gypi',
    'mac.gypi',
    'linux.gypi',
  ],
  'variables': {
    'variables': {
      'variables': {
        'variables': {
          'variables': {
            'build_os%': '<(OS)',
          },
          'build_os%': '<(build_os)',
          'conditions': [
            [ 'build_os == "win"', {
              'build_win': 1,
            }, {
              'build_win': 0,
            }],
            [ 'build_os == "mac"', {
              'build_mac': 1,
            }, {
              'build_mac': 0,
            }],
            [ 'build_os == "linux"', {
              'build_linux': 1,
            }, {
              'build_linux': 0,
            }],
          ],
          'special_build_target%': '',
        },
        'build_os%': '<(build_os)',
        'build_win%': '<(build_win)',
        'build_mac%': '<(build_mac)',
        'build_linux%': '<(build_linux)',
        'special_build_target%': '<(special_build_target)',

        'conditions': [[ '"<(special_build_target)" == "osx"', {
          'build_macold': 0,
          'build_osx': 1,
        }, {
          'build_macold': 0,
          'build_osx': 0,
        }], [ '"<(special_build_target)" == "macstore"', {
          'build_macstore': 1,
        }, {
          'build_macstore': 0,
        }], [ '"<(special_build_target)" == "uwp"', {
          'build_uwp': 1,
        }, {
          'build_uwp': 0,
        }]],
      },
      'conditions': [[ 'build_mac and not build_osx', {
        'libs_loc%': '<(DEPTH)/../../../Libraries/macos',
      }, {
        'libs_loc%': '<(DEPTH)/../../../Libraries',
      }]],

      'build_os%': '<(build_os)',
      'build_win%': '<(build_win)',
      'build_uwp%': '<(build_uwp)',
      'build_mac%': '<(build_mac)',
      'build_macold%': '<(build_macold)',
      'build_macstore%': '<(build_macstore)',
      'build_osx%': '<(build_osx)',
      'build_linux%': '<(build_linux)',

      'special_build_target%': '<(special_build_target)',
      'ci_build%': '',
      'build_standard_win%': 'c++latest',
      'submodules_loc%': '<(DEPTH)/..',
      'private_loc%': '<(DEPTH)/../../../DesktopPrivate',
      'third_party_loc%': '<(DEPTH)/../ThirdParty',
    },
    'build_os%': '<(build_os)',
    'build_win%': '<(build_win)',
    'build_mac%': '<(build_mac)',
    'build_linux%': '<(build_linux)',
    'special_build_target%': '<(special_build_target)',
    'ci_build%': '<(ci_build)',
    'build_standard_win%': '<(build_standard_win)',
    'libs_loc%': '<(libs_loc)',
    'submodules_loc%': '<(submodules_loc)',
    'private_loc%': '<(private_loc)',
    'third_party_loc%': '<(third_party_loc)',
    'build_defines%': '',

    # GYP does not support per-configuration libraries :(
    # So they will be emulated through additional link flags,
    # which will contain <(ld_lib_prefix)LibraryName<(ld_lib_postfix)
    'conditions': [
      [ 'build_win', {
        'ld_lib_prefix': '',
        'ld_lib_postfix': '.lib',
        'exe_ext': '.exe',
      }, {
        'ld_lib_prefix': '-l',
        'ld_lib_postfix': '',
        'exe_ext': '',
      }],
      [ '"<(special_build_target)" == "osx"', {
        'mac_target%': '10.10',
        'build_macold': 0,
        'build_osx': 1,
      }, {
        'mac_target%': '10.12',
        'build_macold': 0,
        'build_osx': 0,
      }],
      [ '"<(special_build_target)" == "macstore"', {
        'build_macstore': 1,
      }, {
        'build_macstore': 0,
      }],
      [ '"<(special_build_target)" == "uwp"', {
        'build_uwp': 1,
      }, {
        'build_uwp': 0,
      }],
    ],
    'ld_lib_prefix': '<(ld_lib_prefix)',
    'ld_lib_postfix': '<(ld_lib_postfix)',
    'exe_ext': '<(exe_ext)',

    'library%': 'static_library',
  },

  'defines': [
    'NOMINMAX'
  ],
  'configurations': {
    'Debug': {
      'defines': [
        '_DEBUG',
      ],
    },
    'Release': {
      'defines': [
        'NDEBUG',
      ],
    },
  },
}
