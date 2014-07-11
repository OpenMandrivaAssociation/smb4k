%define major 4
%define libname %mklibname smb4kcore %major

Name:		smb4k
Version:	1.0.5
Release:	7
Summary:	A KDE SMB share browser
Source0:	http://downloads.sourceforge.net/smb4k/%{name}-%{version}.tar.bz2
License:	GPLv2+
Group:		Networking/Other
Url:		http://smb4k.sourceforge.net
BuildRequires:  kdelibs4-devel
Requires:	samba-client
Requires:	%libname = %version
Obsoletes:	%{mklibname smb4kdialogs 2} < %version-%release
Conflicts:	%name-devel < 0.10.0-rc

%description
An SMB network and share browser for KDE 4 or later.

%files -f %{name}.lang
%_kde_sysconfdir/dbus-1/system.d/de.berlios.smb4k.mounthelper.conf
%{_kde_bindir}/smb4k*
%_kde_datadir/apps/kconf_update/*
%_kde_datadir/dbus-1/system-services/de.berlios.smb4k.mounthelper.service
%_kde_datadir/polkit-1/actions/de.berlios.smb4k.mounthelper.policy
%{_kde_libdir}/kde4/*.so
%{_kde_libdir}/libsmb4ktooltips.so
%{_kde_libdir}/kde4/libexec/mounthelper
%{_kde_applicationsdir}/smb4k.desktop
%{_kde_appsdir}/smb4k/
%{_kde_datadir}/config.kcfg/smb4k.kcfg
%{_kde_iconsdir}/*/*/*/*

#------------------------------------------------	
%package -n %libname
Summary:	SMB4K core library
Group:		System/Libraries

%description -n %libname
Library for %{name}.

%files -n %libname
%_kde_libdir/libsmb4kcore.so.%{major}*

#------------------------------------------------
%package devel
Summary:	SMB4K development files
Group:		Development/KDE and Qt
Requires:	%libname = %version

%description devel
Development files for applications that need %{name}.

%files devel
%_kde_libdir/libsmb4kcore.so


#------------------------------------------------
%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %name --with-html
