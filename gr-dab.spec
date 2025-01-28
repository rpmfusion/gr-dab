#%%global git_commit a33609bd75192878f9f60c1a9b02fd7473649160
#%%global git_date 20180925

#%%global git_short_commit %%(echo %%{git_commit} | cut -c -8)
#%%global git_suffix %%{git_date}git%%{git_short_commit}

Name:          gr-dab
URL:           https://github.com/andrmuel/gr-dab
Version:       0.5
Release:       2%{?dist}
License:       GPLv3+
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: python3-devel
BuildRequires: python3-scipy
BuildRequires: gnuradio-devel
BuildRequires: python3-matplotlib
BuildRequires: cppunit-devel
BuildRequires: boost-devel
# Takes to long to complete
#BuildRequires: doxygen
BuildRequires: ghostscript
BuildRequires: fftw-devel
BuildRequires: pybind11-devel
BuildRequires: faad2-devel
BuildRequires: findutils
BuildRequires: texlive-latex
BuildRequires: texlive-dvips
BuildRequires: python3-mako
BuildRequires: texlive-newunicodechar
BuildRequires: log4cpp-devel
BuildRequires: gmp-devel
BuildRequires: orc-devel
BuildRequires: libunwind-devel
BuildRequires: libsndfile-devel
BuildRequires: spdlog-devel
Requires:      python3-scipy
Requires:      python3-matplotlib
Summary:       GNU Radio DAB digital audio broadcasting module
Source0:       %{url}/archive/%{version}/%{name}-%{version}.tar.gz

%description
GNU Radio DAB digital audio broadcasting module.

%package devel
Summary:          Development files for gr-dab
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for gr-dab.

#%%package doc
#Summary:          Documentation files for gr-dab
#Requires:         %%{name} = %%{version}-%%{release}
# doxygen bug workaround
#BuildArch:        noarch

#%%description doc
#Documentation files for gr-dab.

%prep
%autosetup -p1

%build
%cmake -DENABLE_DOXYGEN=OFF
%cmake_build

%install
%cmake_install

# remove hashbangs
pushd %{buildroot}%{python3_sitearch}/gnuradio
find . -type f -exec sed -i '/^[ \t]*#!\/usr\/bin\/\(env\|python\)/ d' {} \;
popd

%check
cd %{_vpath_builddir}
make test

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS README.md THANKS
%{_datadir}/gnuradio/grc/blocks/*
%{_libdir}/libgnuradio-dab.so.3.*
%{python3_sitearch}/gnuradio/
%{_bindir}/*

%files devel
%{_includedir}/dab
%{_libdir}/*.so
%{_libdir}/cmake/gnuradio-dab/

#%%files doc
#%%doc %%{_docdir}/%%{name}/html
#%%doc %%{_docdir}/%%{name}/xml

%changelog
* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Sep 01 2024 Leigh Scott <leigh123linux@gmail.com> - 0.5-1
- Update to 0.5

* Thu Jun 13 2024 Leigh Scott <leigh123linux@gmail.com> - 0.4-20
- Rebuilt for Python 3.13

* Sat Feb 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 11 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4-18
- Rebuilt for new volk

* Wed Nov 08 2023 Leigh Scott <leigh123linux@gmail.com> - 0.4-17
- Rebuild for new faad2 version

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Leigh Scott <leigh123linux@gmail.com> - 0.4-15
- Rebuilt for Python 3.12

* Wed Feb 08 2023 Leigh Scott <leigh123linux@gmail.com> - 0.4-14
- rebuilt

* Thu Jan 19 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4-13
- Dropped empty doc subpackage
- Rebuilt for new volk

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Sat Jun 25 2022 Robert-André Mauchin <zebob.m@gmail.com> - 0.4-11
- Rebuilt for Python 3.11

* Mon Feb 07 2022 Leigh Scott <leigh123linux@gmail.com> - 0.4-10
- Rebuild for libgnuradio

* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Leigh Scott <leigh123linux@gmail.com> - 0.4-8
- Rebuild for python-3.10

* Wed Feb 24 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4-7
- Added support for gnuradio-3.9 (experimental, untested)

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 28 2020 Leigh Scott <leigh123linux@gmail.com> - 0.4-5
- Rebuilt for new gnuradio

* Mon Aug 24 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4-4
- Rebuilt for new gnuradio

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4-1
- New version
- Switched to Python 3

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.3-3
- Temporaly disabled tests (https://github.com/andrmuel/gr-dab/issues/21)

* Fri May 17 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.3-2
- Enabled tests

* Wed May  1 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.3-1
- New version
- Dropped libdir, install-apps, and traceback-fix patches

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.1-3.20180925gita33609bd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 26 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.1-2.20180925gita33609bd
- Fixed issues found by review

* Tue Sep 25 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.1-1.20180925gita33609bd
- Initial version
