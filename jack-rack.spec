Summary:	Stereo LADSPA effects rack.
Summary(pl):	Stereofoniczny rack efektów LADSPA.
Name:		jack-rack
Version:	1.4.1
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://pkl.net/~node/software/%{name}-%{version}.tar.gz
Patch0:		jack-rack-desktop.patch
URL:		http://pkl.net/~node/jack-rack.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	ladspa-devel >= 1.1
BuildRequires:	libxml2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	pkgconfig
Requires:	jack-patch-bay
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JACK Rack is a stereo LADSPA effects rack for the JACK audio API. It
uses GTK+ 2 (and optionally GNOME 2) for the gui.

%description -l pl
JACK Rack jest stereofonicznym rackiem efektów LADSPA dla API JACK. 
U¿ywa GUI opartego na GTK+ 2.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
    --disable-lrdf \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc NEWS AUTHORS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%attr(755,root,root) %{_datadir}/dtds/*.dtd
%{_pixmapsdir}/*.png
