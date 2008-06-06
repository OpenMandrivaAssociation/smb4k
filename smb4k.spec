%define major 1
%define libname %mklibname %name %major
%define develname %mklibname -d smb4k

Summary:	A KDE SMB share browser
Name:		smb4k
Version:	0.9.5
Release:	%mkrel 1
Source:		http://download.berlios.de/smb4k/%{name}-%{version}.tar.bz2
License:	GPLv2+
Group:		Networking/Other
Url:		http://smb4k.berlios.de
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	samba-client
BuildRequires:  kde3-macros
BuildRequires:  kdebase3-devel
BuildRequires:	autoconf
BuildRequires:  desktop-file-utils
Obsoletes:	%mklibname %name 0
# fwang: I remove libname in 0.9.0-1, because:
# 1) libname is only used by the application
# 2) the application is mainly an end user application rather than
#    a development library
Obsoletes:	%mklibname %name 1
Conflicts:	%name-devel < 0.9.1-2

%description
An SMB network and share browser for KDE 3 or later.

%package devel
Summary:	Headers files for smb4k
Group:		Development/KDE and Qt
Requires:       %name = %version-%release
Obsoletes:	%mklibname -d %name 1
Obsoletes:	%mklibname -d %name 0
Obsoletes:	%mklibname -d %name

%description devel
Headers files for smb4k.

%prep
%setup -q

%build
make -f admin/Makefile.common cvs
%configure2_5x 
%make

%install
rm -Rf %{buildroot}

%makeinstall_std

# Fix KDE's absolute symlinks
pushd $RPM_BUILD_ROOT%{_docdir}/HTML/en/smb4k/
	ln -sf ../common
popd

%find_lang %{name} --with-html

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun  -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/kde3/*
%{_datadir}/applications/kde/smb4k.desktop
%dir %{_datadir}/apps/smb4k
%{_datadir}/apps/*/*.rc
%{_datadir}/config.kcfg/smb4k.kcfg
%{_iconsdir}/crystalsvg/*/apps/smb4k.png
%_datadir/apps/konqsidebartng/add/smb4k_add.desktop
%_libdir/libsmb4kdialogs.so
%_libdir/libsmb4kdialogs.la
%_libdir/libsmb4kcore.so.*
%_libdir/libsmb4kcore.la

%files devel
%defattr(-,root,root,-)
%_includedir/*.h
%_libdir/libsmb4kcore.so
