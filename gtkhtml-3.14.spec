%define major 19
%define package_name gtkhtml
%define api_version 3.14
%define libname %mklibname %{package_name}- %{api_version} %{major}
%define libnamedev %mklibname -d %{package_name}- %{api_version}

Summary:	HTML rendering/editing library
Name:		%{package_name}-%{api_version}
Version:	3.32.2
Release:	5
License:	LGPLv2+
Group:		Graphical desktop/GNOME
URL:		http://ftp.gnome.org/pub/gnome/sources/gtkhtml/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtkhtml/%{package_name}-%{version}.tar.bz2
Patch0:		gtkhtml-3.32.2-fix-linking.patch
BuildRequires:	pkgconfig(gail)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	iso-codes
BuildRequires:	pkgconfig(enchant)
BuildRequires:	gnome-icon-theme >= 1.2.0
BuildRequires:	intltool
BuildRequires:	pkgconfig(gconf-2.0) GConf2
Requires:	%{libname} >= %{version}


%description 
GtkHTML is a HTML rendering/editing library.  GtkHTML is
not designed to be the ultimate HTML browser/editor: instead, it is
designed to be easily embedded into applications that require
lightweight HTML functionality.

GtkHTML was originally based on KDE's KHTMLW widget, but is now
developed independently of it.  The most important difference between
KHTMLW and GtkHTML, besides being GTK-based, is that GtkHTML is also
an editor.  Thanks to the Bonobo editor component that comes with the
library, it's extremely simple to add HTML editing to an existing
application.

%package -n %{libname}
Summary:	Libraries for GtkHTML
Group:		System/Libraries

%description -n %{libname}
GtkHTML is a HTML rendering/editing library.  GtkHTML is
not designed to be the ultimate HTML browser/editor: instead, it is
designed to be easily embedded into applications that require
lightweight HTML functionality.

This package contains libraries used by GtkHTML.

%package -n %{libnamedev}
Summary:	Development libraries, header files and utilities for GtkHTML
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}
Requires:	%{libname} = %{version}
Provides:	%{package_name}-%{api_version}-devel = %{version}-%{release}
Conflicts:	%{mklibname -d gtkhtml-3.8 15} < 3.32.2-5
Obsoletes:	%{mklibname -d gtkhtml- 3.14 19} < 3.32.2-5

%description -n %{libnamedev}
GtkHTML is a HTML rendering/editing library.  GtkHTML is
not designed to be the ultimate HTML browser/editor: instead, it is
designed to be easily embedded into applications that require
lightweight HTML functionality.

This package contains the files necessary to develop applications with GtkHTML.

%prep
%setup -q -n %{package_name}-%{version}
%apply_patches
autoreconf -fi

%build
%configure2_5x \
	--enable-deprecated-warning-flags=no \
	--disable-static
%make LIBS=-lm

%install
%makeinstall_std

# gw these produce rpmlint errors:
rm -rf %{buildroot}%{_datadir}/locale/{bn_IN,si}

%find_lang %{package_name}-%{api_version}

%files -f %{package_name}-%{api_version}.lang -n %{name}
%doc AUTHORS NEWS README TODO
%{_datadir}/gtkhtml-%{api_version}

%files -n %{libname}
%doc AUTHORS COPYING
%{_libdir}/libgtkhtml-%{api_version}.so.%{major}*
%{_libdir}/libgtkhtml-editor-%{api_version}.so.0*

%files -n %{libnamedev}
%doc ChangeLog
%_bindir/gtkhtml-editor-test
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*


%changelog
* Thu Dec 15 2011 Götz Waschk <waschk@mandriva.org> 3.32.2-4mdv2012.0
+ Revision: 741502
- really remove libtool archives
- fix linking
- remove libtool archives

* Tue May 24 2011 Funda Wang <fwang@mandriva.org> 3.32.2-3
+ Revision: 678060
- br gconf

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild
    - mass rebuild

* Sun Feb 06 2011 Götz Waschk <waschk@mandriva.org> 3.32.2-1
+ Revision: 636458
- update to new version 3.32.2

* Mon Nov 15 2010 Götz Waschk <waschk@mandriva.org> 3.32.1-1mdv2011.0
+ Revision: 597724
- update to new version 3.32.1

* Mon Sep 27 2010 Götz Waschk <waschk@mandriva.org> 3.32.0-1mdv2011.0
+ Revision: 581340
- update to new version 3.32.0

* Mon Sep 13 2010 Götz Waschk <waschk@mandriva.org> 3.31.92-1mdv2011.0
+ Revision: 577911
- update to new version 3.31.92

* Mon Aug 30 2010 Götz Waschk <waschk@mandriva.org> 3.31.91-1mdv2011.0
+ Revision: 574283
- new version
- build with deprecated symbols

