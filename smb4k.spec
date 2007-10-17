%define major 1
%define libname %mklibname %name %major
%define develname %mklibname -d smb4k

Summary:	A KDE SMB share browser
Name:		smb4k
Version:	0.8.6
Release:	%mkrel 1
Source:		http://download.berlios.de/smb4k/%{name}-%{version}.tar.bz2
License:	GPL
Group:		Networking/Other
Url:		http://smb4k.berlios.de
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	samba-client
BuildRequires:  kdebase-devel
BuildRequires:	autoconf
BuildRequires:  desktop-file-utils
Conflicts:	%mklibname %name 0
Requires:	%libname = %version-%release

%description
An SMB network and share browser for KDE 3.1 or later.

%package -n %develname
Summary:	Headers files for smb4k
Group:		Development/KDE and Qt
Provides:	smb4k-devel = %version-%release
Requires:       %libname = %version-%release
Conflicts:	%mklibname %name 0

%description -n %develname
Headers files for smb4k.

%package -n %libname
Summary:	Lib files for smb4k
Group:		Development/KDE and Qt
Obsoletes:	%mklibname %{name} 0

%description -n %libname
Lib files for smb4k.

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

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/kde3/*
%{_datadir}/applications/kde/smb4k.desktop
%{_datadir}/apps/smb4k
%doc %_docdir/HTML/en/smb4k
%{_iconsdir}/crystalsvg/*/apps/smb4k.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%_datadir/apps/konqsidebartng/add/smb4k_add.desktop

%files -n %libname
%defattr(-,root,root,-)
%_libdir/libsmb4kcore.so.%{major}*
%_libdir/libsmb4kwidgets.so.{major}*

%files -n %develname
%defattr(-,root,root,-)
%_includedir/*.h
%_libdir/*.so
%_libdir/*.la
