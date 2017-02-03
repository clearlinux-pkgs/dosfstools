#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dosfstools
Version  : 4.1
Release  : 14
URL      : https://github.com/dosfstools/dosfstools/archive/v4.1.tar.gz
Source0  : https://github.com/dosfstools/dosfstools/archive/v4.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: dosfstools-bin
Requires: dosfstools-doc
BuildRequires : pkgconfig(libudev)
BuildRequires : systemd-dev

%description
dosfstools consists of the programs mkfs.fat, fsck.fat and fatlabel to create,
check and label file systems of the FAT family.  The dosfstools are licensed
under the GNU GPL version 3 or later. See the file COPYING for details.

%package bin
Summary: bin components for the dosfstools package.
Group: Binaries

%description bin
bin components for the dosfstools package.


%package doc
Summary: doc components for the dosfstools package.
Group: Documentation

%description doc
doc components for the dosfstools package.


%prep
%setup -q -n dosfstools-4.1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1486141328
%reconfigure --disable-static --enable-compat-symlinks
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1486141328
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

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/dosfstools/*
%doc /usr/share/man/man8/*
