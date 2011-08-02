%define		_state		stable
%define		qtver		4.7.3

Name:		kruler
Version:	4.7.0
Release:	0.1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	882e82f9d5a934663401d8f3349da8cd
Summary:	KRuler
Summary(pl.UTF-8):	Linijka dla KDE
Summary(pt_BR.UTF-8):	Régua de pixels para a tela
Group:		X11/Applications/Graphics
URL:		http://www.kde.org/
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libgphoto2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	perl
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	xorg-lib-libX11-devel
Requires:	kde4-kdebase >= %{version}
Requires:	kde4-kdebase >= %{version}
Obsoletes:	kde4-kdegraphics-kruler
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
%setup -q

%build
install -d build
cd build
%cmake \
	-DGWENVIEW_SEMANTICINFO_BACKEND=Nepomuk \
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