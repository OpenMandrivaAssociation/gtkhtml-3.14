%define major	19
%define package_name gtkhtml
%define api_version 3.14
%define libname %mklibname %{package_name}- %{api_version} %{major}
%define libnamedev %mklibname -d %{package_name}- %{api_version}

Summary:	HTML rendering/editing library
Name:		%{package_name}-%{api_version}
Version: 3.32.2
Release: %mkrel 4
License:	LGPLv2+
Group:		Graphical desktop/GNOME
Source0: http://ftp.gnome.org/pub/GNOME/sources/gtkhtml/%{package_name}-%{version}.tar.bz2

URL:		http://ftp.gnome.org/pub/gnome/sources/gtkhtml/
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	gail-devel
BuildRequires:	gtk+2-devel
#BuildRequires:	glade3-devel
BuildRequires:	libsoup-devel >= 2.1.6
BuildRequires:	iso-codes
BuildRequires:	enchant-devel
BuildRequires:	gnome-icon-theme >= 1.2.0
BuildRequires:	intltool
BuildRequires:	libGConf2-devel GConf2
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
Summary:        Libraries for GtkHTML
Group:          System/Libraries

%description -n %{libname}
GtkHTML is a HTML rendering/editing library.  GtkHTML is
not designed to be the ultimate HTML browser/editor: instead, it is
designed to be easily embedded into applications that require
lightweight HTML functionality.

This package contains libraries used by GtkHTML.

%package -n %{libnamedev}
Summary:        Development libraries, header files and utilities for GtkHTML
Group:          Development/GNOME and GTK+
Requires:	%{name} = %{version}
Requires:       %{libname} = %{version}
Provides:	%{package_name}-%{api_version}-devel = %{version}-%{release}
Conflicts: %mklibname -d gtkhtml-3.8 15 
Obsoletes: %mklibname -d %{package_name}- 3.14 19

%description -n %{libnamedev}
GtkHTML is a HTML rendering/editing library.  GtkHTML is
not designed to be the ultimate HTML browser/editor: instead, it is
designed to be easily embedded into applications that require
lightweight HTML functionality.

This package contains the files necessary to develop applications with GtkHTML.

%prep
%setup -q -n %{package_name}-%{version}

%build
%configure2_5x --enable-deprecated-warning-flags=no
%make LIBS=-lm

%install
rm -rf %{buildroot}

%makeinstall_std

# gw these produce rpmlint errors:
rm -rf %buildroot%_datadir/locale/{bn_IN,si}
%{find_lang} %{package_name}-%{api_version}

# remove unpackaged files
rm -f %{buildroot}%{_libdir}/bonobo/plugin/*.{la,a}  \
 %{buildroot}%{_libdir}/gtkhtml/*.{la,a} %{_libdir}/*.la

%clean
rm -rf %{buildroot}

%files -f %{package_name}-%{api_version}.lang -n %{name}
%defattr(-, root, root)
%doc AUTHORS NEWS README TODO
%{_datadir}/gtkhtml-%{api_version}

%files -n %{libname}
%defattr(-, root, root)
%doc AUTHORS COPYING 
%{_libdir}/libgtkhtml-%{api_version}.so.%{major}*
%{_libdir}/libgtkhtml-editor-%{api_version}.so.0*

%files -n %{libnamedev}
%defattr(-, root, root)
%doc ChangeLog 
%attr(644,root,root) %{_libdir}/*a
%_bindir/gtkhtml-editor-test
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