* Mon Aug 16 2010 Götz Waschk <waschk@mandriva.org> 3.31.90-1mdv2011.0
+ Revision: 570425
- update to new version 3.31.90

* Tue Aug 03 2010 Götz Waschk <waschk@mandriva.org> 3.31.6-1mdv2011.0
+ Revision: 565414
- update to new version 3.31.6

* Fri Jul 30 2010 Götz Waschk <waschk@mandriva.org> 3.31.5-1mdv2011.0
+ Revision: 563363
- new version
- update build deps
- update file list

* Mon Jun 21 2010 Frederic Crozat <fcrozat@mandriva.com> 3.30.2-1mdv2010.1
+ Revision: 548380
- Release 3.30.2

* Wed Apr 28 2010 Christophe Fergeau <cfergeau@mandriva.com> 3.30.1-2mdv2010.1
+ Revision: 540034
- rebuild so that shared libraries are properly stripped again

* Mon Apr 26 2010 Götz Waschk <waschk@mandriva.org> 3.30.1-1mdv2010.1
+ Revision: 538833
- update to new version 3.30.1

* Mon Mar 29 2010 Götz Waschk <waschk@mandriva.org> 3.30.0-1mdv2010.1
+ Revision: 528929
- update to new version 3.30.0

* Wed Mar 10 2010 Götz Waschk <waschk@mandriva.org> 3.29.92.1-1mdv2010.1
+ Revision: 517417
- update to new version 3.29.92.1

* Mon Mar 08 2010 Götz Waschk <waschk@mandriva.org> 3.29.92-1mdv2010.1
+ Revision: 515649
- update to new version 3.29.92

* Mon Feb 22 2010 Götz Waschk <waschk@mandriva.org> 3.29.91-1mdv2010.1
+ Revision: 509580
- update to new version 3.29.91

* Mon Feb 08 2010 Götz Waschk <waschk@mandriva.org> 3.29.90-1mdv2010.1
+ Revision: 502038
- update to new version 3.29.90

* Mon Jan 25 2010 Götz Waschk <waschk@mandriva.org> 3.29.6-1mdv2010.1
+ Revision: 495886
- update to new version 3.29.6

* Mon Jan 11 2010 Götz Waschk <waschk@mandriva.org> 3.29.5-1mdv2010.1
+ Revision: 489883
- update to new version 3.29.5

* Mon Dec 21 2009 Götz Waschk <waschk@mandriva.org> 3.29.4-1mdv2010.1
+ Revision: 480865
- update to new version 3.29.4

* Wed Dec 09 2009 Götz Waschk <waschk@mandriva.org> 3.29.3-1mdv2010.1
+ Revision: 475382
- update to new version 3.29.3

* Wed Oct 21 2009 Frederic Crozat <fcrozat@mandriva.com> 3.28.1-1mdv2010.0
+ Revision: 458602
- Release 3.28.1
- Fix Buildrequires

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 3.28.0-1mdv2010.0
+ Revision: 446527
- update to new version 3.28.0

* Mon Sep 07 2009 Götz Waschk <waschk@mandriva.org> 3.27.92-1mdv2010.0
+ Revision: 432694
- new version

* Mon Aug 24 2009 Götz Waschk <waschk@mandriva.org> 3.27.91-2mdv2010.0
+ Revision: 420472
- rebuild for missing packages

* Mon Aug 24 2009 Götz Waschk <waschk@mandriva.org> 3.27.91-1mdv2010.0
+ Revision: 420257
- update to new version 3.27.91

* Mon Aug 10 2009 Götz Waschk <waschk@mandriva.org> 3.27.90-1mdv2010.0
+ Revision: 414275
- update to new version 3.27.90

* Mon Jul 27 2009 Götz Waschk <waschk@mandriva.org> 3.27.5-1mdv2010.0
+ Revision: 400549
- update to new version 3.27.5

* Mon Jul 13 2009 Götz Waschk <waschk@mandriva.org> 3.27.4-1mdv2010.0
+ Revision: 395455
- update to new version 3.27.4

* Mon Jun 15 2009 Götz Waschk <waschk@mandriva.org> 3.27.3-1mdv2010.0
+ Revision: 386052
- update to new version 3.27.3

* Mon May 25 2009 Götz Waschk <waschk@mandriva.org> 3.27.2-1mdv2010.0
+ Revision: 379627
- update to new version 3.27.2

* Mon May 11 2009 Götz Waschk <waschk@mandriva.org> 3.27.1-2mdv2010.0
+ Revision: 374373
- rebuild

* Mon May 11 2009 Götz Waschk <waschk@mandriva.org> 3.27.1-1mdv2010.0
+ Revision: 374165
- new version

