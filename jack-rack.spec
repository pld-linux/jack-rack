#
# Conditional build:
%bcond_without	gnome	# disable GNOME2 support
%bcond_with	ladcca	# enable ladcca sesion managment support
#
Summary:	Stereo LADSPA effects rack
Summary(pl.UTF-8):   Rack stereofonicznych efektów LADSPA
Name:		jack-rack
Version:	1.4.4
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/jack-rack/%{name}-%{version}.tar.bz2
# Source0-md5:	99f10d81e9504929c3f897d40f344fdc
Patch0:		%{name}-desktop.patch
URL:		http://jack-rack.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	jack-audio-connection-kit-devel >= 0.50.0
%{?with_ladcca:BuildRequires:	ladcca-devel >= 0.3.1}
BuildRequires:	ladspa-devel >= 1.1
%{?with_gnome:BuildRequires:	libgnomeui-devel >= 2.0}
BuildRequires:	libraptor-devel
BuildRequires:	liblrdf-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
Requires:	jack-patch-bay
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JACK Rack is a stereo LADSPA effects rack for the JACK audio API. It
uses GTK+ 2 (and optionally GNOME 2) for the GUI.

%description -l pl.UTF-8
JACK Rack jest rackiem stereofonicznych efektów LADSPA dla API
dźwiękowego JACK-a. Używa GUI opartego na GTK+ 2 (i opcjonalnie
GNOME2).

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_gnome: --disable-gnome} \
	%{!?with_ladcca: --disable-ladcca}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
# it seems to be the only package using this dir(?)
%dir %{_datadir}/dtds
%{_datadir}/dtds/*.dtd
%{_pixmapsdir}/*.png
