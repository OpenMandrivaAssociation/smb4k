%define major 1
%define libname %mklibname %name %major
%define develname %mklibname -d smb4k

Name:		smb4k
Version:	0.9.6
Release:	%mkrel 1
Summary:	A KDE SMB share browser
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
%configure_kde3 
%make

%install
rm -Rf %{buildroot}

%makeinstall_std

# Fix KDE's absolute symlinks
pushd $RPM_BUILD_ROOT%{_kde3_docdir}/HTML/en/smb4k/
	ln -sf ../common
popd

%find_lang %{name} --with-html

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun  -p /sbin/ldconfig
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%{_kde3_bindir}/*
%{_kde3_libdir}/kde3/*
%{_kde3_datadir}/applications/kde/smb4k.desktop
%dir %{_kde3_datadir}/apps/smb4k
%{_kde3_datadir}/apps/*/*.rc
%{_kde3_datadir}/config.kcfg/smb4k.kcfg
%{_kde3_iconsdir}/crystalsvg/*/apps/smb4k.png
%_kde3_datadir/apps/konqsidebartng/add/smb4k_add.desktop
%_kde3_libdir/libsmb4kdialogs.so
%_kde3_libdir/libsmb4kdialogs.la
%_kde3_libdir/libsmb4kcore.so.*
%_kde3_libdir/libsmb4kcore.la

%files devel
%defattr(-,root,root,-)
%_kde3_includedir/*.h
%_kde3_libdir/libsmb4kcore.so
