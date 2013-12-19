Summary:	MATE Desktop backgrounds
Summary(pl.UTF-8):	Tła dla środowiska MATE Desktop
Name:		mate-backgrounds
Version:	1.6.0
Release:	1
License:	GPL v2+
Group:		Themes
Source0:	http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz
# Source0-md5:	b05ee6b9ef8faecb3fe95140526569cb
URL:		http://mate-desktop.org/
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
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
