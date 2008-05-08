%define major 1
%define libname %mklibname %name %major
%define develname %mklibname -d smb4k

Summary:	A KDE SMB share browser
Name:		smb4k
Version:	0.9.4
Release:	%mkrel 2
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun  -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%{_kde3_bindir}/*
%{_kde3_libdir}/kde3/*
%{_kde3_datadir}/applications/kde/smb4k.desktop
%dir %{_kde3_datadir}/apps/smb4k
%{_kde3_datadir}/apps/*/*.rc
%{_kde3_datadir}/config.kcfg/smb4k.kcfg
%doc %_kde3_docdir/HTML/en/smb4k
%{_kde3_iconsdir}/crystalsvg/*/apps/smb4k.png
%_kde3_appsdir/konqsidebartng/add/smb4k_add.desktop
%_kde3_libdir/libsmb4kdialogs.so
%_kde3_libdir/libsmb4kdialogs.la
%_kde3_libdir/libsmb4kcore.so.*
%_kde3_libdir/libsmb4kcore.la

%files devel
%defattr(-,root,root,-)
%_kde3_includedir/*.h
%_kde3_libdir/libsmb4kcore.so
