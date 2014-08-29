# Copyright 2014 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'sources': [
    '<@(schema_files)',
  ],
  'variables': {
    'chromium_code': 1,
    # TODO: Eliminate these on Android. See crbug.com/305852.
    'android_schema_files': [
      'runtime.json',
    ],
    'main_schema_files': [
      'app_runtime.idl',
      'app_view_internal.json',
      'cast_channel.idl',
      'dns.idl',
      'extensions_manifest_types.json',
      'extension_types.json',
      'hid.idl',
      'power.idl',
      'runtime.json',
      'serial.idl',
      'socket.idl',
      'sockets_tcp.idl',
      'sockets_tcp_server.idl',
      'sockets_udp.idl',
      'storage.json',
      'test.json',
      'usb.idl',
      'usb_private.idl',
    ],
    'non_compiled_schema_files': [
    ],
    'conditions': [
      ['enable_extensions==1', {
        'schema_files': [
          '<@(main_schema_files)',
        ],
      }, {
        'schema_files': [
          '<@(android_schema_files)',
        ],
      }],
    ],
    'cc_dir': 'extensions/common/api',
    'root_namespace': 'extensions::core_api::%(namespace)s',
    'impl_dir_': 'extensions/browser/api',
  },
}
