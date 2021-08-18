Summary:	MATE Desktop backgrounds
Summary(pl.UTF-8):	Tła dla środowiska MATE Desktop
Name:		mate-backgrounds
Version:	1.26.0
Release:	1
License:	GPL v2+
Group:		Themes
Source0:	https://pub.mate-desktop.org/releases/1.26/%{name}-%{version}.tar.xz
# Source0-md5:	a078977e9be2f2b9121a0df9cf8b157d
URL:		http://mate-desktop.org/
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	meson >= 0.41.0
BuildRequires:	mate-common
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
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
%meson build
%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{frp,ie,ku_IQ}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/mate-background-properties
%{_datadir}/backgrounds/mate
