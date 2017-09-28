%global commit b3653d44f6ecff05fbf49b49076d9a57e479268f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global owner seandepagnier
%global project statusbar_pi
%global plugin statusbar

Name: opencpn-plugin-%{plugin}
Summary: Status bar plugin for OpenCPN
Version: 0.0
Release: 0.1.%{shortcommit}%{?dist}
License: GPLv2+

Source0: https://github.com/%{owner}/%{project}/archive/%{commit}/%{project}-%{shortcommit}.tar.gz

BuildRequires: bzip2-devel
BuildRequires: cmake
BuildRequires: gettext
BuildRequires: tinyxml-devel
BuildRequires: wxGTK3-devel
BuildRequires: zlib-devel

Requires: opencpn%{_isa}
Supplements: opencpn%{_isa}
Requires: opencpn-plugin-route%{_isa}

%description
The built-in status bar in OpenCPN is very limited in its
configuration options and can be difficult to read. This plugin
replaces it with a more configurable one. For best results, you should
disable the built-in toolbar on the User Interface tab in the Toolbox
and set the Y position of the plugin toolbar to at least the pixel
size of the font selected in the plugin preferences.

%prep
%autosetup -n %{project}-%{commit}

sed -i -e s'/SET(PREFIX_LIB lib)/SET(PREFIX_LIB %{_lib})/' cmake/PluginInstall.cmake

mkdir build

%build

cd build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF ..
%make_build

%install

cd build
mkdir -p %{buildroot}%{_bindir}
%make_install

%find_lang opencpn-%{plugin}_pi

%files -f build/opencpn-%{plugin}_pi.lang

%{_libdir}/opencpn/lib%{plugin}_pi.so
