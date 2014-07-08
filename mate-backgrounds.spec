Summary:	MATE Desktop backgrounds
Summary(pl.UTF-8):	Tła dla środowiska MATE Desktop
Name:		mate-backgrounds
Version:	1.8.0
Release:	1
License:	GPL v2+
Group:		Themes
Source0:	http://pub.mate-desktop.org/releases/1.8/%{name}-%{version}.tar.xz
# Source0-md5:	1b6adb6f732941afbf8f0f722b361fe4
URL:		http://mate-desktop.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel >= 0.10.40
BuildRequires:	intltool >= 0.35.0
BuildRequires:	mate-common
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Background images and data for MATE Desktop. The MATE backgrounds are
a fork of GNOME backgrounds.

%description -l pl.UTF-8
Obrazy i dane teł dla środowiska MATE Desktop. MATE backgrounds to
odgałęzienie GNOME backgrounds.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

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
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/mate-background-properties
%{_datadir}/backgrounds/mate
