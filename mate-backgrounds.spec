Summary:	MATE Desktop backgrounds
Name:		mate-backgrounds
Version:	1.5.0
Release:	1
License:	GPL v2+
Group:		Themes
Source0:	http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
# Source0-md5:	c385a3151b19e46e3bdd8b0ab0cd18ab
URL:		http://mate-desktop.org/
BuildRequires:	mate-common
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Backgrounds for MATE Desktop.

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure
%{__make} \
	V=1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%{_datadir}/mate-background-properties
%{_pixmapsdir}/backgrounds/mate

# XXX packaged also by libgnome-2.32.1-1.i686
%dir %{_pixmapsdir}/backgrounds
