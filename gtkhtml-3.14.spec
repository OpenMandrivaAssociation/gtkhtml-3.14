%define major	19
%define package_name gtkhtml
%define api_version 3.14
%define lib_name %mklibname %{package_name}- %{api_version} %{major}

Summary:	GtkHTML is a HTML rendering/editing library
Name:		%{package_name}-%{api_version}
Version: 3.15.5
Release: %mkrel 1
License:	LGPL
Group:		Graphical desktop/GNOME
Source0: http://ftp.gnome.org/pub/GNOME/sources/gtkhtml/%{package_name}-%{version}.tar.bz2

URL:		http://ftp.gnome.org/pub/gnome/sources/gtkhtml/
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	libgnomeui2-devel
BuildRequires:	gail-devel
BuildRequires:	libglade2.0-devel
BuildRequires:	libgnomeprintui-devel >= 2.7.0
BuildRequires:	libsoup-devel >= 2.1.6
BuildRequires:	gnome-icon-theme >= 1.2.0
BuildRequires:	perl-XML-Parser
Requires:	%{lib_name} >= %{version}


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

%package -n %{lib_name}
Summary:        Libraries for GtkHTML
Group:          System/Libraries

%description -n %{lib_name}
GtkHTML is a HTML rendering/editing library.  GtkHTML is
not designed to be the ultimate HTML browser/editor: instead, it is
designed to be easily embedded into applications that require
lightweight HTML functionality.

This package contains libraries used by GtkHTML.

%package -n %{lib_name}-devel
Summary:        Development libraries, header files and utilities for GtkHTML
Group:          Development/GNOME and GTK+
Requires:	%{name} = %{version}
Requires:       %{lib_name} = %{version}
Provides:	lib%{package_name}-%{api_version}-devel = %{version}-%{release}
Conflicts: %mklibname -d gtkhtml-3.8 15 

%description -n %{lib_name}-devel
GtkHTML is a HTML rendering/editing library.  GtkHTML is
not designed to be the ultimate HTML browser/editor: instead, it is
designed to be easily embedded into applications that require
lightweight HTML functionality.

This package contains the files necessary to develop applications with GtkHTML.

%prep
%setup -q -n %{package_name}-%{version}

%build

%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%{find_lang} %{package_name}-%{api_version}

# remove unpackaged files
rm -f $RPM_BUILD_ROOT%{_libdir}/bonobo/plugin/*.{la,a}  \
 $RPM_BUILD_ROOT%{_libdir}/gtkhtml/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig -n %{lib_name}
%postun -p /sbin/ldconfig -n %{lib_name}

%files -f %{package_name}-%{api_version}.lang -n %{name}
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/gtkhtml
%{_libdir}/bonobo/servers/*
%{_datadir}/gtkhtml-%{api_version}

%files -n %{lib_name}
%defattr(-, root, root)
%doc AUTHORS COPYING 
%{_libdir}/libgtkhtml-%{api_version}.so.%{major}*

%files -n %{lib_name}-devel
%defattr(-, root, root)
%attr(644,root,root) %{_libdir}/*a
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
