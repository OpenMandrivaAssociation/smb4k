Name:		smb4k
Version:	0.10.12
Release:	1
Summary:	A KDE SMB share browser
Source:		http://downloads.sourceforge.net/project/smb4k/Smb4K%20%28stable%20releases%29/0.10.12/%{name}-%{version}.tar.bz2
Patch1:		smb4k-0.10.10-sudo.patch
License:	GPLv2+
Group:		Networking/Other
Url:		http://sourceforge.net/projects/smb4k
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


%changelog
* Thu Jan 12 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.10.12-1
+ Revision: 760394
- version update 0.10.12

* Mon Jun 27 2011 Funda Wang <fwang@mandriva.org> 0.10.10-2
+ Revision: 687517
- add fedora patch to try fix bug#63521 (only works under konsole)

* Tue Mar 08 2011 Funda Wang <fwang@mandriva.org> 0.10.10-1
+ Revision: 642972
- update to new version 0.10.10

* Sat Sep 11 2010 Funda Wang <fwang@mandriva.org> 0.10.9-1mdv2011.0
+ Revision: 577577
- new version 0.10.9

* Sat Aug 21 2010 Funda Wang <fwang@mandriva.org> 0.10.8-1mdv2011.0
+ Revision: 571607
- update to new version 0.10.8

* Sun May 02 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.10.7-2mdv2010.1
+ Revision: 541670
- Fix patch0
- Fix i18n error in Warning window
  This does not fix bug 58877, but at least fix the display
  CCBUG: 58877

* Wed Apr 07 2010 Funda Wang <fwang@mandriva.org> 0.10.7-1mdv2010.1
+ Revision: 532669
- update to new version 0.10.7

* Thu Mar 25 2010 Funda Wang <fwang@mandriva.org> 0.10.6-1mdv2010.1
+ Revision: 527362
- new version 0.10.6

* Sun Feb 14 2010 Funda Wang <fwang@mandriva.org> 0.10.5-1mdv2010.1
+ Revision: 505829
- New version 0.10.5

* Thu Oct 08 2009 Funda Wang <fwang@mandriva.org> 0.10.4-1mdv2010.0
+ Revision: 456086
- should be 1mdv

* Tue Oct 06 2009 Funda Wang <fwang@mandriva.org> 0.10.4-0.1mdv2010.0
+ Revision: 454642
- New version 0.10.4 (fix crash upon startup)

* Thu Oct 01 2009 Funda Wang <fwang@mandriva.org> 0.10.3-1mdv2010.0
+ Revision: 451925
- New version 0.10.3

* Wed Feb 25 2009 Frederik Himpe <fhimpe@mandriva.org> 0.10.2-1mdv2009.1
+ Revision: 344939
- Update to new version 0.10.2

* Mon Oct 13 2008 Funda Wang <fwang@mandriva.org> 0.10.1-1mdv2009.1
+ Revision: 293065
- New version 0.10.1

* Sat Aug 30 2008 Frederik Himpe <fhimpe@mandriva.org> 0.10.0-1mdv2009.0
+ Revision: 277649
- Update to final 0.10.0 version

* Mon Aug 11 2008 Funda Wang <fwang@mandriva.org> 0.10.0-0.rc.1mdv2009.0
+ Revision: 270668
- New version 0.10.0 rc
- smb4kdialogs becomes non-versioned

* Fri Jul 25 2008 Funda Wang <fwang@mandriva.org> 0.10.0-0.beta2.1mdv2009.0
+ Revision: 248414
- add icon files
- add patch to fix doc install
- 0.10.0 beta2

* Sun Jul 06 2008 Funda Wang <fwang@mandriva.org> 0.10.0-0.beta1.1mdv2009.0
+ Revision: 232238
- New version 0.10.0 beta 1

* Mon Jun 23 2008 Funda Wang <fwang@mandriva.org> 0.10.0-0.alpha.1mdv2009.0
+ Revision: 228080
- New version 0.10.0 alpha ( KDE4 version )

* Sun Jun 15 2008 Funda Wang <fwang@mandriva.org> 0.9.6-1mdv2009.0
+ Revision: 219283
- New version 0.9.6

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Jun 06 2008 Helio Chissini de Castro <helio@mandriva.com> 0.9.5-2mdv2009.0
+ Revision: 216542
- kde 3 application. kde 3 based. Goes to /opt

* Fri Jun 06 2008 Funda Wang <fwang@mandriva.org> 0.9.5-1mdv2009.0
+ Revision: 216483
- New version 0.9.5

* Thu May 08 2008 Helio Chissini de Castro <helio@mandriva.com> 0.9.4-2mdv2009.0
+ Revision: 204610
- Move for new kde3 path

  + Funda Wang <fwang@mandriva.org>
    - fix file list
    - New version 0.9.4

* Sun Feb 24 2008 Funda Wang <fwang@mandriva.org> 0.9.3-1mdv2008.1
+ Revision: 174267
- New version 0.9.3

* Sun Jan 20 2008 Funda Wang <fwang@mandriva.org> 0.9.2-1mdv2008.1
+ Revision: 155292
- New version 0.9.2

  + Thierry Vignaud <tv@mandriva.org>
    - fix description

* Tue Jan 01 2008 Funda Wang <fwang@mandriva.org> 0.9.1-2mdv2008.1
+ Revision: 139977
- move *.la into main pacakge
- finally move libsmb4kdialogs.la into main package (bug#36435)

* Mon Dec 31 2007 Funda Wang <fwang@mandriva.org> 0.9.1-1mdv2008.1
+ Revision: 139764
- New version 0.9.1

* Sat Dec 29 2007 Funda Wang <fwang@mandriva.org> 0.9.0-3mdv2008.1
+ Revision: 139066
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Dec 21 2007 Funda Wang <fwang@mandriva.org> 0.9.0-2mdv2008.1
+ Revision: 136273
- move libsmb4kdialogs.so into main package

* Tue Dec 18 2007 Funda Wang <fwang@mandriva.org> 0.9.0-1mdv2008.1
+ Revision: 131995
- obsoletes old devel name
- obsoletes old lib and devel package
- New version 0.9.0
- drop libname as it is useless for standalone application

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 28 2007 Funda Wang <fwang@mandriva.org> 0.8.7-1mdv2008.1
+ Revision: 113709
- New version 0.8.7

* Wed Oct 17 2007 Funda Wang <fwang@mandriva.org> 0.8.6-1mdv2008.1
+ Revision: 99494
- New version 0.8.6

* Mon Oct 15 2007 Funda Wang <fwang@mandriva.org> 0.8.5-1mdv2008.1
+ Revision: 98366
- New version 0.8.5

* Wed Aug 29 2007 Funda Wang <fwang@mandriva.org> 0.8.4-2mdv2008.0
+ Revision: 73530
- fix menu category -> Only Network/FileTransfer now.

  + Anssi Hannula <anssi@mandriva.org>
    - drop hardcoded packager tag

* Mon Jul 16 2007 Funda Wang <fwang@mandriva.org> 0.8.4-1mdv2008.0
+ Revision: 52398
- New version

* Thu May 03 2007 Laurent Montel <lmontel@mandriva.org> 0.8.3-1mdv2008.0
+ Revision: 20865
- 0.8.3

