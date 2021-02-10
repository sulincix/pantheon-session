project('elementary-session-settings',
        version: '5.0.3',
        default_options: 'sysconfdir=/etc')

prefix = get_option('prefix')
datadir = join_paths(prefix, get_option('datadir'))
bindir = join_paths(prefix, get_option('bindir'))

if get_option('mimeapps-list')
    subdir('applications')
endif
if get_option('gnome-session')
    subdir('session')
    subdir('xsessions')
endif
if get_option('use-non-gnome')
    subdir('xsessions-non-gnome')
endif
