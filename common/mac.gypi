# This file is part of Desktop App Toolkit,
# a set of libraries for developing nice desktop applications.
#
# For license and copyright information please follow this link:
# https://github.com/desktop-app/legal/blob/master/LEGAL

{
  'conditions': [
    [ 'build_mac', {
      'variables': {
        'mac_frameworks': [
          'Cocoa',
          'CoreFoundation',
          'CoreServices',
          'CoreText',
          'CoreGraphics',
          'CoreMedia',
          'IOSurface',
          'Metal',
          'OpenGL',
          'AudioUnit',
          'ApplicationServices',
          'Foundation',
          'AGL',
          'Security',
          'SystemConfiguration',
          'Carbon',
          'AudioToolbox',
          'VideoToolbox',
          'VideoDecodeAcceleration',
          'AVFoundation',
          'CoreAudio',
          'QuartzCore',
          'AppKit',
          'CoreWLAN',
          'IOKit',
        ],
        'mac_common_flags': [
          '-pipe',
          '-g',
          '-Wall',
          '-Werror',
          '-W',
          '-fPIE',
          '-Wno-unused-variable',
          '-Wno-unused-parameter',
          '-Wno-unused-function',
          '-Wno-switch',
          '-Wno-comment',
          '-Wno-missing-field-initializers',
          '-Wno-sign-compare',
          '-Wno-unknown-attributes',
        ],
      },
      'xcode_settings': {
        'SYMROOT': '../../out',
        'OTHER_CFLAGS': [
          '<@(mac_common_flags)',
        ],
        'OTHER_CPLUSPLUSFLAGS': [
          '<@(mac_common_flags)',
        ],
        'OTHER_LDFLAGS': [
          '<!@(python -c "for s in \'<@(mac_frameworks)\'.split(\' \'): print(\'-framework \' + s)")',
        ],
        'MACOSX_DEPLOYMENT_TARGET': '<(mac_target)',
        'COMBINE_HIDPI_IMAGES': 'YES',
        'COPY_PHASE_STRIP': 'NO',
        'CLANG_CXX_LANGUAGE_STANDARD': 'c++1z',
        'GCC_INLINES_ARE_PRIVATE_EXTERN': 'YES',
        'GCC_SYMBOLS_PRIVATE_EXTERN': 'YES',
        'GCC_OPTIMIZATION_LEVEL': '0',
        'GCC_WARN_ABOUT_DEPRECATED_FUNCTIONS': 'NO', # temp for range-v3
        'ALWAYS_SEARCH_USER_PATHS': 'NO',
        'CLANG_CXX_LIBRARY': 'libc++',
        'CLANG_ENABLE_OBJC_WEAK': 'YES',
      },
      'configurations': {
        'Debug': {
          'xcode_settings': {
            'ENABLE_TESTABILITY': 'YES',
            'ONLY_ACTIVE_ARCH': 'YES',
          },
        },
      },
      'conditions': [
        [ '"<(special_build_target)" != "" and "<(special_build_target)" != "mac" and "<(special_build_target)" != "osx" and "<(special_build_target)" != "macstore"', {
          'sources': [ '__Wrong_Special_Build_Target__' ],
        }],
      ],
    }],
    [ 'build_osx', {
      'defines': [
        'OS_OSX',
      ],
    }],
    [ 'build_macstore', {
      'defines': [
        'OS_MAC_STORE',
      ],
    }]
  ],
}