* Tue Apr 14 2009 Götz Waschk <waschk@mandriva.org> 3.26.1.1-1mdv2009.1
+ Revision: 366919
- new version
- drop patch

* Mon Mar 16 2009 Götz Waschk <waschk@mandriva.org> 3.26.0-1mdv2009.1
+ Revision: 355697
- new version

* Mon Mar 02 2009 Götz Waschk <waschk@mandriva.org> 3.25.92-1mdv2009.1
+ Revision: 347250
- update to new version 3.25.92

* Mon Feb 16 2009 Götz Waschk <waschk@mandriva.org> 3.25.91-1mdv2009.1
+ Revision: 340935
- update to new version 3.25.91

* Mon Feb 02 2009 Götz Waschk <waschk@mandriva.org> 3.25.90-1mdv2009.1
+ Revision: 336492
- update to new version 3.25.90

* Mon Jan 19 2009 Götz Waschk <waschk@mandriva.org> 3.25.5-1mdv2009.1
+ Revision: 331251
- update to new version 3.25.5

* Tue Jan 06 2009 Götz Waschk <waschk@mandriva.org> 3.25.4-1mdv2009.1
+ Revision: 325273
- update to new version 3.25.4

* Fri Dec 19 2008 Götz Waschk <waschk@mandriva.org> 3.25.3-1mdv2009.1
+ Revision: 316145
- new version
- fix build

* Tue Dec 02 2008 Götz Waschk <waschk@mandriva.org> 3.25.2-1mdv2009.1
+ Revision: 309010
- update to new version 3.25.2

* Sun Nov 09 2008 Oden Eriksson <oeriksson@mandriva.com> 3.25.1-2mdv2009.1
+ Revision: 301507
- rebuilt against new libxcb

* Mon Nov 03 2008 Götz Waschk <waschk@mandriva.org> 3.25.1-1mdv2009.1
+ Revision: 299475
- update to new version 3.25.1

* Mon Oct 20 2008 Götz Waschk <waschk@mandriva.org> 3.24.1-1mdv2009.1
+ Revision: 295641
- new version
- update to new version 3.24.1

* Mon Sep 22 2008 Götz Waschk <waschk@mandriva.org> 3.24.0-1mdv2009.0
+ Revision: 286522
- new version

* Mon Sep 08 2008 Götz Waschk <waschk@mandriva.org> 3.23.92-1mdv2009.0
+ Revision: 282512
- new version

* Mon Sep 01 2008 Götz Waschk <waschk@mandriva.org> 3.23.91-1mdv2009.0
+ Revision: 278185
- new version

* Mon Aug 18 2008 Frederic Crozat <fcrozat@mandriva.com> 3.23.90-1mdv2009.0
+ Revision: 273218
- Release 3.23.90
- Remove patch0 (merged upstream)

* Tue Aug 12 2008 Pascal Terjan <pterjan@mandriva.org> 3.23.6-2mdv2009.0
+ Revision: 271076
- Fix a crash in evolution when starting composer in non UTF8 locale

* Mon Aug 04 2008 Götz Waschk <waschk@mandriva.org> 3.23.6-1mdv2009.0
+ Revision: 263138
- new version

* Tue Jul 22 2008 Götz Waschk <waschk@mandriva.org> 3.23.5-1mdv2009.0
+ Revision: 240019
- new version

* Thu Jul 03 2008 Götz Waschk <waschk@mandriva.org> 3.23.4-1mdv2009.0
+ Revision: 230966
- fix buildrequires
- new version
- remove bonobo server
- add gtkhtml-editor library

* Mon Jun 30 2008 Götz Waschk <waschk@mandriva.org> 3.18.3-1mdv2009.0
+ Revision: 230218
- new version
- update license

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue May 27 2008 Götz Waschk <waschk@mandriva.org> 3.18.2-1mdv2009.0
+ Revision: 211715
- fix buildrequires
- new version
- fix build

* Wed Apr 09 2008 Götz Waschk <waschk@mandriva.org> 3.18.1-1mdv2009.0
+ Revision: 192464
- new version

* Mon Mar 10 2008 Götz Waschk <waschk@mandriva.org> 3.18.0-1mdv2008.1
+ Revision: 183285
- new version

