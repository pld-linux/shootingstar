Summary:	Shooting game
Summary(pl):	Strzelanka
Name:		shootingstar
Version:	1.2.0
Release:	2
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://www.2ndpoint.fi/ss/%{name}-%{version}.tar.gz
# Source0-md5:	6cd6e11ec00be95a0a5b5e4cd3649ace
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-gcc34.patch
URL:		http://www.2ndpoint.fi/ss/
BuildRequires:	OpenGL-devel 
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	SDL_image-devel >= 1.2
BuildRequires:	SDL_mixer-devel >= 1.2
BuildRequires:	automake
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Shooting Star is a 2D action game. The goal is to clear all levels of
bad guys and make the World a better place.

%description -l pl
Shooting Star jest dwuwymiarow± gr± akcji, której celem jest
oczyszczenie wszystkich poziomów ze z³ych postaci i sprawienie by
¦wiat sta³ siê lepszym miejscem.

%prep
%setup -q
%patch0 -p1

%build
%configure
cp -f /usr/share/automake/config.sub .
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
