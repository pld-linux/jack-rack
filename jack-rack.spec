#
# Conditional build:
# _without_gnome	- disable GNOME2 support
Summary:	Stereo LADSPA effects rack
Summary(pl):	Stereofoniczny rack efektów LADSPA
Name:		jack-rack
Version:	1.4.2
Release:	0.1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://pkl.net/~node/software/%{name}-%{version}.tar.gz
# Source0-md5:	4b7f0ab02495b8cd7b865cad5776d885
Patch0:		%{name}-desktop.patch
URL:		http://pkl.net/~node/jack-rack.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	jack-audio-connection-kit-devel >= 0.50.0
BuildRequires:	ladspa-devel >= 1.1
%{!?_without_gnome:BuildRequires:	libgnomeui >= 2.0}
BuildRequires:	liblrdf-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
Requires:	jack-patch-bay
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JACK Rack is a stereo LADSPA effects rack for the JACK audio API. It
uses GTK+ 2 (and optionally GNOME 2) for the GUI.

%description -l pl
JACK Rack jest rackiem stereofonicznych efektów LADSPA dla API
d¼wiêkowego JACK. U¿ywa GUI opartego na GTK+ 2 (i opcjonalnie GNOME2).

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
	%{?_without_gnome:--disable-gnome}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
