#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dosfstools
Version  : 3.0.28
Release  : 11
URL      : https://github.com/dosfstools/dosfstools/archive/v3.0.28.tar.gz
Source0  : https://github.com/dosfstools/dosfstools/archive/v3.0.28.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: dosfstools-bin
Requires: dosfstools-doc
Requires: dosfstools-data
Patch1: 0000-change-prefix.patch

%description
Atari format support
====================
Both mkdosfs and dosfsck now can also handle the Atari variation of
the MS-DOS filesystem format. The Atari format has some minor
differences, some caused by the different machine architecture (m68k),
some being "historic" (Atari didn't change some things that M$
changed).

%package bin
Summary: bin components for the dosfstools package.
Group: Binaries
Requires: dosfstools-data

%description bin
bin components for the dosfstools package.


%package data
Summary: data components for the dosfstools package.
Group: Data

%description data
data components for the dosfstools package.


%package doc
Summary: doc components for the dosfstools package.
Group: Documentation

%description doc
doc components for the dosfstools package.


%prep
%setup -q -n dosfstools-3.0.28
%patch1 -p1

%build
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dosfsck
/usr/bin/dosfslabel
/usr/bin/fatlabel
/usr/bin/fsck.fat
/usr/bin/fsck.msdos
/usr/bin/fsck.vfat
/usr/bin/mkdosfs
/usr/bin/mkfs.fat
/usr/bin/mkfs.msdos
/usr/bin/mkfs.vfat

%files data
%defattr(-,root,root,-)
/usr/share/man/de/man8/fatlabel.8
/usr/share/man/de/man8/fsck.fat.8
/usr/share/man/de/man8/mkfs.fat.8

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/dosfstools/*
%doc /usr/share/man/man8/*
