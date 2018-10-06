%global git_commit a33609bd75192878f9f60c1a9b02fd7473649160
%global git_date 20180925

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:             gr-dab
URL:              https://github.com/andrmuel/gr-dab
Version:          0.2.1
Release:          2.%{git_suffix}%{?dist}
License:          GPLv3+
BuildRequires:    cmake, gcc-c++, python2-devel, scipy, gnuradio-devel
BuildRequires:    python2-matplotlib, cppunit-devel, boost-devel, doxygen
BuildRequires:    swig, faad2-devel, findutils
Requires:         scipy, python2-matplotlib
Summary:          GNU Radio DAB digital audio broadcasting module
Source0:          %{url}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz
# https://github.com/andrmuel/gr-dab/pull/16
Patch0:           gr-dab-0.2.1-libdir-fix.patch
# https://github.com/andrmuel/gr-dab/pull/17
Patch1:           gr-dab-0.2.1-install-apps.patch
# https://github.com/andrmuel/gr-dab/pull/18
Patch2:           gr-dab-0.2.1-traceback-fix.patch

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
BuildArch:        noarch

%description doc
Documentation files for gr-dab.

%prep
%autosetup -p1 -n %{name}-%{git_commit}

%build
mkdir build
cd build
%cmake -DENABLE_DOXYGEN=on ..
%make_build

%install
cd build
%make_install

# remove hashbangs
pushd %{buildroot}%{python2_sitearch}/grdab
find . -type f -exec sed -i '/^[ \t]*#!\/usr\/bin\/\(env\|python\)/ d' {} \;
popd

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS README.md THANKS
%exclude %{_docdir}/%{name}/html
%exclude %{_docdir}/%{name}/xml
%{_datadir}/gnuradio/grc/blocks/*
%{_libdir}/libgnuradio-dab.so.3.*
%{python2_sitearch}/grdab
%{_bindir}/*

%files devel
%{_includedir}/grdab
%{_libdir}/*.so
%{_libdir}/cmake/grdab

%files doc
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/xml

%changelog
* Wed Sep 26 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.1-2.20180925gita33609bd
- Fixed issues found by review

* Tue Sep 25 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.1-1.20180925gita33609bd
- Initial version
