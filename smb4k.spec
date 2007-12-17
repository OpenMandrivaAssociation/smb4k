%define major 1
%define libname %mklibname %name %major
%define develname %mklibname -d smb4k

Summary:	A KDE SMB share browser
Name:		smb4k
Version:	0.9.0
Release:	%mkrel 1
Source:		http://download.berlios.de/smb4k/%{name}-%{version}.tar.bz2
License:	GPLv2+
Group:		Networking/Other
Url:		http://smb4k.berlios.de
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	samba-client
BuildRequires:  kdebase-devel
BuildRequires:	autoconf
BuildRequires:  desktop-file-utils
Obsoletes:	%mklibname %name 0
# fwang: I remove libname in 0.9.0-1, because:
# 1) libname is only used by the application
# 2) the application is mainly an end user application rather than
#    a development library
Obsoletes:	%mklibname %name 1

%description
An SMB network and share browser for KDE 3.1 or later.

%package devel
Summary:	Headers files for smb4k
Group:		Development/KDE and Qt
Requires:       %name = %version-%release
Obsoletes:	%mklibname -d %name 1
Obsoletes:	%mklibname -d %name 0

%description devel
Headers files for smb4k.

%prep
%setup -q

%build
make -f admin/Makefile.common cvs
%configure2_5x \
		--disable-debug \
		--enable-shared \
		--disable-static \
		--disable-rpath 
%make

%install
rm -Rf %{buildroot}

%makeinstall_std

# Menu
desktop-file-install --vendor="" \
  --add-category="Network" \
  --add-category="FileTransfer" \
  --add-category="P2P" \
  --remove-category="Utility" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications/kde $RPM_BUILD_ROOT%{_datadir}/applications/kde/*

# Icons
mkdir -p %{buildroot}/{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
ln -s %{_iconsdir}/crystalsvg/16x16/apps/%{name}.png %{buildroot}/%{_miconsdir}
ln -s %{_iconsdir}/crystalsvg/32x32/apps/%{name}.png %{buildroot}/%{_iconsdir}
ln -s %{_iconsdir}/crystalsvg/48x48/apps/%{name}.png %{buildroot}/%{_liconsdir}

# Fix KDE's absolute symlinks
pushd $RPM_BUILD_ROOT%{_docdir}/HTML/en/smb4k/
ln -sf ../common
 popd

#remove buildroot path from libtool files:
perl -pi -e  "s,-L$RPM_BUILD_DIR\S+,,g" %{buildroot}/%{_libdir}/kde3/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun  -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/kde3/*
%{_datadir}/applications/kde/smb4k.desktop
%{_datadir}/apps/smb4k
%{_datadir}/apps/*/*.rc
%{_datadir}/config.kcfg/smb4k.kcfg
%doc %_docdir/HTML/en/smb4k
%{_iconsdir}/crystalsvg/*/apps/smb4k.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%_datadir/apps/konqsidebartng/add/smb4k_add.desktop
%_libdir/*.so.*

%files devel
%defattr(-,root,root,-)
%_includedir/*.h
%_libdir/*.so
%_libdir/*.la