* Mon Feb 25 2008 Götz Waschk <waschk@mandriva.org> 3.17.92-1mdv2008.1
+ Revision: 174977
- new version

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 3.17.91-3mdv2008.1
+ Revision: 170881
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Mon Feb 11 2008 Götz Waschk <waschk@mandriva.org> 3.17.91-2mdv2008.1
+ Revision: 165447
- fix installation
- remove locales (bug #12216)
- fix devel provides according to the blino policy
- *** empty log message ***

* Mon Feb 11 2008 Götz Waschk <waschk@mandriva.org> 3.17.91-1mdv2008.1
+ Revision: 165205
- new version

* Tue Jan 29 2008 Götz Waschk <waschk@mandriva.org> 3.17.90.1-1mdv2008.1
+ Revision: 159759
- new version

* Mon Jan 28 2008 Götz Waschk <waschk@mandriva.org> 3.17.90-1mdv2008.1
+ Revision: 159382
- new version

* Mon Jan 14 2008 Götz Waschk <waschk@mandriva.org> 3.17.5-1mdv2008.1
+ Revision: 151328
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Götz Waschk <waschk@mandriva.org> 3.17.4-1mdv2008.1
+ Revision: 129090
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Dec 04 2007 Götz Waschk <waschk@mandriva.org> 3.17.3-1mdv2008.1
+ Revision: 115201
- new version

* Tue Nov 13 2007 Götz Waschk <waschk@mandriva.org> 3.17.2-1mdv2008.1
+ Revision: 108386
- new version

* Mon Oct 29 2007 Götz Waschk <waschk@mandriva.org> 3.17.1-1mdv2008.1
+ Revision: 102945
- new version

* Mon Oct 15 2007 Götz Waschk <waschk@mandriva.org> 3.16.1-1mdv2008.1
+ Revision: 98420
- new version
- new version

* Mon Sep 17 2007 Götz Waschk <waschk@mandriva.org> 3.16.0-1mdv2008.0
+ Revision: 89312
- new version

* Mon Sep 03 2007 Götz Waschk <waschk@mandriva.org> 3.15.92-1mdv2008.0
+ Revision: 78753
- new version

* Mon Aug 27 2007 Götz Waschk <waschk@mandriva.org> 3.15.91-1mdv2008.0
+ Revision: 72032
- new version

* Tue Aug 14 2007 Götz Waschk <waschk@mandriva.org> 3.15.90-1mdv2008.0
+ Revision: 63029
- new version

* Wed Aug 01 2007 Götz Waschk <waschk@mandriva.org> 3.15.6.1-1mdv2008.0
+ Revision: 57658
- new version
- fix buildrequires
- fix build

* Wed Aug 01 2007 Götz Waschk <waschk@mandriva.org> 3.15.6-2mdv2008.0
+ Revision: 57584
- new devel name

* Tue Jul 31 2007 Götz Waschk <waschk@mandriva.org> 3.15.6-1mdv2008.0
+ Revision: 56916
- fix buildrequires
- new version
- fix build

* Mon Jul 09 2007 Götz Waschk <waschk@mandriva.org> 3.15.5-1mdv2008.0
+ Revision: 50636
- new version

* Mon Jun 18 2007 Götz Waschk <waschk@mandriva.org> 3.15.4-1mdv2008.0
+ Revision: 41000
- new version
- new version

  + Anssi Hannula <anssi@mandriva.org>
    - rebuild with correct optflags

* Mon May 28 2007 Götz Waschk <waschk@mandriva.org> 3.14.2-1mdv2008.0
+ Revision: 32134
- new version

* Tue Apr 17 2007 Götz Waschk <waschk@mandriva.org> 3.14.1-1mdv2008.0
+ Revision: 14039
- new version


* Mon Mar 12 2007 Götz Waschk <waschk@mandriva.org> 3.14.0-1mdv2007.1
+ Revision: 142116
- rename

* Mon Feb 26 2007 Götz Waschk <waschk@mandriva.org> 3.13.92-2mdv2007.1
+ Revision: 126094
- fix devel package conflict

* Mon Feb 26 2007 Götz Waschk <waschk@mandriva.org> 3.13.92-1mdv2007.1
+ Revision: 125971
- new version
- new major

* Mon Feb 12 2007 Götz Waschk <waschk@mandriva.org> 3.13.91-1mdv2007.1
+ Revision: 120023
- new version

* Mon Jan 22 2007 Götz Waschk <waschk@mandriva.org> 3.13.6-1mdv2007.1
+ Revision: 112048
- new version

* Tue Dec 19 2006 Götz Waschk <waschk@mandriva.org> 3.13.4-1mdv2007.1
+ Revision: 99061
- new version

* Tue Dec 05 2006 Götz Waschk <waschk@mandriva.org> 3.13.3-1mdv2007.1
+ Revision: 90774
- new version

* Thu Nov 30 2006 Götz Waschk <waschk@mandriva.org> 3.13.2-4mdv2007.1
+ Revision: 89221
- bot rebuild
- fix buildrequires again

* Mon Nov 27 2006 Götz Waschk <waschk@mandriva.org> 3.13.2-2mdv2007.1
+ Revision: 87730
- fix buildrequires
- new version

* Wed Nov 22 2006 Götz Waschk <waschk@mandriva.org> 3.12.2-1mdv2007.1
+ Revision: 86296
- new version
- Import gtkhtml-3.8

