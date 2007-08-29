%define name		smb4k
%define version		0.8.4


%define lib_name_orig %mklibname smb4k
%define lib_major 0
%define lib_name %lib_name_orig%lib_major
%define develname %mklibname -d smb4k


%define __libtoolize /bin/true

Summary:	A KDE SMB share browser
Name:		%{name}
Version:	%{version}
Release:	%mkrel 2
Source:		http://download.berlios.de/smb4k/%{name}-%{version}.tar.bz2
License:	GPL
Group:		Networking/Other
Url:		http://smb4k.berlios.de
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	samba-client
BuildRequires:  kdebase-devel
BuildRequires:	autoconf
BuildRequires:  desktop-file-utils
Requires:	%lib_name = %version-%release

%description
An SMB network and share browser for KDE 3.1 or later.

%package -n %develname
Summary:	Headers files for smb4k
Group:		Development/KDE and Qt

Provides:	smb4k-devel = %version-%release

Provides:	%lib_name_orig-devel = %version-%release
Requires:       %lib_name = %version-%release
Obsoletes:	%lib_name-devel

%description -n %develname
Headers files for smb4k.


%package -n %lib_name
Summary:	Lib files for smb4k
Group:		Development/KDE and Qt


%description -n %lib_name
Lib files for smb4k.



%prep
%setup -q

%build
make -f admin/Makefile.common cvs

export QTDIR=%_prefix/lib/qt3
export KDEDIR=%_prefix

export LD_LIBRARY_PATH=$QTDIR/%_lib:$KDEDIR/%_lib:$LD_LIBRARY_PATH
export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH


%{?__cputoolize: %{__cputoolize} }

%configure2_5x \
		--disable-debug \
		--enable-shared \
		--disable-static \
%if "%{_lib}" != "lib"
    --enable-libsuffix="%(A=%{_lib}; echo ${A/lib/})" \
%endif
		--disable-rpath 
		#--enable-final

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

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/%{name}*
%{_datadir}/applications/kde/smb4k.desktop
%{_datadir}/apps/smb4k
%doc %_docdir/HTML/en/smb4k
%{_iconsdir}/crystalsvg/*/apps/smb4k.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%_datadir/apps/konqsidebartng/add/smb4k_add.desktop


%files -n %lib_name
%defattr(-,root,root,-)
%_libdir/kde3/konqsidebar_smb4k.la
%_libdir/kde3/konqsidebar_smb4k.so

%_libdir/libsmb4kcore.la
%_libdir/libsmb4kcore.so.*
%_libdir/libsmb4kwidgets.la
%_libdir/libsmb4kwidgets.so.*


%files -n %develname
%defattr(-,root,root,-)
%_includedir/*.h
%_libdir/libsmb4kcore.so
%_libdir/libsmb4kwidgets.so


