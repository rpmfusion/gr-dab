#%%global git_commit a33609bd75192878f9f60c1a9b02fd7473649160
#%%global git_date 20180925

#%%global git_short_commit %%(echo %%{git_commit} | cut -c -8)
#%%global git_suffix %%{git_date}git%%{git_short_commit}

Name:          gr-dab
URL:           https://github.com/andrmuel/gr-dab
Version:       0.4
Release:       7%{?dist}
License:       GPLv3+
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: python3-devel
BuildRequires: python3-scipy
BuildRequires: gnuradio-devel
BuildRequires: python3-matplotlib
BuildRequires: cppunit-devel
BuildRequires: boost-devel
BuildRequires: doxygen
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
Requires:      python3-scipy
Requires:      python3-matplotlib
Summary:       GNU Radio DAB digital audio broadcasting module
Source0:       %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# https://github.com/andrmuel/gr-dab/issues/28
# experimental and untested downstream patch
Patch0:        gr-dab-0.4-gnuradio39.patch

%description
GNU Radio DAB digital audio broadcasting module.

%package devel
Summary:          Development files for gr-dab
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for gr-dab.

%package doc
Summary:          Documentation files for gr-dab
Requires:         %{name} = %{version}-%{release}
# doxygen bug workaround
#BuildArch:        noarch

%description doc
Documentation files for gr-dab.

%prep
%autosetup -p1

# hack to deal with wrong name
# drop when upstream adds correct support for gnuradio-3.9
pushd include
ln -s grdab dab
popd

%build
%cmake -DENABLE_DOXYGEN=on
%cmake_build

%install
%cmake_install

# remove hashbangs
pushd %{buildroot}%{python3_sitearch}/grdab
find . -type f -exec sed -i '/^[ \t]*#!\/usr\/bin\/\(env\|python\)/ d' {} \;
popd

# tests not ported to gnuradio-3.9, re-enable once ported by upstream
#%%check
#cd %%{_vpath_builddir}
#make test

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS README.md THANKS
%exclude %{_docdir}/%{name}/html
%exclude %{_docdir}/%{name}/xml
%{_datadir}/gnuradio/grc/blocks/*
%{_libdir}/libgnuradio-dab.so.3.*
%{python3_sitearch}/{dab,grdab}
%{_bindir}/*

%files devel
%{_includedir}/grdab
%{_libdir}/*.so
%{_libdir}/cmake/{dab,grdab}

%files doc
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/xml

%changelog
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
