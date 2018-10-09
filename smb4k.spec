%define major 5
%define libname %mklibname smb4kcore %major

Name:		smb4k
Version:	2.1.1
Release:	1
Summary:	A KDE SMB share browser
Source0:	http://downloads.sourceforge.net/smb4k/%{name}-%{version}.tar.xz
License:	GPLv2+
Group:		Networking/Other
Url:		http://smb4k.sourceforge.net
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5PrintSupport)

# KF5 modules
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5Sonnet)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5Crash)

Requires:	samba-client
Requires:	%libname = %version
Obsoletes:	%{mklibname smb4kdialogs 2} < %version-%release
Conflicts:	%name-devel < 0.10.0-rc

%description
An SMB network and share browser for KDE 4 or later.

%files -f %{name}.lang
%_kde5_sysconfdir/dbus-1/system.d/org.kde.smb4k.mounthelper.conf
%{_kde5_bindir}/smb4k*
%_kde5_datadir/kconf_update/*
%_kde5_datadir/dbus-1/system-services/org.kde.smb4k.mounthelper.service
%_kde5_datadir/polkit-1/actions/org.kde.smb4k.mounthelper.policy
%{_kde5_libdir}/qt5/plugins/*.so
%{_kde5_libdir}/libexec/kauth/mounthelper
%{_kde5_applicationsdir}/org.kde.smb4k.desktop
%{_kde5_datadir}/config.kcfg/smb4k.kcfg
%{_kde5_iconsdir}/*/*/*/*
%{_datadir}/metainfo/org.kde.smb4k.appdata.xml
%{_datadir}/kxmlgui5/smb4k
%{_datadir}/knotifications5/smb4k.notifyrc
%{_datadir}/plasma/plasmoids/org.kde.smb4kqml
%{_datadir}/kservices5/plasma-applet-org.kde.smb4kqml.desktop
%{_libdir}/qt5/qml/org/kde/smb4k
%{_datadir}/metainfo/org.kde.smb4kqml.appdata.xml

#------------------------------------------------	
%package -n %libname
Summary:	SMB4K core library
Group:		System/Libraries

%description -n %libname
Library for %{name}.

%files -n %libname
%_kde5_libdir/libsmb4kcore.so.%{major}*

#------------------------------------------------
%package devel
Summary:	SMB4K development files
Group:		Development/KDE and Qt
Requires:	%libname = %version

%description devel
Development files for applications that need %{name}.

%files devel
%_kde5_libdir/libsmb4kcore.so


#------------------------------------------------
%prep
%setup -q
sed -e '/kdoctools_install/d' -i CMakeLists.txt

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build


%find_lang %name --with-html --all-name
