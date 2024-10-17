%define oldlibname %mklibname smb4kcore 6

Name:		smb4k
Version:	3.2.90
Release:	1
Summary:	A KDE SMB share browser
Source0:	https://invent.kde.org/network/smb4k/-/archive/%{version}/smb4k-%{version}.tar.bz2
License:	GPLv2+
Group:		Networking/Other
Url:		https://smb4k.sourceforge.net
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Keychain)

# KF modules
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Auth)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6DNSSD)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(KF6Sonnet)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6Wallet)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6StatusNotifierItem)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(PlasmaQuick)
BuildRequires:	pkgconfig(smbclient)

Requires:	samba-client
Obsoletes:	%{mklibname smb4kdialogs 2} < %version-%release
Obsoletes:	%{oldlibname} < %{EVRD}
Obsoletes:	%{name}-devel < %{EVRD}

%description
An SMB network and share browser for KDE 4 or later.

%files -f %{name}.lang
%{_kde5_bindir}/smb4k*
%_kde5_datadir/dbus-1/system-services/org.kde.smb4k.mounthelper.service
%_kde5_datadir/polkit-1/actions/org.kde.smb4k.mounthelper.policy
%{_kde5_applicationsdir}/org.kde.smb4k.desktop
%{_kde5_datadir}/config.kcfg/smb4k.kcfg
%{_kde5_iconsdir}/*/*/*/*
%{_datadir}/metainfo/org.kde.smb4k.appdata.xml
%{_datadir}/knotifications6/smb4k.notifyrc
%{_datadir}/plasma/plasmoids/org.kde.smb4kqml
%{_datadir}/metainfo/org.kde.smb4kqml.appdata.xml
%{_datadir}/dbus-1/system.d/org.kde.smb4k.mounthelper.conf
%_kde5_libdir/libsmb4kcore.so
%{_libdir}/libexec/kf6/kauth/mounthelper
%{_libdir}/libsmb4kdialogs.so
%{_qtdir}/plugins/smb4kconfigdialog.so
%{_qtdir}/qml/org/kde/smb4k

#------------------------------------------------
%prep
%autosetup -p1
#sed -e '/kdoctools_install/d' -i CMakeLists.txt
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %name --with-html --all-name
