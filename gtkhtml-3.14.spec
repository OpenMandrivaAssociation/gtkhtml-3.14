%define url_ver %(echo %{version}|cut -d. -f1,2)

%define oname	gtkhtml
%define api	3.14
%define major	19
%define majeditor	0
%define libname %mklibname %{oname} %{api} %{major}
%define libeditor %mklibname %{oname}-editor %{api} %{majeditor}
%define devname %mklibname -d %{oname} %{api}

Summary:	HTML rendering/editing library
Name:		%{oname}%{api}
Version:	3.32.2
Release:	11
License:	LGPLv2+
Group:		Graphical desktop/GNOME
Url:		http://ftp.gnome.org/pub/gnome/sources/gtkhtml/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtkhtml/%{url_ver}/%{oname}-%{version}.tar.bz2
Patch0:		gtkhtml-3.32.2-fix-linking.patch

BuildRequires:	gnome-icon-theme >= 1.2.0
BuildRequires:	intltool
BuildRequires:	iso-codes
BuildRequires:	pkgconfig(enchant)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gail)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libsoup-2.4)
Requires:	%{libname} >= %{version}
### MD TODO rename src pkg directory
Obsoletes:	gtkhtml-3.14 < 3.32.2-6

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
Suggests:	%{name} = %{version}-%{release}
Obsoletes:	%{_lib}gtkhtml-3.14_19 < 3.32.2-6

%description -n %{libname}
This package contains libraries used by GtkHTML.

%package -n %{libeditor}
Summary:	Libraries for GtkHTML
Group:		System/Libraries
Suggests:	%{name} = %{version}-%{release}
Conflicts:	%{_lib}gtkhtml-3.14_19 < 3.32.2-6

%description -n %{libeditor}
This package contains libraries used by GtkHTML.

%package -n %{devname}
Summary:	Development libraries, header files and utilities for GtkHTML
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}-%{release}
Requires:	%{libname} = %{version}
Requires:	%{libeditor} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}gtkhtml-3.14-devel < 3.32.2-6

%description -n %{devname}
This package contains the files necessary to develop applications with GtkHTML.

%prep
%setup -qn %{oname}-%{version}
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
#rm -rf %{buildroot}%{_datadir}/locale/{bn_IN,si}

%find_lang %{oname}-%{api}

%files -f %{oname}-%{api}.lang
%doc AUTHORS NEWS README TODO
%{_datadir}/gtkhtml-%{api}

%files -n %{libname}
%{_libdir}/libgtkhtml-%{api}.so.%{major}*

%files -n %{libeditor}
%{_libdir}/libgtkhtml-editor-%{api}.so.%{majeditor}*

%files -n %{devname}
%doc ChangeLog COPYING
%_bindir/gtkhtml-editor-test
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

