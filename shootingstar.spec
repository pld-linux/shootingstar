Summary:	Shooting game
Summary(pl):	Strzelanina
Name:		shootingstar
Version:	1.2.0
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.2ndpoint.fi/ss/%{name}-%{version}.tar.gz
# Source0-md5:	6cd6e11ec00be95a0a5b5e4cd3649ace
#Source1:	%{name}.desktop
URL:		http://www.2ndpoint.fi/ss/
BuildRequires:	OpenGL-devel 
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	SDL_image-devel >= 1.2
BuildRequires:	SDL_mixer-devel >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shooting Star is a 2D action game. The goal is to clear all levels of
bad guys and make the World a better place.

%description -l pl
Shooting Star jest dwu wymiarow± gr± akcji, której celem jest
oczyszczenie wszystkich poziomów ze z³ych postaci i sprawienie by
¦wiat sta³ siê lepszym miejscem.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
