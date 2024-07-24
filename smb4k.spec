%define oldlibname %mklibname smb4kcore 6

Name:		smb4k
Version:	3.2.80
Release:	1
Summary:	A KDE SMB share browser
Source0:	https://downloads.sourceforge.net/smb4k/%{name}-%{version}.tar.xz
License:	GPLv2+
Group:		Networking/Other
Url:		https://smb4k.sourceforge.net

BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Widgets)

# KF6 modules

BuildRequires:	cmake(KF6Auth)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DNSSD)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(KF6Wallet)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6Kirigami)

BuildRequires:	cmake(Plasma) >= 6.1.3
BuildRequires:	cmake(KDSoap-qt6)
BuildRequires:	cmake(KDSoapWSDiscoveryClient)
BuildRequires:	cmake(Qt6Keychain)

BuildRequires:	pkgconfig(smbclient)

Requires:	samba-client
Obsoletes:	%{mklibname smb4kdialogs 2} < %version-%release
Obsoletes:	%{oldlibname} < %{EVRD}
Obsoletes:	%{name}-devel < %{EVRD}

%description
An SMB network and share browser for KDE 4 or later.

%files -f %{name}.lang
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
%{_datadir}/dbus-1/system.d/org.kde.smb4k.mounthelper.conf
%_kde5_libdir/libsmb4kcore.so

#------------------------------------------------
%prep
%autosetup -p1
#sed -e '/kdoctools_install/d' -i CMakeLists.txt
%cmake -DQT_MAJOR_VERSION=6

%build
%make_build

%install
%make_install -C build

%find_lang %name --with-html --all-name
