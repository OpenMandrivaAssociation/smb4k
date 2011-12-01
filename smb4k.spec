Name:		smb4k
Version:	0.10.10
Release:	%mkrel 2
Summary:	A KDE SMB share browser
Source:		http://download.berlios.de/smb4k/%{name}-%{version}.tar.bz2
Patch1:		smb4k-0.10.10-sudo.patch
License:	GPLv2+
Group:		Networking/Other
Url:		http://smb4k.berlios.de
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	samba-client
Requires:	kdebase4-runtime
BuildRequires:  kdelibs4-devel
Obsoletes:	%mklibname %name 0
# fwang: I remove libname in 0.9.0-1, because:
# 1) libname is only used by the application
# 2) the application is mainly an end user application rather than
#    a development library
Obsoletes:	%mklibname %name 1
Obsoletes:	%{mklibname smb4kdialogs 2} < %version-%release
Conflicts:	%name-devel < 0.10.0-rc

%description
An SMB network and share browser for KDE 4 or later.

%files -f %{name}.lang
%defattr(-,root,root)
%{_kde_bindir}/*
%_kde_datadir/apps/kconf_update/*
%{_kde_libdir}/kde4/*.so
%{_kde_libdir}/libsmb4kdialogs.so
%{_kde_datadir}/applications/kde4/smb4k.desktop
%dir %{_kde_datadir}/apps/smb4k
%{_kde_datadir}/apps/*/*.rc
%{_kde_datadir}/config.kcfg/smb4k.kcfg
%{_kde_iconsdir}/*/*/*/*

#------------------------------------------------	

%define smb4kcore_major 3
%define libsmb4kcore %mklibname smb4kcore %smb4kcore_major

%package -n %libsmb4kcore
Summary: SMB4K core library
Group: System/Libraries

%description -n %libsmb4kcore
SMB4K core library.

%files -n %libsmb4kcore
%defattr(-,root,root)
%_kde_libdir/libsmb4kcore.so.%{smb4kcore_major}*

#------------------------------------------------
%package devel
Summary: Developemnt files for smb4k
Group: Development/KDE and Qt
Requires: %libsmb4kcore = %version-%release

%description devel
Developemnt files for smb4k.

%files devel
%defattr(-,root,root)
%_kde_libdir/libsmb4kcore.so

#------------------------------------------------

%prep
%setup -q -n %name-%version
%patch1 -p1

cd po/pt
mv pt.po %name.po

%build
%cmake_kde4
%make

%install
rm -Rf %{buildroot}
%makeinstall_std -C build

%find_lang %name --with-html

%clean
rm -rf %{buildroot}
