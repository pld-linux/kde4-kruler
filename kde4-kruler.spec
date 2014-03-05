%define		_state		stable
%define		orgname		kruler
%define		qtver		4.8.0

Name:		kde4-kruler
Version:	4.12.3
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	3a420c40d9f9c02d79d6b2017bff5374
Summary:	KRuler
Summary(pl.UTF-8):	Linijka dla KDE
Summary(pt_BR.UTF-8):	Régua de pixels para a tela
Group:		X11/Applications/Graphics
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	xorg-lib-libX11-devel
Requires:	kde4-kdebase >= %{version}
Obsoletes:	kde4-kdegraphics-kruler < 4.6.99
Obsoletes:	kruler <= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KRuler is a very simple application, with only one aim in life. To
measure distances on your screen.

%description -l pl.UTF-8
KRuler jest prostą aplikacją, z tylko jednym celem w życiu: mierzenie
odległości na ekranie.

%description -l pt_BR.UTF-8
Régua de pixels para a tela.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kruler
%{_datadir}/apps/kruler
%{_desktopdir}/kde4/kruler.desktop
%{_iconsdir}/*/*/apps/kruler.*
%{_kdedocdir}/en/kruler
%{_iconsdir}/*/*/actions/kruler*
